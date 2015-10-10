import requests
import json
r = requests.get("http://yesno.wtf/api")
parsed_json = json.loads(r.content)
print(parsed_json['image'])
