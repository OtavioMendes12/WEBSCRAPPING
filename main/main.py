# PROCESSO SELETIVO BLUETAPE - Otávio Mendes




from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Links
urls = ["https://www.exemplo1.com/", "https://www.exemplo2.com/", "https://www.exemplo3.com/","https://www.exemplo4.com/","https://www.exemplo5.com/","https://www.exemplo6.com/","https://www.exemplo7.com/"]

# Palavras-chave
palavras_chave = ["exemplo1", "exemplo2", "exemplo3","exemplo4","exemplo5","exemplo6","exemplo7","exemplo8","exemplo","exemplo","exemplo","exemplo"]

# objeto de serviço do ChromeDriver
obj_servico = Service('caminho_para_o_chromedriver')
#objeto do ChromeDriver
driver = webdriver.Chrome(service=obj_servico)

# cria um dicionário para armazenar as palavras-chave encontradas em cada URL
palavras_chave_encontradas = {}

# percorre a lista de URLs e realiza a verificação de palavras-chave em cada página
for url in urls:
    #abrir a página no navegador
    driver.get(url)
    
    #código-fonte
    codigo_fonte = driver.page_source
    
    #objeto BeautifulSoup para analisar o código-fonte da página
    soup = BeautifulSoup(codigo_fonte, 'html.parser')
    
    # busca as palavras-chave no código-fonte
    palavras_chave_encontradas[url] = []
    for palavra_chave in palavras_chave:
        if palavra_chave in codigo_fonte:
            palavras_chave_encontradas[url].append(palavra_chave)
    
#fechar o navegador
driver.quit()

#dataframe para guardar as palavras-chave encontradas e os URLs
df = pd.DataFrame(columns=['Palavra-chave', 'URL'])

#palavras-chave encontradas no dataframe
for url, palavras in palavras_chave_encontradas.items():
    for palavra in palavras:
        df = df.append({'Palavra-chave': palavra, 'URL': url}, ignore_index=True)

#cria o arquivo Excel e salva o dataframe nele
df.to_excel('Relatorio.xlsx', index=False)
