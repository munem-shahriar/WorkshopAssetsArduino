from bs4 import BeautifulSoup
import requests


source = requests.get('http://www.ru.ac.bd/?page_id=843/').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

for content in soup.find_all('div',class_='box_feat_home'):
    
        teachers = content.text
	print(teachers)
        print("\n")

print("\n")
