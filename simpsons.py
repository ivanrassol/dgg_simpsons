import urllib.parse
import urllib.request
import json

url = "https://api.duckduckgo.com/?q=The%20Simpsons%20Characters&format=json"

req = urllib.request.Request(url)

results = {"Characters": []}

def exclude_parenthesis(s):
    if "(" in s or ")" in s:
        return False
    return True

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read())

    for i in data["RelatedTopics"]:
        result = {}
        result["URL"] = i["FirstURL"]
        result["Icon"] = "https://duckduckgo.com" + i["Icon"]["URL"]

        name = (urllib.parse.unquote(i["FirstURL"]).split("/")[-1].split("_"))
        result["Name"] = " ".join(filter(exclude_parenthesis, name))

        results["Characters"].append(result)

with open("simpsons.json", "w") as f:
    f.write(json.dumps(results, indent=2))
