import requests
import os

from dotenv import load_dotenv
load_dotenv()

from config import *

TOKEN = os.getenv("GITHUB_TOKEN") 

url = f"https://api.github.com/repos/{OWNER}/{REPO}/pages"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

payload = {
    "source": {
        "branch": "main",
        "path": "/"
    }
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.json())