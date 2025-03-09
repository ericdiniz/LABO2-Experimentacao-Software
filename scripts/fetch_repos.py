import requests
import os
import json
from queries.repositories import QUERY_REPOSITORIES
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
URL = "https://api.github.com/graphql"

def fetch_repositories():
    repositories = []
    cursor = None

    while len(repositories) < 1000:
        variables = {"cursor": cursor}
        response = requests.post(URL, json={"query": QUERY_REPOSITORIES, "variables": variables}, headers=HEADERS)

        if response.status_code != 200:
            print(f"Erro na requisição: {response.text}")
            break

        data = response.json()
        search_data = data.get("data", {}).get("search", {})
        nodes = search_data.get("nodes", [])
        print(f"Repositórios encontrados na página: {len(nodes)}")

        repositories.extend(nodes)

        cursor = search_data.get("pageInfo", {}).get("endCursor")

        if not search_data.get("pageInfo", {}).get("hasNextPage"):
            break

        if len(repositories) % 500 == 0:
            print(f"Coletados {len(repositories)} repositórios...")

    return repositories