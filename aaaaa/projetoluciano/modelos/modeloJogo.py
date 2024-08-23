class Jogos:
  def __init__(self, nome, id, id_empre, id_dev, preco, desc, foto, data_lancamento):
    self.__nome = nome
    self.__id = id 
    self.__id_empre = id_empre
    self.__id_dev = id_dev 
    self.__preco = preco
    self.__desc = desc
    self.__foto = foto
    self.__data_lancamento = data_lancamento
  
  def getNome(self):
    return self.__nome
  def setNome(self, nome):
    self.__nome = nome
  def getId(self):
    return self.__id
  def getId_empre(self):
    return self.__id_empre
  def getId_dev(self):
    return self.__id_dev
  def getPreco(self):
    return self.__preco
  def setPreoc(self, preco):
    self.__preco = preco
  def getDesc(self):
    return self.__desc
  def setDesc(self, desc):
    self.__desc = desc
  def getFoto(self):
    return self.__foto
  def setFotos(self, foto):
    self.__foto = foto
  def getData_lancamento(self):
    return self.__data_lancamento
  def setData_lancamento(self, data_lancamento):
    self.__data_lancamento = data_lancamento