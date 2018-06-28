# Edmond-S-MST-Python

## Goal
This project deals with the segmentation of  sentences into parts using syntactic analysis.
The setences are in the form of directed , weighted graphs stored in graphml format.Each node represents a word having the following  attributes : 
- chunk number 
- morph
- lemma 
- position id 
- starting index
- length of the word,
and every edge between the nodes is assigned an attribute named weight.

## Steiner Tree
A Steiner tree is one which spans though a given subset of vertices selected from a graph. 
Words having the same chunk number represent sandhi which occur prominently in the phonology of Indian languages. 
A Sandhi is a cover term for a wide variety of phonological processes that occur at morpheme or word boundaries.
A sandhi can be identified from a list of nodes having the same chunk number whose starting or ending indices overlap with the one another,among which only one node has to be selected.
The Steiner tree algorithm aims at spanning only those set of selected nodes and forming a maximum spanning subtree using its adjacent edges.`Steiner_Tree.py` forms a maximum spannning arborescence of the subgraph on user choice.

## Edmond's Chu Liu Algorithm
`MST.py` is a python implementation of Chu-Liu/Edmond's algorithm to find the minimum spanning tree in a directed graph.Edmond's Chu Liu Algorithm spans the entire set of nodes in the graph to form a maximum spanning arborescence.

## Testing Steiner_Tree.py
Run the code :
- Case 1 : Maximum Spanning Arborescence (user input = 0) *Syntax : `python` `Steiner_Tree.py` `0` `<Directory of the folder containing the graphml files>`
- Case 2 : Maximum Spanning Arborescence of the subgraph(user input = 1) *Syntax: `python` `Steiner_Tree.py` `1` `<Directory of the folder containing the graphml files>`
 
 ## Sample Input:
 - `Sample Input.graphml` is a sample graphml file having the aforementioned node and edgeattributes
 - `graph.zip` containing 10,000 graphs in graphml format has been provided for further use
 
 
 
