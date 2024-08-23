from modeloUser import User

class Cliente:
  def __init__(self, nome, id, id_empre, email, senha, jogos, lucro, foto, biblioteca, operacoes, carrinho):
    User.__init__(self, id, nome, email, senha, foto)
    self.__id_empre = id_empre
    self.__jogos = jogos
    self.__lucro = lucro
    self.__biblioteca = biblioteca
    self.__operacoes = operacoes
    self.__carrinho = carrinho
  def getId_empre(self):
    return self.__id_empre
  def getJogos(self):
    return self.__jogos
  def setJogos(self, jogos):
    self.__jogos = jogos
  def getLucros(self):
    return self.__lucro
  def setLucros(self, lucro):
    self.__lucro = lucro
  def getBiblioteca(self):
    return self.__biblioteca
  def getOperacoes(self):
    return self.__operacoes
  def getCarrinho(self):
    return self.__carrinho