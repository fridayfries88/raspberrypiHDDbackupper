import os
from time import sleep

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

os.system('sudo apt update && sudo apt -y upgrade')
os.system('sudo fdisk -l')
input("\n \n \n \n \n \n \n \n \n please plug in your drive and press return ")
sleep(3)
os.system('sudo fdisk -l')
dev = input('\n \n \n \n \n \n \n \n \n \n please input your drive path and press return (ex. /dev/sda1)')
out = input('type your output location (ex. /home/pi')
filename = input('input the output filename (ex. disk 1)')
os.system('mkdir ' + out + '/' + filename)
os.system('sudo umount ' + dev)
os.system('mkdir /media/HDD')
os.system('mount ' + dev + ' /media/HDD')
os.system('cp /media/HDD ' + out + '/' + filename + '/backup -r -v')
os.system('sudo dd if=' + dev + ' of=' + out + '/' + filename + '/' + 'diskimage.img' + ' bs=1k conv=noerror status=progress')
print ('\n \n \n \n \n \n \n \n \n Backup Complete')
