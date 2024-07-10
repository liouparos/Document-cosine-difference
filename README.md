# Cosine Similarity Tool

This Python script calculates the cosine similarity between multiple text files. It processes the text to remove certain characters and convert it to lowercase, then calculates the term frequency vectors for each text file and determines the cosine similarity between them.

### Requirements

```
Python 3.x
numpy
scikit-learn
```

### Installation

You can install the required Python packages using pip:
```
pip install numpy scikit-learn
```

### Usage

Run the script with the following command:
```bash
./text_similarity.py N file1.txt file2.txt file3.txt ...
```

N is the number of top similarity results you want to display.
file1.txt, file2.txt, file3.txt, etc., are the text files you want to compare.

### Example

```
./text_similarity.py 5 document1.txt document2.txt document3.txt
```
This will output the top 5 pairs of documents with the highest cosine similarity.


### How It Works

Read Input Files: The script reads the text files provided as arguments and splits them into lists of words.
Preprocess Text: The text is processed to remove specified characters and convert to lowercase.
Build Dictionary: A unique list of words is created from all text files combined.
Calculate Similarity: For each pair of text files, the script calculates the cosine similarity between their term frequency vectors.
Output Results: The script prints the top N pairs of text files with the highest cosine similarity.

### Example Output

```
Cosine difference of document1.txt, document2.txt is 0.8765
Cosine difference of document2.txt, document3.txt is 0.8453
...
```
The output shows the cosine similarity between pairs of documents, sorted in descending order.

### Notes
The script removes specific characters (!@#$(),.) from the text before processing.
The cosine similarity values range from 0 to 1, where 1 means the documents are identical in terms of term frequency.
