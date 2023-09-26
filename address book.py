add={}
def addd(s,value):
    add[s]=value
    print(add)
def edit(s,value):
    add[s]=value
def view(s):
    return add[s]
def delete(s):
    del add[s] 
##add={}
#add=dict(add)
print("for adding any contact entre 1\n for editing any contact enter 2\n for viewing any contact enter 3\n for deleting any contact enter 4\n")
p='continue'
while p=='continue':
    s=int(input("enter which action do you wanna perform?\n"))
    if s==1:
        x=input("name of the person you wanna add to contact?\n ")
        y=input("contact no. of the person?\n")
        addd(x,y)
        print("contact added\n")
    elif s==2:
        p=input("name of the person you wanna edit contact no.?\n")
        q=input("enter new phone no.\n")
        edit(p,q)
        print("contact edited\n")
    elif s==3:
        r=input("name of the person you wanna see contact no.?\n")
        print(view(r))
    elif s==4:
        s=input("enter whose contact no. you wanna delete\n ")
    p=input("if you wanna continue working enter 'continue' otherwise enter 'stop'\n")

print("thanks for visiting")





