---
name: triage
description: "Triage the to-do app's issues: label each bug, feature or question and say why. Use when asked to triage or sort issues."
---

# Triage

1. List the open issues: `gh issue list --state open --json number,title,body,labels`.
2. Read each issue's title and body. For a reported bug, follow its steps with `python todo.py` in an empty scratch directory, so the real `todo.json` stays untouched.
3. Give each issue exactly one label:
   - `bug`: the app does something wrong, and you could reproduce it or the steps are clear;
   - `feature`: it asks for something the app does not do yet;
   - `question`: it asks how something works.
4. Say why in one sentence for each issue, naming the evidence: what you ran and what happened, or the words in the issue.
5. Report a table: number, title, label, why.
6. Apply the labels only when you are asked to: `gh issue edit <number> --add-label <label>`. Create a missing label with `gh label create <label>` first.
7. Do not close, assign or comment on an issue unless you are asked to.
