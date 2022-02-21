from django.db import models
from account.models import Account


    
class City(models.Model):
    
    name = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    
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
    
class Evenement(models.Model):
    
    title = models.CharField(max_length=150)
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    all_day = models.BooleanField(default=False)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        
    def __str__(self):
        return self.title
 
class Customer(models.Model):
    
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=25)
    company = models.CharField(max_length=150, default="")
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "clients"
        
    def __str__(self):
        return self.lastname + " " + self.company
    
class Adress(models.Model):
    
    number = models.CharField(max_length=5)
    streetname = models.CharField(max_length=200)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Adress"
        verbose_name_plural = "Adresses"
        
    def __str__(self):
        return self.number + " " + self.streetname