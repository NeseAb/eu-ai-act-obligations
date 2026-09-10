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