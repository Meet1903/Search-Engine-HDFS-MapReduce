# Serach Engine using Map Reduce

This project is aimed at building a Search Engine capabilities using HDFS & MapReduce. The task is to read all the files under Documents folder and generate inverted index for all words and use to build a Search Engine.

### Files & its work:
1. mapper-1.py

    **Task**: To print words, DocID.

    **Logic**:  
    - First extract Document ID using Regular Expression.
    - Extract words from input files.
    - Split words on any characters other than alphanumeric.
    - Print word and DocID. (word as key)

2. reducer-1.py

    **Task**: Generate Inverted Index.

    **Logic**:  
    - As the key is “word” in the Mapper. The input to the mapper would be sorted based on “word”.
    -  This means that similar words will be together in the input.
    -  Just like the counting problem, we find all the DocIDs where the word is present.
    - Remove the duplicate DocIDs.
    - Print words, DocIDs, and occurrences in output.

3. mapper-2.py

    **Task**: Find DocIDs for the user input sentence.

    **Logic**:  
    - Run through the entire output file of the last MapReduce code.
    - If any word is present in the input sentence, collect the DocIDs.
    - Print DocID, word, total words in the input sentence, occurrences.
    - Here the key is DocID.
    - Total words in input sentence helps in deciding whether all words are present in the particular Document.
    - Total occurrences helps in the ranking part.

4. reducer-2.py

    **Task**: Find DocIDs where all words are present.

    **Logic**:  
    - As the key in Mapper output was DocID. Similar DocID will be together.
    - Now the same logic as the counting problem, will find the count of DocID present in the output of Mapper.
    - If the count of DocID is the same as count of total words, that means that particular Document contains all the words.
    - Ranking logic:
        - While collecting DocIDs, collect occurrences of each word in the Document as well.
        - For this search engine, higher the total occurrences, higher the rank.

### Commands to run the code.

```
mapred streaming -D mapred.min.split.size=10000000000 -input Documents/*.txt -output output-1 -mapper "python mapper-1.py" -reducer "python reducer-1.py" -file mapper-1.py -file reducer-1.py
```

```
hdfs dfs -cat output-1/part* | sort > result-mapred-1.txt
```

```
mapred streaming -D mapred.min.split.size=10000000000 -input result-mapred-1.txt -output output-2 -mapper "python mapper-2.py can you judge Italian cooking well?" -reducer "python reducer-2.py" -file mapper-2.py -file reducer-2.py
```

```
hdfs dfs -cat output-2/part* > result-mapred-2.txt
```
