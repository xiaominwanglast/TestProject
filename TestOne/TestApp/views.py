# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Book
def lasted_books(request):
    book_list=Book.objects.order_by('-pub_date')[:10]
    return render_to_response('lasted_books.html',{'book_list': book_list})
# Create your views here.
