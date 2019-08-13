from .forms import DocumentForm
from .models import Document
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
import json


def documents(request):
    document = Document.objects.all()
    return render(request, 'DropboxApp/documents.html', {
        'document': document
    })

# uploads file with optional title and saves reference in database
# to be accessed on documents page
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = DocumentForm()
    return render(request, 'DropboxApp/dropbox.html', {
        'form': form
    })


    