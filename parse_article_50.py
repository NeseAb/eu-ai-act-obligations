import re

with open("data/article_50.txt", "r", encoding="utf-8") as f:
    text= f.read()

paragraphs = re.split(r"\n(?=\d+\.)", text)

print(f"Found {len(paragraphs)} chunks\n")
for i, p in enumerate(paragraphs):
    print(i, "|", p[:60].replace("\n", " "))