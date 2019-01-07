from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def about(request):
	return HttpResponse("Welcome to WordCount!!!")

def count(request):
	fulltext = request.GET['fulltext']
	wordcount = fulltext.split()
	worddictionary = {}

	for word in wordcount:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1
	return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordcount), 'wordcount': worddictionary.items()})