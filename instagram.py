from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class Instagram:
    def __init__(self):
        self.driver_path = 'bin/chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def enter_instagram(self):
        self.chrome.get('https://www.instagram.com/accounts/login/')

    def exit_instagram(self):
        self.chrome.quit()

    # def retornar_url_perfil(self):
    #     return self.chrome.current_url

    def login(self, login, password):
        try:
            # Primeiro momento tela de login
            sleep(2)
            self.chrome.find_element(By.NAME, 'username').send_keys(login)
            self.chrome.find_element(By.NAME, 'password').send_keys(password)
            self.chrome.find_element(By.NAME, 'password').send_keys(Keys.ENTER)

            # Segundo momento "agora não"
            sleep(3.23)
            self.chrome.find_element(By.CLASS_NAME, 'aOOlW').click()
        except Exception as e:
            print(f'Error {e}')

    def search_profile(self, user):
        try:
            sleep(2.15)
            # Realizando busca por um usuario e clicando no usuário
            self.chrome.find_element(By.CLASS_NAME, 'XTCLo').send_keys(user)
            sleep(1.5)
            self.chrome.find_element(By.XPATH, '/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div').click()
        except Exception as e:
            print(f'Error {e}')

    def like_and_save_photos(self, qtd_fotos):
        try:
            # Abrindo a primeira imagem
            sleep(2.99)
            self.chrome.find_element(By.CLASS_NAME, 'v1Nh3').click()

            # Curtindo e salvado
            for i in range(qtd_fotos):
                sleep(1.5)
                self.chrome.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
                sleep(1)
                self.chrome.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div/div/button').click()
                # Passando página
                sleep(1)
                #self.chrome.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/button').click()
                self.chrome.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div/div/button').send_keys(Keys.ARROW_RIGHT)

            # Fechando fotos
            self.chrome.find_element(By.XPATH, '/html/body/div[6]/div[1]/button').click()

        except Exception as e:
            print(f'Error {e}')



