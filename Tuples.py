'''
Title     : Tuples
Subdomain : Data Types
Domain    : Python
Author    : Devraj Ganguly
Created   : 06 July 2021
Problem   : https://www.hackerrank.com/challenges/python-tuples/problem
'''
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))