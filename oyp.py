import random
a=random.randint(1000000,9999999)
print(a)
otp=int(input("enter otp"))
if(a==otp):
    print("verified successfully")
else:
    print("invalid")
