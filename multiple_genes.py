from pandas import read_csv,DataFrame
from bs4 import BeautifulSoup
import requests
import pandas as pd


location = r"C:/Users/stegecm/Documents/gene_script_practice.csv"

df = pd.read_csv(location,names=['initial gene symbol'])
official_symbol = []
official_name = []
entrez_ID = []
species = []
gene_type = []


for i in range(len(df)):
    initial = df['initial gene symbol'][i]

    search = 'https://www.ncbi.nlm.nih.gov/gene/?term=' + initial
    r = requests.get(search)
    search_html = r.text
    search_soup = BeautifulSoup(search_html, 'html.parser')

    if 'No items found' in search_soup.find('title').contents[0]:
        official_symbol.append('null')
        official_name.append('null')
        entrez_ID.append('null')
        species.append('null')
        gene_type.append('null')
        break
    elif initial not in search_soup.find('title').contents[0]:
        gene_url = search_soup.find(class_='geneid').contents[0].replace('\n                        ', ' ')
        gene_url = gene_url.split(':')[1]
        gene_url = gene_url.split(',')[0].strip()
        url = 'https://www.ncbi.nlm.nih.gov/gene/' + gene_url
        r = requests.get(url)
        url_html = r.text
        gene_soup = BeautifulSoup(url_html, 'html.parser')
        summary = gene_soup.find(class_="section")

        offsym = summary.find_all(class_="noline")[1].contents[0]
        official_symbol.append(offsym)

        offname = summary.find_all('dd')[1].contents[0]
        official_name.append(offname)

        entrez = gene_soup.find(class_="geneid").contents[0].replace('\n                        ', ' ')
        entrez = entrez.split(':')[1]
        entrez = entrez.split(',')[0].strip()
        entrez_ID.append(entrez)

        org = summary.find(class_='tax').text.strip()
        species.append(org)

        genetype = summary.find_all('dd')[4].contents[0]
        gene_type.append(genetype)
    elif (initial + ' - Gene - NCBI') in search_soup.find('title').contents[0]:
        gene_url = search_soup.find(class_="portlet_title").a
        url = 'https://www.ncbi.nlm.nih.gov' + gene_url.get('href')
        r = requests.get(url)
        url_html = r.text
        gene_soup = BeautifulSoup(url_html, 'html.parser')
        summary = gene_soup.find(class_="section")

        offsym = summary.find_all(class_="noline")[1].contents[0]
        official_symbol.append(offsym)

        offname = summary.find_all('dd')[1].contents[0]
        official_name.append(offname)

        entrez = gene_soup.find(class_="geneid").contents[0].replace('\n                        ', ' ')
        entrez = entrez.split(':')[1]
        entrez = entrez.split(',')[0].strip()
        entrez_ID.append(entrez)

        org = summary.find(class_='tax').text.strip()
        species.append(org)

        genetype = summary.find_all('dd')[4].contents[0]
        gene_type.append(genetype)
    elif initial in search_soup.find('title').contents[0]:
        gene_url = search_soup.find(class_='geneid').contents[0].replace('\n                        ', ' ')
        gene_url = gene_url.split(':')[1]
        gene_url = gene_url.split(',')[0].strip()
        url = 'https://www.ncbi.nlm.nih.gov/gene/' + gene_url
        r = requests.get(url)
        url_html = r.text
        gene_soup = BeautifulSoup(url_html, 'html.parser')
        summary = gene_soup.find(class_="section")

        offsym = summary.find_all(class_="noline")[1].contents[0]
        official_symbol.append(offsym)

        offname = summary.find_all('dd')[1].contents[0]
        official_name.append(offname)

        entrez = gene_soup.find(class_="geneid").contents[0].replace('\n                        ', ' ')
        entrez = entrez.split(':')[1]
        entrez = entrez.split(',')[0].strip()
        entrez_ID.append(entrez)

        org = summary.find(class_='tax').text.strip()
        species.append(org)

        genetype = summary.find_all('dd')[4].contents[0]
        gene_type.append(genetype)
    else:
        official_symbol.append('null')
        official_name.append('null')
        entrez_ID.append('null')
        species.append('null')
        gene_type.append('null')
        break

if len(official_symbol) == len(df):
    df['official symbol'] = official_symbol
if len(official_name) == len(df):
    df['official name'] = official_name
if len(entrez_ID) == len(df):
    df['entrez ID'] = entrez_ID
if len(species) == len(df):
    df['organism'] = species
if len(gene_type) == len(df):
    df['gene type'] = gene_type

df.to_csv('geneinfo.csv')
# print(df)