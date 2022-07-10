import os
from time import sleep

#check to see if the script has super user
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

#run updates on the system
os.system('sudo apt update && sudo apt -y upgrade')
#installs one of the requirements 7Zip
os.system('sudo apt install 7zip')
#lists currently connected drives
os.system('sudo fdisk -l')
#requests the drive to be connected
input("\n \n \n \n \n \n \n \n \n please plug in your drive and press return ")
#Waits for the disk to spin up (Takes a bit somedimes)
sleep(15)
#lists connected disks again
os.system('sudo fdisk -l')
#requests the drive path
dev = input('\n \n \n \n \n \n \n \n \n \n please input your drive path and press return (ex. /dev/sda1) {if it doesn`t appear restart the program (ctrl + c)}')
#requests the location for the *.7z file to be stored
out = input('type your output location (ex. /home/pi')
#input the name for the *.7z archive
filename = input('input the output filename (ex. disk 1)')
#Makes the temporary Directory For The files
os.system('mkdir ' + out + '/' + filename)
#un-mounts the drive incase it is already mounted
os.system('sudo umount ' + dev)
#creates a directory to mount the drive to
os.system('mkdir /media/HDD')
#mounts the Drive under the Directory under /media/HDD
os.system('mount ' + dev + ' /media/HDD')
#copys the files off the disk
os.system('cp /media/HDD ' + out + '/' + filename + '/backup -r -v')
os.system('clear')
#makes a disk image of the disk
os.system('sudo dd if=' + dev + ' of=' + out + '/' + filename + '/' + 'diskimage.img' + ' bs=1k conv=noerror status=progress')
#clears the Screen of the previous text
os.system('clear')
#clears the display of text again
os.system('clear')
#compresses the files
os.system('sudo 7z a -r -y -sdel ' + out + '/' + filename + '.7z' + ' ' + out + '/' + filename)
#unmounts the disk
os.system('sudo umount ' + dev)
#exits the program
exit('\n \n \n \n \n \n \n \n \n Backup Complete')
