# RSA-in-Python

     Simple implementation of the RSA algorithm in Python and Python GUI(TkInter)

###(1) RSA: 
	1. select two primes p q
	2. calculate n=p*q
	3. calculate t(n)=(p-1)*(q-1);
	4. select e gcd(t(n),e)=1
	5. determine d  ed=1 mod t(n)
	   puclic key:pu{e,n}
	   private key:pr{d,n}
	6. encryption: ciphertext=plaintext ** e mod n
	7. decryption: plaintext=ciphertext ** d mod n
	
      
        Given two primes p=2357,q=1733	

###(2) Function Description
       * def get_n(p,q): calculate n=p*q 
       * def get_tn(p,q): calculate t(n)=(p-1)*(q-1)
       * def gcd(x,y): select e gcd(t(n),e)=1
       * def get_e(tn): select e and public key=(e,n)
       * def get_d(e, tn): determine d and get private key=(d,n)
       * def rsa(M, key_ed, n): encrypt and decrypt in terms of values of key_ed and M

       * def submitclick_encrypt(): get inputing value(plaintext) and execute rsa(M, e, n), show the ciphertext
       * def submitclick_decrypt(): get inputing value(ciphertext) and execute rsa(M, d, n), show the plaintext



###(3) ScreenShot
![](https://github.com/Linjiayu6/RSA/raw/master/screen.jpg)  
