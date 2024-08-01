# Create the input

item = int(input())
a = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    cmd, _  = input().split()
    new_item = set(map(int, input().split()))
    getattr(a, cmd)(new_item)


    