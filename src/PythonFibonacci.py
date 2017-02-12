# coding:utf-8
import os

def add(x, y): return x + y

def fibonacci_formula(n):
    fib = [1, 1]
    for i in range(n):
        fib.append(add(fib[i],fib[i+1]))
    print 'Fib[%d]: %d' %(n,fib[n])

def main():
    for i in range(100):
        fibonacci_formula(i)
    
main()
