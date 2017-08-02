import requests
from bs4 import BeautifulSoup

initial = input('enter gene symbol: ')

search = 'https://www.ncbi.nlm.nih.gov/gene/?term=' + initial
r = requests.get(search)
search_html = r.text
search_soup = BeautifulSoup(search_html, 'html.parser')

if 'No items found' in search_soup.find('title').contents[0]:
    print('No matches found in gene search. See ' + search + 'for more information.')
elif initial not in search_soup.find('title').contents[0]:
    gene_url = search_soup.find(class_='geneid').contents[0].replace('\n                        ', ' ')
    gene_url = gene_url.split(':')[1]
    gene_url = gene_url.split(',')[0].strip()
    url = 'https://www.ncbi.nlm.nih.gov/gene/' + gene_url
    r = requests.get(url)
    url_html = r.text
    gene_soup = BeautifulSoup(url_html, 'html.parser')

    print(url + "\n")

    summary = gene_soup.find(class_="section")

    offsym = summary.find_all(class_="noline")[0].contents[0].replace('\n                         ',
                                                                      ' ').strip() + ": " + \
             summary.find_all(class_="noline")[1].contents[0]
    offname = summary.find_all('dt')[1].contents[0].replace('\n                         ', ' ').strip() + ": " + \
              summary.find_all('dd')[1].contents[0]
    entrez = gene_soup.find(class_="geneid").contents[0].replace('\n                        ', ' ')
    species = 'Organism: ' + summary.find(class_='tax').text.strip()
    genetype = 'Gene type: ' + summary.find_all('dd')[4].contents[0]

    print(offsym)
    print(offname)
    print(entrez)
    print(species)
    print(genetype)
elif (initial + ' - Gene - NCBI') in search_soup.find('title').contents[0]:
    gene_url = search_soup.find(class_="portlet_title").a
    url = 'https://www.ncbi.nlm.nih.gov' + gene_url.get('href')
    r = requests.get(url)
    url_html = r.text
    gene_soup = BeautifulSoup(url_html, 'html.parser')

    print(url + "\n")

    summary = gene_soup.find(class_="section")

    offsym = summary.find_all(class_="noline")[0].contents[0].replace('\n                         ',
                                                                      ' ').strip() + ": " + \
             summary.find_all(class_="noline")[1].contents[0]
    offname = summary.find_all('dt')[1].contents[0].replace('\n                         ', ' ').strip() + ": " + \
              summary.find_all('dd')[1].contents[0]
    entrez = gene_soup.find(class_="geneid").contents[0].replace('\n                        ', ' ')
    species = 'Organism: ' + summary.find(class_='tax').text.strip()
    genetype = 'Gene type: ' + summary.find_all('dd')[4].contents[0]

    print(offsym)
    print(offname)
    print(entrez)
    print(species)
    print(genetype)
elif initial in search_soup.find('title').contents[0]:
    gene_url = search_soup.find(class_='geneid').contents[0].replace('\n                        ', ' ')
    gene_url = gene_url.split(':')[1]
    gene_url = gene_url.split(',')[0].strip()
    url = 'https://www.ncbi.nlm.nih.gov/gene/' + gene_url
    r = requests.get(url)
    url_html = r.text
    gene_soup = BeautifulSoup(url_html, 'html.parser')

    print(url + "\n")

    summary = gene_soup.find(class_="section")

    offsym = summary.find_all(class_="noline")[0].contents[0].replace('\n                         ',
                                                                      ' ').strip() + ": " + \
             summary.find_all(class_="noline")[1].contents[0]
    offname = summary.find_all('dt')[1].contents[0].replace('\n                         ', ' ').strip() + ": " + \
              summary.find_all('dd')[1].contents[0]
    entrez = gene_soup.find(class_="geneid").contents[0].replace('\n                        ', ' ')
    species = 'Organism: ' + summary.find(class_='tax').text.strip()
    genetype = 'Gene type: ' + summary.find_all('dd')[4].contents[0]

    print(offsym)
    print(offname)
    print(entrez)
    print(species)
    print(genetype)
