import os
import csv
import subprocess
import time


REPO_DIR = "repositories_java"  
CSV_FILE = r"C:\Users\ian18\OneDrive\Documentos\GitHub\LABO2-Experimentacao-Software\resultados\repositories.csv"# Aki tem que colocar o local do arquivo CSV( onde ele ta salvo no pc de vcs)
METRICS_FILE = "metrics.csv" 

os.makedirs(REPO_DIR, exist_ok=True)

def clone_repository(repo_url, repo_name):
    """ Clona um repositório do GitHub """
    repo_path = os.path.join(REPO_DIR, repo_name)
    
    if os.path.exists(repo_path):
        print(f"Repositório {repo_name} já existe. Pulando clone...")
        return repo_path
    
    try:
        print(f"Clonando {repo_name}...")
        subprocess.run(["git", "clone", "--depth", "1", repo_url, repo_path], check=True)
        return repo_path
    except subprocess.CalledProcessError as e:
        print(f"Erro ao clonar {repo_name}: {e}")
        return None

def collect_metrics(repo_path):
    """ Coleta métricas do repositório usando cloc """
    try:
        print(f"Coletando métricas de {repo_path}...")
        result = subprocess.run(["cloc", "--json", repo_path], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao coletar métricas de {repo_path}: {e}")
        return None

def save_metrics(repo_name, metrics_data):
    """ Salva as métricas coletadas em um arquivo CSV """
    try:
        with open(METRICS_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([repo_name, metrics_data])
    except Exception as e:
        print(f"Erro ao salvar métricas de {repo_name}: {e}")

def main():
    """ Executa o processo de automação: clone e coleta de métricas """
    print("Iniciando automação de clone e coleta de métricas...")


    if not os.path.exists(METRICS_FILE):
        with open(METRICS_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Repositorio", "Metricas"])


    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  

        for row in reader:
            repo_name = row[0].split("/")[1]  
            repo_url = row[3]  

            repo_path = clone_repository(repo_url, repo_name)
            if repo_path:
                metrics_data = collect_metrics(repo_path)
                if metrics_data:
                    save_metrics(repo_name, metrics_data)
            

            time.sleep(5)

    print("Processo concluído!")

if __name__ == "__main__":
    main()
