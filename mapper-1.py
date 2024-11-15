import sys
import re

doc_id_pattern = re.compile(r'DocID:(\d+)', re.IGNORECASE)
doc_id = None
for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    matchpattern = doc_id_pattern.match(line)
    if matchpattern and matchpattern.group(1):
        doc_id = matchpattern.group(1)
    if doc_id:
        for word in words:
            # word = re.sub(r'[^\w\s]', '', word)
            split_words = re.split(r'[^a-zA-Z0-9]+', word)  #Split words on special characters
            if split_words:
                for split_word in split_words:
                    if split_word:
                        print('%s\t%s' % (split_word, doc_id))