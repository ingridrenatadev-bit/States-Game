from typing import Dict, TypedDict

estados: Dict[str, str] = {
    "São Paulo" : "São Paulo",
    "Rio de Janeiro" : "Rio de Janeiro",
    "Minas Gerais" : "Belo Horizonte",
}

def jogar_partida() -> tuple[int, int, bool]:

    print("\n--- Vamos começar o jogo! ---")
    lista_estados = list(estados.keys())
    tentativas = 0
    acertos = 0

    while len(lista_estados) > 0:
        estado = lista_estados.pop(0)
        option_user = input(f"Qual é a capital do estado {estado}? (ou digite 'sair'):")
        
        if option_user.strip().lower() == 'sair':
            print("Você escolheu sair do jogo.")
            break

        tentativas += 1
    
        if option_user.strip().lower() == estados[estado].lower():
            acertos += 1
            print(f"Parabéns! Você acertou! A capital de {estado} é {estados[estado]}.")
            continue

        else:
            print("Tente novamente: ")
            lista_estados.append(estado)
            continue

    if tentativas > 0:
        porcentagem = (acertos / tentativas) * 100
        print(f"\n--- FIM DE JOGO ---")
        print(f"Acertos: {acertos} | Tentativas: {tentativas}")
        print(f"Aproveitamento: {porcentagem:.2f}%")
    else:
        print("\nNenhuma pergunta respondida.")

    completou_jogo = len(lista_estados) == 0
    return tentativas, acertos

def percorrer_estados() -> None:#Não esqueça de criar um feature que só permite o usuário acessar a função percorrer_estados() após o término do jogo, ou seja, quando o usuário acertar todas as capitais.
    for estado, capital in estados.items():
        print(f"Parabéns!\n{estado} -> {capital}") 

def buscar_estado(estado: str) -> str:

    estado_nome = estado.strip().upper()

    return estados.get(estado_nome, "Estado não encontrado")


def main():
    lista_estados = list(estados.keys())
    print("Seja bem-vindo ao jogo de adivinhação de capitais!")

    while True:

        print("\n=== JOGO DOS ESTADOS ===")
        print("1 - Jogar")
        print("2 - Listar Estados e Capitais")
        print("3 - Sair")
        
        opcao = input("Sua opção: ").strip()

        if opcao == "1":
            jogar_partida()

        elif opcao == "2":
            percorrer_estados()
        elif opcao == "3":
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        


if __name__ == "__main__":
    main()