import sys
from collections import defaultdict

current_document = None
current_count = 0
word = None
isOutputNull = True
document = None
total_count = 0

ranking_dictionary = defaultdict(int)   # This is for ranking part. Use of Data Structures were allowed.
current_occurances = 0  # This is for ranking part.
for line in sys.stdin:
    line = line.strip()
    document, word, total_count, occurance = line.split('\t')
    try:
        total_count = int(total_count)
    except ValueError:
        continue

    if current_document == document:
        current_count += 1
        current_occurances += int(occurance)
    else:
        if current_document and (current_count == total_count):
            isOutputNull = False
            ranking_dictionary[current_document] = current_occurances
            # print('%s' % (current_document))
        # resetting everything
        current_count = 1
        current_document = document
        current_occurances = int(occurance)
if current_document and current_document == document and current_count == total_count:
    isOutputNull = False
    ranking_dictionary[current_document] = current_occurances
    # print('%s' % (current_document))

# Sort dictionary based on the scores in reverse manner
ranked_dictionary = dict(sorted(ranking_dictionary.items(), key=lambda item: item[1], reverse=True))

for key in ranked_dictionary.keys():
    print('%s' % (key)) # Printing the DocIds
    # print(key, ranking_dictionary[key])