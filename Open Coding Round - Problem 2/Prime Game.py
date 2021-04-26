''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    # Write code here 
    testCase = int(input())
    while testCase>0:
        LR = list(map(int,input().strip().split()))
        lst=[]
        for i in range(LR[0],LR[1]+1):
            isPrime = True
            for num in range(2, int(i ** 0.5) + 1):
                if i % num == 0:
                    isPrime = False
                    break
            if isPrime:
                lst.append(i)

        n=len(lst)
        if n>1:
            print(max(lst)-min(lst))
        elif n==1:
            print(0)
        else:
            print(-1)

        testCase -=1
main()
