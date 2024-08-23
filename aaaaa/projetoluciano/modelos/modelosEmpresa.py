from modeloUser import User

class Empresa:
  def __init__(self, nome, id, lucros, email, senha, devs,jogos, foto, desc):
    User.__init__(self, id, nome, email, senha, foto)
    self.__lucros = lucros
    self.__devs = devs
    self.__jogos = jogos
    self.__desc = desc
  def getLucros(self):
    return self.__lucros
  def setLucros(self, lucros):
    self.__lucros = lucros
  def getDevs(self):
    return self.__devs
  def setDevs(self, devs):
    self.__devs = devs
  def getJogos(self):
    return self.__jogos
  def setJogos(self, jogos):
    self.__jogos = jogos
  def getDesc(self):
    return self.__desc
  def setDesc(self, desc):
    self.__desc = desc