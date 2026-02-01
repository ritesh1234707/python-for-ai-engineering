import json
import requests
import sys

if len(sys.argv) != 2: 
    sys.exit("do it again")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])

x = response.json()
for result in x["results"]: 
    print(result["trackName"])

''' In this perticular code we use the API of apples 
itunes to bring songs of different artists.'''

