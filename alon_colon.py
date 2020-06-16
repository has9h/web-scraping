import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get("http://genomics-pubs.princeton.edu/oncology/affydata/I2000.html?fbclid=IwAR0foyaQ4TifB_lhAukolaAn0DTipEOSdk_pWP3eHIgbe2CvyzZcLiZXpbU").content, features="html5lib")
fonts = soup.findAll("font")

with open("data.txt", "w+") as fw:
    for font in fonts:
        fw.writelines(font.text)
