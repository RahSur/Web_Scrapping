import requests
import bs4  #BeautifulSoup

print('Web Scrapping using BeautifulSoup in Python')
print('-----------------------------\n')

#provide any webpage link inside the brackets
res = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')

#res.text
#displays the complete structure of the webpage ink provided

#make use of beatifulSoup

soup = bs4.BeautifulSoup(res.text,'lxml')

soup.select('.mw-headline')

#mw-headline is taken from the title by inspecting the class name
#if id need to be taken, replace . by #
#displays as tags of all the headings available in the webpage

#To display only the headings/titles alone loop it

for i in soup.select('.mw-headline'):
          print(i.text)

#lists all the titles available
