from urllib.parse import urlparse
from urllib.request import urlretrieve
import csv

from bs4 import BeautifulSoup
from tqdm import tqdm
import requests

source = 'https://techgrabyte.com/springer-released-65-machine-learning-data-science-books-free/'
raw = requests.get(source).text

soup = BeautifulSoup(raw, 'html5lib')

csv_file = open('springer-books-info.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Author', 'Link'])

error_list = []

for tag in tqdm(soup.find_all('a', class_='cq gv ie if ig ih')):
    redirect = requests.get(f'{tag.text}').text
    parsed_url = urlparse(tag.text)

    spr_soup = BeautifulSoup(redirect, 'html5lib')

    # Retrieving title and author names:
    content = spr_soup.find('div', class_='evaluation-section__text-col')
    name = content.find('div', class_='page-title').h1.text
    authorlist = [author.text.replace(u'\xa0', u' ') for author in \
                  content.find_all('span', class_='authors__name')]
    authorlist = ', '.join(authorlist)

    csv_writer.writerow([name, authorlist, tag.text])

    try:
        button = spr_soup.find('div', class_='cta-button-container__item')
        link = '{}://{}{}'.format(parsed_url.scheme, parsed_url.hostname, button.a['href'])

        urlretrieve(link, f'{name} - {authorlist}.pdf')
    except Exception as e:
        error_list = error_list.append((name, link))

    # Alternatively, using requests for larger streams
    # response_obj = requests.get(link, stream=True)
    # with open('test.pdf', 'wb') as f:
    #     # The following is preferred, although you can simply write instead
    #     for chunk in tqdm(response_obj.iter_content(chunk_size=1024)):
    #         if chunk:
    #             f.write(chunk)

print(error_list)
csv_file.close()
