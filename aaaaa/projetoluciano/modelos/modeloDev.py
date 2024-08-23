from modeloUser import User

class Dev:
  def __init__(self, nome, id, id_empre, email, senha, jogos, lucro, foto):
    User.__init__(self, id, nome, email, senha, foto)
    self.__id_empre = id_empre
    self.__jogos = jogos
    self.__lucro = lucro
  def getId_empre(self):
    return self.__id_empre
  def getJogos(self):
    return self.__jogos
  def setJogos(self, jogos):
    self.__jogos = jogos
  def getLucros(self):
    return self.__lucros
  def setLucros(self, lucros):
    self.__lucros = lucros