def sugerir_top2_carreiras(respostas):
    logica, visual, dados, seguranca = respostas

    pontuacao = {
        "Backend Developer": 0,
        "Frontend Developer": 0,
        "Cientista de Dados": 0,
        "QA Tester": 0,
        "Especialista em Cibersegurança": 0,
        "DevOps": 0
    }

    if logica:
        pontuacao["Backend Developer"] += 2
        pontuacao["Cientista de Dados"] += 2
        pontuacao["QA Tester"] += 1

    if visual:
        pontuacao["Frontend Developer"] += 3

    if dados:
        pontuacao["Cientista de Dados"] += 3
        pontuacao["Backend Developer"] += 1

    if seguranca:
        pontuacao["Especialista em Cibersegurança"] += 3
        pontuacao["DevOps"] += 1

    # Ordena as carreiras da maior para a menor pontuação
    top2 = sorted(pontuacao.items(), key=lambda x: x[1], reverse=True)[:2]
    carreira_1, carreira_2 = top2[0][0], top2[1][0]

    return (carreira_1, gerar_explicacao(carreira_1)), (carreira_2, gerar_explicacao_secundaria(carreira_2))

def gerar_explicacao(carreira):
    explicacoes = {
        "Backend Developer": "Tu curtes lógica e trabalhar nos bastidores. Backend é ideal pra ti!",
        "Frontend Developer": "Tens olho pro visual e curtes criar interfaces. Frontend é tua cara!",
        "Cientista de Dados": "Gosta de dados, estatísticas e descobrir padrões. Ciência de Dados te espera!",
        "QA Tester": "Te interessa por testes, qualidade e encontrar erros? QA é pra ti!",
        "Especialista em Cibersegurança": "Gosta de proteger sistemas e lidar com riscos? Segurança digital é teu mundo.",
        "DevOps": "Curte automatizar processos e integrar sistemas? DevOps pode ser teu caminho."
    }
    return explicacoes.get(carreira, "Carreira interessante no mundo tech!")

def gerar_explicacao_secundaria(carreira):
    secundarias = {
        "Backend Developer": "Também poderias seguir como Backend, pela tua afinidade com lógica e estrutura.",
        "Frontend Developer": "O visual e a interatividade podem ser um bom caminho alternativo.",
        "Cientista de Dados": "Também tens perfil pra lidar com dados e insights.",
        "QA Tester": "Teu olhar crítico pode se encaixar bem com QA.",
        "Especialista em Cibersegurança": "Segurança também pode ser um bom caminho, se tiveres curiosidade.",
        "DevOps": "Automação e infraestrutura podem ser tua segunda via."
    }
    return secundarias.get(carreira, "Outra carreira possível no mundo tech!")
