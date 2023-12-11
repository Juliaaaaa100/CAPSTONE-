from django.shortcuts import render
import pandas as pd
from .models import Product, Purchase

# Create your views here
# Define a view function to render a chart content
def render_chart_view(request):
    display_error_message= None
    dataframe_merged= None
    # fetch all product objects from the database and convert them into a pandas DataFrame
    product_dataframe = pd.DataFrame(Product.objects.all().values())
    # fetch all the purchase objects from the database and convert them into a pandas DataFrame
    purchase_dataframe = pd.DataFrame(Purchase.objects.all().values())
    product_dataframe['product_id'] = product_dataframe['id']
 
    if purchase_dataframe.shape[0] > 0:
        dataframe_merged = pd.merge(purchase_dataframe, product_dataframe, on='product_id').drop(['date_y', 'id_y'], axis=1).rename({'date_x':'purchase date','id_x':'id'}, axis=1)
        print(dataframe_merged['purchase date'][0])
        print(type(dataframe_merged['purchase date'][0]))

        if request.method == 'POST':
            print(request.POST)
            chart_type = request.POST.get('sales')
            date_from = request.POST.get('date_from')
            date_to = request.POST.get('date_to')
    else:
        display_error_message = "Sorry, no records have been found in the database"


    # create a context dictionary containing the product data in html format
    context = {
        'error': display_error_message,

    }
    # Render products/main.html template with an empty context
    return render(request, 'products/main.html', context)
