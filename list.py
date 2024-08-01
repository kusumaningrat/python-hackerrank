N = int(input())
item = []
a_list = []

for _ in range(N):
    cmd = input().split()
    method_name = cmd[0]
    args = map(int, cmd[1:])


    if method_name == "print":
        print(item)
    else:
        if hasattr(item, method_name):
            method = getattr(item, method_name)
            method(*args)
    
    a_list.append(list(item))
