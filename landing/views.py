from django.shortcuts import render


def landing(request):
  context = {'title': 'Saint Stephen School'}
  return render(request, 'landing/index.html', context)
