def print_formatted(number):
    # your code goes here
    w = len(str(bin(n)).replace('0b',''))
    for i in range(1,number+1):
        print(str(i).rjust(w, ' '),oct(int(i)).replace('0o','').rjust(w, ' '),hex(int(i)).replace('0x','').upper().rjust(w, ' '), bin(int(i)).replace('0b','').rjust(w, ' '))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)