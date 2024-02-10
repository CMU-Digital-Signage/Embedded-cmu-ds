import requests
import getmac

mac = getmac.get_mac_address("eth0")

r = requests.post('https://api-cmu-ds.onrender.com/api/v1/pi',params={'mac': mac})
