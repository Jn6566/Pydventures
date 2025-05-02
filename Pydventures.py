######################## Pydventures ########################
import random # Importa a biblioteca random:

""" ############### Novo Jogo ############### """
def novo_jogo():
    print("######################## Pydventures ########################\n\n")
    
    # Criação de personagem:
    print("########### Novo jogo ###########\n")
    player_nivel = 1
    player_nome = input("Insira o nome do seu aventureiro:\n")
    
    # Epílogo:
    print(f"\n\nUma nova masmorra no reino de Python foi descoberta e o rei criou uma expedição voluntária para aqueles que tivessem coragem para explorá-la: {player_nome} um aventureiro cujo estava precisando de uma grana decide entrar para a expedição em busca de tesouros e riquezas.")
    print(f"\n{player_nome} entra na dungeon:")
    
    return player_nome, player_nivel



""" ######################################## Inicio: Banco de Dados ######################################## """

########### Lista de armaduras ###########
lista_armaduras = [
    {"item_indice": 1, "armadura": "Armadura de couro", "armadura_poder": 3},
    {"item_indice": 2, "armadura": "Armadura de bronze", "armadura_poder": 4},
    {"item_indice": 3, "armadura": "Armadura de bronze reforçada", "armadura_poder": 5},
    {"item_indice": 4, "armadura": "Armadura de ferro", "armadura_poder": 6},
    {"item_indice": 5, "armadura": "Armadura de mitrio", "armadura_poder": 8},
    {"item_indice": 0, "armadura": "Roupas normais", "armadura_poder": 0}
]

########### Lista de armas ###########
lista_armas = [
    {"item_indice": 10, "arma": "Espada de bronze", "arma_poder": 1},
    {"item_indice": 11, "arma": "Espada de ferro", "arma_poder": 3},
    {"item_indice": 12, "arma": "Arco e flecha", "arma_poder": 2},
    {"item_indice": 13, "arma": "Machado de guerra", "arma_poder": 4},
    {"item_indice": 14, "arma": "Espada de fogo", "arma_poder": 5}
]

########### Lista de consumíveis ###########
lista_consumiveis = [
    {"item_indice": 6, "consumivel": "Poção de força", "consumivel_poder": 2},
    {"item_indice": 7, "consumivel": "Pergaminho Mísseis Mágicos", "consumivel_poder": 3},
    {"item_indice": 8, "consumivel": "Poção de cura", "consumivel_poder": 1},
    {"item_indice": 9, "consumivel": "Pergaminho Bola de Fogo", "consumivel_poder": 5}
]

########### Lista de monstros ###########
lista_monstros = [
    {"monstro_indice": 1, "monstro": "Zumbi", "monstro_poder": 1},
    {"monstro_indice": 2, "monstro": "Esqueleto", "monstro_poder": 2},
    {"monstro_indice": 3, "monstro": "Esqueleto Arqueiro", "monstro_poder": 4},
    {"monstro_indice": 4, "monstro": "Soldado Esqueleto", "monstro_poder": 7},
    {"monstro_indice": 5, "monstro": "Ork", "monstro_poder": 5},
    {"monstro_indice": 6, "monstro": "Soldado Ork", "monstro_poder": 8},
    {"monstro_indice": 7, "monstro": "Feiticeiro Ork", "monstro_poder": 9},
    {"monstro_indice": 8, "monstro": "Slime", "monstro_poder": 1},
    {"monstro_indice": 9, "monstro": "Aranha Gigante", "monstro_poder": 10},
    {"monstro_indice": 10, "monstro": "Ogro", "monstro_poder": 12},
    {"monstro_indice": 11, "monstro": "Golem de pedra", "monstro_poder": 15},
    {"monstro_indice": 12, "monstro": "Beholder", "monstro_poder": 17},
    {"monstro_indice": 13, "monstro": "Morcego", "monstro_poder": 1},
    {"monstro_indice": 14, "monstro": "Aranha", "monstro_poder": 1},
    {"monstro_indice": 8005, "monstro": "Dragão", "monstro_poder": 20},
    {"monstro_indice": 800, "monstro": "Mímico", "monstro_poder": 7}
]

########### Inventário do jogador ###########
inventario = [
]

""" ######################################## Fim: Banco de Dados ######################################## """



""" ############### Player ############### """
def player(player_nome, player_nivel, player_armadura, player_arma, player_poder):
    print(f"\n\n######################## {player_nome} ########################\n")
    print(f"Nome: {player_nome}     Nivel: {player_nivel}     Poder: {player_poder}")
    print(f"\nArmadura: {player_armadura["armadura"]}     Poder da armadura: {player_armadura["armadura_poder"]}")
    print(f"\nArma: {player_arma["arma"]}     Poder da arma: {player_arma["arma_poder"]}")
    print(f"\n#########################################################")



""" ############### Ver Inventario ############### """
def ver_inventario(inventario):
    print(f"\n\n######################## Inventário ########################\n")
    
    # Imprime a lista inventario:
    for item in inventario:
        print(f"{item["item_indice"]}. {item["consumivel"]}, Poder: {item["consumivel_poder"]}\n")
    
    print("Obs. Os consumíveis serão descartados após o uso em combate.")
    print(f"\n############################################################")



""" ############### Morte do jogador ############### """
def player_morte(player_nome, player_nivel, player_armadura, player_arma, inventario):
    # Biblioteca para chamada de ações da cena:
    opcoes_player_morte = {
        "1": lambda: sala_vazia(player_nome, player_nivel, player_armadura, player_arma, inventario),
        "2": lambda: exit()
    }
    
    print(f"\n\n######################## Game Over ########################\n")
    print("Você Morreu!\n")
    print("1. Respawnar: (Perca 3 níveis)\n")
    print("2. Sair do jogo:")
    
    # Retira 3 níveis do jogador: se o nivel for menor que 3 iguala a um.
    if player_nivel > 3:
        player_nivel = player_nivel - 3
        
    else:
        player_nivel = 1
    
    # Escolhe a próxima ação:
    while True:
        escolha_player_morte = input("\nEscolha uma opcao: ")
        acao_player_morte = opcoes_player_morte.get(escolha_player_morte)
        
        if acao_player_morte:
            acao_player_morte()
            
        else:
            print("Opcao invalida, tente novamente.\n")
            False



""" ############### Fugir ############### """
def fugir(player_nome, player_nivel, player_armadura, player_arma, inventario):
    # Sorteia um número de 1 a 6:
    sort_d6 = random.randint(1, 6)
    
    # Diz se conseguiu fugir ou se falhou:
    if sort_d6 >= 5:
        print(f"\n{player_nome} conseguiu escapar com vida.")
        sala_vazia(player_nome, player_nivel, player_armadura, player_arma, inventario)
    
    else:
        print(f"\n{player_nome} tenta escapar mas o monstro alcança ele no caminho e termina de finaliza-lo.")
        player_morte(player_nome, player_nivel, player_armadura, player_arma, inventario)



""" ############### Baú ############### """
def bau(player_nome, player_nivel, player_armadura, player_arma, inventario, lista_armaduras, lista_armas, lista_consumiveis):
    print("Ao olhar para uma das extremidades da sala você encontra um baú.")
    print("\n\n######################## Baú ########################\n")
    
    # Sorteia qual será o item no baú:
    item_sorteia_bau = random.randint(1, 14)
    
    # Se o item do baú for uma armadura (índices 1 a 5):
    if item_sorteia_bau >= 1 and item_sorteia_bau <= 5:
        armadura_retirada = next((armadret for armadret in lista_armaduras if armadret["item_indice"] == item_sorteia_bau), None)
        
        if armadura_retirada:
            print(f"Você encontrou: {armadura_retirada['armadura']}, Poder da armadura: {armadura_retirada['armadura_poder']}\n")
            equipar_armadura = input("Deseja equipar? (y/n)\n").lower()
            
            while True:
                if equipar_armadura == "y":
                    player_armadura = armadura_retirada
                    print(f"\n{player_nome} equipou a {armadura_retirada['armadura']}!")
                    sala_vazia(player_nome, player_nivel, player_armadura, player_arma, inventario)
                    break
                
                elif equipar_armadura == "n":
                    print(f"{player_nome} decide deixar no baú.")
                    sala_vazia(player_nome, player_nivel, player_armadura, player_arma, inventario)
                    break
                
                else:
                    print("Opção inválida, tente novamente.\n")
                    equipar_armadura = input("Deseja equipar? (y/n)\n").lower()

    # Se o item do baú for uma arma (índices 10 a 14):
    elif item_sorteia_bau >= 10 and item_sorteia_bau <= 14:
        arma_retirada = next((armaret for armaret in lista_armas if armaret["item_indice"] == item_sorteia_bau), None)
        
        if arma_retirada:
            print(f"Você encontrou: {arma_retirada['arma']}, Poder da arma: {arma_retirada['arma_poder']}\n")
            equipar_arma = input("Deseja equipar? (y/n)\n").lower()
            
            while True:
                if equipar_arma == "y":
                    player_arma = arma_retirada
                    print(f"\n{player_nome} equipou a {arma_retirada['arma']}!")
                    sala_vazia(player_nome, player_nivel, player_armadura, player_arma, inventario)
                    break
                
                elif equipar_arma == "n":
                    print(f"{player_nome} decide deixar no baú.")
                    sala_vazia(player_nome, player_nivel, player_armadura, player_arma, inventario)
                    break
                
                else:
                    print("Opção inválida, tente novamente.\n")
                    equipar_arma = input("Deseja equipar? (y/n)\n").lower()

    # Se o item do baú for um consumível (índices 6 a 9):
    elif item_sorteia_bau >= 6 and item_sorteia_bau <= 9:
        consumivel_retirado = next((consret for consret in lista_consumiveis if consret["item_indice"] == item_sorteia_bau), None)
        
        if consumivel_retirado:
            print(f"Você encontrou: {consumivel_retirado['consumivel']}, Poder do consumível: {consumivel_retirado['consumivel_poder']}\n")
            add_inventario = input("Deseja colocar no inventário? (y/n)\n").lower()
            
            while True:
                if add_inventario == "y":
                    inventario.append(consumivel_retirado)
                    print(f"\n{player_nome} colocou o {consumivel_retirado['consumivel']} no inventário.")
                    sala_vazia(player_nome, player_nivel, player_armadura, player_arma, inventario)
                    break
                
                elif add_inventario == "n":
                    print(f"{player_nome} decide deixar no baú.")
                    sala_vazia(player_nome, player_nivel, player_armadura, player_arma, inventario)
                    break
                
                else:
                    print("Opção inválida, tente novamente.\n")
                    add_inventario = input("Deseja colocar no inventário? (y/n)\n").lower()



""" ############### Vitória Luta ############### """
def vitoria_luta(player_nome, player_nivel, player_armadura, player_arma, inventario, lista_armaduras, lista_armas, lista_consumiveis):
    print("\n\n######################## Vitória ########################\n")
    
    # Sobe o nívvel do jogador em um:
    player_nivel = player_nivel + 1
    print("Você subiu 1 nível.\n")
    
    # Caso o jogador chegue no nível 10 ele zera o jogo.
    if player_nivel == 10:
        print("\n\n######################## Jogo Completo ########################\n")
        print(f"Após enfrentar vários desafios {player_nome} finalmente se tornou um oponente imbatível.")
        print(f"Sendo assim {player_nome} retorna triunfante da masmorra com uma imensurável quantidade")
        print(f"de tesouros, o suficiente para passar o resto de sua vida em uma mansão tranquilamente.\n")
        print(f"No reino de Python inumeras cantigas e lendas foram criadas sobre {player_nome} e seja")
        print(f"homem ou monstro não existe um que não tenha ouvido falar de {player_nome}.")
        
        print(f"\n\nCréditos:\nDesenvolvedor: José Riguetti Neto")
        exit() # Encerra  o jogo.
    
    else:
        # Executa a função baú:
        bau(player_nome, player_nivel, player_armadura, player_arma, inventario, lista_armaduras, lista_armas, lista_consumiveis)



""" ############### Lutar ############### """
def lutar(player_nome, player_nivel, player_armadura, player_arma, player_poder, inventario, monstro_encontrado):
    # Mensagem de derrota 1:
    if player_poder == monstro_encontrado["monstro_poder"]:
        print(f"\n{player_nome} bravamente empunha sua arma e luta contra o {monstro_encontrado["monstro"]}.")
        print(f"Após uma longa troca de golpes com o {monstro_encontrado["monstro"]}, {player_nome} recebe um golpe fatal.")
        player_morte(player_nome, player_nivel, player_armadura, player_arma, inventario)
    
    # Mensagem de derrota 2:
    elif player_poder < (monstro_encontrado["monstro_poder"]) and player_poder > (monstro_encontrado["monstro_poder"] - 7):
        print(f"\n{player_nome} bravamente empunha sua arma e luta contra o {monstro_encontrado["monstro"]}.")
        print(f"Após uma troca de golpes com o {monstro_encontrado["monstro"]}, {player_nome} recebe um golpe fatal.")
        player_morte(player_nome, player_nivel, player_armadura, player_arma, inventario)
    
    #Mensagem de derrota 3:
    elif player_poder < (monstro_encontrado["monstro_poder"] - 7):
        print(f"\nO {monstro_encontrado["monstro"]} te pisoteia e você morre. Seu fraco!")
        player_morte(player_nome, player_nivel, player_armadura, player_arma, inventario)

    # Mensagem de vitória 1:
    elif player_poder > monstro_encontrado["monstro_poder"] and player_poder - 7 < monstro_encontrado["monstro_poder"]:
        print(f"\n{player_nome} bravamente empunha sua arma e luta contra o {monstro_encontrado['monstro']}.")
        print(f"Após uma troca de golpes {player_nome} desfere um golpe decisivo que finaliza o {monstro_encontrado['monstro']}.")
        vitoria_luta(player_nome, player_nivel, player_armadura, player_arma, inventario, lista_armaduras, lista_armas, lista_consumiveis)
    
    # Mensagem de vitória 2:
    elif player_poder - 7 > monstro_encontrado["monstro_poder"]:
        print(f"\nSua aura já foi o suficiente para deixar o {monstro_encontrado['monstro']} tremendo de medo.")
        print(f"Bastou um golpe e a existência do {monstro_encontrado['monstro']} foi apagada.")
        vitoria_luta(player_nome, player_nivel, player_armadura, player_arma, inventario, lista_armaduras, lista_armas, lista_consumiveis)



""" ############### Retorno Combate ############### """
def retorno_combate(player_nome, player_nivel, player_armadura, player_arma, player_poder, inventario, lista_monstros, monstro_encontrado):
    # Biblioteca para a chamada de ações da cena:
    opcoes_retorno_combate = {
        "1": lambda: player(player_nome, player_nivel, player_armadura, player_arma, player_poder),
        "2": lambda: lutar(player_nome, player_nivel, player_armadura, player_arma, player_poder, inventario, monstro_encontrado),
        "3": lambda: ver_inventario(inventario),
        "4": lambda: fugir(player_nome, player_nivel, player_armadura, player_arma, inventario)
    }
    
    print(f"\n\nMonstro: {monstro_encontrado["monstro"]}, Poder: {monstro_encontrado["monstro_poder"]}\n")
    print("1. Consultar Status do Jogador:\n")
    print("2. Lutar:\n")
    print("3. Inventário:\n")
    print("4. Fugir:\n")
    
    # Escolhe a próxima ação:
    while True:
        escolha_retorno_combate = input("\nEscolha uma opcao: ")
        acao_retorno_combate = opcoes_retorno_combate.get(escolha_retorno_combate)
        
        if acao_retorno_combate:
            acao_retorno_combate()
            
        else:
            print("Opcao invalida, tente novamente.\n")
            False



""" ############### Usar consumível ############### """
def usar_consumivel(player_nome, player_nivel, player_armadura, player_arma, player_poder, inventario, lista_monstros, monstro_encontrado):
    # Exibe inventário:
    ver_inventario(inventario)
    
    while True:
        # Escolhe qual item o jogador quer utilizar
        escolha_item_consumido = int(input("\nSelecione um item consumível (tecle 0 para retornar ao combate): "))
        
        # Se o jogador escolhe 0, volta ao combate
        if escolha_item_consumido == 0:
            retorno_combate(player_nome, player_nivel, player_armadura, player_arma, player_poder, inventario, lista_monstros, monstro_encontrado)
            return
        
        # Procura o consumível no inventário
        item_consumido = next((icons for icons in inventario if icons["item_indice"] == escolha_item_consumido), None)
        
        # Se o item não for encontrado
        if not item_consumido:
            print("Item não encontrado no inventário. Tente novamente.\n")
            continue
        
        print(f"\n{player_nome} usa {item_consumido['consumivel']} e sente-se mais preparado.")
        print(f"\nPoder: + {item_consumido['consumivel_poder']}")
        
        # Adiciona o poder do item ao poder total do personagem:
        player_poder += item_consumido["consumivel_poder"]
        
        # Remove o item selecionado do inventário
        inventario.remove(item_consumido)
        
        # Volta ao combate
        retorno_combate(player_nome, player_nivel, player_armadura, player_arma, player_poder, inventario, lista_monstros, monstro_encontrado)
        return



""" ############### Sala c/ Monstro ############### """
def sala_monstro(player_nome, player_nivel, player_armadura, player_arma, player_poder, inventario, lista_monstros):
    # Sorteia qual será o monstro na sala:
    monstro_sorteia = random.randint(1, 14)
    monstro_encontrado = next((mi for mi in lista_monstros if mi["monstro_indice"] == monstro_sorteia), None)
    
    # Biblioteca para a chamada de ações da cena:
    opcoes_sala_monstro = {
        "1": lambda: player(player_nome, player_nivel, player_armadura, player_arma, player_poder),
        "2": lambda: lutar(player_nome, player_nivel, player_armadura, player_arma, player_poder, inventario, monstro_encontrado),
        "3": lambda: usar_consumivel(player_nome, player_nivel, player_armadura, player_arma, player_poder, inventario, lista_monstros, monstro_encontrado),
        "4": lambda: fugir(player_nome, player_nivel, player_armadura, player_arma, inventario),
    }
    
    print("\n\n######################## Combate ########################\n")
    print(f"{player_nome} se depara com um {monstro_encontrado["monstro"]}.\n")
    print(f"Monstro: {monstro_encontrado["monstro"]}, Poder: {monstro_encontrado["monstro_poder"]}\n")
    print("1. Consultar Status do Jogador:\n")
    print("2. Lutar:\n")
    print("3. Usar consumível:\n")
    print("4. Fugir:\n")
    
    # Escolhe a próxima ação:
    while True:
        escolha_sala_monstro = input("\nEscolha uma opcao: ")
        acao_sala_monstro = opcoes_sala_monstro.get(escolha_sala_monstro)
        
        if acao_sala_monstro:
            acao_sala_monstro()
            
        else:
            print("Opcao invalida, tente novamente.\n")
            False



""" ############### Sala Vazia ############### """
def sala_vazia(player_nome, player_nivel, player_armadura, player_arma, inventario):
    # Atualiza status do jogador
    player_poder = player_nivel + player_armadura["armadura_poder"] + player_arma["arma_poder"]
    
    # Biblioteca para a chamada de ações da cena:
    opcoes_sala_vazia = {
        "1": lambda: player(player_nome, player_nivel, player_armadura, player_arma, player_poder),
        "2": lambda: sala_monstro(player_nome, player_nivel, player_armadura, player_arma, player_poder, inventario, lista_monstros),
        "3": lambda: ver_inventario(inventario)
    }
    
    print("\n\n######################## Sala Vazia ########################\n")
    print(f"{player_nome} se depara com uma sala vazia.\n")
    print("1. Consultar Status do Jogador:\n")
    print("2. Avançar na dungeon:\n")
    print("3. Inventário:")
    
    # Escolhe a próxima ação:
    while True:
        escolha_sala_vazia = input("\nEscolha uma opcao: ")
        acao_sala_vazia = opcoes_sala_vazia.get(escolha_sala_vazia)
        
        if acao_sala_vazia:
            acao_sala_vazia()
            
        else:
            print("Opcao invalida, tente novamente.\n")
            False



""" ############### Main ############### """
def main():
    # Chama os valores da criação de personagem:
    player_nome, player_nivel = novo_jogo()
    
    # Adiquirindo arma e armadura inicial:
    player_armadura = next((parmadura for parmadura in lista_armaduras if parmadura["item_indice"] == 0), None)
    player_arma = next((parma for parma in lista_armas if parma["item_indice"] == 10), None)
    
    # Inicia o jogo:
    sala_vazia(player_nome, player_nivel, player_armadura, player_arma, inventario)

if __name__ == "__main__":
    main()
