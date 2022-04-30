import email
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from crud.models import Bio
from crud.forms import BioForm

def index(request):
    """Index Page, to list all data"""
    try:
        bio = Bio.objects.all()
    except Bio.DoesNotExist:
        raise Http404()
    form = BioForm()
    return render(request, "crud/index.html", {"bio": bio, "form": form})

def create_data(request):
    """Function to create data in HTML page"""
    if request.method == "POST":
        form = BioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfullt create one data to database.")
            return redirect("crud:index")
        else:
            messages.error(request, "Error while save data to database.")
            return redirect("crud:index")

def update_data(request):
    """Function to update data in HTML page"""
    if request.method == "POST":
        pk = request.POST["pk"]
        try:
            q = Bio.objects.get(pk=pk)
        except Bio.DoesNotExist:
            raise Http404()
        full_name = request.POST["full_name"]
        email = request.POST["email"]
        address = request.POST["address"]
        
        # Update the data and save it;
        q.full_name = full_name
        q.email = email
        q.address = address 
        q.save()
        messages.success(request, "Successfully updating data for id: %s, fullname: %s" % (id, full_name))
        return redirect("crud:index")

def delete_data(request, pk):
    """Function to delete data"""
    try:
        q = Bio.objects.get(pk=pk)
    except Bio.DoesNotExist:
        raise Http404
    name = q.full_name
    q.delete()
    messages.warning(request, "Successfully delete data for %s" % name)
    return redirect("crud:index")