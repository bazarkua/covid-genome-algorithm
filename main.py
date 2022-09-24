import sys

def file_contents_letters(file_name):
    """
    Takes a file name as input and returns a string consisting of the file's contents
    with all non-letter characters removed.
    
    Parameters:
        file_name: The name of the file.
    
    Returns:
        A string with the contents of <file_name> but with all non-letter characters removed.
    """

    f = open(file_name, "r")
    file_contents = f.read()
    f.close()
    return "".join([c for c in file_contents if c.isalpha()])
    
def edit_distance(s1, s2):
    """
    Computes the edit distance between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
    
    Returns:
        The edit distance between s1 and s2.
    """

    # TODO: Implement this function!
    
    #Initilize 2D array for our Matrix
    EditDistance = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]

    #Fill out Matrix
    for i in range(len(s1) + 1):
        EditDistance[i][0] = i

    #Fill out Matrix
    for j in range(len(s2) + 1):
        EditDistance[0][j] = j

    #Checking subproblems for matching between s1 and s2
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                EditDistance[i][j] = EditDistance[i - 1][j - 1]
            else:
                insertion = 1 + EditDistance[i][j - 1]
                deletion = 1 + EditDistance[i - 1][j]
                replacement = 1 + EditDistance[i - 1][j - 1]
                EditDistance[i][j] = min(insertion, deletion, replacement)
    #print(EditDistance)
    
    return EditDistance[len(s1)][len(s2)]
    
def longest_common_subsequence(s1, s2):
    """
    Computes the length of the longest common subsequence between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
    
    Returns:
        The length of the longest common subsequence between s1 and s2.
    """

    # TODO: Implement this function!
    
    #Initilize 2D array for our Matrix
    LongestCommonSub = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    
    #Fill out row of the Matrix
    for i in range(len(s1) + 1):
        LongestCommonSub [i][0] = 0

    #Fill out columns of the Matrix
    for j in range(len(s2) + 1):
        LongestCommonSub [0][j] = 0

    #Find matches between s1 and s2, then if matches continue by piking max val from subproblems
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                LongestCommonSub[i][j] = 1+LongestCommonSub[i-1][j-1]
            else:
                LongestCommonSub[i][j] = max(LongestCommonSub[i-1][j], LongestCommonSub[i][j-1])
    
    i = len(s1)
    j = len(s2)
    index = LongestCommonSub[len(s1)][len(s2)]
    longest = ""
    
    while i > 0 and j > 0:
  
        if(s1[i-1] == s2[j-1]):
            longest = longest + s1[i-1]
            i-=1
            j-=1
            index-=1

        elif LongestCommonSub[i-1][j] > LongestCommonSub[i][j-1]:
            i-=1
        else:
            j-=1
    
    #We print reversed, because in while loop above we added chars from the end to beginning
    print("Extra Credit:",''.join(reversed(longest)))

    return LongestCommonSub[len(s1)][len(s2)]

s1 = file_contents_letters(sys.argv[1])
s2 = file_contents_letters(sys.argv[2])
print(edit_distance(s1, s2), longest_common_subsequence(s1, s2))
