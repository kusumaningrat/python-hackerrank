if __name__ == '__main__':
    s = input()
    n = [0] * 5
    for c in s:
        n[0] += c.isalnum()
        n[1] += c.isalpha()
        n[2] += c.isdigit()
        n[3] += c.islower()
        n[4] += c.isupper()
    for i in n:
        print(bool(i))
        