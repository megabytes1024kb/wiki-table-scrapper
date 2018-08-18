import requests
from bs4 import BeautifulSoup
from olympicanalysis.models import MedalTable


# WIKI_URL = "https://en.wikipedia.org/wiki/2018_Winter_Olympics_medal_table"
# WIKI_URL = "https://en.wikipedia.org/wiki/2018_Winter_Paralympics_medal_table"

def wiki_table_scrapper(url, year, olympic):
	print(" ============== In Wiki table scrapper =====================")
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'lxml')
	table_classes = {"class": ["sortable", "plainrowheaders"]}
	wikitables = soup.find("table", table_classes)

	saved_rowspans = []
	rank = 1
	for row in wikitables.find_all("tr")[1:]:	# To Not consider header row of the table
		cells = row.find_all(["th", "td"])
		l = [cell.text for index, cell in enumerate(cells)]
		
		try:
			a = int(l[0])
			del l[0]
		except ValueError as err:
			pass
		if 'Total' not in l[0]:
			mt = MedalTable()
			mt.save_details(l[0], l[1], l[2], l[3], year, olympic, rank)
			print(" | ".join(l))
		rank +=1
		


