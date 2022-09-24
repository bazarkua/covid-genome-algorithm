Measuring the evolution of the COVID genome algorithm. The edit
distance d between two strings s1 and s2 is the minimum number of insertions, deletions, and
substitutions necessary to transform s1 into s2. The length k of the longest common
subsequence between two strings s1[1,...,n1], s2[1,...,n2] is the largest value k such that there
exist indices 1 ≤i1,1 < ···< ii,k ≤n1 and 1 ≤i2,1 < ···< i2,k ≤n2 such that s1[i1,j ] = s2[i2,j ] for
all 1 ≤j ≤k.
This algorithm implements the dynamic programming. As input, program will take the names file1 and file2. As output, it
will print two numbers: the edit distance d between and length k of the longest common subsequence
of the text in file1 and file2 but with all numbers, whitespaces, and punctuation removed so
that just letters remain. I.e., your program should produce strings s1 and s2 corresponding to the
text in the inputs files but with all numbers, whitespaces, and punctuation from the strings, and
then computes the edit distance d between and length k of the longest common subsequence in s1
and s2.