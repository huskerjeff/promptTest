# VMware Console Access Troubleshooting Prompt

## Full Structured Prompt

```
You are an experienced VMware administrator with deep expertise in ESXi, vCenter, and VM console troubleshooting. I need systematic help diagnosing and resolving a terminal/console access issue.

## Problem Statement

I am encountering the error "unable to access terminal from interface" when attempting to access a VM console in my VMware environment.

## Environment Details (Please ask me to fill in any blanks)

- **VMware Product**: [ESXi / vCenter / Workstation / Fusion] version: ____
- **Host OS** (if applicable): ____
- **Guest OS**: ____
- **Access Method**: [vSphere Web Client / vSphere Client / VMRC / Direct ESXi Host UI / SSH]
- **Network Configuration**: [Direct / VPN / Jump host / Browser-based]
- **Recent Changes**: [None / Updated VMware / Changed network / Modified VM settings / Other: ____]

## Symptoms Observed

- [ ] Black screen when opening VM console
- [ ] Console window opens but no response to input
- [ ] Error message appears (exact text): ____
- [ ] Connection timeout
- [ ] Authentication/permission errors
- [ ] Console was working previously: [Yes, stopped on DATE / Never worked / Intermittent]
- [ ] Issue affects: [Single VM / Multiple VMs / All VMs]

## What I Have Already Tried

- [ ] Restarted the VM
- [ ] Restarted VMware services on host
- [ ] Cleared browser cache / tried different browser
- [ ] Verified VM is powered on and responsive via other methods (ping, SSH)
- [ ] Checked VMware Tools status
- [ ] Other: ____

## Requested Assistance

Please provide troubleshooting guidance in this format:

1. **Initial Diagnostic Commands**: ESXi shell or vSphere CLI commands to gather diagnostic information
2. **Service Checks**: Which VMware services to verify and how to restart them
3. **Log Files**: Specific log file paths and what to look for
4. **Network Diagnostics**: Firewall ports, connectivity tests between client and host
5. **Common Causes**: Ranked list of most likely causes for this error
6. **Step-by-Step Resolution**: Ordered troubleshooting steps from least to most disruptive
7. **Prevention**: How to prevent this issue in the future

For each solution, please indicate:
- Risk level (Low/Medium/High)
- Whether it requires VM downtime
- Whether it requires host maintenance mode

If you need additional information to diagnose this issue, please ask specific questions.
```

---

## Quick Minimal Version

```
I'm getting "unable to access terminal from interface" error accessing a VM console in VMware [ESXi/vCenter version: ____].

Environment: [Describe your setup]
Symptoms: [Black screen / No input response / Connection error]
Already tried: [List attempts]

Please provide:
1. Diagnostic commands to run on ESXi host
2. Services to check/restart
3. Log files to examine
4. Most likely causes ranked by probability
5. Step-by-step fix with risk levels noted
```

---

## How to Use This Prompt

1. **Copy the prompt** from either the full or minimal version above
2. **Fill in the bracketed sections** with your actual environment details
3. **Check the applicable symptom boxes** (replace `[ ]` with `[x]`)
4. **Remove any sections that do not apply** to keep the prompt focused
5. **Paste into your AI assistant** (Claude, ChatGPT, etc.) or support forum

---

## Why This Prompt Works

- **Role Assignment**: Opens with expert persona to prime the LLM for technical depth
- **Structured Input Template**: Fill-in-the-blank format ensures you provide all relevant context
- **Checkbox Symptom List**: Covers both black screen and terminal access variations
- **Explicit Output Format**: Numbered sections ensure comprehensive, organized response
- **Risk Indicators**: Requests risk assessment for production environment safety
- **Escape Hatch**: Invites follow-up questions rather than forcing assumptions

---

## Expected Output Quality

A well-configured LLM should respond with:
- 5-10 specific diagnostic commands
- Relevant log paths (`/var/log/vmware/`, `hostd.log`, `vpxa.log`)
- Port verification steps (443, 902, 903 for console traffic)
- Service restart commands (`/etc/init.d/` scripts or `esxcli`)
- Progressive troubleshooting from simple fixes to advanced remediation
