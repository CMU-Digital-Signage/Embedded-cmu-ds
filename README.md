# CPE Digital Signage
## Schematic diagram of module connection
![image](https://github.com/CMU-Digital-Signage/Embedded-cmu-ds/assets/90751135/3e76e572-853a-4f13-a013-b893e3a2128d)

## Installing on Raspberry Pi OS (Legacy,64-bit)
Install using Raspberry Pi [Imager](https://www.raspberrypi.com/software/)
> [!NOTE]
> Please remember the username and hostname for SSH.
>
> ![Screenshot 2024-03-06 150844](https://github.com/CMU-Digital-Signage/Embedded-cmu-ds/assets/90751135/d5892a2c-4c19-4e61-b142-5f2bafc032ef)
>
> In the `configure wireless LAN` section, you can set it to your network or use `JumboPlusIoT` ([details](https://network.cmu.ac.th/wiki/index.php/JumboPlusIoT)).


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
_Then enter the following to the bottom of `.bashrc` file._
```
echo Running at boot
sudo rm -r  ~/.cache/chromium/Default/Cache/*
sudo python ~/Embedded-cmu-ds/setStart.py
sudo python ~/Embedded-cmu-ds/sendmac.py
```
![image](https://github.com/CMU-Digital-Signage/Embedded-cmu-ds/assets/90751135/2cb98451-b110-4f69-8f42-dfb31b8f69c6)

`Ctrl + O` _save file and_ `Ctrl + x` _Exit file._
**Increasing the size of the swap file.([link](https://youtu.be/NyGeUwIeH-s?si=UfU7Ykd6CQcibb4Q))**
```
sudo dphys-swapfile swapoff
```
```
sudo nano /etc/dphys-swapfile
```
_Change_ `CONF_SWAPSIZE`
```
#CONF_SWAPSIZE=100
CONF_SWAPSIZE=2048
```
![image](https://github.com/CMU-Digital-Signage/Embedded-cmu-ds/assets/90751501/fe779abf-258b-44e7-831a-a20fbe836f54)

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

_The very first step is to install LIRC after setting up the Raspberry PI OS. Enter the command below to install LIRC._
```
sudo apt-get update -y && sudo apt-get upgrade -y
```
```
sudo apt-get install lirc -y
```
_Your Raspberry PI OS has now been up-to-date and got the LIRC module installed._

![image](https://devkimchi.com/2020/08/turning-raspberry-pi-into-remote-controller-01.png)

**LIRC Module Configuration**

_Let's configure the LIRC module to send and receive the IR signal._

**Bootloader Configuration**

_By updating the bootloader file, when Raspberry PI starts the LIRC module starts at the same time. Open the bootloader file:_
```
sudo nano /boot/config.txt
```
_Uncomment the following lines and correct the pin number. The default values before being uncommented were 17 for gpio-ir-tx._
```
# Uncomment this to enable infrared communication.
#dtoverlay=gpio-ir,gpio_pin=17
#dtoverlay=gpio-ir-tx,gpio_pin=18
dtoverlay=gpio-ir-tx,gpio_pin=17
```
![image](https://github.com/CMU-Digital-Signage/Embedded-cmu-ds/assets/90751501/23a3cafe-5093-4ed6-bb7d-ae16eed55136)

`Ctrl + O` _save file and_ `Ctrl + x` _Exit file._

**LIRC Module Hardware Configuration**

_Let's configure the LIRC module hardware. Open the file below:_
```
sudo nano /etc/lirc/hardware.conf
```
_Then enter the following:_
```
LIRCD_ARGS="--uinput --listen"
LOAD_MODULES=true
DRIVER="default"
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
```
![image](https://github.com/CMU-Digital-Signage/Embedded-cmu-ds/assets/90751501/f1785f30-d5c9-4acc-bdab-88c7ef5070de)

`Ctrl + O` _save file and_ `Ctrl + x` _Exit file._

**LIRC Module Options Configuration**

_Update the LIRC module options. Open the file with the command:_
```
sudo nano /etc/lirc/lirc_options.conf
```
_Change both_ `driver` _and_ `device` _values (line #3-4)._
```
#driver          = devinput
#device          = auto
driver          = default
device          = /dev/lirc0
```
![image](https://github.com/CMU-Digital-Signage/Embedded-cmu-ds/assets/90751501/bee1daf6-8fca-4327-8a6c-c30df6eebacc)

`Ctrl + O` _save file and_ `Ctrl + x` _Exit file._

_Once you've completed by now, reboot Raspberry PI to recognise the updated bootloader._
```
sudo reboot
```
_Send this command to check the LIRC module working or not._
```
sudo /etc/init.d/lircd status
```
![image](https://devkimchi.com/2020/08/turning-raspberry-pi-into-remote-controller-02.png)
_It's now working!_

**Remote Controller Registration**

_This is the most important part of all. I have to register the remote controller I'm going to use._

**Use Remote Controller Database for Registration**

_The easiest and promising way to register the remote controller is to visit [Remote Controller Database website](https://lirc-remotes.sourceforge.net/remotes-table.html), search the remote controller and download it. But we have prepared it for you._

![image](https://github.com/CMU-Digital-Signage/Embedded-cmu-ds/assets/90751135/30a152d9-e750-429c-bfe3-23cb6292bd94)
```
sudo cp ~/Embedded-cmu-ds/AKB74475403.lircd.conf /etc/lirc/lircd.conf.d/LG.lircd.conf
```
```
sudo nano ~/.bashrc
```
_Then enter the following to the bottom of `.bashrc` file._
```
sudo python ~/Embedded-cmu-ds/mqtt.py
```
![image](https://github.com/CMU-Digital-Signage/Embedded-cmu-ds/assets/90751135/f29d0760-2c39-4149-97a6-b3e661305271)

`Ctrl + O` _save file and_ `Ctrl + x` _Exit file._

_Reboot Raspberry PI._
```
sudo reboot
```
