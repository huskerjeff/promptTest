# What's Next - Handoff Document

<original_task>
The user invoked the `/whats-next` skill to create a handoff document for the current conversation. The conversation itself involved exploring Claude Code's thinking skills and creating a prompt for ESXi PSOD (Purple Screen of Death) troubleshooting.
</original_task>

<work_completed>

## Skills and Commands Explored

1. **First Principles Thinking Skill** (`/taches-cc-resources:\consider:first-principles`)
   - First invocation: User ran the skill without arguments
   - Response: Applied first principles thinking to analyze the first-principles thinking tool itself
   - Analysis included: challenging assumptions about when to use the tool, identifying fundamental truths about problem-solving, and suggesting practical applications

2. **First Principles Applied to Technical Problem**
   - Second invocation: User provided argument "my server is not working with the router"
   - Response: Comprehensive first-principles breakdown of network troubleshooting
   - Covered: OSI layers (Physical through Application), systematic diagnostic approach, assumption challenging
   - Provided actionable diagnostic workflow from physical layer up

3. **Create Prompt Skill** (`/taches-cc-resources:create-prompt`)
   - User provided argument: "your an expert vmware engineer and my esxi just had a purple sceen how to figure out why"
   - Workflow completed:
     - Checked for existing prompts using Glob tool (`./prompts/*.md`) - none found
     - Conducted intake questionnaire via AskUserQuestion:
       * Log access: User confirmed "Yes, I can access logs"
       * Available info: User selected "None yet"
       * Goal: User selected "Find root cause"
     - User approved proceeding with prompt creation
     - Generated comprehensive VMware PSOD analysis prompt
     - Saved to: `./prompts/001-esxi-psod-root-cause-analysis.md`

4. **File Location Questions**
   - User asked where the created prompt was saved
   - Provided both relative and absolute paths
   - User asked where `create-prompt.md` is located
   - Explained plugin vs. local skill architecture:
     * Plugin skills (like `/create-prompt` from taches-cc-resources) are managed externally
     * Local skills stored in `.claude/commands/`, `.claude/skills/`, `.claude/agents/`
     * Listed current local files in project

5. **Add Todo Skill** (`/taches-cc-resources:add-to-todos`)
   - User ran command with argument "eat lunch"
   - Created new `./TO-DOS.md` file (didn't exist previously)
   - Added todo item with timestamp 2025-12-31 14:54
   - User confirmed they were going to grab lunch

## Artifacts Created

1. **`./prompts/001-esxi-psod-root-cause-analysis.md`**
   - Comprehensive VMware ESXi PSOD troubleshooting prompt
   - Structured with XML tags: `<objective>`, `<context>`, `<investigation_workflow>`, `<analysis_requirements>`, `<output>`, `<research_guidance>`, `<verification>`, `<success_criteria>`, `<constraints>`, `<examples>`
   - Designed for root cause analysis with log access
   - Output target: `./esxi-psod-analysis.md` (to be created when prompt runs)
   - Contains specific ESXi commands for data collection
   - Includes systematic backtrace analysis methodology
   - References VMware KB, HCL, and community resources

2. **`./TO-DOS.md`**
   - New todo tracking file
   - Contains one item: "Eat Lunch - 2025-12-31 14:54"
   - Format: Heading with timestamp, bullet points with Problem/Files fields

## Key Decisions Made

1. **Prompt Structure Decision**: Created single comprehensive prompt rather than multiple prompts
   - Rationale: PSOD troubleshooting is a cohesive sequential workflow (gather data → analyze → diagnose)
   - Not parallelizable since analysis depends on data collection

2. **Prompt Complexity Level**: Chose "moderate complexity" with extended thinking triggers
   - Included phrases like "thoroughly analyze" for deep investigation
   - Added systematic methodology with verification checkpoints
   - Balanced technical depth with actionable guidance

3. **Skip File Reading**: Did not request reading existing files during prompt creation
   - Rationale: Creating greenfield prompt, no existing code to examine
   - ESXi troubleshooting is domain knowledge, not codebase-specific

</work_completed>

<work_remaining>

## Immediate Next Steps

None currently pending. The user went to lunch after completing the prompt creation workflow.

## Potential Future Work

1. **Execute the Created Prompt**
   - User has option to run: `/run-prompt 001`
   - This will execute `./prompts/001-esxi-psod-root-cause-analysis.md`
   - Will generate analysis report at `./esxi-psod-analysis.md`
   - Prerequisites: User needs actual PSOD data (logs, error codes, backtraces) to analyze

2. **Explore More Thinking Models**
   - User showed interest in first-principles thinking
   - Other available `/\consider:*` skills not yet explored:
     * `/\consider:5-whys` - Root cause drilling
     * `/\consider:second-order` - Consequences analysis
     * `/\consider:inversion` - Backward problem solving
     * `/\consider:pareto` - 80/20 analysis
     * `/\consider:swot` - Strengths/weaknesses mapping
     * And 6 more in taches-cc-resources plugin

3. **Create Additional VMware/Homelab Prompts**
   - CLAUDE.md indicates repository focus on homelab (networking + compute)
   - Could create prompts for:
     * Network configuration troubleshooting
     * Proxmox/ESXi setup and optimization
     * Container/virtualization workflows
     * Infrastructure automation

4. **Todo Management**
   - User now has `TO-DOS.md` file
   - Could use `/check-todos` skill to review and select todos
   - Current todo: "eat lunch" (may want to remove after completing)

</work_remaining>

<attempted_approaches>

## Successful Approaches

1. **Adaptive Intake Questionnaire**: Used AskUserQuestion effectively
   - Asked only relevant questions based on task context (PSOD troubleshooting)
   - Limited to 3 questions (log access, available info, objective)
   - User provided clear answers enabling targeted prompt creation

2. **Plugin Architecture Explanation**: Successfully explained difference between plugin and local skills
   - Used Glob to show local .claude/ directory structure
   - Used Bash to list directory contents
   - Clarified that taches-cc-resources is external/managed

## No Failed Approaches

- No blockers, errors, or dead ends encountered
- All tool calls succeeded
- User questions answered satisfactorily
- Workflow completed as designed

</attempted_approaches>

<critical_context>

## Repository Context

- **Working Directory**: `C:\Users\jeffkit\OneDrive - CDW\Claude_Code_testing\DocGitTest`
- **Platform**: Windows (win32)
- **Git Status**: Clean working tree on `main` branch
  - Untracked files in `.claude/` (agents, commands, skills, settings)
  - Untracked PDF and Python scripts in root
  - Untracked `split_sections/` directory
- **Repository Purpose**: Homelab implementations (networking + compute) per CLAUDE.md
  - Focus: Proxmox, ESXi virtualization, Docker/Kubernetes, network configs
  - Emphasis: Self-hosting, resource efficiency, security by default

## Available Local Resources

**Agents** (`.claude/agents/`):
- `prompt-engineer.md` - AI/LLM prompt optimization expert
- `task-decomposition-expert.md` - Complex task breakdown specialist
- `report-generator.md` - Research findings to report transformer

**Skills** (`.claude/skills/`):
- `pdf-anthropic/` - PDF manipulation toolkit

**Commands** (`.claude/commands/`):
- `ultra-think.md` - Deep analysis and problem solving

## Plugin Skills Available (taches-cc-resources)

The user has access to extensive plugin-based skills:
- **Planning**: `/create-plan`, `/run-plan`, `/create-prompt`, `/run-prompt`
- **Development**: `/create-subagent`, `/create-slash-command`, `/create-skill`, `/create-hook`
- **Auditing**: `/audit-skill`, `/audit-slash-command`, `/audit-subagent`
- **Workflow**: `/add-to-todos`, `/check-todos`, `/whats-next`, `/debug`
- **Thinking Models**: 12 `/\consider:*` skills (first-principles, 5-whys, pareto, swot, etc.)
- **Commit Helpers**: From commit-commands plugin (`/commit`, `/commit-push-pr`, `/clean_gone`)

## ESXi PSOD Context (from created prompt)

**PSOD = Purple Screen of Death**: VMware ESXi's critical kernel panic
- Equivalent to Windows BSOD
- Causes: Hardware failures, driver bugs, firmware issues, resource exhaustion, storage failures
- Critical impact: VM downtime, potential data loss

**Common PSOD Types**:
- `#PF Exception 14` - Page Fault (memory/driver issues)
- `#GP Exception 13` - General Protection Fault (driver/code bug)
- `#UD Exception 6` - Invalid Opcode (CPU/firmware)
- Watchdog timeout - Deadlock/infinite loop

**Diagnostic Locations**:
- Core dumps: `/var/core/`
- VMkernel logs: `/var/log/vmkernel.log`
- Key commands: `esxcli`, `vmware -vl`, hardware status checks

## Prompt Engineering Best Practices (applied)

From the create-prompt skill workflow:
1. **XML structure** with semantic tags for clarity
2. **Context inclusion**: WHY task matters, WHO uses it, WHAT it's for
3. **Extended thinking triggers** for complex analysis ("thoroughly analyze")
4. **Explicit success criteria** and verification steps
5. **WHY explanations** for constraints (not just what, but reasoning)
6. **Examples** showing good vs. bad approaches
7. **Relative paths** for file outputs (`./filename`)
8. **Evidence-based approach**: Never guess, cite sources, require proof

## File Naming Conventions

**Prompts**: `./prompts/[number]-[descriptive-name].md`
- Number format: 001, 002, 003 (zero-padded)
- Name: lowercase, hyphen-separated, max 5 words
- Next available: 002 (001 is used for PSOD analysis)

**Todos**: `./TO-DOS.md`
- Section format: `## Brief Title - YYYY-MM-DD HH:MM`
- Item format: `- **[Action] [Component]** - Description. **Problem:** X. **Files:** Y. **Solution:** Z.`

</critical_context>

<current_state>

## File System State

**Created and Finalized**:
1. `./prompts/001-esxi-psod-root-cause-analysis.md` - Complete, ready to execute
2. `./TO-DOS.md` - Complete, contains one todo item
3. `./whats-next.md` - This handoff document (being written now)

**No In-Progress Work**: All requested tasks completed

**No Temporary Changes**: No workarounds or pending modifications

## Conversation State

**Last User Action**: Confirmed going to grab lunch (after adding "eat lunch" todo)

**Context Window**: Currently at ~42,000 tokens of 200,000 budget

**No Pending Questions**: All user queries answered

**No Blockers**: No errors, no missing information, no waiting on external factors

## Next Session Recommendations

When user returns from lunch, likely scenarios:

1. **Run PSOD Analysis**: If they have actual PSOD to troubleshoot
   - Command: `/run-prompt 001`
   - Will need: ESXi logs, PSOD error details, system access
   - Output: `./esxi-psod-analysis.md` with findings

2. **Clean Up Todos**: Remove or mark "eat lunch" as complete
   - Could use `/check-todos` to manage
   - Or manually edit `./TO-DOS.md`

3. **Explore More Skills**: User showed interest in thinking models
   - Could try other `/\consider:*` skills
   - Could explore `/create-plan` for homelab projects
   - Could use `/debug` for systematic troubleshooting

4. **Continue Homelab Work**: Per CLAUDE.md focus
   - Create more infrastructure-related prompts
   - Document network configurations
   - Set up virtualization workflows

## Open Questions

None currently. User can pick up exactly where they left off or start fresh direction.

</current_state>
