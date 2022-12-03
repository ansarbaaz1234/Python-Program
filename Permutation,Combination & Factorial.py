def Fact(n):
   product = 1
   for i in range(n):
        product = product * (i+1)
        if n == 1 or n == 0 :
            return 1
   return product


def perm(n,r):
    diff = n - r
    perm = Fact(n)/Fact(diff)
    return perm

def comb(n,r):
    diff = n - r
    comb = Fact(n)/Fact(r) * Fact(diff)  
    return comb

op = input("Enter the anyone of the operators(Factorial,Permutation,Combination) : ")
if op == 'Factorial':
    num = int(input("Enter a number : "))
    print("The Factorial of the entered number is : ", Fact(num))

elif op == 'Permutation':
    no = int(input("Enter a number : "))
    r = int(input("Enter the number of selections  : "))
    difference = no - r
    print("The Permutation will be : ", perm(no,r))

elif op == 'Combination':
    no = int(input("Enter a number : "))
    r = int(input("Enter the number of selections  : "))
    difference = no - r
    print("The Combination will be : ", comb(no,r))

else :
    print('Try Again !!')

    