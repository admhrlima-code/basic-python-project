from user import User
from datetime import datetime

def register_user(name):
  if not name:
    raise ValueError("Nome inválido")

  user = User(name)

  with open("users.log", "a") as file:
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file.write(f"{data} - Usuário criado: {usuario.nome}\n")

return user
