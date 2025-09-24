# ==========================================
# main.py - Script principal
# ==========================================
# 1. Abre o navegador com Selenium
# 2. Extrai as 250 séries mais bem avaliadas do IMDB
# 3. Para cada série, acessa a página individual e extrai dados adicionais
# 4. Limpa e transforma os dados (parser)
# 5. Salva em JSON (utils)
# ==========================================

from scraper import get_top_250_series, get_series_details
from parser import clean_series_data
from utils import save_to_json

def main():
    # Passo 1: pegar as 250 séries da lista principal
    series_list = get_top_250_series()

    # Passo 2: coletar detalhes de cada série individualmente
    for serie in series_list:
        details = get_series_details(serie["link"])
        serie.update(details)  # junta os dados básicos com os detalhes

    # Passo 3: limpar e padronizar os dados
    cleaned_data = clean_series_data(series_list)

    # Passo 4: salvar em JSON
    save_to_json(cleaned_data, "data/series.json")

if __name__ == "__main__":
    main()






# ==========================================
# PROJETO: Coleta de Dados com Selenium - IMDB
# ==========================================
# Trabalho em grupo (duplas, trios ou quartetos) - NÃO pode ser individual
# Data de entrega: 29/09/2024
# Forma de entrega:
#   - Apresentação do código em funcionamento para o professor (em aula, com horário marcado)
#   - Entrega no Moodle:
#       1. Scripts Python ou Jupyter Notebook com o código
#       2. Arquivo JSON com os dados extraídos
#       3. README.txt OU comentários no código explicando como executar o projeto
#       4. Incluir instruções sobre configuração do ambiente (instalação Selenium, driver, etc.)



# ==========================================
# TAREFA 1 - Web Scraping com Selenium
# ==========================================
# Site alvo: https://www.imdb.com/
#
# Passo 1:
#   - Fazer scraping da lista das 250 séries mais bem avaliadas do IMDB
#   - Para cada série coletar:
#       * Título
#       * Ano de estreia e de encerramento (se existir)
#       * Número total de episódios
#       * Classificação indicativa
#       * Nota do IMDB
#       * Link da página da série
#
# Passo 2:
#   - Acessar a página individual de cada uma das 250 séries
#   - Coletar:
#       * Popularidade
#       * Elenco principal (nome do ator/atriz, personagem, número de episódios)
#
# Passo 3:
#   - Salvar todas as informações em um arquivo JSON
#   - Tratar os dados:
#       * Remover números extras do título
#       * Converter valores para tipos corretos (int, float, string)
#
# ==========================================
# OBSERVAÇÕES IMPORTANTES
# ==========================================
# - Comentar o código para facilitar a explicação durante a apresentação
# - Garantir que o código rode em qualquer máquina do grupo:
#     * Versão do Python usada
#     * Dependências (selenium, webdriver_manager, etc.)
# - Testar a execução ANTES da apresentação
# - JSON final deve conter todos os dados estruturados de forma clara
