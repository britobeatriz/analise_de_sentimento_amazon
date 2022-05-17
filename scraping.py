from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import pandas as pd

dados = []

for i in range(45):
    url ='https://www.amazon.com.br/Como-fazer-amigos-influenciar-pessoas/product-reviews/8543108683/ref=cm_cr_arp_d_paging_btm_prev_44'+str(i+1)+'&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1633879188&ref=sr_pg_1'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    req = Request(url, headers = headers)
    response = urlopen(req)
    html = response.read().decode('utf-8')
    conteudo = BeautifulSoup(html,'html.parser')

    # TAG MAE #
    tag_mae = conteudo.findAll('div', class_='a-section review aok-relative')
    #  #  #  #

    for anuncios in tag_mae:
        lista = {}

        lista['avaliacao'] = anuncios.find('span', class_="a-icon-alt").getText()

        lista['texto'] = anuncios.find('span', class_="a-size-base review-text review-text-content").getText()
        dados.append(lista)

# SALVADO EM CSV #
dataset = pd.DataFrame(dados)
dataset.to_csv('./dados/scrap.csv',sep=';',index=False,encoding=('utf-8-sig'))
#  #  #  #