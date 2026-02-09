# Leading an Agentic Development Team

<small>v1.1</small>

I was convinced AI coding tools were garbage. A few years ago, when people started saying "we don't need developers anymore," I set out to prove them wrong. I asked ChatGPT to build a simple REST service. It generated code with dependencies that didn't exist. You could search the entire internet and not find them. It confidently handed me fictional libraries. Complete garbage.

So I shelved it. Every time someone told me they were "coding professionally" with AI, I thought they were insane. I even started writing a blog post to demonstrate how terrible these tools were.

I had to trash the blog post.

I went back to generate code as evidence for my argument and discovered the models had improved in six months. Then I
saw that people I deeply respected, Patrick Dubois and John Willis, both foundational members of the DevOps movement, were
experimenting with AI. Patrick coined the word DevOps. John helped coin CALMS. Both have deep development and
operational experience. These aren't hype-chasers. I joined one of their
hackathons, used languages I'd never touched before on problems I didn't have a clue how to solve before, but I had a
clear vision of the goal I wanted to achieve. I used help from ChatGPT to finish a working RAG application with open source models in a few hours that responded
to questions about [MinimumCD.org](https://minimumcd.org) with answers, not just copied text. That
was the turning point.

## You've Led Teams Before

When I started using AI agents for real work, I ran into the same problems I see people complain about today. I spent
most of my time correcting the code. "No, do it this way. No, not like that either." Endless back and forth, burning
time instead of saving it. I'd get frustrated and just code it myself. However, I knew I needed to figure this out, so I
kept at it.

Then I realized I'd been here before. Not with AI. With people. I'd seen this exact dynamic on every development team I
worked on that lacked engineering discipline. Teams that started coding before they understood what they were building,
skipped tests, spent weeks debugging, and confused activity with progress. The problem wasn't the developers. The
problem was that nobody made sure the team had the right information at the right time and had the workflow to get
feedback and self-correct.

The same thing was happening with my agents. I was handing them vague instructions or telling them HOW to build
something and getting frustrated with the results. Same dysfunction, different team. The fix was the same fix it's always been: make sure the team has what it needs to succeed. Clear goals. Business context. Quality processes that catch problems before the problems can be created, and then keep hardening those validations. AI didn't change the fundamentals of leading a development team. It amplified them.

## Building Your Agentic Team

Here's how I lead my agentic development team today. If you've ever been on a good human team, this will feel familiar.

### Set the Mission

On the best teams I've been part of, we all understood the reasons behind the feature, not just the tasks assigned to
us. I make it my job to ensure that context is available. On a human team, I'll create a flow diagram of the business process, walk
through the user's problem, share why this feature matters. A team that has the right business and technical information
asks the right questions and makes the right decisions without anyone standing over them.

I use the same mindset with agents. Start with three to five sentences describing the feature and its goals. Not how to build it. What it should accomplish and why. Then tell the agent: "Here's what we're building. Plan the approach and ask me any clarifying questions." Let it generate a plan. Give feedback. Iterate until the plan makes sense. This takes maybe ten minutes and saves hours of rework.

This is where most people fail. They skip the mission briefing and jump straight to "write me a function that does X." The agent needs a broad enough understanding of the feature's goals to make architectural decisions. If you scope the task to a single function, it has no context for where that function fits, how it relates to the rest of the system, or how the pieces should be organized. It will produce something that works in isolation and creates a mess in context.

When the agent understands the full scope of what you're trying to accomplish, it architects the solution. It decomposes the problem sensibly, puts boundaries in the right places, and designs components that interact cleanly. The AI is trained on good patterns. You don't have to remember them all and feed them in. You just have to give it enough context to apply them.

### Define "Done" Before You Start

For each item in the plan, generate Gherkin feature files with test scenarios. Review them carefully. The AI will sometimes generate scenarios that are good ideas in general but wrong for your specific context. I've had it produce intense security test scenarios for a desktop tool I was building for myself. That's over-engineering. Cut what doesn't belong.

This is acceptance-test-driven development, not classic TDD. The distinction matters when you're working with agents. Classic TDD operates at the unit level: write a failing test for a small piece of logic, make it pass, refactor. That's a powerful discipline for a human developer building up a solution incrementally with fast feedback on every decision. But when you hand that workflow to an agent, you're micromanaging at the wrong level. You're telling it to think one function at a time, which means it never sees the bigger picture and can't make architectural decisions.

ATDD works at the scenario level. You define a behavior the system should exhibit from the user's perspective, write a failing acceptance test for that scenario, make it pass, then refactor. One scenario at a time. The failing test proves you're testing something real. Making it pass proves the code works. Refactoring keeps the codebase clean before you move to the next scenario. The agent has enough scope to decide how to structure the code, which components to create, and how they should interact, because it's solving for a meaningful outcome instead of an isolated unit. Unit tests still get written along the way, but the agent generates them as part of making the scenario pass, not as the primary driver.

On a good team, nobody starts coding until everyone agrees on what success looks like. Same principle applies here.

### Build Focused Specialists with an Orchestrator

On a good human team, you have generalists with overlapping, complementary specialist skills. Everyone contributes
broadly, but each person also brings depth in specific areas. With agents, you take that principle and sharpen it:
create focused specialist agents for specific quality checks. A narrow focus with an optimized context window produces more
accurate results. When you stuff an agent's context with everything in the repository and ask it to "check quality," you
get vague, generic feedback. It's the same thing that happens when you tell a human team member to "just make it good."
When you give an agent a specific job and only the information relevant to that job, it catches things a human reviewer
would miss. This is the same principle behind Unix pipelines: small, sharp tools composed together beat one monolithic
tool every time.

An orchestrating agent with the overall feature context coordinates the work, the same way a team lead who understands the full picture makes sure the specialists are pulling in the same direction.

Set up focused agents for the different aspects of quality:

- A test review agent that validates tests are well-written and declarative
- An architecture agent that checks for clean, modular structure
- A domain agent that validates proper design patterns
- A naming agent that ensures names are meaningful throughout the application

"Why do names matter if AI generates the code?" Because names provide context for every agent that touches the code going forward. Meaningless names mean agents misuse things, regenerate things unnecessarily, and lose track of what's what. Names are more important now than they were before, not less. Clear communication between team members prevents compounding mistakes, whether those team members are human or not.

I still use static analysis tools and unit testing for everything that's rule-based. Agents handle the things that take judgment.

### Let the Team Work

Define your coding agent to use acceptance-test-driven development. Take the first scenario from the first feature.
Write the test. Make it pass. Never skip a test. Never alter a test to make things pass. After writing each test, have
the test review agent check it for completeness and make sure it describes what should happen, not how it should happen.
Brittle tests that break when implementation changes are worse than no tests. So, have a test review agent review the
tests for implementation coupling and edge case completeness.

Don't tell the agent how to write the code. Tell it what the code should do. You wouldn't dictate every keystroke to a teammate. You'd share the context, define the acceptance criteria, and trust them to deliver, then review the work together. Same approach here.

I use adversarial cross-checking across the team. The coding agent writes, the test review agent validates the tests, the architecture agent validates the structure. They build guardrails and controls, just like I would for a human team. The difference is I can automate the controls that used to require manual review.

### Validate Outcomes, Not Activity

Once a feature is done, I validate whether it does what I intended it to do. If there's a mismatch between what I wanted and what I told the team, I fix my instructions, not the code. Then the team adjusts and we try again. The miscommunication was mine. I gave bad information.

After that, I run the pre-commit checks. All the static analysis, all the CI tests, all the review agents run and verify everything passes. Rules-based checks handle rules. Judgment-based agents handle judgment.

After I build my automated quality process, I don't look at the code anymore. I can't. It's dangerous. That sounds
radical, but think about what happens when I do. If I manually review every line, I become the constraint. Everything
waits on me. That means batching up more work before each review, which means larger deliveries, which means more risk
that we're building the wrong thing even if we're building it the right way. Manual code review recreates the same
bottleneck that manual QA gates create: it feels like quality, but it slows feedback and increases batch size. If the
tests prove the code does what it should, the architecture agents confirm the structure is clean, and the static
analysis passes, what exactly am I looking for by reading the code?

[You can find my reference review architecture here.](https://bdfinst.github.io/ai-patterns/agentic-code-review/)

### Post-Delivery Review for Critical Components

Senior engineers often review critical code after it's been delivered. This doesn't disrupt the flow of delivery or increase batch size risk—the feature is already in production, getting real feedback. These reviews focus on identifying opportunities for improvement in components that matter most: security-sensitive code, high-traffic paths, or foundational abstractions that many other features depend on.

This is different from pre-merge code review as a gate. A gate forces batching. Post-delivery review is continuous improvement. The code shipped on time with automated quality checks. The senior review happens afterward to find optimizations, security hardening, or architectural improvements that weren't obvious during initial development. It's learning applied to code that's already delivering value.

These reviews often reveal patterns that should be captured in your review agents or added to your static analysis rules. When you find the same issue twice, automate the check. The goal isn't to create a second gate—it's to continuously improve your automated quality system so it catches more over time.

## The Leadership Lesson

This workflow takes maybe 20 to 30 minutes of planning for any normal-sized feature. Then I go drink coffee while the
team builds and keep an eye on how things are going to see if I need to tweak an agent or the information. Things that would have taken me days or weeks now finish in minutes or hours. After 30 years of doing this
job, I have a reliable baseline for how long things take, both for work I've done before and for research into things I
haven't. The acceleration is real.

But here's what nobody wants to hear: AI is a high-pass filter for your leadership and engineering discipline. If you have the discipline of continuous delivery, of test-driven development, of defining what you're building before you build it, an agentic team gives you a dramatic improvement. If you don't have that discipline, you'll struggle. You'll generate garbage faster and spend all your time cleaning it up.

The developers who complain that AI produces bad code are often the same developers who think testing comes later or that coding is the work. They never decompose work into testable outcomes before starting. They never define a pipeline to validate changes. They never build a system of quality checks, never execute a CI workflow with small, focused tasks that build to the goal. They jump into the code and write a feature. Their workflow also includes constant rework that they don't notice because it's been normalized. When they apply that workflow to agents, they get a mirror of their work methods.

## Getting Started

1. **Set the mission.** Three to five sentences. What you're building and why, not how.
2. **Plan with the team.** Have the agent generate a plan. Give it feedback. Agree on the approach.
3. **Define "done" first.** Gherkin features. Prune anything that doesn't belong.
4. **Build focused specialists with an orchestrator.** Review agents for tests, architecture, naming, domain patterns, coordinated by an agent with overall context.
5. **Let the team code.** Define what the code should do and let them deliver it.
6. **Validate outcomes, not activity.** If the tests pass and the architecture is clean, ship it.
7. **Run your pipeline.** Pre-commit checks, all agents, all analysis. Every time.

Leading an agentic team takes the same skills as leading any development team: ensuring the right information flows at the right time, both business context and technical context. Define the mission. Share the "why." Build quality processes. The difference is that those skills now pay compound interest. If you don't have them yet, that's the first thing to learn. Not prompt engineering. Not which model is best. Learn how to make sure a team has what it needs to deliver. The agents are ready when you are.
