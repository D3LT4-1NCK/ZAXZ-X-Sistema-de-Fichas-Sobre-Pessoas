# Respostas de escolhas:

try:
    resposta_nome = (
        "Nome", "Nome completo", "Nomear", "Nomeação", "Nome da pessoa", 
        "Primeiro nome", "Nome todo", "Nome de batismo", "Nome civil", 
        "Vulgo nome", "Nome registrado", "Identificação", "Seu nome", "Nome e sobrenome"
    )

    resposta_nick = (
        "Nick", "Nickname", "Apelido", "Nome de usuário", "Username", 
        "User", "Arroba", "Codinome", "Alcunha", "Pseudônimo", 
        "Nome na rede", "Nome do perfil", "Login", "Id", "Vulgo"
    )

    resposta_idade = (
        "Idade", "Anos", "Tempo de vida", "Quantos anos", "Primaveras", 
        "Idade atual", "Quantos anos tem", "Faixa etária", "Nível de idade", 
        "Contagem de anos", "Ciclos", "Quantas primaveras", "Idade em anos"
    )

    resposta_cpf = (
        "Cpf", "C.p.f.", "Documento", "Cadastro de pessoa física", "Cpf número", 
        "Número do cpf", "Cadastro nacional", "Cpf do usuário", "Documento cpf", 
        "Registro cpf", "Cpf digital"
    )

    resposta_rg = (
        "Rg", "R.g.", "Identidade", "Registro geral", "Carteira de identidade", 
        "Número do rg", "Rg número", "Documento de identidade", "Cédula de identidade", 
        "Rg do usuário", "Registro civil"
    )

    resposta_aniversario = (
        "Aniversário", "Data de nascimento", "Nascimento", "Bday", "Data niver", 
        "Dia de nascimento", "Nascido em", "Data natalícia", "Data de nasc", 
        "Dia do nascimento", "Data do niver", "Aniversariante"
    )

    resposta_genero = (
        "Gênero", "Sexo", "Identidade de gênero", "Orientação", "Opção", 
        "Sexo biológico", "Gênero do usuário", "Identificação de gênero", 
        "Tipo de gênero", "Opção sexual"
    )

    resposta_email = (
        "Email", "E-mail", "Correio eletrônico", "Endereço eletrônico", "Mail", 
        "Caixa de entrada", "Email do usuário", "Endereço de email", "Contato email", 
        "E mail", "Correio digital", "Email corporativo"
    )

    resposta_numero = (
        "Número", "Celular", "Zap", "Telefone", "Tel", "Cel", "Whatsapp", 
        "Telefone celular", "Número de telefone", "Contato", "Telefone de contato", 
        "Whats", "Número do zap", "Tel celular"
    )

    resposta_cep = (
        "Cep", "C.e.p.", "Código postal", "Código de endereçamento", "Cep residencial", 
        "Código de área", "Código postal cep", "Cep do usuário", "Número do cep", "Endereço cep"
    )

    resposta_rua = (
        "Rua", "Avenida", "Logradouro", "Endereço", "Moradia", "Residência", 
        "Local", "Logradouro residencial", "Endereço de casa", "Bairro", 
        "Casa", "Alameda", "Travessa", "Praça"
    )

    resposta_cidade = (
        "Cidade", "Município", "Localidade", "Distrito", "Cidade natal", 
        "Metrópole", "Cidade atual", "Comarca", "Município de residência", "Região"
    )

    resposta_pais = (
        "País", "Nação", "Estado soberano", "Pátria", "Pais", "Terra natal", 
        "País de origem", "País de residência", "Território", "Nacionalidade"
    )

    resposta_trabalho_escolaridade = (
        "Trabalho/Escolaridade", "Trabalho", "Escolaridade", "Profissão", "Estudos", "Emprego", 
        "Ocupação", "Cargo", "Formação", "Grau de instrução", "Nível escolar", 
        "Nível de estudo", "Trampo", "Função", "Atividade"
    )

    resposta_ip = (
        "Ip", "Ipzão", "Íp"
    )

    # Respostas definitivas:

    respostas_nao = (
        "Não", "Nao", "N", "Negativo", "Recuso", "Jamais", "Nunca", "Nem pensar", 
        "De jeito nenhum", "Nopes", "Nop", "Nada disso", "Falso", "Cancelar", 
        "Dispensar", "Tô fora", "Obrigado mas não"
    )

    respostas_sim = (
        "Sim", "Com certeza", "Positivo", "Afirmativo", "Claro", "Demorou", 
        "Pode ser", "Ok", "Opa", "Yep", "S", "Verdadeiro", "Aceito", 
        "Confirmar", "Confirmo", "Dale", "Bora"
    )

    respostas_cancelar = (
        "Cancelar", "Sair", "Fechar", "Abortar", "Parar", "Interromper", 
        "Desistir", "Voltar", "Anular", "Excluir", "Apagar", "Ignorar", 
        "Encerrar", "Drop", "Quit", "Resetar"
    )

except Exception as erro:
    print("\n\nErro ao montar resposats padrão para o funcionamento do sistema, você modificou o código?\n")
    print(f"\nDetalhes do erro: {erro}\n\n")
    exit()
