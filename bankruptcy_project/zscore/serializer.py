from rest_framework import serializers
from zscore.models import Zscore


class Zscoreserializer(serializers.ModelSerializer):
	class Meta:
		model = Zscore
		fields = ('id',
			      'year',
			      'ebit',
			      'equity',
			      'retained_earnings',
			      'sales',
			      'total_assets',
			      'total_liability')