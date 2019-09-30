from bs4 import BeautifulSoup
import requests


source = requests.get('http://103.79.117.242/ru_profile/public/teacher/227/profiles').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

for content in soup.find_all('div',class_='col-xs-8 col-lg-10'):
    
        teachers = content.strong.text
	print(teachers)
        print("\n")

print("\n")
