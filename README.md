# Minerador de Links

## Descrição

O Minerador de Links é um projeto desenvolvido em Python com o objetivo de coletar, processar e analisar dados textuais provenientes da web.
O sistema segue um fluxo simples de mineração de dados, passando pelas etapas de coleta, processamento, análise e exportação.A aplicação foi organizada de forma modular, com separação de responsabilidades entre os arquivos.

## Estrutura do Projeto
minerador-ia/

├── data/                diretório para dados gerados (ignorado pelo Git)
├── scraper.py          responsável pela coleta de dados
├── parser.py           responsável pelo processamento e limpeza
├── analisador.py       responsável pela análise dos dados
├── exportador.py       responsável pela exportação
├── main.py             arquivo principal
├── requirements.txt    dependências do projeto
├── .gitignore          arquivos ignorados
└── README.md           documentação

## Funcionamento
O sistema executa um fluxo sequencial.
Primeiro o scraper coleta os dados.
Depois o parser realiza a limpeza e organização do conteúdo.
Em seguida o analisador executa operações como contagem de palavras.
Por fim o exportador salva os resultados em arquivos.

## Módulos

Scraper: Responsável por buscar os dados.
Parser: Responsável pela limpeza e padronização.
Analisador: Responsável pela análise dos dados.
Exportador: Responsável por salvar os resultados.

## Execução
Clonar o repositório
git clone [https://github.com/vladimirsejas/mineradorlinks.git](https://github.com/vladimirsejas/mineradorlinks.git)
cd minerador-ia
Instalar dependências
pip install -r requirements.txt
Executar o sistema
python main.py

## Tecnologias
Python 3
requests
expressões regulares

## Melhorias futuras
Implementação de menu interativo
Persistência em banco de dados

## Objetivo
Aplicar conceitos de organização de código, separação de responsabilidades e mineração de dados.

## Autor
Vladimir (auxilio de IAs Claude, Chatgpt)

## Referências
Fontes utilizadas para coleta de dados
arXiv
[https://arxiv.org/search/?query={query}&searchtype=all](https://arxiv.org/search/?query={query}&searchtype=all)

SciELO
[https://search.scielo.org/?q={query}&lang=pt](https://search.scielo.org/?q={query}&lang=pt)

Redalyc
[https://www.redalyc.org/busquedaArticuloFiltros.oa?q={query}](https://www.redalyc.org/busquedaArticuloFiltros.oa?q={query})

BASE Search
[https://www.base-search.net/Search/Results?q={query}](https://www.base-search.net/Search/Results?q={query})

Documentação técnica

[https://docs.python.org/3/](https://docs.python.org/3/)
[https://requests.readthedocs.io/](https://requests.readthedocs.io/)
[https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)

## Licença

Uso acadêmico.
