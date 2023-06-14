from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requist):
    return HttpResponse("<script> alert('lala my God') </script>")