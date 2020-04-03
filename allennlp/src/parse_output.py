import csv
import json

languages = ['arabic', 'danish', 'english', 'greek', 'turkish']
for lang in languages:
    labels = [json.loads(line)['label'] for line in open(f'data/{lang}/pred_test.txt', 'r')]
    idds = [json.loads(line)['id'] for line in open(f'data/{lang}/test_data.json', 'r', encoding="utf8")]

    with open(f'data/{lang}/result.csv', 'w', newline='', encoding="utf8") as out_file:
        tsv_writer = csv.writer(out_file, delimiter=',')
        for idd, label in zip(idds, labels):
            tsv_writer.writerow([idd, label])
