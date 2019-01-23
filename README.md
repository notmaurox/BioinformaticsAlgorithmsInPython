# BioinformaticsAlgorithmsInPython
*Directory is work in progress with more work samples to be uploaded soon*

Various bioinformatics algorithms written for CSE 181: Molecular Sequence Analysis taught by Dr. Pavel Pevzner

## Kmer Counting - FreqWords.py + inputA.txt
#### Symbol2Number
Takes a nucleotide base letter as a character and returns number 0, 1, 2, or 3. Used for mapping nucleotide bases to unique numbers.
#### Number2Symbol
Takes a number 0, 1, 2, or 3 and returns a letter representing a nucleotide base. Used for returning nucleotide mapped to number.
#### Pattern2Number
Recursively turns a kmer consisting of A,C,T,G into a unique number where the last character gets turned into a number 0-3 and gets added to the score of the prefix value * 4.  
#### Number2Pattern
Recursively turns a number into its unique k-mer consisting of A,C,T,G where the number mod 4 recovers the contribution of the last character and the score of the prefix is recovered by computing the number div 4. With the prefix and the score of the prefix, a recursive call does the same thing until reaching the base case of the score of the first character in the kmer. 
#### hamDist
Returns the hamming distance between two strings where a mismatch between characters at same position contributes +1 to the distance. 
#### approxPatternCount
Given a string of text, a pattern, and distance d, this method scans the text and computes the hamming distance between each of its substrings of length(pattern). If the hamming distance from the substring to the pattern is less than input parameter d, a match counter is incremented. After scanning the entire text, the number if matches between pattern and substrings of text with at most d mismatches is returned. 
#### Neighbors
Computes a list of strings of length pattern - 1 that are at most d mismatches from the suffix of the input pattern. The base case is when the pattern only contains 1 character and a list containing A,C,G,T is returned.  From there, for each string that matches the suffix by at most d-1 mismatches, 4 new copies of the string are added to the neighbor collection with A,C,G,T appended to the front. If the string already contains d mismatches to the input pattern, only the character that matches the prefix is added to the front of the string. In the end this returns a list of all strings that match the pattern with at most  d mismatches. 
#### freqWordsWithMismatches
Make two lists that are 4^k long containing zeroes. First scan text and for each substring of length k, generate its neighbors with at most d mismatches. For each string in this collection, mark that they appeared in the close array with a 1. This can be completed in linear time due to Pattern2Number mapping each kmer to an index in the list. From there, for each string marked with a 1 in the close array, do approximate pattern count for that string in the text. Report how many times it appears with at most d mismatches in the frequency array at the index defined by turning the string into a unique index using Pattern2Number. From there scan the frequency array for the elements with max count. While the time complexity for scanning a list of 4^k elements seems extreme, relative to the length of text (a region of a genome), it is small. 

## BurrowsWheelerTransformPatternMatching.py

## BetterBurrowsWheelerTransformPatternMatching.py
Burrows Wheeler transform pattern matching with speed improvements through implementation of count matrix in addition to first to last mapping for faster jumping between columns of matrix as characters in query are searched.

## GlobalAlignment.py
For computing global alignment between two english words with functionality to define scoring matrix for precise point allocation for different character combinations. 

## LocalAlignment.py
For computing local alignment between two english words with functionality to define scoring matrix for precise point allocation for different character combinations. 
