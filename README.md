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
sudo pip install getmac requests paho-mqtt
```
**Clone Git.**
```
cd ~
```
```
git clone https://github.com/CMU-Digital-Signage/Embedded-cmu-ds.git
```
**Config working at startup of Raspberrypi.**
```
sudo python ~/Embedded-cmu-ds/setStart.py
```
```
sudo nano ~/.bashrc
```
_Then enter the following to `.bashrc` file._
```
echo Running at boot
sudo rm -r  ~/.cache/chromium/Default/Cache/*
sudo python ~/Embedded-cmu-ds/sendmac.py
sudo python ~/Embedded-cmu-ds/mqtt.py
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

## Raspberry Pi into Remote Controller [Link](https://devkimchi.com/2020/08/12/turning-raspberry-pi-into-remote-controller/)
**LIRC Module Installation**
The very first step is to install LIRC after setting up the Raspberry PI OS. Enter the command below to install LIRC.
```
sudo apt-get update -y && sudo apt-get upgrade -y
```
```
sudo apt-get install lirc -y
```
Your Raspberry PI OS has now been up-to-date and got the LIRC module installed.

[image](https://devkimchi.com/2020/08/turning-raspberry-pi-into-remote-controller-01.png)

**LIRC Module Configuration**
Let's configure the LIRC module to send and receive the IR signal.

**Bootloader Configuration**
By updating the bootloader file, when Raspberry PI starts the LIRC module starts at the same time. Open the bootloader file:
```
sudo nano /boot/config.txt
```
Uncomment the following lines and correct the pin number. The default values before being uncommented were 17 for gpio-ir-tx.
```
# Uncomment this to enable infrared communication.
#dtoverlay=gpio-ir,gpio_pin=17
#dtoverlay=gpio-ir-tx,gpio_pin=18
dtoverlay=gpio-ir-tx,gpio_pin=17
```

**LIRC Module Hardware Configuration**
Let's configure the LIRC module hardware. Open the file below:
```
sudo nano /etc/lirc/hardware.conf
```
Then enter the following:
```
LIRCD_ARGS="--uinput --listen"
LOAD_MODULES=true
DRIVER="default"
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
```

**LIRC Module Options Configuration**
Update the LIRC module options. Open the file with the command:
```
sudo nano /etc/lirc/lirc_options.conf
```
Change both `driver` and `device` values (line #3-4).
```
#driver          = devinput
#device          = auto
driver          = default
device          = /dev/lirc0
```
Once you've completed by now, reboot Raspberry PI to recognise the updated bootloader.
```
sudo reboot
```
Send this command to check the LIRC module working or not.
```
sudo /etc/init.d/lircd status
```
[image](https://devkimchi.com/2020/08/turning-raspberry-pi-into-remote-controller-02.png)
It's now working!

**Remote Controller Registration**
This is the most important part of all. I have to register the remote controller I'm going to use.

**Use Remote Controller Database for Registration**
The easiest and promising way to register the remote controller is to visit [Remote Controller Database website](https://lirc-remotes.sourceforge.net/remotes-table.html), search the remote controller and download it.

[image](https://devkimchi.com/2020/08/turning-raspberry-pi-into-remote-controller-03.png)
```
sudo cp ~/Embedded-cmu-ds/AKB74475403.lircd.conf /etc/lirc/lircd.conf.d/LG.lircd.conf
```
Reboot Raspberry PI.
```
sudo reboot
```