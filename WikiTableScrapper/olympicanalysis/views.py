from django.shortcuts import render
from django.shortcuts import redirect
from olympicanalysis.models import MedalTable
from django.db.models import Count
from django.http import HttpResponse
import json

# Create your views here.
def index_page(request):
	return render(request, 'home.html')

def scrape_page(request):
	context = { 'message': ''}
	return render(request, 'scrape-page.html', context)	

def visual_page(request):
	records = []
	olympic_list = MedalTable.objects.values("olympic").distinct()
	for olympic in olympic_list:
		records.append(olympic['olympic'])
	context = { 'records': records }
	return render(request, 'visualization.html', context)	


def scraper_call(request):
	try:
		url = request.GET.get('url')
		year = request.GET.get('year')
		url_s = url.split("/")
		olympic = url_s[-1]
		print("Olympic : ", olympic)
		from olympicanalysis import scrapper
		scrapper.wiki_table_scrapper(url, year, olympic)
		redirect_url = "show-data/"+ str(year) + "/" + olympic
		# return redirect(redirect_url)
		context = { 'message': "Scraping of the data from given link is completed" }
		return render(request, 'scrape-page.html', context)
	except Exception as err:
		print(err)
		context = { 'message': "Server Error, Please insert correct year and Link in the box and try again" }
		return render(request, 'scrape-page.html', context)


def show_data(request, olympic):
	try:
		records = MedalTable.objects.filter(olympic=olympic)
		context = { 'records': records, 'tag': olympic }
		return render(request, 'datatable-and-charts.html', context)
	except Exception as err:
		context = { 'records': [], 'tag': olympic }
		return render(request, 'datatable-and-charts.html', context)


def get_table_data(request, olympic):
	records = MedalTable.objects.filter(olympic=olympic)
	final_record = [[row.rank, row.country, row.gold, row.silver, row.bronze, row.total] for row in records]
	data = { 'data': final_record}
	return HttpResponse(json.dumps(data), content_type="application/json")


def get_chart_data(request, olympic):
	records = MedalTable.objects.filter(olympic=olympic).order_by('-gold')
	# final_record = [[row.rank, row.country, row.gold, row.silver, row.bronze, row.total] for row in records]
	# data = { 'data': final_record}
	country_labels = [row.country for row in records[:10]]
	gold_values = [row.gold for row in records[:10]]
	silver_values = [row.silver for row in records[:10]]
	bronze_values = [row.bronze for row in records[:10]]

	values = {'labels': country_labels, 'gold': gold_values, 'silver': silver_values, 'bronze': bronze_values }

	return HttpResponse(json.dumps(values), content_type="application/json")
