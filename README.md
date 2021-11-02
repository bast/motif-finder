# motif-finder

A tiny example that shows how one can pattern match motifs using regular expressions.


### How to run the example

```console
$ python example.py

GAAA.{1,2}GAAA found in ...
Example 1 [(408, 417)]

TTC.{2,4}GAA found in ...
Example 1 [(157, 165)]
Example 2 [(8, 16)]
Example 3 [(5, 13)]
Example 5 [(147, 156)]
Example 8 [(10, 20)]
Example 13 [(345, 354), (359, 368)]

ATTGG found in ...
Example 1 [(85, 90)]
Example 3 [(91, 96)]
Example 6 [(216, 221)]
Example 7 [(216, 221)]
Example 9 [(56, 61)]
Example 10 [(62, 67)]
Example 11 [(58, 63)]
Example 12 [(56, 61)]
Example 13 [(77, 82)]
```
