import os
import documentcloud
import requests

os.environ["DC_USERNAME"] = 'davegod@bu.edu'
os.environ["DC_PASSWORD"] = 'C0rt3X7940'
os.environ['GITHUB_TOKEN'] = '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'

dc = documentcloud.DocumentCloud(
    username = os.environ["DC_USERNAME"], password = os.environ["DC_PASSWORD"]
)

access, refresh = dc._get_tokens(dc.username, dc.password)

payload = {
    "token": access,
    "refresh_token": refresh,
    "base_uri": "https://api.www.documentcloud.org/api/",
    "id": None,
    "documents": None,
    "query": None,
    "data": {"name": "dave-godfrey-105568"},
    "user": 105568,
    "organization": 125,
}

api_url = "https://api.github.com/EliteEagle77/documentcloud-hello-world-addon"
api_headers = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}

resp = requests.post(
    f"{api_url}/dispatches",
    headers = api_headers,
    json = {"event_type": "Hello World", "client_payload": payload},
)