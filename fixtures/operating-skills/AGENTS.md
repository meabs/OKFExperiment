# Working in this repository

This repository is large and has many repeated names. Knowledge for it is in three places. It was generated or written to help you work here, so use it, then confirm in the source before you rely on it.

- **`okf/`**: a guide generated from the source. One file per package, with the file and line each fact came from. Start at `okf/index.md`.
- **`.agent-knowledge/bin/kg`**: a code graph you can query. For structural questions run it before you grep:
  - who calls a method: `kg callers <method>` (add `--depth 3` for callers of callers)
  - what breaks if something changes: `kg impact <type or method>`
  - every implementation or subclass: `kg subclasses <type>` (add `--overrides <method>`)
  - how two things connect: `kg path <from> <to>`; find an exact name: `kg find <text>`
- **`.agents/skills/`**: how to operate here. Read the matching one before you start:
  - `navigate-the-repo` before you explore or answer a question
  - `change-the-code` before you edit anything
  - `check-your-work` before you report a change as done

Lines marked `[medium]` are inferences, not facts read from the code. Use the guide and the graph to find your way around, then read the source to confirm before you rely on it. If a generated claim is wrong, trust the source and say so in your final message.
