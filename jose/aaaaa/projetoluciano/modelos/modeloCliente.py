from modeloUser import User

class Cliente:
  def __init__(self, nome, id, email, senha, jogos, foto, biblioteca):
    User.__init__(self, id, nome, email, senha, foto)
    self.__jogos = jogos
    self.__biblioteca = biblioteca
  def getJogos(self):
    return self.__jogos
  def setJogos(self, jogos):
    self.__jogos = jogos
  def getBiblioteca(self):
    return self.__biblioteca