# # Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

book = [input().split() for i in range(n)]
d = {n:p for n,p in book}

while True:
    try:
        key = input()
        if key in d:
            print("{}={}".format(key, d[key]))
        else:
            print("Not found")
    except:
        break
