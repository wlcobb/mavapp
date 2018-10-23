from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum


def home(request):
    return render(request, 'shopcart/index.html',
                  {'shopcart': home})

