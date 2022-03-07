from bs4 import BeautifulSoup
import requests
import csv
  
# creating function
def scrape_views(url):
	soup = BeautifulSoup(requests.get(url).text, 'lxml')
	data = soup.select_one('meta[itemprop="interactionCount"][content]')['content']
	return data

views = []

for line in open("links.txt"):
	data = scrape_views(line)
	print(data)
	views.append(data)

print(views)

with open('views.tsv', 'a', newline="") as view_file:
    cw = csv.writer(view_file)
    cw.writerow(views)