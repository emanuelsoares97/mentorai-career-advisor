import requests

def buscar_vagas(carreira):
    termos_busca = {
        "Backend Developer": "backend",
        "Frontend Developer": "frontend",
        "Cientista de Dados": "data",
        "QA Tester": "qa",
        "Especialista em Cibersegurança": "security",
        "DevOps": "devops"
    }

    termo = termos_busca.get(carreira.lower().title(), carreira.lower())
    url = "https://remoteok.com/api"

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resposta = requests.get(url, headers=headers, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        vagas = dados[1:]  # ignora o metadata
        encontradas = []

        for vaga in vagas:
            titulo = vaga.get("position", "").lower()
            if termo in titulo:
                url_vaga = vaga['url']
                if url_vaga.startswith("/"):
                    url_vaga = "https://remoteok.com" + url_vaga
                encontradas.append({
                    "titulo": vaga['position'],
                    "empresa": vaga['company'],
                    "link": url_vaga
                })

        return encontradas[:3]
    except requests.RequestException:
        return []
