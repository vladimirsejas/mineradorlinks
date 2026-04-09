import requests
from bs4 import BeautifulSoup


class Scraper:
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive"
    }

    def buscar_pagina(self, url):
        try:
            resposta = requests.get(url, headers=self.HEADERS, timeout=10)
            resposta.raise_for_status()
            return BeautifulSoup(resposta.text, "html.parser")
        except requests.exceptions.HTTPError as e:
            print(f"[ERRO HTTP] {e}")
        except requests.exceptions.Timeout:
            print(f"[ERRO] Timeout em: {url}")
        except Exception as e:
            print(f"[ERRO] {e}")
        return None