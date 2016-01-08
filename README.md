# RSA-in-Python

Simple implementation of the RSA algorithm in Python and Python GUI(TkInter)<br><br>

###(1) RSA: <br>
	1. select two primes p q<br>
	2. calculate n=p*q<br>
	3. calculate t(n)=(p-1)*(q-1);<br>
	4. select e gcd(t(n),e)=1<br>
	5. determine d  ed=1 mod t(n)<br>
	   puclic key:pu{e,n}<br>
	   private key:pr{d,n}<br>
	6. encryption: ciphertext=plaintext ** e mod n<br>
	7. decryption: plaintext=ciphertext ** d mod n<br><br>
	
      
        Given two primes p=2357,q=1733	<br><br>

###(2) Function Description<br>
* def get_n(p,q): calculate n=p*q <br>
* def get_tn(p,q): calculate t(n)=(p-1)*(q-1)<br>
* def gcd(x,y): select e gcd(t(n),e)=1<br>
* def get_e(tn): select e and public key=(e,n)<br>
* def get_d(e, tn): determine d and get private key=(d,n)<br>
* def rsa(M, key_ed, n): encrypt and decrypt in terms of values of key_ed and M<br><br>

* def submitclick_encrypt(): get inputing value(plaintext) and execute rsa(M, e, n), show the ciphertext<br>
* def submitclick_decrypt(): get inputing value(ciphertext) and execute rsa(M, d, n), show the plaintext<br><br>



##ScreenShot
![](https://github.com/Linjiayu6/RSA/raw/master/RSA/img/imgCache/screen.jpg)  <br>
