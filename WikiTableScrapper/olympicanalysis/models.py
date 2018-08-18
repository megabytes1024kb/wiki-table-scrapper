from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MedalTable(models.Model):
	mid = models.AutoField(primary_key=True)
	country = models.CharField(max_length=100)
	gold = models.IntegerField()
	silver = models.IntegerField()
	bronze = models.IntegerField()
	total = models.IntegerField()
	year = models.CharField(max_length=5)
	olympic = models.CharField(max_length=50)
	rank = models.IntegerField(default=0)


	def save_details(self, country, gold, silver, bronze, year, olympic, rank):
		self.country = country
		self.gold = int(gold)
		self.silver = int(silver)
		self.bronze = int(bronze)
		self.year = year
		self.olympic = olympic
		self.rank = rank
		self.total = self.gold + self.silver + self.bronze
		self.save()



