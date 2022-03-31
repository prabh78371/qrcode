from django.shortcuts import render
from .models import modelqrp

# Create your views here.
def home(request,id):
    name ="welcome"

    obj = modelqrp.objects.get(id=id)
    context = {'name':name,
    'obj':obj}
    return render(request,'home.html',context)