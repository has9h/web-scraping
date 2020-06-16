from urllib.parse import urlparse
from urllib.request import urlretrieve
import csv

from bs4 import BeautifulSoup
from tqdm import tqdm
import requests

source = 'https://techgrabyte.com/springer-released-65-machine-learning-data-science-books-free/'
raw = requests.get(source).text

soup = BeautifulSoup(raw, 'html5lib')

csv_file = open('springer_links.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['link'])


# # # 
# tag = soup.find('a', class_='cq gv ie if ig ih')
# redirect = requests.get(f'{tag.text}').text
# parsed_url = urlparse(tag.text)

# spr_soup = BeautifulSoup(redirect, 'html5lib')

# dl_path = spr_soup.find('a', class_='c-button c-button--blue c-button__icon-right test-download-book-options test-bookpdf-link')['href']
# link = '{}://{}{}'.format(parsed_url.scheme, parsed_url.hostname, dl_path)

# # Using urllib:
# # urlretrieve(link, '1.pdf')

# # Using requests:
# response_obj = requests.get(link, stream=True)
# with open('test.pdf', 'wb') as f:
#     # The following is preferred, although you can simply write instead
#     for chunk in tqdm(response_obj.iter_content(chunk_size=1024)):
#         if chunk:
#             f.write(chunk)


# for tag in soup.find_all('a', class_='cq gv ie if ig ih'):
#     redirect = requests.get(f'{tag.text}').text
#     parsed_url = urlparse(tag.text)

#     spr_soup = BeautifulSoup(redirect, 'html5lib')

#     dl_path = spr_soup.find('a', class_='c-button c-button--blue c-button__icon-right test-download-book-options test-bookpdf-link')['href']
#     link = '{}://{}{}'.format(parsed_url.scheme, parsed_url.hostname, dl_path)

#     urlretrieve(link, '1.pdf')
    # csv_writer.writerow([tag.text])
    # print(tag.text)

csv_file.close()
