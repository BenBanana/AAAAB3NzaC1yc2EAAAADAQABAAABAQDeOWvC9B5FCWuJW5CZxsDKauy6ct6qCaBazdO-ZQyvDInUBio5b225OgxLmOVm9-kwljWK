from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Entry


# Create your views here.
def entry_list(request):
    allentries = Entry.objects.all()
    return render(request, 'journal/contents.html', {'entries':allentries})
    #return HttpResponse(response)

def entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    #responsetext = ""
    #responsetext = "<p>Journal Entry: #" + str(entry.id) + "</p>"
    #responsetext += "<h1>" + entry.title + "</h1>"
    #responsetext += "<h2>" + entry.content + "</h2>"
    return render(request, 'journal/entry.html', {'entry':entry})
    #return HttpResponse(responsetext)
    
def entry_number(request):
    allentries = Entry.objects.all()
    entrynumber = 0
    for entry in allentries:
        if entry.month == 'February':
            entrynumber += 1
        else:
            return entrynumber
    return render(request, 'journal/contents.html', {'number':entrynumber})
    
    
    