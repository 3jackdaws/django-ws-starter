import mimetypes

from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect


from app.settings import STATIC_BASE, BASE_DIR
from django.contrib.auth import login, authenticate, logout


def index(request):
    return render(request, 'app/index.html')

def static(request, path):
    filepath = STATIC_BASE + path
    with open(filepath, 'rb') as fp:
        sometext = fp.read()
    return FileResponse(sometext, content_type=mimetypes.guess_type(filepath)[0])
