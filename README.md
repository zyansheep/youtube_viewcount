# Simple Youtube Viewcount scraper
Download a page from youtube with a bunch of videos (Tested with subscription feed page as of Mar 5 12022)

run `$ nix develop` for dev environment or just download python with the packages: beautifulsoup4, pandas and requests.

run `$ python scrape_links.py > links.txt` (may need to modify link)

run `$ watch -n <seconds between scraping links.txt> python scrape_views.py`