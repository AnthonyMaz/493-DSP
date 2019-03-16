import requests

print("Hello World")
my_ip=requests.get("http://bot.whatismyipaddress.com/")
print(my_ip.text)
