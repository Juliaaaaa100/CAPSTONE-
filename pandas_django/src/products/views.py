from django.shortcuts import render

# Create your views here
# Define a view function to render a chart content
def render_chart_view(request):
    # Render products/main.html template with an empty context
    return render(request, 'products/main.html', {})
