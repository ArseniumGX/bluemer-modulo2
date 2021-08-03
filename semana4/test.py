# algoritmo de test de criptografia

from cryptography.fernet import Fernet

class Acesso:
    def __init__(self, name, username, password, key) -> None:
        self.name = name
        self.username = username
        self.password = password
        self.key = key

    def __str__(self) -> str:
        return f'\n{self.name}\n{self.username}\n{self.password}\n{self.key}'


senha = b'Angellos@2012'
key = Fernet.generate_key()
f = Fernet(key)
password = f.encrypt(senha)

print(key)
print(f)
print(password)

user = Acesso(
    'José',
    'arseniumgx',
    password,
    key
)

print(user)
decript = f.decrypt(password)
print(decript)