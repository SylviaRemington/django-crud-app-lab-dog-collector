from django.shortcuts import render

# Create your views here.
# In django, a view function is similar to a "route handler" in Express,
# where you define the logic that gets executed in response to a specific http request
# Creating a basic view function that will serve as the response for the homepage

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    # We import HttpResponse as per above and then this function is used to construct an HTTP response to send back to the browser, similar to res.send() in Express.
    return HttpResponse('<h1>Welcome to the Dog Collector App!</h1>')
    # This above is my view function responding to the HTTP request.
    # The HttpResponse object we used is the simplest way to return content in Django.

