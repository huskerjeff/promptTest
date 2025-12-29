# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository is focused on computer homelab implementations, covering both networking and compute aspects. When working in this repository, prioritize practical homelab solutions that balance functionality, cost-effectiveness, and learning opportunities.

## Homelab Context

When developing or documenting homelab solutions:

- **Networking**: Consider common homelab networking scenarios including VLANs, routing, firewalls, VPNs, and network segmentation for security and isolation
- **Compute**: Focus on virtualization platforms (Proxmox, ESXi, etc.), containerization (Docker, Kubernetes), and efficient resource utilization
- **Hardware constraints**: Assume typical homelab hardware limitations (power consumption, noise, space, budget)
- **Self-hosting**: Prioritize solutions that can run independently without heavy cloud dependencies
- **Documentation**: Homelab projects benefit from clear setup instructions, troubleshooting guides, and architecture diagrams

## Development Approach

Since this is a homelab-focused repository, code and configurations should be:
- Reproducible and well-documented for others to replicate
- Modular to allow mixing different components
- Mindful of resource efficiency (power, CPU, RAM)
- Secure by default, especially for services exposed to networks

## Available Agents

This repository has specialized Claude Code agents installed to assist with specific tasks:

### Prompt Engineer (`prompt-engineer`)

Located at `.claude/agents/prompt-engineer.md`

**Use this agent when:**
- Building AI-powered homelab features (automation, monitoring, chatbots)
- Creating system prompts for LLM-based tools
- Optimizing prompts for AI assistants or agents
- Designing conversational interfaces for homelab management

**Invocation:** Use the Task tool with the agent name when you need prompt engineering expertise

The agent specializes in:
- LLM prompt optimization and testing
- Chain-of-thought reasoning design
- Model-specific tuning (Claude, GPT, open models)
- AI system architecture for homelab automation

### Task Decomposition Expert (`task-decomposition-expert`)

Located at `.claude/agents/task-decomposition-expert.md`

**Use this agent when:**
- Breaking down complex homelab projects into manageable steps
- Planning multi-phase infrastructure implementations
- Organizing migration or upgrade workflows
- Creating structured implementation roadmaps

**Invocation:** Use the Task tool with the agent name when you need help decomposing complex tasks

The agent specializes in:
- Breaking complex tasks into actionable subtasks
- Identifying dependencies and sequencing
- Creating clear implementation workflows
- Estimating scope and complexity of homelab projects
