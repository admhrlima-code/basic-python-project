import pytest
from system import register_user

def test_user_valid():
  user = register_user("Fulano de Tal")
  assert user.name == "Fulado de Tal"
  assert user.status() == "Ativo"

def test_user_invalid():
  with pytest.raises(ValueError):
    register_user("")
