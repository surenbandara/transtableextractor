import requests

resp = requests.post("https://index-kgxqczsvjq-du.a.run.app", files={'file': open('Tes.pdf', 'rb')})

print(resp)



