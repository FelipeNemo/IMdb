# Projeto: Web Scraping com Selenium - IMDB

Alunos:
Felipe Augusto Batista Mendes dos Santos
Thiago Farias dos Santos
Gustavo Henrique da SilvaGustavo 
Guilherme Couto de Castro

## Descrição
Este projeto coleta informações das 250 séries mais bem avaliadas do IMDB, incluindo título, anos, episódios, classificação,
nota, popularidade e elenco completo (atores, personagens e episódios). Os dados são salvos em um arquivo JSON.


## Configuração do ambiente
1. Crie e ative o ambiente virtual usando Conda:
   conda create -n imdb_scraper python=3.10
   conda activate imdb_scraper

2. Instale as dependências:
   pip install -r requirements.txt

## Como executar
1. Abra o Jupyter Notebook:
   jupyter notebook

2. Abra e execute todas as células do notebook `coletor_de_series.ipynb`.

3. Ao final, os dados extraídos serão salvos em:
   `data/series_detalhes.json`

