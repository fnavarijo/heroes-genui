# Heroes GEN UI

This is the codebase for the basic setup for the Gen UI workshop from GDG Guatemala.

## Setup

### Pre-requisites

1. Install Node.js 20+ (easiest: nvm)
2. Install python

```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.13
```

### Install dependencies

```bash
pnpm install
```

### Run project

```bash
pnpm dev
```

## Knowledge

### Libraries/frameworks/stacks

- [CopilotKit](https://docs.copilotkit.ai/): frontend stack for agentice UX.
- [Initial setup](https://docs.copilotkit.ai/a2a/generative-ui/declarative-a2ui)

### Concepts

- [A2A](https://a2a-protocol.org/latest/): protocol of communication between Agents.
- [A2UI](https://adk.dev/integrations/a2ui/): standard that tells the agents how to write the UI components
- [AG-UI](https://docs-ag--ui-com.translate.goog/introduction): defines the delivery of the UI to the client.
- [ADK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk): framework to develop and build AI agents.
