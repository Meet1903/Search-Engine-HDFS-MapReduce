import sys
from collections import defaultdict

current_word = None
word = None
documents = ''
previous_doc_id = ''

# Dictionary is used for storing the occurances. This is for ranking part only. This has nothing to do with the Map Reducer.
# This does not break the rules. As it is not being used for finding inverted Index.
# All operations for finding inverted index are done using String manipulations.
occurances = defaultdict(int) 

for line in sys.stdin:
    line = line.strip()

    word, doc_id = line.split('\t')

    if current_word == word:
        occurances[doc_id] += 1 # Update the occurance
        if doc_id != previous_doc_id:
            documents += str(doc_id) + ','
            previous_doc_id = doc_id
    else:
        if current_word:
            result_docIDs = ',' # Inverted Index result
            result_occurances = ''  # Occurences result
            for document in documents.strip(',').split(','):
                if ',' + document + ',' not in result_docIDs:
                    result_docIDs += document + ','
                    result_occurances += str(occurances[document]) + ','
            result_docIDs = result_docIDs.lstrip(',')
            print('%s\t%s\t%s' % (current_word, result_docIDs, result_occurances))
        # Reseting everything
        current_word = word 
        documents = str(doc_id) + ','
        previous_doc_id = doc_id
        occurances = defaultdict(int)
        occurances[doc_id] += 1
if current_word == word:
    result_docIDs = ''  # Inverted Index result
    result_occurances = ''  # Occurences result
    for document in documents.strip(',').split(','):
        if ',' + document + ',' not in result_docIDs:
            result_docIDs += document + ','
            result_occurances += str(occurances[document]) + ','
    result_docIDs = result_docIDs.lstrip(',')
    print('%s\t%s\t%s' % (current_word, result_docIDs, result_occurances))