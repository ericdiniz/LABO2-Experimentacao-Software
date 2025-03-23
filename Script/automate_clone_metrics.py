import os
import csv
import subprocess
import time
from datetime import datetime

REPO_DIR = "repositories_java"
CSV_INPUT = r"C:\Users\ian18\OneDrive\Documentos\GitHub\LABO2-Experimentacao-Software\resultados\repositories.csv"
METRICS_FILE = "metrics.csv"
CK_JAR_PATH = "ck.jar"  

os.makedirs(REPO_DIR, exist_ok=True)

def clone_repository(repo_url, repo_name):
    path = os.path.join(REPO_DIR, repo_name)
    if not os.path.exists(path):
        subprocess.run(["git", "clone", repo_url, path])
    return path

def get_first_commit_date(repo_path):
    result = subprocess.run(["git", "-C", repo_path, "log", "--reverse", "--format=%at"],
                            capture_output=True, text=True)
    timestamps = result.stdout.strip().split("\n")
    if timestamps:
        first_commit = int(timestamps[0])
        return datetime.fromtimestamp(first_commit)
    return None

def get_releases_count(repo_path):
    result = subprocess.run(["git", "-C", repo_path, "tag"], capture_output=True, text=True)
    return len(result.stdout.strip().splitlines())

def run_ck(repo_path):
    output_dir = os.path.join(repo_path, "ck_output")
    os.makedirs(output_dir, exist_ok=True)
    subprocess.run(["java", "-jar", CK_JAR_PATH, repo_path, "false", "0", output_dir],
                   capture_output=True, text=True)
    
    class_file = os.path.join(output_dir, "class.csv")
    cbo_total = dit_total = lcom_total = loc_total = comment_total = class_count = 0

    if os.path.exists(class_file):
        with open(class_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                class_count += 1
                cbo_total += int(row.get("cbo", 0))
                dit_total += int(row.get("dit", 0))
                lcom_total += int(row.get("lcom", 0))
                loc_total += int(row.get("loc", 0))
                comment_total += int(row.get("comment", 0))

    if class_count == 0:
        return 0, 0, 0, 0, 0

    return (
        round(cbo_total / class_count, 2),
        round(dit_total / class_count, 2),
        round(lcom_total / class_count, 2),
        loc_total,
        comment_total
    )

def main():
    with open(CSV_INPUT, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(METRICS_FILE, "w", newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow([
                "Repository", "Stars", "LOC", "Comments",
                "Releases", "Age (years)", "CBO", "DIT", "LCOM"
            ])

            for row in reader:
                repo_url = row["url"]
                stars = row.get("stars", 0)
                repo_name = repo_url.rstrip("/").split("/")[-1]

                print(f"Processing {repo_name}...")

                repo_path = clone_repository(repo_url, repo_name)

                first_commit = get_first_commit_date(repo_path)
                if first_commit:
                    age = round((datetime.now() - first_commit).days / 365, 2)
                else:
                    age = "N/A"

                releases = get_releases_count(repo_path)
                cbo, dit, lcom, loc, comments = run_ck(repo_path)

                writer.writerow([
                    repo_name, stars, loc, comments,
                    releases, age, cbo, dit, lcom
                ])

if __name__ == "__main__":
    main()
