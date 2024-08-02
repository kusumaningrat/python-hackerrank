def swap_case(s):

    casee = [l.lower() if l.isupper() else l.upper() for l in s]
    res = ''.join(casee)
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

