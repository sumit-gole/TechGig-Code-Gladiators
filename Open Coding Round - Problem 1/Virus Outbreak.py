''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main(str1, str2):
  #write your code here
    m = len(str1)
    n = len(str2)

    j = 0
    i = 0 

    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j+1
        i = i + 1

    return j == m

# Driver Program
str2 = str(input())
N = int(input())

for i in range(N):
    str1 = str(input())
    if main(str1, str2):
        print("POSITIVE") 
    else:
        print( "NEGATIVE")
