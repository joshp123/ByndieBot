import requests
import json
r = requests.get("http://api.icndb.com/jokes/random")
parsed_json = json.loads(r.content)
print(parsed_json['value']['joke'])