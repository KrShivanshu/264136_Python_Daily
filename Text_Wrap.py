import textwrap

def wrap(string, max_width):
    list = ""
    for i in range(0,len(string)+1,max_width):
        list += (string[i:i+max_width]) + "\n"
    return list

if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)