import selenium.webdriver.firefox.webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

CIDADES = ['pr/curitiba', 'ro/porto-velho']
SECOES = ['Educação', 'População', 'Trabalho e Rendimento', 'Território e Ambiente', 'Economia', 'Saúde']
PAGE = 'https://cidades.ibge.gov.br/brasil/'
browser = webdriver.Firefox()
# options = FirefoxOptions()
# options.add_argument("--headless")


if __name__ == '__main__':
    browser.get(PAGE + CIDADES[0])

# options = webdriver.ChromeOptions()
# #options.add_argument('headless') # Com essa opção o chrome não abre na interface gráfica
# browser = webdriver.Chrome(options=options)
# #browser = webdriver.Firefox()
#
# browser.get('https://cidades.ibge.gov.br/') # Get Page
#
# input_elem = browser.find_element_by_tag_name('input')  # Find the search box
#
# for cidade in cidades:
#     input_elem.send_keys(str(cidade) + Keys.RETURN) # Put city name and press return
#     sleep(1) # Wait
#     elem = browser.find_element_by_class_name('busca__codigo') # Quando insere o nome da cidade aparece esse elemento pra clicar
#     elem.click() # Click on the result
#     sleep(1) # Wait
#     print(browser.current_url)
#     sleep(1)
#
#     # Essa forma pega mais dados, mas as vezes dá uns erros
#     '''
#     for section in sections:
#         elem = browser.find_element_by_xpath("//th[contains(@class,'lista__titulo') and text()='" + section + "']")
#         print(elem.text)
#         elem.click() # Open section
#         sleep(1)
#         elements_indi_names = browser.find_elements_by_class_name('lista__nome')
#         elements_indi_values = browser.find_elements_by_class_name('lista__valor')
#         sleep(1)
#         for name,value in zip(elements_indi_names, elements_indi_values):
#             if (name.text != ''):
#                 try:
#                     print(name.text + ': ' + value.text)
#                 except:
#                     pass # Sem a opção do chrome headless, cai em um erro aqui
#     '''
#
#     # Essa forma parece funcionar bem, mas pega menos dados
#     elements_indi_names = browser.find_elements_by_class_name('indicador__nome')
#     elements_indi_values = browser.find_elements_by_class_name('indicador__valor')
#     sleep(1)
#     for name,value in zip(elements_indi_names, elements_indi_values):
#         print(name.text + ': ' + value.text)
