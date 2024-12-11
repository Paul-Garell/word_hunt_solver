# Word Hunter

1) user input a board
2) compute DFS over a 4x4 grid and save paths 3 or longer
3) create set of all words from paths
4) filter set based on real words


Optimizations:
- 
- caching: zero improvement. Likely because the board is small. I expect performance boost for large board size
- DFS
- Sets

Future features:
- detect board from picture. Use a cnn to read in letters
- 