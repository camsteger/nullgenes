# script meant for single unmapped genes from MSIGDB curation project #

from bs4 import BeautifulSoup
import requests

initial = input('Enter gene symbol: ')

search = 'https://www.ncbi.nlm.nih.gov/gene/?term=' + initial
r = requests.get(search)
search_html = r.text
search_soup = BeautifulSoup(search_html, 'html.parser')


if 'No items found' in search_soup.find('title').contents[0]:
    ofcsym = 'null'
    geneid = 'null'
    notes = 'none'
elif initial not in search_soup.find('title').contents[0]:
    if 'Homo sapiens' not in search_soup.find('title').contents[0]:
        summary = search_soup.find(class_="section")
        if 'Orthologs' in summary.text:
            orth = summary.find(class_="ortholog-links")
            orth_link = orth.find('a').get('href')

            r = requests.get(orth_link)
            human_html = r.text
            human_soup = BeautifulSoup(human_html,'html.parser')

            ofcsym = human_soup.find(class_="section").find_all(class_="noline")[1].contents[0]
            geneid = human_soup.find(class_="geneid").contents[0].split(':')[1].split(',')[0].strip()
            notes = 'human ortholog'
            print(ofcsym)
            print(geneid)
            print(notes)

        elif 'Orthologs' not in summary.text:
            ofcsym = 'null'
            geneid = 'null'
            notes = 'no human ortholog'
            print(ofcsym)
            print(geneid)
            print(notes)
    else:
        summary = search_soup.find(class_="section")
        ofcsym = summary.find(class_="section").find_all(class_="noline")[1].contents[0]
        geneid = search_soup.find(class_="geneid").contents[0].split(':')[1].split(',')[0].strip()
        notes = 'fix'
        print(ofcsym)
        print(geneid)
        print(notes)
elif initial in search_soup.find('title').contents[0]:
    if (initial + ' - Gene - NCBI') in search_soup.find('title').contents[0]:
        gene_url = search_soup.find(class_="portlet_title").a
        url = 'https://www.ncbi.nlm.nih.gov' + gene_url.get('href')
        r = requests.get(url)
        url_html = r.text
        gene_soup = BeautifulSoup(url_html, 'html.parser')
        if 'Homo sapiens' not in gene_soup.find('title').contents[0]:
            summary = gene_soup.find(class_="section")
            if 'Orthologs' in summary.text:
                orth = summary.find(class_="ortholog-links")
                orth_link = orth.find('a').get('href')

                r = requests.get(orth_link)
                human_html = r.text
                human_soup = BeautifulSoup(human_html, 'html.parser')

                ofcsym = human_soup.find(class_="section").find_all(class_="noline")[1].contents[0]
                geneid = human_soup.find(class_="geneid").contents[0].split(':')[1].split(',')[0].strip()
                notes = 'human ortholog'
                print(ofcsym)
                print(geneid)
                print(notes)
            elif 'Orthologs' not in summary.text:
                ofcsym = 'null'
                geneid = 'null'
                notes = 'no human ortholog'
                print(ofcsym)
                print(geneid)
                print(notes)
    else:
        ofcsym = human_soup.find(class_="section").find_all(class_="noline")[1].contents[0]
        geneid = human_soup.find(class_="geneid").contents[0].split(':')[1].split(',')[0].strip()
        notes = 'human ortholog'
        print(ofcsym)
        print(geneid)
        print(notes)




