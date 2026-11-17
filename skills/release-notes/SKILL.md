---
name: release-notes
description: Write release notes for the to-do app from its git log. Use when asked for release notes or a changelog.
---

# Release notes

1. Find the range: from the latest tag to `HEAD` (`git describe --tags --abbrev=0`), or the whole history when there is no tag.
2. Read the commits in that range: `git log --no-merges --format='%h %s' <range>`.
3. Put each commit in one group: Added, Changed, Fixed or Other. Leave out commits that only touch tests, unless nothing else changed.
4. Write one line for each change, in words a user of the app understands: say what changed for them, not which function changed.
5. When a commit names an issue or a pull request (`#1`), keep the number in the line.
6. Leave out a group that has nothing in it.
7. Start with a heading: `## <version, or Unreleased> (<today's date>)`.
8. Do not invent changes. When a commit message is unclear, say so under Other.
9. Give the notes back as Markdown. Do not commit, tag or publish anything unless you are asked to.
