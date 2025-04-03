# MentorAI - Descobre a tua Carreira Tech Ideal

 **MentorAI** é uma aplicação web desenvolvida com Flask que ajuda pessoas a descobrirem qual área da tecnologia combina mais com elas com base em perguntas simples e personalizadas. O sistema oferece uma sugestão principal e uma secundária, busca vagas reais para a carreira sugerida e ainda gera um relatório em PDF personalizado com base nas respostas.

---

## Funcionalidades

- Formulário interativo com perguntas sobre preferências e perfil
- Sugestão de 2 carreiras tech ideais com explicação
- Busca automática de vagas reais (via RemoteOK)
- Geração de PDF personalizado com nome, perfil e vagas
- Armazena histórico de resultados em JSON e exporta para CSV

---

## Estrutura do Projeto

```
mentorai-career-advisor/
├── run.py
├── historico_resultados.json
├── historico_resultados.csv
├── requirements.txt
├── README.md
└── app/
    ├── __init__.py
    ├── routes/
    │   └── frontend.py
    ├── services/
    │   ├── sugestoes.py
    │   └── vagas_api.py
    ├── utils/
    │   ├── historico.py
    │   └── exportador.py
    ├── templates/
    │   ├── inicio.html
    │   ├── index.html
    │   └── resultado.html
    └── static/
        └── style.css
```

---

## Como executar localmente

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/mentorai-career-advisor.git
cd mentorai-career-advisor
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o projeto:
```bash
python run.py
```

5. Acesse no navegador:
```
http://127.0.0.1:5000
```

---

## Tecnologias Utilizadas

- Python 3
- Flask
- FPDF
- Requests
- HTML5 + CSS3

---

## Autor

Desenvolvido por **Emanuel Soares**

> Projeto criado para estudos e portfólio. Com ideias práticas e abordagem real, o MentorAI visa ajudar iniciantes a encontrarem direção no mundo tech.

