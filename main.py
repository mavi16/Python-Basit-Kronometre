"""

"Basit Kronometre"
@author: mavi16

"""

# Başlangıç değerlerini atama
secs = 0
min = 0
hour = 0

# Zaman ve Sistem kütüphanesi
from time import sleep as sd
from os import system as lk

lk("color a")
while True:
    lk("cls")

    print(str(hour).zfill(2) + ":" + str(min).zfill(2) + ":" + str(secs).zfill(2))
    secs += 1
    sd(1)
    if secs == 60:
        secs = 0
        min += 1
    if min == 60:
        min = 0
        hour += 1
    if min == 25:
        print("\a")
        break
