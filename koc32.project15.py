
print("\nWelcome :)\n")
print("_______________________________")
x=int(input("\n>>>Enter the positive integer lower limit⏬: "))
y=int(input(">>>Enter the positive integer upper limit⏫: "))
print("_______________________________\n")
s=0
g=0
if x>y:
    c=input("\nThe lower limit cannot be more than the upper limit🙄 \nIf you wish to interchange the values type 'Yes' else 'No': ").lower()
    print()
    if c=="yes":
     temp=y
     y=x
     x=temp
for i in range(x,y+1):
    if i==1:
        print(i,"is neither prime nor composite.")
    elif i>1:
        a=i
        c=0
        for j in range(2,a):
            if a%j==0:
                c=1
                s+=1
                print(f"{a} is Composite.")
                break
        if c==0:
            print(f"{a} is Prime.")
            g+=1
if c=="no":
 pass
else:
 print(f"\nThere are total of {g} prime numbers and \n{s} composite numbers in the given range.")
 print("")
 print("Thank You!!")
0 comments on commit 1518ddc
Please sign in to comment.
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status