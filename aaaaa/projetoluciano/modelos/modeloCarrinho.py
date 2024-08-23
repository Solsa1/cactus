class Carrinho:
  def __init__(self, id, id_user, id_jogo, preco):
    self.__id = id
    self.__id_user = id_user
    self.__id_jogo = id_jogo
    self.__preco = preco
  def getId(self):
    return self.__id
  def getId_jogo(self):
    return self.__id_jogo
  def getId_user(self):
    return self.__id_user
  def getPreco(self):
    return self.__preco
  def setPreco(self, preco):
    self.__preco = preco