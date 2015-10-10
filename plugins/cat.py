import requests
import json
r = requests.get("http://looq.nl/cat/index.php")
print(r.content)