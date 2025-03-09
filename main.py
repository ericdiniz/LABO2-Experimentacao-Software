from scripts.fetch_repos import fetch_repositories
from scripts.save_repos import save_repositories_to_csv

def main():
    repos = fetch_repositories()
    save_repositories_to_csv(repos)

if __name__ == "__main__":
    main()