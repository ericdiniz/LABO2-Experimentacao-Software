import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

plt.style.use("seaborn-v0_8-darkgrid")
sns.set_palette("Set2")
sns.set_context("talk")

CSV_REPOS = r"C:\Users\Pablo Benevenuto\Downloads\LABO2-Experimentacao-Software\resultados\repositories.csv"
CSV_QUALITY = r"C:\Users\Pablo Benevenuto\Downloads\LABO2-Experimentacao-Software\resultados\quality_metrics.csv"

repos_df = pd.read_csv(CSV_REPOS)
quality_df = pd.read_csv(CSV_QUALITY)

repos_df["createdAt"] = pd.to_datetime(repos_df["createdAt"], errors="coerce").dt.tz_localize(None)
repos_df["Idade (anos)"] = (datetime.datetime(2025, 1, 1) - repos_df["createdAt"]).dt.days / 365
if "releaseCount" in repos_df.columns:
    repos_df["Atividade"] = pd.to_numeric(repos_df["releaseCount"], errors="coerce")
else:
    repos_df["Atividade"] = None

if "loc" in repos_df.columns and "comment_lines" in repos_df.columns:
    repos_df["Tamanho Total (LOC + Comentários)"] = pd.to_numeric(repos_df["loc"], errors="coerce") + pd.to_numeric(repos_df["comment_lines"], errors="coerce")
else:
    repos_df["Tamanho Total (LOC + Comentários)"] = None

quality_df["CBO_Média"] = pd.to_numeric(quality_df["CBO_Média"], errors="coerce")
quality_df["DIT_Média"] = pd.to_numeric(quality_df["DIT_Média"], errors="coerce")
quality_df["LCOM_Média"] = pd.to_numeric(quality_df["LCOM_Média"], errors="coerce")

min_len = min(len(repos_df), len(quality_df))
repos_df = repos_df.iloc[:min_len].reset_index(drop=True)
quality_df = quality_df.iloc[:min_len].reset_index(drop=True)

df = pd.concat([repos_df, quality_df], axis=1)

def barplot_by_quartile(x, y, xlabel, ylabel, title):
    df["grupo"] = pd.qcut(df[x], 4, labels=["Q1", "Q2", "Q3", "Q4"])
    media_por_grupo = df.groupby("grupo")[[y]].mean().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(data=media_por_grupo, x="grupo", y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(f"Média de {ylabel}")
    plt.tight_layout()
    plt.show()

barplot_by_quartile("stargazerCount", "CBO_Média", "Popularidade (Estrelas)", "CBO", "RQ1: Estrelas vs CBO Média")
barplot_by_quartile("stargazerCount", "DIT_Média", "Popularidade (Estrelas)", "DIT", "RQ1: Estrelas vs DIT Média")
barplot_by_quartile("stargazerCount", "LCOM_Média", "Popularidade (Estrelas)", "LCOM", "RQ1: Estrelas vs LCOM Média")

barplot_by_quartile("Idade (anos)", "CBO_Média", "Maturidade (anos)", "CBO", "RQ2: Maturidade vs CBO Média")
barplot_by_quartile("Idade (anos)", "DIT_Média", "Maturidade (anos)", "DIT", "RQ2: Maturidade vs DIT Média")
barplot_by_quartile("Idade (anos)", "LCOM_Média", "Maturidade (anos)", "LCOM", "RQ2: Maturidade vs LCOM Média")

if df["Atividade"].notnull().any():
    barplot_by_quartile("Atividade", "CBO_Média", "Atividade (releases)", "CBO", "RQ3: Atividade vs CBO Média")
    barplot_by_quartile("Atividade", "DIT_Média", "Atividade (releases)", "DIT", "RQ3: Atividade vs DIT Média")
    barplot_by_quartile("Atividade", "LCOM_Média", "Atividade (releases)", "LCOM", "RQ3: Atividade vs LCOM Média")
else:
    print("Coluna de atividade (releases) não disponível para análise.")

if df["Tamanho Total (LOC + Comentários)"].notnull().any():
    barplot_by_quartile("Tamanho Total (LOC + Comentários)", "CBO_Média", "Tamanho (LOC + Comentários)", "CBO", "RQ4: Tamanho vs CBO Média")
    barplot_by_quartile("Tamanho Total (LOC + Comentários)", "DIT_Média", "Tamanho (LOC + Comentários)", "DIT", "RQ4: Tamanho vs DIT Média")
    barplot_by_quartile("Tamanho Total (LOC + Comentários)", "LCOM_Média", "Tamanho (LOC + Comentários)", "LCOM", "RQ4: Tamanho vs LCOM Média")
else:
    print("Colunas de tamanho (LOC e comentários) não disponíveis para análise.")
