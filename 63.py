#Powerful digit counts
#Problem 63

#The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
#How many n-digit positive integers exist which are also an nth power?

def main():
    cnt = 0
    for i in range(1, 10):
        for j in range(1, 22):
            ps = pow(i,j)
            #Check wheather the digit of number is same as power
            if len(str(ps)) == j:
                print ps, i, j
                cnt = cnt + 1
    print "cnt", cnt

if __name__ == '__main__':
    main()

'''
1 1 1
2 2 1
3 3 1
4 4 1
16 4 2
5 5 1
25 5 2
125 5 3
6 6 1
36 6 2
216 6 3
1296 6 4
7 7 1
49 7 2
343 7 3
2401 7 4
16807 7 5
117649 7 6
8 8 1
64 8 2
512 8 3
4096 8 4
32768 8 5
262144 8 6
2097152 8 7
16777216 8 8
134217728 8 9
1073741824 8 10
9 9 1
81 9 2
729 9 3
6561 9 4
59049 9 5
531441 9 6
4782969 9 7
43046721 9 8
387420489 9 9
3486784401 9 10
31381059609 9 11
282429536481 9 12
2541865828329 9 13
22876792454961 9 14
205891132094649 9 15
1853020188851841 9 16
16677181699666569 9 17
150094635296999121 9 18
1350851717672992089 9 19
12157665459056928801 9 20
109418989131512359209 9 21
cnt 49

The reason behind this i started with 
range(1, 10) --> cnt was 37
range(1, 100) --> cnt was 49
range(1, 200) --> cnt was 49
range(1, 300) --> cnt was 49
range(1, 1000) --> cnt was 49 --> Took too much time to complete but still 49 
was the answer.

Got concluded that this is constant for all range(1, n)..

109418989131512359209 9 21 --> This is the last result in the output.
Restricted the for loop in from range(1,10) to range(1, 22)

49 is the answer for this.
'''