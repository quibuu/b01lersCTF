from pwn import *
import time
import random

p1 = process('mes')
r = process('meshuggah')
#r = remote('pwn.ctf.b01lers.com', 1003)
rand_num = p1.recv().split('\n')
print(rand_num[0])
r.recvuntil('1. Meshuggah-')
test_num = r.recvuntil('\n')
print(test_num)
print(r.recv())
for i in range(3,len(rand_num)):
	try:
		r.sendline(rand_num[i])
		print(r.recv())
		print(r.recv())
	except:
		continue






