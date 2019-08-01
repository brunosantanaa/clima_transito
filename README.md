# Clima - Transito

Repositório contém um estudo para captação de dados usando Open Weather Map para dados climáticos e o Waze para dados referente ao trânsito.

# Configuração

Antes de começar a desenvolver prepare o ambiente do Anaconda:

Entre no terminal, navegue até a pasta onde está o gitclone e coloque os seguintes comandos:

- **conda env create** -f environment.yaml
- **source activate**  climatempo_env

## Chrome Driver

Para o wazeScrapping funcionar é necessario instalar o Driver do Chrome no seu ambiente conda. Faça o download no [link](https://sites.google.com/a/chromium.org/chromedriver/), descompacte-o na pasta anaconda(3)/envs/(climatempo_env)/bin.

## exemp_lib.ipynb

Notebook para testes e exemplo da biblioteca/métodos criados para o projeto.

Classes-Métodos até o momento:

**baltar_met**
  - data
     - wazeScraping
     - clima
