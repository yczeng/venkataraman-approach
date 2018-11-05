# venkataraman-approach

This is a python reimplementation of the maximum-likelihood estimation approach proposed by Anand Venkataraman for unsupervised word segmentation.

The paper describing the approach can be found at the link [here](http://www.aclweb.org/anthology/J01-3002)

As of 10/17/18, this repo only implements backoffs for unigrams and phonemes.
To run, clone the repo:
```
git clone https://github.com/yczeng/venkataraman-approach.git
```
cd into the directory, and run:
```
python search.py
```
The results of the segmentation will be stored in `results/result.txt`.

## Scoring
Performance is measured using precision, recall, and F-score.

Precision is the number of correct words found out of all words found, recall is the number of correct words found out of all correct words, and F-scores it he geometric average of pricision and recall (2 * precision * recall) / (precision + recall).

To score a segmented lexicon, run `score.py [segmented lexicon] [model lexicon]` where segmented lexicon and model lexicon are text files containing a dictionary of words in the lexicon. An example command is:

`python score.py results/lexicon.txt data/Bernstein-Ratner87-lexicon`

It looks like results are:
```
Precision: 0.526275115919629
Recall: 0.5155185465556397
f1 Score: 0.5208413001912047
``` 