def count_substring(string, sub_string):

    sub_len = len(sub_string)

    subs = [i for i in range(len(string)) if string[i:i+sub_len] == sub_string]

    return len(subs)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)