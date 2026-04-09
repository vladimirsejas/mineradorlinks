from scraper import Scraper
from parser import Parser
from exportador import Exportador
from urllib.parse import quote_plus
import glob

BASE_URL_ARXIV = "https://arxiv.org/search/?query={query}&searchtype=all"
BASE_URL_SCIELO = "https://search.scielo.org/?q={query}&lang=pt"
BASE_URL_REDALYC = "https://www.redalyc.org/busquedaArticuloFiltros.oa?q={query}"
BASE_URL_BASE = "https://www.base-search.net/Search/Results?q={query}"


def exibir_menu():
    print("\n" + "=" * 60)
    print("   MINERADOR DE REVISTAS CIENTÍFICAS")
    print("=" * 60)
    print("  1 → Buscar artigos por termo ou expressão")
    print("  2 → Ver arquivos gerados")
    print("  0 → Sair")
    print("=" * 60)
    return input("Escolha uma opção: ").strip()


def opcao_busca_personalizada():
    termo = input("Digite termo ou expressão: ").strip()
    if not termo:
        print("Termo vazio.")
        return

    scraper = Scraper()
    parser = Parser()
    exportador = Exportador(prefixo=f"links_{termo[:15].replace(' ', '_')}")

    artigos = []

    # arXiv
    soup = scraper.buscar_pagina(BASE_URL_ARXIV.format(query=quote_plus(termo)))
    if soup:
        artigos.extend(parser.extrair_arxiv(soup))

    # SciELO
    soup = scraper.buscar_pagina(BASE_URL_SCIELO.format(query=quote_plus(termo)))
    if soup:
        artigos.extend(parser.extrair_scielo(soup))

    # Redalyc
    soup = scraper.buscar_pagina(BASE_URL_REDALYC.format(query=quote_plus(termo)))
    if soup:
        artigos.extend(parser.extrair_redalyc(soup))


    # BASE
    soup = scraper.buscar_pagina(BASE_URL_BASE.format(query=quote_plus(termo)))
    if soup:
        artigos.extend(parser.extrair_base(soup))

    def contem(texto):
        return texto and termo.lower() in texto.lower()

    links = []
    vistos = set()

    for a in artigos:
        link = a.get("link")
        if not link or link in vistos:
            continue

        if contem(a.get("titulo", "")) or contem(a.get("resumo", "")):
            vistos.add(link)
            links.append({"link": link})

    if links:
        exportador.exportar_csv(links)
        exportador.exportar_json(links)

        print("\nLinks encontrados:\n")
        for l in links:
            print(l["link"])
    else:
        print("Nenhum resultado encontrado.")


def opcao_ver_arquivos():
    arquivos = glob.glob("data/*")
    if not arquivos:
        print("Pasta data vazia.")
        return

    print("\nArquivos gerados:")
    for arq in arquivos:
        print(f" - {arq}")


def main():
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            opcao_busca_personalizada()
        elif opcao == "2":
            opcao_ver_arquivos()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()