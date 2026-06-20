# Architecture Concepts: A2A, AG-UI, A2UI & the Server Stack

A short reference for the protocols and frameworks used in this app, with
Python ↔ Node analogies to make the layers concrete.

## The big picture

```
Browser UI  ──AG-UI──►  Next.js / CopilotKit  ──A2A (+A2UI)──►  Python RestaurantAgent
 (user)                  (client agent)                          (A2A server)
```

- **AG-UI** carries the _user ↔ agent_ interaction.
- **A2A** carries the _agent ↔ agent_ communication.
- **A2UI** is an extension _inside_ A2A that lets the agent send renderable UI
  instead of plain text.

## The protocols

| Term                               | What it is                                                                                   | Connects                           | Web analogy                                                                   |
| ---------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------- |
| **A2A** (Agent-to-Agent)           | Wire protocol for agents to discover and call each other (tasks, streaming, agent cards)     | Client agent ↔ server agent        | **HTTP** — the transport/rules on the wire                                    |
| **AG-UI** (Agent-User Interaction) | Protocol streaming events between a UI and an agent (user input in; text/state/activity out) | Browser/CopilotKit ↔ agent runtime | The browser ↔ server event channel (think SSE/WebSocket conventions for chat) |
| **A2UI** (Agent-to-UI)             | An A2A **extension**: agent emits renderable UI payloads (cards, forms) instead of text      | Rides on top of A2A                | **REST** — an interaction style layered on the underlying protocol            |

In this repo:

- A2UI messages are validated against `A2UI_SCHEMA` (`agent/prompt_builder.py:16`)
  and built/validated in `agent/agent.py` + `agent/agent_executor.py`.
- The `@ag-ui/a2a` `A2AAgent` (in `app/api/copilotkit/[[...slug]]/route.tsx`) is
  the **bridge**: it makes an A2A backend look like a standard AG-UI agent that
  CopilotKit can drive.

## The server frameworks

| Term                          | What it is                                                                                                                              | Web analogy                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Starlette**                 | The ASGI **web framework** — routing, middleware, app object                                                                            | **Express / Fastify**                                                                 |
| **Uvicorn**                   | The ASGI **server runtime** that actually listens on the port                                                                           | **Node's `http` module**                                                              |
| **A2A Python SDK** (`a2a`)    | Framework that **implements the A2A protocol** on top of Starlette (`AgentCard`, `AgentExecutor`, task store)                           | **NestJS** (a protocol/structure layer on top of Express)                             |
| **A2AStarletteApplication**   | A pre-built A2A **app builder** layered on Starlette — wires up all the protocol routes, then `.build()` returns a normal Starlette app | A factory that returns a ready-configured Express app with the routes already mounted |
| **Google ADK** (`google.adk`) | The **agent framework** — `LlmAgent`, `Runner`, tools, sessions (the LLM "brain")                                                       | Your **service/business-logic layer**                                                 |
| **AgentCard**                 | Required machine-readable manifest (identity, URL, skills, capabilities) served for discovery                                           | **OpenAPI/Swagger spec** — but mandatory and first-class, not optional docs           |

## `A2AStarletteApplication` — framework or app?

It is **not a new framework**; it's a **pre-configured application built on the
Starlette framework**, purpose-wired for A2A. The two-step shape gives it away:

```python
server = A2AStarletteApplication(agent_card=..., http_handler=...)  # configure
app = server.build()          # → returns a plain Starlette app (ASGI)
app.add_middleware(CORS...)   # keep customizing it like any Starlette app
uvicorn.run(app, ...)         # run it
```

Node equivalent in spirit:

```js
function createA2AApp({ agentCard, handler }) {
  const app = express();                          // the framework
  app.get("/.well-known/agent-card.json", ...);   // protocol routes,
  app.post("/", taskHandler(handler));            // pre-wired for A2A
  return app;                                     // hand back a normal express app
}
const app = createA2AApp({ ... });   // ≈ A2AStarletteApplication(...).build()
app.use(cors());                     // you keep customizing
app.listen(10002);                   // ≈ uvicorn.run
```

So: **the framework is Starlette; `A2AStarletteApplication` is the A2A-specific
app builder on top of it** ("pre-configured app/router", not "new framework").

## Python ↔ Node cheat sheet

| Role                           | Python (this app)                 | Node analogy                       |
| ------------------------------ | --------------------------------- | ---------------------------------- |
| Protocol (wire)                | A2A                               | HTTP                               |
| Interaction style on top       | A2UI                              | REST                               |
| Discovery/contract             | AgentCard                         | OpenAPI spec                       |
| Protocol framework             | A2A SDK (`a2a`)                   | NestJS                             |
| Web framework                  | Starlette                         | Express / Fastify                  |
| Server runtime                 | Uvicorn                           | node `http`                        |
| Agent/business logic           | Google ADK (`LlmAgent`, `Runner`) | your services/controllers          |
| Request handler ("controller") | `RestaurantAgentExecutor`         | Express route handler              |
| User↔agent UI protocol         | (handled by client) AG-UI         | chat event channel (SSE/WebSocket) |

### One-sentence summary

> **A2A is to HTTP what the A2A SDK is to NestJS, what Starlette is to Express,
> and what Uvicorn is to Node's http server** — while **Google ADK** is your
> business logic and **AG-UI** is the separate user↔agent channel that the
> Next.js client uses to reach this A2A server.
