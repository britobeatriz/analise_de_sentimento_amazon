# Análise de Sentimento sobre comentários a respeito de um produto da Amazon

## Objetivo:
Analisar se as avaliaçoes estavam boas e os gaps dos comentários negativos. :bar_chart:

Produto: livro - Como fazer amigos e influenciar pessoas

# Para essa Análise:
Utilizei bibliotecas do Python

- pandas
- seaborn
- wordcloud
- matplotlib
- re
- numpy
- nltk
- beatifulsoup
- request

Fiz a extração dos dados por meio de Web scraping utilizando a biblioteca do Beautifulsoup(não foi preciso utilizar o selenium), em seguida salvei os dados em csv por meio do pandas, o tratamento dos dados usando a biblioteca nltk para remoção das stopwords... e por ultimo, para a visualização, utilizei o seaborn para plotar o gráfico e wordcloud para gerar as nuvens de palavras. 
