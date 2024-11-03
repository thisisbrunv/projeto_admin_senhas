import sys
import os
sys.path.append(os.path.abspath(os.curdir))

from model.password import Password
from views.password_views import FernetHasher


action = input('Digite 1 para salvar uma nova senha ou 2 para ver uma senha salva')

if action == '1':
    if len(Password.get()) == 0:
        key, path = FernetHasher.create_key(archive=True)
        print('sua chave foi criada com sucesso')
        print(f'Chave: {key.decode("utf-8")}')
        if path:
            print('Chave salva no arquivo, lembre-se de remover o arquivo após o transferir de local')
            print(f'Caminho: {path}')
    else:
        key = input('Digite sua chave usada para criptografia, use sempre a mesma chave: ')

    domain = input('dominio: ')
    password = input('senha: ')
    fernet_user = FernetHasher(key)
    p1 = Password(domain=domain, password=fernet_user.encrypt(password).decode('utf-8'))
    p1.save()