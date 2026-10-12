---
name: check-your-work
description: How to check a change before you report it done, when you cannot build or run tests. Read it before you finish.
---

# Checking your work

You may have no compiler or test runner here. Check by reading, and say what you did and did not check.

1. **Re-run the search that found the places.** Run the same graph query and text search again. Every place on your list must now show the new form, and no place that should keep the old form may have changed.
2. **Read your own diff.** Run `git diff --stat`, then read the diff. Every changed line must be on your list. Remove any change that is not.
3. **Count.** The number of places you changed must equal the number on your list. If it does not, find the difference.
4. **Look for the near misses.** Check the cases that are easy to get wrong: calls split over several lines, calls through the interface, overloads with the same name, and implementations in another module.
5. **Report plainly.** State what you changed (files, count), what you checked and how, and anything you were unsure of. Do not claim a build or a test that you did not run.
