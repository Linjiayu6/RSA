# RSA-in-Python

Simple implementation of the RSA algorithm in Python and Python GUI(TkInter)<br>

RSA: <br>
	1. select two primes p q<br>
	2. calculate n=p*q<br>
	3. calculate t(n)=(p-1)*(q-1);<br>
	4. select e gcd(t(n),e)=1<br>
	5. determine d  ed=1 mod t(n)<br>
	 puclic key:pu{e,n}<br>
	 private key:pr{d,n}<br>
	6. encryption: ciphertext=plaintext ** e mod n<br>
	7. decryption: plaintext=ciphertext ** d mod n<br><br>
	
	
	
##ScreenShot
![](https://github.com/Linjiayu6/RSA/raw/master/RSA/img/imgCache/screen.jpg)  <br>
