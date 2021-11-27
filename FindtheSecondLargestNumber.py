'''
Title     : Find the Runner-Up Score!
Subdomain : Data Types
Domain    : Python
Author    : Devraj Ganguly
Created   : 15 July 2021
Problem   : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr), reverse=True)[1])
