# Edmond-S-MST-Python
This project deals with the segmentation of  sentences into parts using syntactic analysis:
The setences are in the form of directed , weighted graphs stored in graphml format.Each node represents a word having the following  attributes : chunk number , morph, lemma, position id and the length of the word.
Words having the same chunk number represent sandhi which occur prominently in the phonology of Indian languages. 
A Sandhi is a cover term for a wide variety of phonological processes that occur at morpheme or word boundaries.
A sandhi can be identified from a list of nodes having the same chunk number whose starting or ending indices overlap with the one another,among which only one node has to be selected.
The Steiner tree algorithm aims at spanning only those set of selected nodes and forming a maximum spanning subtree using its adjacent edges.
Edmond's Chu Liu Algorithm spans the entire set of nodes in the graph to form a maximum spanning arborescence.
Steiner_Tree.py provides a user choice:
ch=0 results in a maximum spanning arborescence
ch=1 forms a maximum spannning arborescence of the subgraph
