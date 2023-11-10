from tkinter import *
from tkinter import messagebox
import random

def isPrime(n):
    for i in range(2,n):
        if (n%i)==0:
            return False
    return True    

def Prime_g():
    while True:
        n=random.randint(500,1000)
        if (isPrime(n)):
            return n

def gcd(a,b):
    if b!=0:
        return gcd(b,a%b)
    else:
        return a

def e_g(z):
    while True:
        e=random.randrange(1,z)
        if (gcd(e,z)==1):
            break
    return e

def Keys_g():
    global e,N,d
    N=d=e=0
    p=Prime_g()
    q=Prime_g()
    N=p*q 
    z=(p-1)*(q-1)
    e=e_g(z)
    d=modular_inv(e,z)
    pb=(e,N)
    pv=(d,N)

    public_key.insert(10,pb)
    private_key.insert(10,pv)
    return N,e,d

def egcd(a, b):
    s1=0 ; s0=1
    t1=1 ; t0=0
    r1=b ; r0=a

    while r1!=0:
        quotient=r0 // r1
        r0 , r1 = r1 , r0-quotient*r1
        s0 , s1 = s1 , s0-quotient*s1
        t0 , t1 = t1 , t0-quotient*t1

    # return gcd, x, y
    return r0, s0, t0

def modular_inv(a, b):
    gcd, x, y = egcd(a, b)
    if x < 0:
        x += b
    return x



def encrypt():
    global e,N
    e1=int(public_key1.get())
    N1=int(public_key2.get())

    if e1==e and N1==N:

        msg=text1.get()
        cipher = ""

        for i in msg:
            m = ord(i)
            cipher += str((m**e1)%N1) + " "
        encrypted.insert(10,cipher)

    else:
        messagebox.showerror("X","Keys doesn't match!!")
        public_key1.delete(0,END)
        public_key2.delete(0,END)

    



def decrypt():
    global d,N
    d1=int(private_key1.get())
    N1=int(private_key2.get())

    if d1==d and N1==N:

        msg = ""
        cipher=text2.get()


        parts = cipher.split()
        for j in parts:
            if j:
                c = int(j)
                msg += chr((c**d1)%N1)

        decrypted.insert(10,msg)
    
    else:
        messagebox.showerror("X","Keys doesn't match!!")
        private_key1.delete(0,END)
        private_key2.delete(0,END)



def fill_keys():
    global e,N,d
    public_key1.insert(10,e)
    public_key2.insert(10,N)

    private_key1.insert(10,d)
    private_key2.insert(10,N)

def clear():
    public_key.delete(0,END)
    public_key1.delete(0,END)
    public_key2.delete(0,END)

    private_key.delete(0,END)
    private_key1.delete(0,END)
    private_key2.delete(0,END)

    text1.delete(0,END)
    text2.delete(0,END)

    encrypted.delete(0,END)
    decrypted.delete(0,END)

    text1.focus_set()

    
    
    




root=Tk()
root.title("RSA")
root.configure(bg="light blue")
root.geometry("400x380")



b1=Button(root,text="GENERATE KEYS",fg='black',bg='light green',command=Keys_g).grid(row=0,column=1)

l1=Label(root,text="Public Key :",fg='black',bg='light pink')
l2=Label(root,text="Private Key : ",fg='black',bg='light pink')

l1.grid(row=1,column=0,sticky="E")
l2.grid(row=2,column=0,sticky="E")

public_key=Entry(root)
private_key=Entry(root)

public_key.grid(row=1,column=1,ipadx="55")
private_key.grid(row=2,column=1,ipadx="55")

l3=Label(root,text="Encryption",fg='black',bg='violet').grid(row=3,column=1)

l4=Label(root,text="Text to encrypt: ",fg='black',bg='light pink').grid(row=4,column=0,sticky="E")

l5=Label(root,text="Enter Public key : ",fg='black',bg='light pink').grid(row=5,column=0,sticky="E")

text1=Entry(root)
text1.grid(row=4,column=1,ipadx="55")

public_key1=Entry(root)
public_key1.place(x=100,y=110)

public_key2=Entry(root)
public_key2.place(x=235,y=110)

b2=Button(root,text=" ENCRYPT ",fg='black',bg='light green',command=encrypt).grid(row=6,column=1)

l6=Label(root,text="Encrypted Text : ",fg='black',bg='light pink').grid(row=7,column=0,sticky="E")

encrypted=Entry(root)
encrypted.grid(row=7,column=1,ipadx="55")


l7=Label(root,text="Decryption",fg='black',bg='violet').grid(row=8,column=1)

l8=Label(root,text="Text to decrypt: ",fg='black',bg='light pink').grid(row=9,column=0,sticky="E")

l9=Label(root,text="Enter Private key : ",fg='black',bg='light pink').grid(row=10,column=0,sticky="E")

text2=Entry(root)
text2.grid(row=9,column=1,ipadx="55")

private_key1=Entry(root)
private_key1.place(x=100,y=220)

private_key2=Entry(root)
private_key2.place(x=235,y=220)

b3=Button(root,text=" DECRYPT ",fg='black',bg='light green',command=decrypt).grid(row=11,column=1)

l10=Label(root,text="Decrypted Text : ",fg='black',bg='light pink').grid(row=12,column=0,sticky="E")

decrypted=Entry(root)
decrypted.grid(row=12,column=1,ipadx="55")

b4=Button(root,text=" FILL ABOVE KEYS",fg='black',bg='light green',command=fill_keys).grid(row=21,column=1)

b5=Button(root,text="CLEAR!!",fg='black',bg='pink',command=clear).grid(row=22,column=1)



root.mainloop()