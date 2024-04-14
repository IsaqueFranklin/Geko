import requests
from bs4 import BeautifulSoup

headers = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}

pesquisa = input("Qual a sua pesquisa? ")

response = requests.get(
        "https://www.google.com/search",
        headers = headers,
        params = {
            "q": pesquisa,
            "tbm": "shop"
            }
        )

soup = BeautifulSoup(response.text, "lxml")

soup_ads = soup.find_all("a", {"class": "shntl sh-np__click-target"})
soup_results = soup.find_all("div", {"class": "sh-dgr__gr-auto sh-dgr__grid-result"})

print(f"Resultados: {len(soup_results)}\nResultados patrocinados: {len(soup_ads)}\n")

print("Primeiro resultado: ")
for soup_result in soup_results:
    if soup_result.find("h4") and soup_result.find("div", {"class" : "aULzUe IuHnof"}) and soup_result.find("span", {"class" : "a8Pemb OFFNJ"}):
        print({
            "Título": soup_results[0].find("h4").get_text(),
            "Loja" : soup_results[0].find("div", {"class" : "aULzUe IuHnof"}).get_text(),
	        "Preço" : soup_results[0].find("span", {"class" : "a8Pemb OFFNJ"}).get_text().split("\xa0")
        })

print("\nPrimeiro resultado patrocinado: ")
print({
    "Título" : soup_ads[0].find("div", {"class" : "sh-np__product-title translate-content"}).get_text(),
	"Loja" : soup_ads[0].find("span", {"class" : "E5ocAb"}).get_text(),
	"Preço" : soup_ads[0].find("b", {"class" : "translate-content"}).get_text().split("\xa0")
})

input("Pressione a tecla para sair")
