#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home.html')
