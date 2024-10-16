import time

def test_home(browser):
    url = "http://10.10.113.22:8080/"
    browser.get(url)
    time.sleep(5)
    assert browser.title == "Dash"
    print("Teste da página inicial concluído com sucesso!")

