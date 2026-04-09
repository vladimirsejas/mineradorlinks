from bs4 import BeautifulSoup


class Parser:

    def extrair_arxiv(self, soup):
        artigos = []
        for item in soup.find_all("li", class_="arxiv-result"):
            a = item.find("p", class_="list-title")
            if a:
                link_tag = a.find("a")
                if link_tag:
                    link = link_tag["href"]
                    titulo = link_tag.get_text(strip=True)

                    artigos.append({
                        "titulo": titulo,
                        "resumo": "",
                        "link": link,
                        "fonte": "arXiv"
                    })
        return artigos


    def extrair_scielo(self, soup):
        artigos = []
        for item in soup.find_all("div", class_="item"):
            a = item.find("a")
            if a:
                link = a.get("href")
                titulo = a.get_text(strip=True)

                artigos.append({
                    "titulo": titulo,
                    "resumo": "",
                    "link": link,
                    "fonte": "SciELO"
                })
        return artigos


    def extrair_redalyc(self, soup):
        artigos = []
        for a in soup.find_all("a", href=True):
            link = a["href"]
            titulo = a.get_text(strip=True)

            if "/articulo.oa?id=" in link:
                if not link.startswith("http"):
                    link = "https://www.redalyc.org" + link

                artigos.append({
                    "titulo": titulo,
                    "resumo": "",
                    "link": link,
                    "fonte": "Redalyc"
                })
        return artigos


    def extrair_pubmed(self, soup):
        artigos = []
        for a in soup.find_all("a", class_="docsum-title"):
            link = a.get("href")
            titulo = a.get_text(strip=True)

            if link:
                link = "https://pubmed.ncbi.nlm.nih.gov" + link

                artigos.append({
                    "titulo": titulo,
                    "resumo": "",
                    "link": link,
                    "fonte": "PubMed"
                })
        return artigos


    def extrair_base(self, soup):
        artigos = []
        for a in soup.find_all("a", href=True):
            link = a["href"]
            titulo = a.get_text(strip=True)

            if link.startswith("http") and len(titulo) > 20:
                artigos.append({
                    "titulo": titulo,
                    "resumo": "",
                    "link": link,
                    "fonte": "BASE"
                })
        return artigos