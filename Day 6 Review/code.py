# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(input())
for i in range(test_cases):
    input_str = input()
    for j in range(len(input_str)):
        if j%2 == 0:
            print(input_str[j],end = "")
    print(end = " ")
    for j in range(len(input_str)):
        if j%2 != 0:
            print(input_str[j],end = "")
            
    print(end = "\n")