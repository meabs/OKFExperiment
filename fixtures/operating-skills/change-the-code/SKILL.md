---
name: change-the-code
description: How to make a change safely in this repository: scope it, list every place it touches, edit minimally, then re-check. Read it before you edit anything.
---

# Making a change

A change is finished when every place it touches is changed and nothing else is. Work in this order.

1. **Write down the scope before you edit.** In one short list, name the thing you are changing exactly (owner, name, parameter types) and what you must not touch (same name on other classes, other overloads).
2. **Find every place it touches, then list them.** Include the definition, the interface, every class that implements or overrides it, every caller (including calls split over several lines and calls in other modules), and tests. Use `kg callers <name>` and `kg subclasses <type> --overrides <method>` first, then confirm each place in the source. Write the list down with file and line.
3. **Check the list against a second source.** Search the text for the name and explain every hit that is not on your list (a different class, a comment, a different overload). Do not edit a hit you cannot explain.
4. **Make the smallest edit that does the job.** Change only what the task states. Do not tidy, reorder, reformat or fix other things on the way. Keep the existing style.
5. **Change related places together.** A definition and all its implementations and callers must move in the same pass, or the code will not build.
6. **Do not guess.** If the task is ambiguous, pick the narrowest reading, say which you chose and why, and carry on.
7. **If something blocks the change, stop and say so.** Do not work around it with an edit the task did not ask for.
