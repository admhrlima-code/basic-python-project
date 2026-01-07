class User:
  def __init__(self, nome, ativo=True):
    self.nome = nome
    self.ativo = ativo

  def status(self):
    return "Ativo" if self.ativo else "Inativo"
