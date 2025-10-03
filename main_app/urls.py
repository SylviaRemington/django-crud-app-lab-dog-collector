from django.urls import path
from . import views # Importing views to connect routes to view functions

# The urlpatterns list is where you specify each route, 
# similar to how routes are defined and grouped in controllers in Express.
urlpatterns = [
    # Routes will be added here
    # Here is where we define the main_app's homepage URL & view
    # HOMEPAGE DEFINED HERE:
    path('', views.home, name='home'),
    # The above code defines a root path using an empty string and maps it to the view.home view function that does not exist yet. 
    # We’ll remedy this with a new view in the next step.
]
# Addtl notes:
# The name='home' kwarg is technically optional but will come in handy for referencing the URL in other parts of the app, 
# especially from within templates, so we will always use it.