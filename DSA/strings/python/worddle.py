# cook your dish here
n = int(input())
for i in range(n):
    S = input()
    T = input()
    M = ""
    for i in range(len(S)):
         if S[i] == T[i]:
              M += "G"
         else:
              M += "B"
    print(M)