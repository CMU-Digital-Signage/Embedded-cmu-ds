import getmac

mac = getmac.get_mac_address("eth0")

path = "/etc/xdg/lxsession/LXDE-pi/autostart"

textDefault = '@lxpanel --profile LXDE-pi\n' + '@pcmanfm --desktop --profile LXDE-pi\n' + '@xscreensaver -no-splash\n' 

web = f'https://signage.se.cpe.eng.cmu.ac.th/device/{mac}'
runWeb = '@xset s off\n' + '@xset -dpms\n' + '@xset s noblank\n' + f'@chromium-browser --kiosk {web}\n'
hideCursor = '@unclutter -idle 0.1 -root\n'

runTerminal = '@lxterminal\n'

file1 = open(path,"w")
file1.write(textDefault + runWeb + hideCursor + runTerminal)
file1.close()


file1 = open(path,"r")
print(file1.read())
file1.close()
