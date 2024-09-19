from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


options = Options()
driver = webdriver.Firefox(options=options)

driver.get('https://www.vagas.com.br/')  # Site a ser acessado
sleep(5)  # Aguardar o site Carregar


def login():
    login = "joaovitorpenha@hotmail.com"
    senha = "Jv@ncfom1994"

    botao_entrar = driver.find_element(
        By.XPATH, "//a[@id='main-navigation__signin']")
    botao_entrar.click()
    sleep(1)

    campo_login = driver.find_element(
        By.XPATH, '//input[@id="login_candidatos_form_usuario"]')
    campo_login.click()
    campo_login.send_keys(login)
    sleep(1)

    campo_senha = driver.find_element(
        By.XPATH, '//input[@id="login_candidatos_form_senha"]')
    campo_senha.click()
    campo_senha.send_keys(senha + Keys.RETURN)
    sleep(1)


def menu_lateral():
    menu_lateral = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "menuLateralButton"))
    )
    menu_lateral.click()
    sleep(1)


def fichas_pendentes():
    botao_fichas_pendentes = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//li[@data-testid="VG_ASIDE_MENU_ITEM_FICHAS-PENDENTES"]'))
    )
    botao_fichas_pendentes.click()
    sleep(1)


def remover():
    botao_remover = driver.find_element(By.XPATH, '//font[@id="PrTl"]')
    botao_remover.click()
    sleep(1)


def confirmar_remocao():
    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert.accept()  # ou alert.accept() dependendo do que você precisa
        sleep(1)
    except selenium.common.exceptions.TimeoutException:
        pass  # Nenhum alerta apareceu


def app():
    login()
    menu_lateral()

    while True:
        try:
            fichas_pendentes()
            remover()
            confirmar_remocao()  # Adicione esta linha
            sleep(1)
        except TimeoutException:
            driver.quit()
            break


if __name__ == "__main__":
    app()
