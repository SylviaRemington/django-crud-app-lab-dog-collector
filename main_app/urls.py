from django.urls import path
from . import views # Importing views to connect routes to view functions

# The urlpatterns list is where you specify each route, 
# similar to how routes are defined and grouped in controllers in Express.
# Best practice for each app to manage its own routes & then include those in the project's urlconfig
urlpatterns = [
    # Routes will be added here
    # Here is where we define the main_app's homepage URL & view
    # This code defines a root path using an empty string and maps it to the view.home view function that does not exist yet. We’ll remedy this with a new view in the next step.

    # HOMEPAGE DEFINED HERE:
    path('', views.home, name='home'),
    # The above code defines a root path using an empty string and maps it to the view.home view function that does not exist yet. We’ll remedy this with a new view in the next step.

    # ABOUT PAGE
    path('about/', views.about, name='about'),

    # DOGS INDEX PAGE - route
    path('dogs/', views.dog_index, name='dog-index'),

]


