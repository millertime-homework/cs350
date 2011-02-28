#!/usr/bin/python

import sys

def main():
    # dimensions of each matrix
    a = [5,10,3,12,5,50,6]

    m,s = matrix_chain_order(a)

    for line in m:
        print(line)
    for line in s:
        print(line)

    print_opt_parens(s,1,6)
    sys.stdout.write('\n')

def matrix_chain_order(p):
    n = len(p) - 1
    m = []
    s = []
    for i in range(n):
        m.append([])
        s.append([])
        for j in range(n):
            m[i].append(0)
            s[i].append(0)
    
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j = i + l - 1
            m[i-1][j-1] = 9999
            for k in range(i,j):
                q = m[i-1][k-1] + m[k][j-1] + p[i-1]*p[k]*p[j]
                if q < m[i-1][j-1]:
                    m[i-1][j-1] = q
                    s[i-1][j-1] = k
            
    return m,s

def print_opt_parens(s,i,j):
    if i == j:
        sys.stdout.write("A_" + str(i) + " ")
    else:
        sys.stdout.write("(")
        print_opt_parens(s,i,s[i-1][j-1])
        print_opt_parens(s,s[i-1][j-1] + 1, j)
        sys.stdout.write(")")


if __name__=="__main__":
    main()
