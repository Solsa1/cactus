class Biblioteca:
  def __init__(self, id, id_jogo, id_user):
    self.__id = id
    self.__id_jogo = id_jogo
    self.__id_user = id_user
  def getId(self):
    return self.__id
  def getId_jogo(self):
    return self.__id_jogo
  def getId_user(self):
    return self.__id_user