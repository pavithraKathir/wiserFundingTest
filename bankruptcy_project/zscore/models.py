from django.db import models

class Zscore(models.Model):
	year = models.IntegerField(blank=False)
	ebit = models.DecimalField(max_digits=5,decimal_places=2)
	equity = models.DecimalField(max_digits=5, decimal_places=2)
	retained_earnings = models.DecimalField(max_digits=5, decimal_places=2)
	sales = models.DecimalField(max_digits=6,decimal_places=2)
	total_assets = models.DecimalField(max_digits=5, decimal_places=2)
	total_liability = models.DecimalField(max_digits=5, decimal_places=2)

