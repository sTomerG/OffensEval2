import csv
import json

languages = ['arabic', 'danish', 'greek', 'turkish']
for lang in languages:
    labels = [json.loads(line)['label'] for line in open(f'data/{lang}/pred_dev.txt', 'r')]
    texts = [json.loads(line)['text'] for line in open(f'data/{lang}/dev_data.json', 'r', encoding="utf8")]
    correct_labels = [json.loads(line)['label'] for line in open(f'data/{lang}/dev_data.json', 'r', encoding="utf8")]

    with open(f'data/{lang}/summary.csv', 'w', newline='', encoding="utf8") as out_file:
        tsv_writer = csv.writer(out_file, delimiter=',')
        off_not = 0
        not_not = 0
        not_off = 0
        off_off = 0

        for text, correct_label, label in zip(texts, correct_labels, labels):
            if correct_label != label:
                if correct_label == "NOT":
                    not_off += 1
                else:
                    off_not += 1
            else:
                if correct_label == "NOT":
                    not_not += 1
                else:
                    off_off += 1
            tsv_writer.writerow([correct_label, label, text])

        tsv_writer.writerow([])
        tsv_writer.writerow(["not_not", "off_not", "not_off", "off_off"])
        tsv_writer.writerow([not_not, off_not, not_off, off_off])
