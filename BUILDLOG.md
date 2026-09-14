# Build log

## 7 September 2026 — session 1

Set up from nothing.

- Created the repo, MIT licensed
- Installed VS Code, Python 3.14, configured Git
- Cloned locally, made the first push from my own machine

Two things fought back: python3 kept resolving to the old 3.9 until I fixed the PATH, and GitHub no longer accepts account passwords for pushes — needed a personal access token.

Next: start on the actual parsing.

## 10 September 2026 — session 2

Done from Amsterdam, straight off the train.

- Added Article 50 of the AI Act as source text:
  data/article_50.txt
- Source: EUR-Lex, Regulation (EU) 2024/1689, OJ text
  as published in 2024:
  https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng

What fought back: I first copied the wrong Article 50,
the TEU withdrawal clause. An article number alone
identifies nothing. The parser has to know which law
a provision belongs to.

Also learned: on a Mac, the menu bar belongs to
whichever app is in front.

Next: a script that splits Article 50 into paragraphs
and tags each one provider or deployer.


## Session 3 — Monday, 14 September 2026

First working code in the repo.

- Wrote `parse_article_50.py`: reads `data/article_50.txt`,
  splits it into numbered paragraphs with a regex lookahead,
  prints them.
- Found 8 chunks — the heading plus the seven paragraphs.
  Split was clean on the first run.
- Added a `who_owes()` tagger: looks at the opening 80
  characters of each paragraph and returns provider,
  deployer, or unknown.
- Result: 1 and 2 provider, 3 and 4 deployer, 5 / 6 / 7
  unknown.

What fought back: nothing in the code. The law did.
Paragraphs 5, 6 and 7 don't name a provider or a deployer
because they aren't that kind of provision — 5 is a rule
about how the first four must be discharged, 6 is a savings
clause, 7 puts a duty on the AI Office. Two boxes is the
wrong shape. Naming the third category is the next job.

Commits: 7c18ca7, 110cd6a