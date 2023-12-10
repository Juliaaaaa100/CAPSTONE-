from django.shortcuts import render
import pandas as pd
from .models import Product

# Create your views here
# Define a view function to render a chart content
def render_chart_view(request):
    # take the data from the database and put it in a dataframe and pass it as a context
    queriy1 = Product.objects.all().values()
    print(queriy1)
    # Render products/main.html template with an empty context
    return render(request, 'products/main.html', {})
