# CPE Digital Signage
logo
## About CPE Digital Signage
CPE Digital Signage is ?
## Installing on Raspberry Pi OS (Legacy,64-bit)
Install using Raspberry Pi [Imager](https://www.raspberrypi.com/software/)
> [!NOTE]
> Please remember the username and hostname for SSH.
>
> ![image](https://github.com/CMU-Digital-Signage/Embedded-cmu-ds/assets/90751135/801dfcec-06a8-4b69-9ee3-dd58568e6fd7)

## Remote to Raspberry Pi
Use lan cable connect to Raspberry Pi and use [Putty](https://putty.org/) for SSH to Raspberry Pi using HostName(IP address) is
```
{username}@{hostname}.local
```

## Getting Started
**Update && Upgrade**
```
sudo apt update -y && sudo apt upgrade -y
```
**Install Tools.**
```
sudo apt-get install unclutter -y
```
**Install Library Python.**
```
sudo pip install getmac requests
```
**Clone Git.**
```
cd /home/{username}
```
```
git clone https://github.com/CMU-Digital-Signage/Embedded-cmu-ds.git
```
**Config working at startup of Raspberrypi.**
```
sudo python ~/Embedded-cmu-ds/setStart.py
```
```
sudo nano /home/{username}/.bashrc
```
_Add data to the `.bashrc` file._
```
echo Running at boot
sudo python /home/{username}/Embedded-cmu-ds/sendmac.py
```
**Increasing the size of the swap file.([link](https://youtu.be/NyGeUwIeH-s?si=UfU7Ykd6CQcibb4Q))**
```
sudo dphys-swapfile swapoff
```
```
sudo nano /etc/dphys-swapfile
```
_Change_ `CONF_SWAPSIZE`
```
#CONF_SWAPSIZE = 100
CONF_SWAPSIZE = 2048
```
`Ctrl + O` _save file and_ `Ctrl + x` _Exit file._
```
sudo dphys-swapfile setup
```
```
sudo dphys-swapfile swapon
```
**Reboot Raspberry pi.**
```
sudo reboot
```
