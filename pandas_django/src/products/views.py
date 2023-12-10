from django.shortcuts import render
import pandas as pd
from .models import Product, Purchase

# Create your views here
# Define a view function to render a chart content
def render_chart_view(request):
    # fetch all product objects from the database and convert them into a pandas DataFrame
    product_dataframe = pd.DataFrame(Product.objects.all().values())
    # fetch all the purchase objects from the database and convert them into a pandas DataFrame
    purchase_dataframe = pd.DataFrame(Purchase.objects.all().values())
    product_dataframe['product_id'] = product_dataframe['id']
    dataframe_merged = pd.merge(purchase_dataframe, product_dataframe, on='product_id').drop(['date_y', 'id_y'], axis=1).rename({'date_x':'purchase date','id_x':'id'}, axis=1)



    # create a context dictionary containing the product data in html format
    context = {
        'products' : product_dataframe.to_html(),
        'purchase':purchase_dataframe.to_html(),
        'dataframes_merged':dataframe_merged.to_html(), 

    }
    # Render products/main.html template with an empty context
    return render(request, 'products/main.html', context)
