import json
dosya=open("sinan.json","r")
json_dosya=json.load(dosya)
print("API KEY:",json_dosya["ad"])
print("API KEY:",json_dosya["soyad"])
print("API KEY:",json_dosya["access_token"])
print("API KEY:",json_dosya["kimlik"])
