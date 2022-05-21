from django.shortcuts import  render
def index(requests):
    return render(requests,'home.html',{})
def explain(requests):
    return render(requests,'explain.html',{})

# Create your views here.
