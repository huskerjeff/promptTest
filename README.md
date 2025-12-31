# Homelab Prompt Repository

A curated collection of system prompts, documentation, and troubleshooting guides for computer homelab enthusiasts, covering both networking and compute aspects.

## Repository Structure

```
.
├── README.md                 # This file
├── CLAUDE.md                 # Claude Code agent instructions
├── .claude/                  # Claude Code configuration
│   └── agents/              # Custom Claude Code agents
│       ├── prompt-engineer.md              # Prompt engineering specialist
│       └── task-decomposition-expert.md    # Complex task breakdown expert
├── docs/                     # Documentation and guides
│   └── troubleshooting/     # Troubleshooting guides
│       └── vmware-console-access.md       # VMware console access issues
└── prompts/                  # System prompts and AI templates
    └── homelab-compute-expert.md          # Homelab compute specialist prompt
```

## Contents

### System Prompts

Located in the `prompts/` directory:

- **[Homelab Compute Expert](prompts/homelab-compute-expert.md)**: A comprehensive system prompt for AI assistants to provide expert guidance on homelab compute infrastructure, including virtualization platforms, container orchestration, hardware selection, and optimization strategies.

### Documentation

Located in the `docs/` directory:

- **[VMware Console Troubleshooting](docs/troubleshooting/vmware-console-access.md)**: Structured troubleshooting guide for resolving VMware console access issues, including diagnostic commands, service checks, and step-by-step resolution procedures.

### Claude Code Agents

This repository includes specialized Claude Code agents for enhanced functionality:

- **Prompt Engineer** (`.claude/agents/prompt-engineer.md`): Assists with creating and optimizing prompts for AI systems, LLM integration, and homelab automation.
- **Task Decomposition Expert** (`.claude/agents/task-decomposition-expert.md`): Helps break down complex homelab projects into manageable implementation steps.

See [CLAUDE.md](CLAUDE.md) for detailed information about using these agents.

## Usage

### Using System Prompts

The prompts in this repository are designed to be used with AI assistants like Claude, ChatGPT, or other LLMs:

1. Copy the entire prompt from the desired `.md` file
2. Use it as a system prompt or initial message when starting a conversation
3. Provide your specific context and requirements

### Contributing

This is a homelab-focused repository. When contributing:

- Ensure prompts are practical and tested
- Document hardware constraints and assumptions
- Prioritize reproducibility and clear instructions
- Balance functionality with cost-effectiveness

## License

This repository contains prompt templates and documentation for homelab use. Feel free to use, modify, and adapt for your own homelab projects.

## Related Resources

- [r/homelab](https://reddit.com/r/homelab) - Homelab community on Reddit
- [Proxmox Documentation](https://pve.proxmox.com/pve-docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
