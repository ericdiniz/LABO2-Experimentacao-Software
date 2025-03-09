import csv

def save_repositories_to_csv(repositories):
    csv_file_path = "resultados/repositories.csv"

    fieldnames = ["nameWithOwner", "stargazerCount", "forkCount", "url"]

    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for repo in repositories:
            writer.writerow(repo)

    print(f"Salvo {len(repositories)} repositórios em {csv_file_path}.")