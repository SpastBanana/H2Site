from django.shortcuts import render
from django.urls.conf import path
from H2Site import settings
import os
from filemanager import urls
from django.http import HttpResponse
import mimetypes


# Create your views here.
def fileView(request):
    path = settings.BASE_DIR / 'static/excel-data'
    dir_list = os.listdir(path)
    args = {'page': 'files.html', 'dirs': dir_list}
    return render(request, 'default.html', args)

def openfolderView(request, urlDir):
    path = settings.BASE_DIR / 'static/excel-data' / urlDir
    fileList=os.listdir(path)
    args = {'page': 'openfolder.html', 'files': fileList, 'dir': urlDir}
    return render(request, 'default.html', args)

def downloadile(request, urlDir, urlFile):
    # fill these variables with real values
    fl_path = settings.BASE_DIR / 'static/excel-data' / urlDir
    filename = urlFile

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def downloadFile(request, urlDir, urlFile):
    # Define text file name
    filename = urlFile
    # Define the full file path
    filepath = settings.BASE_DIR / 'static/excel-data' / urlDir
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response