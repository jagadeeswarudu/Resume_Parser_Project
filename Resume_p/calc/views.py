
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import time
from .forms import UploadForm,UploadText
from .models import save_resume_data_to_db,process_text_data
import json
import os
import requests
import logging


from .models import Contact
from docx import Document
from docx2txt import process
from django.contrib import messages 



def home(request):
    return render(request, 'index1.html')
def upload(request):
   

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
       
        if form.is_valid():
            messages.success(request, 'File uploaded successfully!')
            form.save()
            file_name = str(request.FILES['file'])
            sanitized_file_name = file_name.replace(' ', '_')
            path = os.path.join('D:\\Resume Parser Project\\Resume_p\\media', sanitized_file_name)
           
            headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzVmZmZhN2UtNzA3Ni00MzdhLWI2NzktMTc3NjkyZTYwNWNlIiwidHlwZSI6ImFwaV90b2tlbiJ9.ngU-dpJqoh1uDEgjjnrE_5EAMeIkbwhpZghJRSDPVkI"}

            url = "https://api.edenai.run/v2/ocr/resume_parser"
            data = {
                "providers": "affinda",
                "fallback_providers": ""
            }


# Sanitize the file name (replace spaces with underscores, for example)

# Create the full path using os.path.join
            if temp==1:
                files = {'file': open(doc_path,'rb')}
            else:
                files = {'file': open(path,'rb')}

            response = requests.post(url, data=data, files=files, headers=headers)

            result = json.loads(response.text)

            # Example
            affinda_data = result.get('affinda', {}).get('extracted_data', {})
            save_resume_data_to_db(affinda_data)


            time.sleep(1)
            
            return render(request, 'index1.html')# You can redirect to a success page
        else:
            logging.error(form.errors)
            time.sleep(1)
            return render(request, 'index1.html') 
            # If the form is not valid, you can handle errors or simply render the form again with errors
            #return render(request, 'upload.html')
    else:
        form = UploadForm()
    return render(request, 'index1.html')
def upload_text(request):
    
    if request.method == 'POST':
        form = UploadText(request.POST)
        if form.is_valid():
            contact = form.save()
            # Process text data and save to the database
            
            process_text_data(contact.text)
            return render(request, 'index1.html')
 # Redirect to a success page
    else:
        form = UploadText()
    return render(request, 'index1.html')
def about(request):
    return render(request, 'about_us.html')
def contact(request):
    return render(request, 'contact.html')

       
