def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2*hanoi(n-1) + 1 
    
print(hanoi(5))
