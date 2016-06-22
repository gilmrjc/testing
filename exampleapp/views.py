from django.shortcuts import render
from .models import Example

# Create your views here.
def home_no_db(request):
    print('view no db')
    return render(request, 'index.html', {'object': 'a'})
    
def home_db(request):
    print('view db')
    print('pre object')
    example_object = Example.objects.all()
    print('objects: ', example_object)
    print('post_object')
    return render(request, 'index.html', {'object': example_object})
