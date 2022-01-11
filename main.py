from time import sleep
from instagram import Instagram

login = 'informe seu login'
password = 'sua senha'
user = 'usuario que deseja curtir'
qtd_fotos = 'quants fotos deseja curtir'

account = Instagram()
account.enter_instagram()

# Login in Intagram
account.login(login, password)

# Buscar usuário
account.search_profile(user)

# Curtir fotos
account.like_and_save_photos(qtd_fotos)

sleep(10)
account.exit_instagram()