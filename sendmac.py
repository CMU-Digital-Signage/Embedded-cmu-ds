import requests
import getmac

mac = getmac.get_mac_address("eth0")

r = requests.post('https://signage.se.cpe.eng.cmu.ac.th/api/v1/pi',params={'mac': mac})

print(mac)