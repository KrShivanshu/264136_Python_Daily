if __name__ == '__main__':
    n = int(input())

def seq(x):
    s='1'
    for i in range(2,x+1):
        s=s+str(i)
    return s

print(seq(n))