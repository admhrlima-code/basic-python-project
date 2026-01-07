class User:
  def __init__(self, name, ativo=True):
    self.name = name
    self.ativo = ativo

  def status(self):
    return "Ativo" if self.ativo else "Inativo"
