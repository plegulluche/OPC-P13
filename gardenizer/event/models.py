from django.db import models
from account.models import Account


    
class City(models.Model):
    
    name = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=12,decimal_places=6,default=0)
    longitude = models.DecimalField(max_digits=12,decimal_places=6,default=0)
    insee = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        
    def __str__(self):
        return self.name 
       
class Category(models.Model):
    
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.title

class Customer(models.Model):
    
    firstname = models.CharField(max_length=100, default="",null=True,blank=True)
    lastname = models.CharField(max_length=100, default="",null=True,blank=True)
    phone = models.CharField(max_length=25)
    company = models.CharField(max_length=150, default="",null=True,blank=True)
    street_number = models.CharField(max_length=5)
    streetname = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.PROTECT,default=1)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        
    def __str__(self):
        if self.company != "":
            return self.company  
        else:
            return self.lastname + " " + self.firstname


class Evenement(models.Model):
    
    title = models.CharField(max_length=150,unique=True)
    event_start = models.DateTimeField()
    event_end = models.DateTimeField(blank=True,null=True)
    all_day = models.BooleanField(default=False,null=True)
    description = models.TextField(default="",blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True)
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        
    def __str__(self):
        return self.title
 

    
