from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Creating the models below
# Define a Product model representing items in the store

class Product(models.Model):
    #name of the product
    name = models.CharField(max_length=220)
    # date when the product was added 
    date = models.DateTimeField(auto_now_add=True)

    # returning the name of the product as a string representation

    def __str__(self):
        return str(self.name)
    
class Purchase(models.Model):
    # the product being purchased
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
     #  price per product
    price = models.PositiveBigIntegerField()
     # qunatity of the product being purchased
    quantity = models.PositiveIntegerField()
     # total prrice per purchased
    total_price = models.PositiveIntegerField(blank= True)
     # which user made the sale
    salesman =models.ForeignKey(User, on_delete=models.CASCADE)
     # date of the purchase
    date = models.DateTimeField(default=timezone.now)  


    # Override the save method to calculate and save the total 
    # price before saving the Purchase object
    def save(self, *args, **kwargs):
        # calculate the total price 
        self.total_price = self.price * self.quantity
        # calling the original save method to save the Purchase object 
        super().save(*args, **kwargs)

    def __str__(self):
        #returning the string representation of the purchase details  
        return "purchased {} - {} items for £ {}".format(self.product.name, self.quantity, self.total_price)