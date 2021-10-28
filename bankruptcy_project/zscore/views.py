from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from zscore.models import Zscore
from zscore.serializer import Zscoreserializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def post_request(request):
	if request.method == 'GET':
		finance = Zscore.objects.all()

		zscore_serializer = Zscoreserializer(finance, many=True)
		return JsonResponse(zscore_serializer.data, safe=False)

	elif request.method == 'POST':
		json_data = JSONParser().parse(request)
		zscore_serializer = Zscoreserializer(data=json_data)
		if zscore_serializer.is_valid():
			zscore_serializer.save()
			return JsonResponse(zscore_serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(zscore_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT'])
def put_request(request, pk):
	try:
		finance = Zscore.objects.get(pk=pk)
	except Zscore.DoesNotExist:
		return JsonResponse({'message': 'The value doesnot exist'}, status=status.HTTP_404_NOT_FOUND)


	if request.method == 'GET':
		zscore_serializer = Zscoreserializer(finance)
		return JsonResponse(zscore_serializer.data)

	elif request.method == 'PUT':
		json_data = JSONParser().parse(request)
		zscore_serializer = Zscoreserializer(finance, data=json_data)
		if zscore_serializer.is_valid():
			zscore_serializer.save()
			return JsonResponse(zscore_serializer.data)
		return JsonResponse(zscore_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
