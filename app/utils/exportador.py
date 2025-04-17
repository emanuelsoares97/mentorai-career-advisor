import json
import csv

def exportar_csv(json_path="historico_resultados.json", csv_path="historico_resultados.csv"):
    with open(json_path, "r", encoding="utf-8") as f:
        historico = json.load(f)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Data", "Nome", "Lógica", "Visual", "Dados", "Segurança", "Carreira Principal", "Sugestão Secundária"])

        for item in historico:
            r = item["respostas"]
            nome = item.get("nome", "N/A")  # usa 'N/A' se o nome não existir
            writer.writerow([
                item["data"],
                nome,
                r["logica"],
                r["visual"],
                r["dados"],
                r["seguranca"],
                item["carreira_principal"],
                item["sugestao_secundaria"]
            ])


    print(f"CSV gerado com sucesso em '{csv_path}'!")


if __name__ == '__main__':
    exportar_csv()