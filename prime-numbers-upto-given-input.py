N = int(input("enter a number:  "))

def isprime(t):

    for i in range(2,t):
        if t<=1:
            False
        if t%i == 0:
            return False

    return True


for num in range(2,N+1):
    if isprime(num):
      print(num, end =' ')
#give a suitable readme/ description
