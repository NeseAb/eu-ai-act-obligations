import re

with open("data/article_50.txt", "r", encoding="utf-8") as f:
    text= f.read()

paragraphs = re.split(r"\n(?=\d+\.)", text)

print(f"Found {len(paragraphs)} chunks\n")

heading = paragraphs[0]
provisions = paragraphs[1:]

def who_owes(p):
    opening = p[:80].lower()
    if "provider" in opening:
        return "provider"
    if "deployer" in opening:
        return "deployer"
    return "unknown"

for p in provisions:
    number = p.split(".")[0].strip()
    print(f"[{who_owes(p):8}] {number}. {p[:70].strip()}...")