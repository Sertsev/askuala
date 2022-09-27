from http.client import HTTPResponse
from django.shortcuts import render



def index(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        html: render an html file
    """    
    return render(request, 'index.html')
