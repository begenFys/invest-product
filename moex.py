import json
import requests

from urllib import parse

def query(method : str, **kwargs):
    try:
        url = "https://iss.moex.com/iss/%s.json" % method
        if kwargs: url += "?" + parse.urlencode(kwargs)
        r = requests.get(url)
        r.encoding = "utf-8"
        j = r.json()
        return j
    except Exception as e:
        print(str(e))
        return None

def flatten(j:dict, blockname:str):
    return [{k: r[i] for i, k in enumerate(j[blockname]['columns'])} for r in j[blockname]["data"]]

def main():
    param = {
        "limit" : 100,
        "start" : 500
    }
    method = "securities"
    j = query(method, **param)
    f = flatten(j, method)
    print(len(f))
    print(f[0])

if __name__ == "__main__":
    main()