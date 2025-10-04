from django.shortcuts import render

# Create your views here.
# In django, a view function is similar to a "route handler" in Express,
# where you define the logic that gets executed in response to a specific http request
# Creating a basic view function that will serve as the response for the homepage

# Import HttpResponse to send text-based responses
from django.http import HttpResponse


# The Homepage view function defined here:
def home(request):
    # Send a simple HTML response
    # We import HttpResponse as per above and then this function is used to construct an HTTP response to send back to the browser, similar to res.send() in Express.
    # This is responding to HTTP requests using Django’s HttpResponse() to send back HTML directly as strings, similar to how you might use res.send() in Express.
    # This is my view function responding to the HTTP request.
    # The HttpResponse object we used is the simplest way to return content in Django.
    # return HttpResponse('<h1>Welcome to the Dog Collector App!</h1>')
    return render(request, 'index.html')

# About page function defined here:
def about(request):
    # return HttpResponse('<h1>About the DogCollector</h1><h2>Who is excited about dogs and their toys?!</h2>')
    return render(request, 'about.html')


