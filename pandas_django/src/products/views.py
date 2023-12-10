from django.shortcuts import render
import pandas as pd
from .models import Product, Purchase

# Create your views here
# Define a view function to render a chart content
def render_chart_view(request):
    # fetch all product objects from the database and convert them into a pandas DataFrame
    product_dataframe = pd.DataFrame(Product.objects.all().values())
    # fetch all the purchase objects from the database and convert them 
    # into a pandas DataFrame
    purchase_dataframe = pd.DataFrame(Purchase.objects.all().values())


    # create a context dictionary containing the product data in html format
    context = {
        'products' : product_dataframe.to_html(),
        'purchase':purchase_dataframe.to_html(),

    }
    # Render products/main.html template with an empty context
    return render(request, 'products/main.html', context)
