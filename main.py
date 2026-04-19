import json
from rag.retriever import create_retriever
from evaluation.evaluator import evaluate


with open("data/dataset.json") as f:
    dataset = json.load(f)


all_texts = []
for item in dataset:
    all_texts.extend(item["contexts"])

retriever = create_retriever(all_texts)

results = evaluate(dataset, retriever)

for r in results:
    print(r)

correct = sum([1 for r in results if r["correct"]])
total = len(results)

print(f"\nAccuracy: {correct}/{total} = {round(correct/total,2)}")