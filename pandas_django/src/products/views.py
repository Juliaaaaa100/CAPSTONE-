from django.shortcuts import render
import pandas as pd
from .models import Product, Purchase
from .utils import fetch_graph

# Create your views here
# Define a view function to render a chart content
def render_chart_view(request):
    graph = None
    display_error_message = None
    dataframe_merged = None
    price = None
    # fetch all product objects from the database and convert them into a pandas DataFrame
    product_dataframe = pd.DataFrame(Product.objects.all().values())
    # fetch all the purchase objects from the database and convert them into a pandas DataFrame
    purchase_dataframe = pd.DataFrame(Purchase.objects.all().values())
    product_dataframe['product_id'] = product_dataframe['id']
 
    if purchase_dataframe.shape[0] > 0:
        dataframe_merged = pd.merge(purchase_dataframe, product_dataframe, on='product_id').drop(['date_y', 'id_y'], axis=1).rename({'date_x': 'date', 'id_x': 'id'}, axis=1)
        price = dataframe_merged['price']
        if request.method == 'POST':
            chart_type = request.POST.get('sales')
            date_from = request.POST.get('date_from')
            date_to = request.POST.get('date_to')

            print(chart_type)

            dataframe_merged['date'] = dataframe_merged['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            dataframe_merged2 = dataframe_merged.groupby('date', as_index=False)['total_price'].agg('sum')

            if chart_type != "":
                if date_from != "" and date_to != "":
                    dataframe_merged = dataframe_merged[(dataframe_merged['date'] > date_from) & (dataframe_merged['date'] < date_to)]
                    dataframe_merged2 = dataframe_merged.groupby('date', as_index=False)['total_price'].agg('sum')
                graph = fetch_graph(chart_type, x=dataframe_merged2['date'], y=dataframe_merged2['total_price'], data=dataframe_merged)
            else:
                display_error_message = "In order to continue, select a chart type"
        else:
            display_error_message = "Sorry, no records have been found in the database"

    # create a context dictionary containing the product data in html format
    context = {
        'graph': graph,
        'price': price,
        'error': display_error_message,
    }
    # Render products/main.html template with an empty context
    return render(request, 'products/main.html', context)
