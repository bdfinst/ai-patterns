# AI Patterns

The current patterns I'm using and hardening for delivering enterprise software with AI agents.

**[→ View on GitHub](https://github.com/bdfinst/ai-patterns)**

## Guides

- **[Automated Code Review with AI Agents Reference Architecture](agentic-code-review.md)** - A hybrid approach combining deterministic rules-based tooling with context-aware AI agents to automate everything that can be automated about code review.

- **[Leading an Agentic Development Team](ai-development-playbook.md)** - A playbook for leading AI agents as team members, covering mission setting, acceptance-test-driven development, building focused specialist agents, and validating outcomes over activity.

- **[CD Defect Detection and Remediation Cheat Sheet](defect-detection-and-fixes.md)** - A comprehensive catalog of where defects are created in the value stream, methods for automated detection, and systemic remediation strategies.

- **[Contract Testing Strategies](contract-testing-strategies.md)** - A comprehensive guide to different contract testing approaches based on your level of organizational control over the services you integrate with.

## References

- **[Agentic Continuous Delivery (ACD)][acd]** - Extends traditional CD practices to AI agent-generated code, providing frameworks and governance structures that hold agent changes to the same quality bar as human-generated changes.

## Articles

- **[AI is a High Pass Filter for Software Delivery][high-pass-filter]** - Why AI amplifies your engineering discipline—teams with strong practices get dramatic improvements, while those without discipline struggle with generated garbage.

- **[Incorporating AI Without Crashing][incorporating-ai]** - A practical roadmap for integrating AI into existing teams, starting with foundational delivery challenges before jumping to code generation.

- **[Write-Only Code][write-only-code]** - An exploration of code that is difficult to read and understand, and strategies for writing code that remains maintainable.

- **[Why Spec-Driven Development Has Reached Its Limit][spec-driven-limit]** - The article argues that traditional spec-driven development has reached its limit because it only automates software structure, proposing instead a Contract-Driven AI Development (C-DAD) framework that uses "living contracts" to encode human intent and ensure systems remain trustworthy as they evolve.

- **[AI Broke Your Code Review. Here's How to Fix It][ai-broke-code-review]** - Traditional code review is inadequate for AI-generated code production rates; replace manual bottlenecks with automated tooling and reserve human judgment for what only humans can evaluate.

- **[Tokenomics: How to Stop Wasting Money on Tokens][tokenomics]** - Developers building agentic AI systems must treat token consumption as a core architectural concern, managing input/output costs, context windows, and prompt caching to avoid wasteful spending.

- **[Clarity Was Always the Bottleneck][clarity-bottleneck]** - AI's speed merely exposes the long-standing problem that clarity in requirements has always been the real bottleneck in software delivery—not a reason to return to waterfall-style upfront documentation.

## Example Skill libraries

- **[Paul Hammond's Skills][paul-hammond-skills]** - A focused collection of skills for frontend and test-driven development, covering TypeScript, React testing, mutation testing, functional patterns, refactoring, and TDD workflows.

- **[Robust Skills][robust-skills]** - Skills for DDD/hexagonal architecture, feature-sliced design, modern CSS and JavaScript, PostgreSQL with Drizzle ORM, Mermaid diagrams, and Slack app development.

- **[Quickstart: Agent-Augmented Development][quickstart-aad]** - A template for AI-augmented workflows built around a five-layer doctrine stack—guidelines, approaches, directives, tactics, and templates—giving agents consistent, inspectable, governance-layered behavior.

- **[nwave.ai][nwave]** - An AI-augmented development framework that standardizes team AI usage through a reviewable SDLC workflow combining specifications, tests, and code reviews for repeatable, auditable results.

- **[Holon: Agentic Coder][holon]** - A blueprint for git-native, sandbox-isolated autonomous coding agents that decompose work recursively, generate competing plans, record decisions in an append-only ledger, and evolve toward proposing their own intents.

[acd]: https://beyond.minimumcd.org/docs/agentic-cd/
[high-pass-filter]: https://bryanfinster.substack.com/p/ai-is-a-high-pass-filter-for-software
[incorporating-ai]: https://bryanfinster.substack.com/p/incorporating-ai-without-crashing
[write-only-code]: https://www.heavybit.com/library/article/write-only-code
[spec-driven-limit]: https://medium.com/software-architecture-in-the-age-of-ai/why-spec-driven-development-has-reached-its-limit-6e9bfed9ee13
[ai-broke-code-review]: https://bryanfinster.substack.com/p/ai-broke-your-code-review-heres-how
[tokenomics]: https://bryanfinster.substack.com/p/tokenomics-how-to-stop-wasting-money
[clarity-bottleneck]: https://bryanfinster.substack.com/p/clarity-was-always-the-bottleneck
[paul-hammond-skills]: https://github.com/citypaul/.dotfiles/tree/main/claude/.claude
[robust-skills]: https://github.com/ccheney/robust-skills
[quickstart-aad]: https://sddevelopment-be.github.io/quickstart_agent-augmented-development/
[nwave]: https://nwave.ai/
[holon]: https://github.com/thomashan/holon-agentic-coder
