# ==========================================
# scraper.py - Funções de scraping com Selenium
# ==========================================
# Funções:
#   get_top_250_series() -> retorna lista com dados básicos de cada série
#   get_series_details(link) -> retorna popularidade + elenco principal
# ==========================================

def get_top_250_series():
    """
    - Acessa https://www.imdb.com/chart/toptv/
    - Extrai informações de cada uma das 250 séries:
        * título
        * ano de estreia e encerramento (se existir)
        * número total de episódios
        * classificação indicativa
        * nota do IMDB
        * link da página da série
    - Retorna uma lista de dicionários
    """
    pass  # implementar aqui


def get_series_details(link):
    """
    - Recebe o link da página da série
    - Extrai:
        * popularidade
        * elenco principal (nome ator/atriz, personagem, nº de episódios)
    - Retorna dicionário com esses dados
    """
    pass  # implementar aqui
