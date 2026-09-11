from typing import Dict, TypedDict

estados: Dict[str, str] = {
    "São Paulo" : "São Paulo",
    "Rio de Janeiro" : "Rio de Janeiro",
    "Minas Gerais" : "Belo Horizonte",
}

def percorrer_estados() -> None:#Não esqueça de criar um feature que só permite o usuário acessar a função percorrer_estados() após o término do jogo.
    for estado, capital in estados.items():
        print(f"Parabéns!\n{estado} -> {capital}") 

def buscar_estado(estado: str) -> str:

    estado_nome = estado.strip().upper()

    return estados.get(estado_nome, "Estado não encontrado")

def main():
    lista_estados = list(estados.keys())
    print("Seja bem-vindo ao jogo de adivinhação de capitais!")
    while(True):
    
        opcao_user = input("Digite uma das opções para continuar: \n1 - Jogar\n2 - Sair\n3 - Listar estados e capitais\nSua opção: ")

        try:
            opcao_user = int(opcao_user)
        except ValueError:
            print("Opção inválida. Por favor, digite um número válido.\n")
            continue

        if opcao_user == "1":

            #verificar a quantide de tentativas e acertos do usuário
            
            print("Vamos começar o jogo!")
            while len(lista_estados) > 0:
                tentivas += 1
                estado = lista_estados.pop(0)

                option_user = input(f"Qual é a capital do estado {estado}? ")

                if option_user.strip().lower() == estados[estado].lower():
                    acertos += 1
                    print(f"Parabéns! Você acertou! A capital de {estado} é {estados[estado]}.")
                    continue
                else:
                    print("Tente novamente: ")
                    lista_estados.append(estado)
                    continue

if __name__ == "__main__":
    main()