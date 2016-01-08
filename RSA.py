# -*- coding: UTF-8 -*-
# UTF-8 编码
# Author: Lin Jiayu
# School: HKBU
# Tkinter: python GUI
from Tkinter import *        
import string 
# RSA-in-Python
# Simple implementation of the RSA algorithm in Python and Python GUI(TkInter)
# *******************Function Area**************************************
# (1). RSA
	#1. select two primes p q
	#2. calculate n=p*q
	#3. calculate t(n)=(p-1)*(q-1);
	#4. select e gcd(t(n),e)=1
	#5. determine d  ed=1 mod t(n)
	# puclic key:pu{e,n}
	# private key:pr{d,n}
	#6. encryption: ciphertext=plaintext ** e mod n
	#7. decryption: plaintext=ciphertext ** d mod n



#   2. calculate n=p*q
def get_n(p,q):
    return p*q;

#   3. calculate t(n)=(p-1)*(q-1)
def get_tn(p,q):
    return (p-1)*(q-1);

#   4-1. select e gcd(t(n),e)=1 gcd(x,y) is for get_e(tn)
def gcd(x,y):
    if y==0:
        return x;
    else:
        return gcd(y,x%y);

#  4-2. get public key= e,n
def get_e(tn):
    e=2 #prime number starts from 2
    #gcd(tn,e)=1 tn & e are relative prime
    while gcd(tn,e)!=1:
      e=e+1;
    #  this way can find the minimal prime
    return e; 

#   5. determine d get private key= d,n
#   ed ≡ 1 (mod t(n)), so: ed = t(n)*n+1
def get_d(e, tn):
  # e is part of public key
  n=1 
  while (tn*n+1) % e !=0:
       n=n+1  
  d=(tn*n+1)/e
  return d

# 6.7 encrypt and decrypt
# encryption: ciphertext=plaintext ** e mod n
# decryption: plaintext=ciphertext ** d mod n
def rsa(M, key_ed, n):
  return_data = 1 
  M = M % n
  
  while key_ed != 0:
    if key_ed % 2 == 1:
      return_data = (return_data * M) % n      
    M = (M * M) % n
    key_ed = key_ed / 2

  return return_data

  



# (2). Interface Function
# +++++++++++++++++Encryption Function+++++++++++++++++
def submitclick_encrypt():
  #get plaintext the user input
  plaintext = entryvalue.get()
  # get the value of tn n e d
  tn=get_tn(2357,1733);
  n=get_n(2357,1733);
  e=get_e(tn);
  d=get_d(e, tn);

  print "Plaintext:",plaintext
  # print public key and private key
  print "Public Key:(",e,",",n,")"
  print "Private Key:(",d,",",n,")"
 
  # encryption
  # string convert into the number
  plaintext1=string.atoi(plaintext)
  ciphertext=rsa(plaintext1,e,n);

  print 'Ciphertext: %s' % ciphertext
  #output to the listbox
  listbox.insert(0,ciphertext)




# +++++++++++++++++Decryption Function+++++++++++++++++
def submitclick_decrypt():
  #get the ciphertext the user input
  ciphertext = entryvalue2.get()

  # get the value of tn n e d
  tn=get_tn(2357,1733);
  n=get_n(2357,1733);
  e=get_e(tn);
  d=get_d(e, tn);

  print "Ciphertext:",ciphertext
  # print public key and private key
  print "Public Key:(",e,",",n,")"
  print "Private Key:(",d,",",n,")"

  # Decryption
  ciphertext=string.atoi(ciphertext)
  plaintext=rsa(ciphertext,d,n);

  print 'Plaintext: %s' % plaintext
  #output to the listbox
  listbox2.insert(0,plaintext)

# *******************Function Area End**************************************









# *******************GUI Area**************************************
root = Tk()    
# GUI title                
root.title('RSA LJY')   

# ******************plaintext input*****************
l = Label(root,text='Input the plaintext')
l.pack() 

# input plaintext
entryvalue = Entry(root) 
entryvalue.pack()

# click the Encrypt button
button = Button(root,text="Encrypt",command=submitclick_encrypt) 
button.pack()

# show the ciphertext info.
show = Label(root,text='Show Ciphertext:')
show.pack() 
listbox  = Listbox(root,height = 1, width = 40)        
listbox.pack() 
# ******************plaintext input ending*****************





# ******************ciphertext input*****************
label = Label(root,text='Input the ciphertext')
label.pack() 

# input ciphertext
entryvalue2 = Entry(root) 
entryvalue2.pack()

# click the Decrypt button
button2 = Button(root,text="Decrypt",command=submitclick_decrypt) 
button2.pack()

# show the plaintext info.
show2 = Label(root,text='Show Plaintext:')
show2.pack() 
listbox2  = Listbox(root,height = 1, width = 40)         
listbox2.pack() 
# ******************ciphertext input ending*****************


root.mainloop()                 

# *******************GUI Area End**************************************
