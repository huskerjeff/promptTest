<objective>
Act as an expert VMware engineer to perform comprehensive root cause analysis of an ESXi Purple Screen of Death (PSOD).

Your goal is to systematically investigate the PSOD, analyze diagnostic data, identify the root cause, and provide actionable remediation steps. This analysis will be used to prevent future occurrences and restore host stability.
</objective>

<context>
A Purple Screen of Death (PSOD) is VMware ESXi's equivalent to Windows BSOD - a critical system failure that crashes the hypervisor. PSODs can be caused by:
- Hardware failures (memory, CPU, storage controllers, NICs)
- Driver incompatibilities or bugs
- Firmware issues
- Resource exhaustion
- Storage path failures
- Third-party VIB (vSphere Installation Bundle) conflicts

The user has access to ESXi host logs and diagnostic files but hasn't gathered specific PSOD details yet.

WHY this matters: PSODs indicate serious stability issues that can lead to VM downtime, data loss, and production outages. Identifying root cause prevents recurrence.
</context>

<investigation_workflow>

## Phase 1: Data Collection

Gather all available diagnostic information. For maximum efficiency, perform multiple independent data collection operations simultaneously.

1. **PSOD Screen Details** (if available)
   - Photograph or transcribe the exact error message
   - Note the PSOD error code (e.g., "#PF Exception 14")
   - Record the backtrace/call stack shown on screen
   - Document timestamp of occurrence

2. **System Logs Retrieval**
   Execute these commands on the ESXi host (via SSH or console):

   ```bash
   # Check for PSOD files (coredumps)
   ls -lh /var/core/

   # Recent VMkernel logs
   tail -500 /var/log/vmkernel.log

   # VMkernel warnings/errors
   grep -i "error\|fail\|panic\|psod" /var/log/vmkernel.log

   # Hardware errors
   grep -i "mce\|hardware" /var/log/vmkernel.log

   # Storage errors
   grep -i "scsi\|nmp\|apd\|pdc" /var/log/vmkernel.log

   # ESXi version and build
   vmware -vl

   # Check hardware compatibility
   esxcli hardware platform get
   ```

3. **Recent Changes Assessment**
   - Check update history: `esxcli software vib list | head -20`
   - Review recent configuration changes in vCenter events (if applicable)
   - Document any recent hardware additions/removals

4. **Hardware Health Check**
   ```bash
   # Memory errors
   esxcli hardware memory get

   # Storage adapter status
   esxcli storage core adapter list

   # Network adapter status
   esxcli network nic list
   ```

</investigation_workflow>

<analysis_requirements>

Thoroughly analyze the collected data using systematic methodology:

## Deep Analysis Steps

1. **PSOD Pattern Recognition**
   - Identify the PSOD type from error code:
     * `#PF Exception 14` = Page Fault (often memory/driver issues)
     * `#GP Exception 13` = General Protection Fault (driver/code bug)
     * `#UD Exception 6` = Invalid Opcode (CPU/firmware)
     * `Watchdog timeout` = Deadlock/infinite loop

2. **Backtrace Analysis**
   - Identify which kernel module/driver appears in the call stack
   - Look for third-party driver names (non-VMware modules)
   - Check if specific VM or storage operation triggered failure

3. **Log Correlation**
   - Timeline analysis: What happened in the 60 seconds before PSOD?
   - Look for patterns: Hardware errors, storage latency, memory pressure
   - Cross-reference vmkernel.log with vobd.log and hostd.log

4. **Known Issue Research**
   - Search VMware KB for the specific PSOD error code and backtrace
   - Check for known issues with identified driver/hardware combination
   - Review VMware HCL (Hardware Compatibility List) for compatibility

5. **Root Cause Hypothesis**
   Develop evidence-based hypothesis considering:
   - Hardware failure probability (ECC errors, controller failures)
   - Software bugs (driver version, ESXi build issues)
   - Configuration problems (memory overcommit, resource exhaustion)
   - Environmental factors (power, temperature)

</analysis_requirements>

<output>

Create a comprehensive analysis report saved to: `./esxi-psod-analysis.md`

The report must include:

### 1. Executive Summary
- PSOD occurrence timestamp
- Immediate impact (VMs affected, downtime duration)
- Root cause (in plain language)
- Criticality assessment (isolated incident vs. recurring risk)

### 2. Technical Details
- PSOD error code and type
- Complete backtrace analysis
- Relevant log excerpts with timestamps
- Hardware/firmware/driver versions involved

### 3. Root Cause Analysis
- Primary cause with supporting evidence
- Contributing factors
- Why this specific combination triggered the PSOD

### 4. Remediation Steps (Prioritized)
**Immediate actions** (prevent recurrence):
- Specific driver updates needed (with KB article links)
- Firmware upgrades required
- Configuration changes to implement
- Workarounds if permanent fix unavailable

**Long-term recommendations**:
- Hardware replacement if failing
- Monitoring improvements
- Preventive maintenance schedule

### 5. Verification Steps
- How to confirm the fix worked
- Monitoring approach to detect early warning signs
- Testing methodology before returning to production

### 6. References
- VMware KB articles referenced
- Driver/firmware download links
- Related community discussions or VMware support cases

</output>

<research_guidance>

When searching for root cause:

1. **Use specific search terms**:
   - "ESXi [version] PSOD [error_code]"
   - "[driver_name] purple screen vmkernel"
   - "[hardware_model] ESXi compatibility"

2. **Prioritize sources**:
   - VMware Knowledge Base (kb.vmware.com)
   - VMware HCL (vmware.com/resources/compatibility)
   - Vendor documentation (Dell, HP, Cisco for hardware-specific)
   - VMware Communities (for real-world experiences)

3. **Cross-reference multiple sources** to validate findings

</research_guidance>

<verification>

Before declaring the analysis complete, verify:

- [ ] PSOD error code identified and explained
- [ ] Backtrace analyzed with specific module/driver identified
- [ ] Log timeline established (what happened before crash)
- [ ] Root cause hypothesis supported by evidence from logs
- [ ] Remediation steps are specific and actionable (not generic advice)
- [ ] VMware KB articles or HCL references included for validation
- [ ] Verification method provided to confirm fix works
- [ ] Report saved to `./esxi-psod-analysis.md`

</verification>

<success_criteria>

A successful analysis delivers:

1. **Definitive root cause** - Not "could be X or Y" but "Evidence shows X because..."
2. **Actionable remediation** - Specific version numbers, KB articles, commands to run
3. **Evidence-based conclusions** - Every claim backed by log entries or VMware documentation
4. **Prevention strategy** - How to detect this issue early in the future
5. **Clear communication** - Technical depth with executive summary for non-experts

</success_criteria>

<constraints>

- **Never guess** - If data is insufficient, state what additional information is needed
- **Cite sources** - Include KB article numbers, HCL links, and driver version references
- **Consider ESXi version** - Solutions vary by ESXi 6.x vs. 7.x vs. 8.x
- **Hardware context matters** - Dell, HP, Cisco have different tools and support approaches
- **Safety first** - If remediation requires downtime, state this explicitly with migration recommendations

WHY these constraints matter: PSOD troubleshooting directly impacts production availability. Incorrect diagnosis can lead to ineffective fixes, recurring outages, or worse - data loss. Precision and verification are critical.

</constraints>

<examples>

**Good root cause statement**:
"PSOD caused by Intel i40e NIC driver version 1.11.29 triggering #PF Exception 14 during VXLAN encapsulation. VMware KB 52187 documents this as a known issue with this driver version when VXLAN offload is enabled. Evidence: vmkernel.log shows i40e module in backtrace at line 2847, preceded by 'NIC queue stall' warnings. Resolution: Update to i40e driver 2.1.26 per KB 52187."

**Bad root cause statement**:
"Probably a driver issue or maybe hardware. Try updating drivers."

**Good remediation step**:
"Update Intel i40e driver: 1) Download VIB from VMware KB 52187, 2) Enable SSH, 3) Upload VIB to /tmp, 4) Run: esxcli software vib install -v /tmp/i40e-2.1.26.vib --no-sig-check, 5) Reboot host during maintenance window, 6) Verify with: esxcli software vib list | grep i40e"

**Bad remediation step**:
"Update drivers to latest version"

</examples>
