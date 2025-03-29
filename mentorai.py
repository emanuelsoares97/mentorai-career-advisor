from vagas_api import buscar_vagas

from sugestoes import sugerir_top2_carreiras



def perguntar(pergunta):
    while True:
        resposta = input(f"{pergunta} (s/n): ").strip().lower()
        if resposta in ['s', 'n']:
            return resposta == 's'
        print("Responde com 's' para sim ou 'n' para não.")

def main():
    print("🧠 Bem-vindo ao MentorAI!")
    print("Responde a algumas perguntas para descobrir tua carreira tech ideal.\n")

    logica = perguntar("Gosta de resolver problemas lógicos?")
    visual = perguntar("Prefere trabalhar com a parte visual e design?")
    dados = perguntar("Gosta de trabalhar com dados e análises?")
    seguranca = perguntar("Tem interesse em segurança digital?")

    respostas = (logica, visual, dados, seguranca)

    (carreira1, explicacao1), (carreira2, explicacao2) = sugerir_top2_carreiras(respostas)

    print("\n🔍 Carreira mais compatível:", carreira1)
    print("💡", explicacao1)

    print("\n🔁 Segunda sugestão:", carreira2)
    print("💭", explicacao2)

    buscar_vagas(carreira1)


if __name__ == "__main__":
    main()
