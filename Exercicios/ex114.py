import requests
import urllib3

urllib3.disable_warnings()


resp = requests.get("https://www.pudim.com.br/", verify=False)
if resp.status_code == 200:
    print("\033[92mConsegui acessar o site com sucesso\033[m")
else:
    print("\033[91mO site nao esta acessivel no momento\033[m")
