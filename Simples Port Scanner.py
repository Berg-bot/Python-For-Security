from socket import *
import time
import os
startTime = time.time()

target = input("Enter the target host : ")
t_ip = gethostbyname(target)
print(f"Scanning the host >>> {t_ip}")

for i in range(20,500):
   s = socket(AF_INET, SOCK_STREAM)
   conn = s.connect_ex((t_ip,i))
   if conn == 0:
      print(f"Port No : {i} is open")
   s.close()

print(f"The scanning takes {time.time()-startTime}")
