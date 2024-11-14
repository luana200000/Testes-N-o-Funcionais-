from selenium import webdriver

def testar_navegador(navegador):
    if navegador == "chrome":
        driver = webdriver.Chrome()
    elif navegador == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Navegador não suportado")
    
    driver.get("http://seu_sistema.com")
    assert "Título do Site" in driver.title
    driver.quit()

testar_navegador("chrome")
testar_navegador("firefox")
