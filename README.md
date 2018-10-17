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
python venkataraman.py
```
The results of the segmentation will be stored in `results/result.txt`.
