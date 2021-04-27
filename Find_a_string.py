def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if match(string[i:i+len(sub_string)],sub_string):
            count+=1
    return count

def match(s, sub_string):
    if s == sub_string:
        return True

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)