def mail(n):
    for i in range(n):
        email = input("Enter your Email:").strip()
        if '@' and '.com' not in email:
            print("Enter valid mail ID")
            if n==1:
                mail(n)
            else:
                mail(n-(n-1))
        else:
            l.append(email)
            n-=1
def checking():
    x=input("How many mails would you like to Slice:")
    if x.isnumeric():
        n=int(x)
        if n<=0:
            print("Enter a positive number")
            checking()
        else:
            mail(n)
    else:
        print("Enter an Integer")
        checking()
l=[]
checking()
if l!=[]:
    for i in l:
        username = i[:i.index('@')]
        domain = i[i.index('@')+1:]
        domain = domain.upper()
        print(f"your username is {username} & domain is {domain}")
