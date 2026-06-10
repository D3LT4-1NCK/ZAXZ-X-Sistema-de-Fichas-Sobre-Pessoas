# O código se repete diversas vezes pois futuramente, cada informação será tratada de forma diferente (alias algumas já são assim)!

try:
    from z_bibliotecas import *
    from y_respostas import *
except Exception as erro:
    print("\n\nErro ao tentar conectar os códigos...\n")
    print(f"\nDetalhes do erro: {erro}\n\n")

try:
    block()

    def pegar_dado(coluna):
        while True:
            mensagem = input_slow(branco() + f"\n\nBoa! Vamos modificar o '{coluna}', insira exatamente o dado que você quer adicionar a esse campo: ")

            if len(mensagem) >= 49 or len(mensagem) < 2:
                print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                continue

            confirmar = input_slow(branco() + f"\nConfirmar dado como '{mensagem}'? (S/N): ").capitalize()
            
            if confirmar in respostas_cancelar:
                print_slow(amarelo() + "\nEncerrando...\n")
                exit()
            elif confirmar in respostas_nao:
                print_slow(branco() + "\nCerto, vamos tentar de novo.\n")
            elif confirmar in respostas_sim:
                print_slow(verde() + "\nBoa! Vamos prosseguir.\n")
                return mensagem
            else:
                print_slow(vermelho() + "\nConfirmação inválida, tente novamente.\n")

    def novo():
        print_slow(verde() + "\nBoa, vamos adicionar um novo alvo...")
        while True:
            nomear = input_slow(branco() + "\nDigite como é nome do nosso alvo (não o nick): ").title()

            if nomear.capitalize() in respostas_cancelar:
                print_slow(amarelo() + "\nEncerrando...\n")
                exit()

            df = pd.read_csv("infos.csv", dtype=str) # Uso a ferramenta de visualização do pandas que lê CSV, e marco que deve ler tudo em formato STR (e não float64), e jogo toda a informação para "df".

            existe = nomear in df["Nome"].values # False/True

            if existe:
                print_slow(vermelho() + "\nEsse nome já existe na tabela.\n")
                continue
            elif len(nomear) >= 39 or len(nomear) < 2:
                print_slow(vermelho() + "\nO nome é grande/curto demais!\n")
                continue
            else:
                df = pd.concat([df, pd.DataFrame([{"Nome": nomear}])], ignore_index=True)
            
            confirmar_nome = input_slow(branco() + f"\nConfirmar dado como '{nomear}'? Cuidado, isso é inalterável! (S/N): ").capitalize()
            
            if confirmar_nome in respostas_cancelar:
                print_slow(amarelo() + "\nEncerrando...\n")
                exit()
            elif confirmar_nome in respostas_nao:
                print_slow(branco() + "\nCerto, vamos tentar de novo.\n")
            elif confirmar_nome in respostas_sim:
                print_slow(verde() + "\nBoa! Vamos prosseguir.\n")
                return nomear
            else:
                print_slow(vermelho() + "\nConfirmação inválida, tente novamente.\n")

            print_slow(branco() + "\nLembre-se, caso você não tenha certa informação, basta teclar 'Enter'.\n")

            # === NICK ===
            while True:
                nickar = input_slow(branco() + "\nDigite o nick do alvo: ")
                if nickar == "":
                    break
                elif nickar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(nickar) >= 39 or len(nickar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{nickar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "Nick"] = nickar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === IDADE ===
            while True:
                idadear = input_slow(branco() + "\nDigite a idade do alvo: ")
                if idadear == "":
                    break
                elif idadear.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(idadear) >= 39 or len(idadear) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                try:
                    if int(idadear) < 12 or int(idadear) > 80:
                        print_slow(vermelho() + "\nForneça uma idade válida.\n")
                        continue
                except ValueError:
                    print_slow(vermelho() + "\nHouve um erro com o campo, tente novamente!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{idadear}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "Idade"] = idadear
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === CPF ===
            while True:
                cpfar = input_slow(branco() + "\nDigite o CPF do alvo: ")
                if cpfar == "":
                    break
                elif cpfar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(cpfar) >= 39 or len(cpfar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{cpfar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "CPF"] = cpfar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === RG ===
            while True:
                rgar = input_slow(branco() + "\nDigite o RG do alvo: ")
                if rgar == "":
                    break
                elif rgar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(rgar) >= 39 or len(rgar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{rgar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "RG"] = rgar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === ANIVERSÁRIO ===
            while True:
                aniversarioar = input_slow(branco() + "\nDigite o aniversário do alvo: ")
                if aniversarioar == "":
                    break
                elif aniversarioar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(aniversarioar) >= 39 or len(aniversarioar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{aniversarioar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "Aniversário"] = aniversarioar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === GÊNERO ===
            while True:
                generoar = input_slow(branco() + "\nDigite o gênero do alvo: ")
                if generoar == "":
                    break
                elif generoar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(generoar) >= 39 or len(generoar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{generoar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "Gênero"] = generoar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === EMAIL ===
            while True:
                emailar = input_slow(branco() + "\nDigite o email do alvo: ")
                if emailar == "":
                    break
                elif emailar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(emailar) >= 39 or len(emailar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{emailar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "Email"] = emailar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === NÚMERO ===
            while True:
                numeroar = input_slow(branco() + "\nDigite o número do alvo: ")
                if numeroar == "":
                    break
                elif numeroar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(numeroar) >= 39 or len(numeroar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{numeroar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "Número"] = numeroar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === CEP ===
            while True:
                cepar = input_slow(branco() + "\nDigite o CEP do alvo: ")
                if cepar == "":
                    break
                elif cepar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(cepar) >= 39 or len(cepar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{cepar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "CEP"] = cepar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === RUA ===
            while True:
                ruaar = input_slow(branco() + "\nDigite a rua do alvo: ")
                if ruaar == "":
                    break
                elif ruaar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(ruaar) >= 39 or len(ruaar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{ruaar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "Rua"] = ruaar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === CIDADE ===
            while True:
                cidadear = input_slow(branco() + "\nDigite a cidade do alvo: ")
                if cidadear == "":
                    break
                elif cidadear.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(cidadear) >= 39 or len(cidadear) < 2:
                    print_slow(vermelho() + "\nO nome é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{cidadear}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "Cidade"] = cidadear
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === PAÍS ===
            while True:
                paisar = input_slow(branco() + "\nDigite o país do alvo: ")
                if paisar == "":
                    break
                elif paisar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(paisar) >= 39 or len(paisar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{paisar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "País"] = paisar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === TRABALHO / ESCOLARIDADE ===
            while True:
                trabalho_escolaridadear = input_slow(branco() + "\nDigite o trabalho/escolaridade do alvo: ")
                if trabalho_escolaridadear == "":
                    break
                elif trabalho_escolaridadear.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(trabalho_escolaridadear) >= 39 or len(trabalho_escolaridadear) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{trabalho_escolaridadear}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "Trabalho/Escolaridade"] = trabalho_escolaridadear
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            # === IP ===
            while True:
                ipar = input_slow(branco() + "\nDigite o IP do alvo: ")
                if ipar == "":
                    break
                try:
                    ipaddress.ip_address(ipar)
                except ValueError:
                    print_slow(vermelho() + "\nIP inválido.\n")
                    continue
                if ipar.capitalize() in respostas_cancelar:
                    print_slow(amarelo() + "\nEncerrando...\n")
                    exit()
                elif len(ipar) >= 39 or len(ipar) < 2:
                    print_slow(vermelho() + "\nO dado é grande/curto demais!\n")
                    continue
                confirmar = input_slow(branco() + f"\nConfirmar dado como '{ipar}'? (S/N): ").capitalize()
                if confirmar in respostas_sim:
                    df.loc[df["Nome"] == nomear, "IP"] = ipar
                    break
                else:
                    print_slow(vermelho() + "\nTente novamente.\n")

            df.to_csv("infos.csv", index=False)
            
            print_slow(verde() + "\nFinalizado.\n")
            subprocess.run("sqlite3 resultado.db < transformador.sql 2>/dev/null", shell=True)
            # fazer sistema de novamente depois.
            return 0

    def existente():
        print_slow(verde() + "\nBoa, vamos adicionar uma informação (ou mais) a um alvo existente...")
        while True:
            print_slow(branco() + "\nDigite o nome do alvo que você quer modificar (não o nick), os nomes são:\n\n")
            subprocess.run("sqlite3 resultado.db < transformador2.sql 2>/dev/null", shell=True)
            nome = input_slow(branco() + "\n\nInsira o nome: ").title()

            if nome.capitalize() in respostas_cancelar:
                print_slow(amarelo() + "\nEncerrando...\n")
                exit()

            df = pd.read_csv("infos.csv", dtype=str) # Uso a ferramenta de visualização do pandas que lê CSV, e marco que deve ler tudo em formato STR (e não float64), e jogo toda a informação para "df".

            existe = nome in df["Nome"].values # False/True

            if not existe:
                print_slow(vermelho() + "\nInsira um nome existente.\n")
                continue

            else:
                print_slow(verde() + f"\nBoa, vamos modificar/adicionar informações ao alvo '{nome}'.")

                while True:
                    print_slow(branco() + "\nDigite o nome exato da coluna que você quer modificar/adicionar uma informação, elas são:\n\n")
                    print_slow(" | ".join(df.columns))
                    coluna = input_slow(branco() + "\n\nInsira: ").capitalize()
                    
                    if coluna in respostas_cancelar:
                        print_slow(amarelo() + "\nEncerrando...\n")
                        exit()

                    elif coluna in resposta_nome:
                        coluna = 'Nome'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_nick:
                        coluna = 'Nick'
                        mensagem = pegar_dado(coluna)
                    
                    elif coluna in resposta_idade:
                        coluna = 'Idade'
                        mensagem = pegar_dado(coluna)
                    
                    elif coluna in resposta_cpf:
                        coluna = 'CPF'
                        mensagem = pegar_dado(coluna)
                    
                    elif coluna in resposta_rg:
                        coluna = 'RG'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_aniversario:
                        coluna = 'Aniversário'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_genero:
                        coluna = 'Gênero'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_email:
                        coluna = 'Email'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_numero:
                        coluna = 'Número'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_cep:
                        coluna = 'CEP'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_rua:
                        coluna = 'Rua'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_cidade:
                        coluna = 'Cidade'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_pais:
                        coluna = 'País'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_trabalho_escolaridade:
                        coluna = 'Trabalho/Escolaridade'
                        mensagem = pegar_dado(coluna)

                    elif coluna in resposta_ip:
                        coluna = 'IP'
                        mensagem = pegar_dado(coluna)

                    else:
                        print_slow(vermelho() + "\nInsira um campo existente.\n")
                        continue

                    print("\n")
                    dormir(2)
                    df.loc[df["Nome"] == f"{nome}", f"{coluna}"] = mensagem # Igual marcar X + Y, essas são as coordenadas exatas, depois passo o valor.
                    df.to_csv("infos.csv", index=False) # Salvo as modificações + não permito indexação usando o parâmetro da função "to_csv".
                    subprocess.run("sqlite3 resultado.db < transformador.sql 2>/dev/null", shell=True)
                    print("\n")

                    while True:
                        continuar = input_slow(branco() + "\nQuer modificar/adicionar outra informação a esse mesmo alvo? (S/N): ").capitalize()

                        if continuar in respostas_nao:
                            pingar = 1
                            break
                        elif continuar in respostas_sim:
                            print_slow(verde() + f"\nBoa, vamos modificar/adicionar mais informações ao alvo '{nome}'.")
                            pingar = 0
                            break
                        else:
                            print_slow(vermelho() + "\nInsira um campo válido.\n")

                    if pingar == 1:
                        while True:
                            continuar = input_slow(branco() + "\nQuer fazer o mesmo procedimento com outro alvo? (S/N): ").capitalize()

                            if continuar in respostas_nao:
                                return 1
                            elif continuar in respostas_sim:
                                print_slow(verde() + f"\nBoa, vamos retornar a tela de seleção de alvos...\n")
                                break
                            else:
                                print_slow(vermelho() + "\nInsira um campo válido.\n")
                    elif pingar == 0:
                        continue

    print(roxo() + figlet_format("ZAXZ    X"))
    print_slow(roxo() + "\nSistema inteligente de anotações pessoais.\n")
    print_slow(branco() + "\nAtenção: Sempre que quiser sair do sistema, basta digitar algo como 'cancelar'; não feche o terminal ou encerre o processo a força!\n")
    while True:
        decisao = input_slow(branco() + "\nVocê quer adicionar um novo alvo a tabela (1), acrescentar informações a um alvo existente (2), ou quer visualizar a tabela atual (3)?\n\n- ").capitalize()
        if decisao in respostas_cancelar:
            print_slow(amarelo() + "\n\nEncerrando...\n\n")
            exit()
        elif decisao in ("1", "Um", "Novo", "Novo alvo", "Adicionar", "Adicionar novo", "Adicionar alvo", "Inserir", "Criar"):
            pyautogui.hotkey("win", "up")
            pyautogui.hotkey("alt", "f10")
            novo()
            break
        elif decisao in ("2", "Dois", "Existente", "Alvo existente", "Acrescentar", "Acrescentar informações", "Adicionar info", "Atualizar", "Modificar", "Mudar"):
            pyautogui.hotkey("win", "up")
            pyautogui.hotkey("alt", "f10")
            existente()
            break
        elif decisao in ("3", "Trẽs", "Tres", "Três", "Visualizar", "Ver", "Ver como está", "Visualizar tabela atual", "Visualizar tabela", "Atual"):
            pyautogui.hotkey("win", "up")
            pyautogui.hotkey("alt", "f10")
            subprocess.run("sqlite3 resultado.db < transformador.sql 2>/dev/null", shell=True)
            print_slow(verde() + "\nTabela carregada!\n\nO que quer fazer agora?\n")
        else:
            print_slow(vermelho() + "\nInsira um campo válido.\n")
        
    print_slow(roxo() + "\nObrigado por usar esse sistema.\n")

except Exception as erro:
    print_slow(vermelho() + "\n\nErro ao tentar executar o código - Reinstale o sistema.\n")
    print_slow(vermelho() + f"\nDetalhes do erro: {erro}\n\n")
