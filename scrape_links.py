from bs4 import BeautifulSoup

# Download from website
with open("Subscriptions - YouTube.html") as fp:
	soup = BeautifulSoup(fp, "html.parser")
	for tag in soup.find_all("a", id="video-title", href=True):
		print(tag["href"])