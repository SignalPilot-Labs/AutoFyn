# The Most Expensive Real Estate in AI: Context Windows, Context Cliffs, and What Engineers Actually Do About It

*Every token you waste is a decision your model cannot make.*

---

## Opening: Let Me Show You Something Expensive (~2 minutes)

> **[SLIDE]** A single number: **$3.00**
> *Slide copy: "Claude Opus. 200K context. $15/M input tokens. Fill it once: $3.00."*

*Speaker note: Pull up the Anthropic pricing page before you go on stage. Verify the current per-token rate for the model you're using as your example. Update the slide if the number has changed. This lands harder when it's accurate.*

Pull up the Anthropic pricing page before you go on stage. Verify the current per-token rate for the model you're using as your example. This number lands harder if it's accurate.

Start with the dollar figure on screen. Say nothing else for a beat. Let the room read it.

Then: "That's the cost of a single API call at maximum context. A single call. Now imagine your agent makes 50 calls per run, and you have 200 concurrent users. You're spending $30,000 a day before you've written a line of business logic. That number is not hypothetical — it's the math on systems people are building right now."

Ask the room directly: "How many of you have built something where the model forgot what you told it ten messages ago?" Wait. Most hands go up.

"That forgetting is not a bug in the model. It is the consequence of a design decision that every engineer building with LLMs must understand and manage deliberately. Not optionally — deliberately."

Frame the talk cleanly: this is about why context is the most precious resource in modern AI systems, what happens when you run out of it, and how production systems deal with it. There is a running concrete example — an autonomous software engineer called AutoFyn — but the engineering principles apply to every system you're building.

> **[TRANSITION]** To understand why context management is hard, you need a precise mental model of what a context window actually is.

---

## Section 1: What Is a Context Window? (~3 minutes)

> **[SLIDE]** "The Input Is Everything"

An LLM has no persistent state between calls. Every inference is stateless. Zero. The "memory" of a model is entirely what you put in the prompt — nothing else. If you didn't include it, the model doesn't know it happened.

The context window is the finite buffer that holds everything the model can see right now: system prompt, conversation history, tool results, file contents, retrieved documents, whatever else you stuffed in. It is the model's entire world for that call.

It's measured in tokens. A token is roughly 0.75 words in English — but code and structured data are token-dense. A 200-line Python file is easily 1,000 tokens. A JSON API response with deep nesting? More. A stack trace from a failing test? Hundreds of tokens for what you could summarize in a sentence.

Current frontier models offer 128K–200K token windows. That sounds large. It is not as large as your codebase, your conversation history, your logs, your retrieved documents, your tool results, and your system prompt — all combined.

And the cost stacks fast. Input tokens are priced per call. If your agentic loop sends a 50K-token context on every turn, and the loop runs 20 turns, you've spent 1 million input tokens before the agent has done anything observable.

> **[DEMO/EXAMPLE]** Walk through a real calculation live.
>
> An autonomous agent working on a medium Python codebase:
> - System prompt: ~3,000 tokens
> - 10 relevant files at 300 lines average: ~15,000 tokens
> - Tool call results (git diff, test output, linter): ~5,000 tokens
> - Conversation history across 10 turns: ~10,000 tokens
> - **Total: ~33,000 tokens per call** — comfortable at 200K
>
> Now add prior-round memory, more files, a debugging trace, and retrieved docs. You're at 80K. Add a second agent writing to the same context and you're at the wall.

The window doesn't run out all at once. It fills gradually and then, suddenly, something must go. What gets dropped and how — that's the context cliff.

> **[TRANSITION]** So what happens when you hit that wall?

---

## Section 2: The Context Cliff (~4 minutes)

> **[SLIDE]** "What Truncation Actually Looks Like"

When context exceeds the window limit, something must be dropped. The model doesn't decide — the API client or framework decides, and the most common default strategy is FIFO truncation: the oldest messages go first.

FIFO truncation is catastrophic for the things that matter most. What's oldest? The system prompt. The initial task definition. The constraints you spent the most effort crafting. The model loses exactly the high-value content at the beginning and keeps the recent noise. You've paid to craft a precise system prompt and the model can no longer see it.

The failure mode that makes this hard to debug: the model cannot tell you it lost something. It responds from what remains, confidently, as if nothing is missing. There's no error code. No warning. The model just — responds. From an incomplete picture. With full confidence.

The symptoms engineers notice in production, usually too late: the model "forgets" earlier instructions and stops following them. It contradicts constraints it was given at the start. It repeats work it already completed. It loops on problems it already solved. Every one of these symptoms looks, from the outside, like a model capability problem. It's not. It's a context management problem.

There's a subtler failure mode beyond raw token count: signal-to-noise ratio. A 200K-token context that is 80% irrelevant content is worse than a 30K-token context that is 100% relevant. The model has more to attend to, more to confuse, more irrelevant patterns to accidentally weight. Filling the context is easy. Filling it with the right things is the hard problem.

> **[DEMO/EXAMPLE]** AutoFyn is an autonomous AI software engineer. It runs in discrete rounds. Each round is a fresh Claude SDK session with a fresh context window.
>
> Without explicit cross-round memory: Round 1 implements a feature and commits. Round 2 starts fresh — zero memory of Round 1. The model might re-implement the same feature, undo committed work, or take a direction that directly conflicts with Round 1 decisions.
>
> This is not hypothetical. Early agent systems without round isolation hit exactly this failure. The system looked coherent turn by turn and incoherent over time. That's the context cliff expressed across sessions rather than within one.

> **[TRANSITION]** The framing that makes this tractable is older than LLMs — it's the same framing computer science has used for memory management for sixty years.

---

## Section 3: The Human Analogy (~2 minutes)

> **[SLIDE]** "Your Brain Does This Too"

Miller's Law, 1956: human working memory holds roughly seven items, plus or minus two. It's fast, it's immediate, and it's tiny. Long-term memory is vast but retrieval is costly and imperfect.

We manage this gap constantly. We take notes. We write summaries. We build calendars and checklists and wikis. A three-hour meeting with no notes and no action items is not just unproductive — it is lost to the context cliff of human memory. Two weeks later, nobody agrees on what was decided. The content existed. It didn't persist.

LLMs have the same two-tier structure: fast and finite working memory (the context window) and slow and unbounded external memory (files, databases, vector stores). The engineering discipline is identical: decide what goes in working memory, externalize everything else, and have a retrieval strategy when you need what's outside.

The analogy breaks down in one critical place: LLMs have no implicit background consolidation. They don't sleep, don't form habits, don't auto-prioritize based on emotional salience. There is no forgetting curve — the model either has it in context or doesn't. Every piece of working-memory content was explicitly put there by an engineer. This makes the discipline more demanding, not less.

> **[TRANSITION]** With that framing, let me show you how a production agentic system actually structures this.

---

## Section 4: How AutoFyn Manages Context — The Real System (~6 minutes)

> **[SLIDE]** "The Architecture of Memory"

*This section is the technical centerpiece. Do not rush it. The concrete details are what separates this talk from a blog post.*

### 4a. The Round Boundary as a Deliberate Context Reset

AutoFyn runs in discrete rounds. Each round is a fresh Claude SDK session. The context window is intentionally cleared between rounds — not as a limitation of the system, but as a deliberate architectural decision.

Fresh context means no accumulated noise. No orphaned tool results from three rounds ago. No confusion between old and new state. No FIFO truncation destroying the system prompt halfway through a long run.

The tradeoff is explicit: you must reconstruct all necessary context at the start of each round. The round boundary forces precision. You can't coast on what the model "remembers" — you must decide, concretely, what it needs to know.

This is the round loop in `autofyn/lifecycle/round_loop.py`. Every round: create a fresh sandbox, build a fresh system prompt, build fresh subagent definitions, run the session, archive results, evaluate the terminal status, loop. The loop is straightforward Python. The discipline is in what gets passed to `build_round_system_prompt()` and `build_agent_defs()` — and what doesn't.

> **[SLIDE]** `build_round_system_prompt()` in `autofyn/prompts/orchestrator.py`
*Every token in this function is intentional. There is nothing here by accident.*

`build_round_system_prompt()` assembles the orchestrator's context from up to five sections: the static `system.md` template (the model's identity and workflow), a dynamic environment block (current round number, tool timeout, mounted paths, env keys, base branch), git rules, time-lock status if the run is duration-bounded, and the user activity timeline. Every section is purposeful. Nothing is appended casually.

### 4b. run_state.md: The Compression Layer

Across rounds, the only content that persists into the next round's context is what gets written to `/tmp/run_state.md`. That's it. One file. The `RUN_STATE_PATH` constant in `autofyn/utils/constants.py` points to `/tmp/run_state.md`.

This file is the compressed, curated cross-round memory. It has five sections, defined by `RUN_STATE_TEMPLATE`: Goal, Goal Updates, Eval History, Rules, State. The orchestrator reads it at the start of every round. It answers the only questions that matter for continuing work: where are we, where are we going, and what have we learned that we shouldn't repeat?

It is intentionally small. Eval history is capped at the first 5 plus the last 20 entries if it exceeds 50 lines — preserving both the baseline and recent trajectory. Rules are capped at 30. Round summaries are capped at 60 characters. The goal is not to store everything — it is to store the minimum decision-relevant content. Full round reports are archived separately and retrieved on demand.

This is the literal answer to the question "what do humans do with notes after a meeting": write compressed summaries that preserve decisions, not transcripts of everything said.

### 4c. Round Reports: Full Detail Without Polluting the Main Context

Full subagent output goes to `/tmp/round-N/<agent-name>.md`. The architect's spec, the code reviewer's findings, the build report — all of it lands in that directory. None of it is injected wholesale into the orchestrator's context.

Instead, the orchestrator is told: here is the list of files in `/tmp/round-N/`. Go read what you need. It reads selectively. A file index, not a data dump.

This is retrieval-augmented context management at the filesystem level. The detail exists. It stays out of the window until specifically needed. The orchestrator has full access to arbitrarily detailed prior-round information — it just doesn't carry it all in working memory simultaneously.

`ReportStore` in `autofyn/memory/report.py` owns this: `ensure_round_directory(n)` creates the directory at round start, `list_round(n)` returns the sorted file list. The orchestrator calls `list_round(round_number - 1)` to get the prior round's index, then reads individual files as needed.

Between sandbox restarts and on run resume, `RoundArchiver` in `autofyn/memory/archiver.py` handles persistence. After each round, `archive_round(n)` pulls `/tmp/round-N/`, `run_state.md`, and `rounds.json` into the agent container's persistent volume at `/home/agentuser/.autofyn/rounds/<run_id>/`. On resume, `restore_all()` pushes everything back into a fresh sandbox. State survives container restarts without any special infrastructure — just file I/O at round boundaries.

### 4d. Subagent Isolation: Protecting the Orchestrator's Budget

AutoFyn has nine specialized subagents across four phases: code-explorer for exploration, architect and debugger for planning, backend-dev and frontend-dev for building, and spec-reviewer, code-reviewer, ui-reviewer, and security-reviewer for review.

Each subagent runs in its own Claude SDK session with its own context window. Subagent output never pollutes the orchestrator's context directly — results go to files in `/tmp/round-N/`. The orchestrator's context stays small: it manages routing, reads report indexes, makes high-level decisions.

The heavy lifting happens in subagent windows. Reading 20 files to understand a codebase. Generating 500 lines of implementation. Running tests and analyzing failures. All of that happens in a subagent's isolated window, optimized for that specific task.

`build_agent_defs()` in `autofyn/prompts/subagent.py` constructs each subagent's prompt: the agent's markdown body plus environment block, git rules, dispatch rules, and conditionally verification rules (for build and review agents) and prior-round context (for round 2 onward). Each subagent gets only what it needs for its role.

> **[SLIDE]** `AGENTS_WITHOUT_RUN_STATE = ("explore/code-explorer",)` in `autofyn/prompts/subagent.py`
*One exception. The code-explorer is the one subagent that doesn't get cross-round context. Its job is always fresh exploration. Prior-round state would bias it toward confirming what's already known rather than discovering what's changed.*

> **[DEMO/EXAMPLE]** The context flow, drawn explicitly:
>
> ```
> [Orchestrator window — one per round]
>   system.md (identity + workflow):    ~3,000 tokens
>   environment block (round, mounts):    ~500 tokens
>   git rules:                            ~300 tokens
>   run_state.md (cross-round memory):  ~2,000 tokens
>   prior round file index:               ~200 tokens
>   user activity timeline:               ~300 tokens
>   ──────────────────────────────────────────────────
>   Total orchestrator context:         ~6,300 tokens
>
> [Subagent windows — separate, parallel, isolated]
>   architect:     reads 10 files, produces spec → /tmp/round-N/architect.md
>   backend-dev:   reads spec + source, writes code → commits to git
>   code-reviewer: reads diff + tests, writes verdict → /tmp/round-N/code-reviewer.md
> ```
>
> The orchestrator never sees the architect's 10-file read. The code-reviewer never carries the architect's deliberation. Each agent's window is scoped to its task.

> **[TRANSITION]** This system works — but only because the engineers designing it made explicit tradeoffs at every decision point. Let's name those tradeoffs.

---

## Section 5: Strategies and Tradeoffs (~3 minutes)

> **[SLIDE]** "The Toolbox"

These are the five general strategies for context management. Every serious LLM system uses a combination of them. None is free.

**Compression and summarization.** Reduce high-value content to its decision-relevant essence. In AutoFyn, `run_state.md` is the compressed summary of all prior rounds — five headings, bounded size, decisions only. The risk: it's lossy. What you decide isn't important might matter three rounds later. The mitigation: keep full archives and retrieve on demand. Never throw away the source; only compress what goes in working memory.

**External memory with selective retrieval.** Store full content out-of-band and inject only what the current task needs. In AutoFyn: the `/tmp/round-N/` files, `list_round()`, and selective reads by the orchestrator. The risk: retrieval quality. If the agent doesn't know to look for something, it won't find it. AutoFyn mitigates this with explicit file indexes — deterministic enumeration, not semantic search. You know exactly what's available.

**Stateless round boundaries.** Deliberately clear the context on a boundary event. The round in AutoFyn. This is unusual — most systems try to keep context alive as long as possible. AutoFyn treats the context window as a scratch pad for one round, not a journal accumulating history. The cost is reconstruction overhead: you must explicitly rebuild context each round. The benefit is zero accumulated noise and predictable window utilization.

**Role-specific windows with subagent isolation.** Give each task role its own fresh window, purpose-built for that task. Nine subagents, nine isolated windows, each optimized for its specific work. The coordination cost: agents communicate through files, not shared context. The standardized coordination medium in AutoFyn is `/tmp/round-N/<name>.md` — a contract both writer and reader know.

**Prompt budget awareness.** Know your token budget before you design the system, not after. In AutoFyn, the orchestrator's system prompt is assembled section by section in `build_round_system_prompt()`. The engineers know approximately what each section costs. Nothing is appended casually. If you're assembling context by concatenating strings and hoping it fits, you are not doing context engineering — you're doing context gambling.

> **[TRANSITION]** Given all of this, where is context management heading?

---

## Section 6: The Future (~2 minutes)

> **[SLIDE]** "Longer Windows Don't Solve the Problem"

Context windows have grown fast: 4K tokens with GPT-3, 32K, 128K, 200K with Claude, 1M with Gemini 1.5. The trajectory continues. In a few years, 10M-token windows are plausible.

Longer windows create new problems. The most well-documented: "lost in the middle." Models attend strongly to content at the beginning and end of a long context and poorly to content in the middle. Put the critical instruction at position 500K of a 1M-token context and the model may effectively ignore it while confidently processing everything around it. This is not a prompt engineering trick — it is an empirically measured attention distribution failure.

The economics shift but don't disappear. At 1M tokens, you could stuff an entire medium-sized codebase into a single call. That call costs $15 at current Opus pricing *(verify before delivery — Anthropic pricing changes)*. If your agent makes 50 such calls per run, you're spending $750 on input tokens alone — per run. The model still performs better on a focused 30K-token context of highly relevant content than on a 1M-token firehose of everything that might be relevant.

The deeper point: context engineering is about signal density, not window size. The discipline of deciding what to include — and at what level of compression — remains as the budget grows. Bigger windows raise the cost of each mistake, they don't eliminate the need for judgment.

The analogy that holds: email clients with unlimited storage didn't eliminate inbox management as a discipline. They raised the cognitive cost of failing to manage. You can now have 300,000 unread emails. That doesn't mean you should.

> **[TRANSITION]** Let me leave you with three things to take home.

---

## Closing: What to Take Home (~2 minutes)

> **[SLIDE]** "Three Principles"

**One. Context is not chat history. It is your agent's entire working memory.** Design it that way, from the first line of the system prompt. Every token you include is a decision about what the model can and cannot know right now. Every token you waste is a decision the model cannot make — because something more important got crowded out.

**Two. The context cliff is silent and confident.** Your agent will not tell you it forgot. It will respond from whatever remains, with full apparent coherence. Build instrumentation: log token usage per call, alert at 70% window utilization, treat context exhaustion as a production incident the way you treat memory leaks or database connection exhaustion. It is the same class of problem.

**Three. Externalize aggressively. Retrieve selectively.** The right pattern is not "stuff everything in and hope." It is: store everything out-of-band, pull only what this task needs. File-based round reports, retrieval-augmented generation, vector stores — these are not advanced features or academic techniques. They are the practical solution to a fundamental hardware constraint. The constraint is not going away.

The context window is the memory of your agent. Managing memory is the oldest problem in computer science. We solved it with hierarchical storage, caching, and explicit memory management in the 1960s. We are solving it again, with LLMs, at $15 per million tokens.

> **[SLIDE]** Final line — choose one based on room energy:
>
> *"The model's working memory is finite. Make sure what's in it is worth paying for."*
>
> *"Context management is memory management. We solved memory management in 1960. We're solving it again, at $15 per million tokens."*
>
> *"Every token you waste is a decision your model cannot make."*

---

## Speaker Notes

### Timing

| Section | Title | Target |
|---|---|---|
| Opening | Let Me Show You Something Expensive | 2 min |
| Section 1 | What Is a Context Window? | 3 min |
| Section 2 | The Context Cliff | 4 min |
| Section 3 | The Human Analogy | 2 min |
| Section 4 | How AutoFyn Manages Context | 6 min |
| Section 5 | Strategies and Tradeoffs | 3 min |
| Section 6 | The Future | 2 min |
| Closing | What to Take Home | 2 min |
| **Total** | | **24 min** |

If running long: compress Section 3 (the human analogy) to one minute — it's a conceptual bridge, not a load-bearing argument. Do not compress Section 4. That section is what makes this talk technically differentiated.

If running short: Section 5 (Strategies) can expand — each of the five strategies can take 90 seconds instead of 60 if you add a second concrete example beyond AutoFyn for each.

### Flexibility Notes

The talk works without slides — the section headers are self-contained and the examples are verbal. If projecting, the most useful visuals are the context budget diagram in Section 4d and the pricing number in the Opening. Everything else is reinforcement.

The AutoFyn examples should not feel like marketing. The framing is: "I'm going to use a system I know in detail because that's how you avoid hand-wavy examples." Acknowledge early that the principles generalize — any autonomous agent system faces the same constraints.

The calculation in Section 1 is most effective if you do it live with a calculator or on a whiteboard. Audiences remember the process more than the result.

### Pre-Talk Checklist

- [ ] Verify current Anthropic pricing at anthropic.com/pricing — update the Opening dollar figure if it has changed
- [ ] Confirm Claude Opus context window size (200K as of talk writing — verify before delivery)
- [ ] If projecting slides, have the context flow diagram from Section 4d ready as an image or drawn on a whiteboard
- [ ] Run the token calculation in Section 1 once yourself so the numbers are natural
- [ ] Decide which closing line fits the room — a research audience responds to the memory management framing; a startup audience responds to the cost framing; a general engineering audience responds to the tagline

### Technical Reference: AutoFyn Files Cited

All file paths verified against the repository at time of writing:

- `autofyn/lifecycle/round_loop.py` — round loop, per-round session lifecycle, archive call
- `autofyn/prompts/orchestrator.py` — `build_round_system_prompt()`, `RoundContext`, section assembly
- `autofyn/prompts/subagent.py` — `build_agent_defs()`, `AGENTS_WITHOUT_RUN_STATE`, `AGENTS_WITH_VERIFICATION`, `SUBAGENT_DEFS`
- `autofyn/memory/report.py` — `ReportStore`, `ensure_round_directory()`, `list_round()`
- `autofyn/memory/archiver.py` — `RoundArchiver`, `archive_round()`, `restore_all()`
- `autofyn/memory/metadata.py` — `MetadataStore`, `record_round()`
- `autofyn/utils/constants.py` — `RUN_STATE_PATH` (`/tmp/run_state.md`), `ROUND_DIR_PREFIX` (`/tmp/round-`), `RUN_STATE_TEMPLATE`, `ROUND_ARCHIVE_AGENT_DIR` (`/home/agentuser/.autofyn/rounds`)
- `autofyn/prompts/system.md` — orchestrator identity, workflow, constraints
- `autofyn/prompts/query/prior-round-context.md` — cross-round context injection block for subagents
