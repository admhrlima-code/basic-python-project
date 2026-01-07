from user import User

def test_usur_active():
    u = User(True)
    assert u.status() == "Ativo"

def test_user_inactive():
    u = User(False)
    assert u.status() == "Inativo"
