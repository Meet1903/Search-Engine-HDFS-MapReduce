import sys
import re

words_found = ''
unique_words = ' '
foundDocIds = ','
unique_documentId_found = ','
missing_words = ''

input_sentence = str(sys.argv[1:])
input_sentence_new = re.split(r'[^a-zA-Z0-9]+', input_sentence.lower())

for word in input_sentence_new:
    if ' ' + word + ' ' not in unique_words:
        unique_words += word + ' '

unique_word_count = len(unique_words.strip().split(' '))    # This is to compare the total DocIds in reducer part.

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split('\t')
    if words[0] in input_sentence_new:
        words_found += words[0] + ' '
        for document, occurance in  zip(words[1].split(','), words[2].split(',')):
            if document:
                foundDocIds += document + ','   # This is to maintain record of documentIDs found.
                print('%s\t%s\t%s\t%s' % (document, words[0], unique_word_count, occurance))   # Here I've passed DocID, word, and count of unique words

# Below function is to remove duplicate DocIds from foundDocIds.
for document in foundDocIds.strip(',').split(','):
    if ',' + document + ',' not in unique_documentId_found:
        unique_documentId_found += document + ','
unique_documentId_found = unique_documentId_found.strip(',')

# Below function is to again print all DocumentIds from the x times. Where x = unique_word_count - count(words_found)
for word in unique_words.strip().split(' '):
    if word not in words_found:
        for document in unique_documentId_found.split(','):
            print('%s\t%s\t%s\t%s' % (document, word, unique_word_count, '0')) # This is to handle the case if the word is missing   


