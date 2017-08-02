import requests
from bs4 import BeautifulSoup

initial = input('enter gene symbol: ')

search = 'https://www.ncbi.nlm.nih.gov/gene/?term=' + initial
r = requests.get(search)
search_html = r.text
search_soup = BeautifulSoup(search_html, 'html.parser')

if 'No items found' in search_soup.find('title').contents[0]:
    print('No matches found in gene search. See ' + search + 'for more information.')
else:
    gene_url = search_soup.find(class_="portlet_title").a
    url = 'https://www.ncbi.nlm.nih.gov' + gene_url.get('href')
    r = requests.get(url)
    url_html = r.text
    gene_soup = BeautifulSoup(url_html, 'html.parser')

    summary = gene_soup.find(class_="section")

    entrez = gene_soup.find(class_="geneid").contents[0].replace('\n                        ', ' ')
    entrez = entrez.split(':')[1]
    entrez = entrez.split(',')[0].strip()

    print(entrez)