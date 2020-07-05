def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
a=int(input("enter a nuber to be checked whether it is prime or not::"))
print(test_prime(a))