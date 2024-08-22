from view import inserir_dados_user, verifica, deletar_dados_user, atualizar_dados_user

def inserir_usuario():
  nome = input('DIGITE O SEU NOME: ')
  email = input('DIGITE SEU EMAIL: ')
  senha = input('DIGITE SUA SENHA: ')
  foto = input('COLOQUE SUA FOTO DE PERFIL: ')
  inserir_user = [nome, email, senha, foto]
  
  return  inserir_dados_user(inserir_user)
    

def deletar_usuario():
  consulta = input('DIGITE A SUA SENHA: ')
  resultado = verifica(consulta)
  if resultado:
    deletar_dados_user(consulta)
    print('DADOS DELETADOS COM SUCESSO!')
  else:
    print('ERRO NA REMOÇÃO DOS DADOS')

def atualizar_usuario():
  consulta = input('DIGITE A SUA SENHA: ')
  resultado = verifica(consulta)
  if resultado:
    coluna_nova = input('DIGITE A COLUNA QUE VOCÊ QUER MUDAR(ex: nome, email, senha, foto): ')
    novo_valor = input(f'DIGITE O NOVO VALOR PARA {coluna_nova}: ')
    atualizar_dados_user(consulta, novo_valor, coluna_nova)
    print('OS DADOS FORAM ATUALIZADOS!')
  else:
    print('ERRO NA ATUALIZAÇÃO DOS DADOS')

atualizar_usuario()