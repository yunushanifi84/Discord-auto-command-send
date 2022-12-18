import requests
import time
from datetime import datetime


islem = input("payload i giriniz: ")
kanal_id= input("Kanal id' sini girin:")
if (islem == "0"):
	payload ={"type":2,
		"application_id":"624187616312426512",
		"guild_id":"787718450206343218",
		"channel_id":kanal_id,
		"session_id":"14351d4f4e9897f76ddb2b2a0df20245",
		"data":{
    	"version":"1042350843300679691",
    	"id":"1042350843103547441",
    	"name":"hunt",
    		}}
#Burada benim kullanacağım komutun kodu var kullanacağınız koda göre değiştirmelisiniz
token = input("Auth tokeni giriniz:")
header = {
    'authorization': token
}
times=int(input("Tekrarlanacak islem sayisini giriniz:"))
b=1
for i in range(times):
	r = requests.post("https://discord.com/api/v9/interactions", json=payload, headers=header)
	time.sleep(5)
	r = requests.post("https://discord.com/api/v9/interactions", json=payload, headers=header)
	now =datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("yapilan islem sayisi : {}   Saat : ".format(b),current_time)
	b=b+1
	time.sleep(620)
	