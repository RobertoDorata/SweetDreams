from bs4 import BeautifulSoup
import requests as requests

inseriti_nuovi_link = 1
lunghezza_lista_link = 0
link_inseriti = []
link_successivo = "https://hanakusogni.blogspot.com/"
while inseriti_nuovi_link == 1:
    lunghezza_lista_link = len(link_inseriti)

    r = requests.get(link_successivo)
    soup = BeautifulSoup(r.content, 'html.parser')

    for a_tag in soup.find_all('a', href=True):
        if 'href' in a_tag.attrs:
            a = a_tag.attrs['href']
            if ".html" in a and "#" not in a:
                link_inseriti.append(a)
            if "updated-max" in a:
                link_successivo = a
    link_inseriti = list(dict.fromkeys(link_inseriti))
    if lunghezza_lista_link == len(link_inseriti):
        inseriti_nuovi_link = 0

for link in link_inseriti:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    ids = [tag['id'] for tag in soup.select('div[id]')]
    for id in ids:
        if "post-body-" in id:
            testo_post = soup.find(id=id).get_text()
            print(testo_post)
            with open('sogni.txt', 'a') as output:
                output.write(testo_post)