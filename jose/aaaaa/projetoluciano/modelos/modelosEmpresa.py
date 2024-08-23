from modeloUser import User

class Empresa:
  def __init__(self, nome, id, email, senha, jogos, foto, desc):
    User.__init__(self, id, nome, email, senha, foto)
    self.__jogos = jogos
    self.__desc = desc
  def getJogos(self):
    return self.__jogos
  def setJogos(self, jogos):
    self.__jogos = jogos
  def getDesc(self):
    return self.__desc
  def setDesc(self, desc):
    self.__desc = desc