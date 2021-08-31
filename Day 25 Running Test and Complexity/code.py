# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
def prime_sieve(n):
    prime_no = [True for i in range(n+1)]
   

    for p in range(2, int(sqrt(n) + 1)):
        if n%p == 0:
            prime_no[p] = False
            
    prime_no[0] = False
    prime_no[1] = False
    
    return prime_no
# for (i = 2; i*i <= n; i++){
#     //if divisible
#     if (n % i == 0)
#         NOT PRIME
# }
if __name__ == "__main__":
    n = int(input())
    list_numbers = list()
    for _ in range(n):
        list_numbers.append(int(input()))
    
    max_no = max(list_numbers)
    
    prime_no = prime_sieve(max_no)
    
    for i in list_numbers:
        if prime_no[i] == True:
            print("Prime")
        else:
            print("Not prime")
