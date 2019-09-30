import requests
import bs4;

session = requests.session()
getNums = session.get('http://www.educationboardresults.gov.bd/')
soup = bs4.BeautifulSoup(getNums.content, 'lxml')
table = soup.find('table', {'class':'black12bold'})
tr = table.find_all('tr')
tds = tr[6].find_all('td')
txt = tds[1].get_text()
bot = str(eval(txt))
print(txt + ' = ' + bot)

post = session.post('http://www.educationboardresults.gov.bd/result.php', data=dict(sr = '3', et='0', button2 = 'Submit', exam = 'hsc', year = '2014', board = 'dhaka', roll = '119416', reg = '948113', value_s = bot))
process = bs4.BeautifulSoup(post.content, 'lxml')
info = process.find_all('table', {'class':'black12'})[0]
result = process.find_all('table', {'class':'black12'})[1]
#print(post.content)
print('_________________Student\'s Information_________________')
for tr1 in info.find_all('tr'):
    tds1 = tr1.find_all('td')
    if len(tds1)==2:
        print(tds1[0].get_text() + '\t' + tds1[1].get_text())
    if len(tds1)==4:
        print(tds1[0].get_text() + '\t' + tds1[1].get_text() + '\t' + tds1[2].get_text() + '\t' + tds1[3].get_text())
print('\n_____________Result______________')
##---------
for tr in result.find_all('tr'):
    tds = tr.find_all('td')
    print(tds[0].get_text() + '\t' + tds[1].get_text() + '\t' + tds[2].get_text())