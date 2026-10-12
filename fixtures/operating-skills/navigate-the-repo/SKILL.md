---
name: navigate-the-repo
description: How to find your way around this repository before you answer a question or plan a change. Read it first.
---

# Navigating this repository

The repository is large and many names repeat. Orient first, then dig. This is a way of working, not a description of the code.

1. **Start with the map.** Read `okf/index.md`. It lists every module and package and links to a file for each. Open only the files that match your question.
2. **Ask the graph before you search text.** For "who calls this", "what uses this type", "what would break if this changed" and "how does A reach B", run the `kg` command from `AGENTS.md` first. It answers from the parsed code in one call and is faster than reading files. Use `kg find <name>` to get the exact identifier.
3. **Treat every generated line as a lead, not a fact.** Each line cites a file and line. Open that line before you rely on it, especially lines marked `[medium]`, and always when your decision depends on it.
4. **Names repeat; identity does not.** Several methods can share a name across classes, and one class can have several overloads. Decide which one you mean by its owner and its parameter types, never by name alone. When a count from a text search is far larger than the graph's count, find out why before you go on.
5. **Code in comments is not code.** A line that sits inside a comment is not a caller or a definition.
6. **Know when to stop.** When two independent routes (the graph and the source) agree, stop looking. When they disagree, trust the source and note the disagreement in your answer.
7. **Say what you used.** End with the files and commands your answer rests on.
