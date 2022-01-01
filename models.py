from django.db import models
from decimal import Decimal
from django.forms import widgets

# Create your models here.
#create user register modelform and add username email and password and phoneno to register
'''
class User(models.Model):
        username = models.CharField(max_length=100,primary_key=True)
        email = models.EmailField(max_length=100)
        password = models.CharField(max_length=100)
        def __str__(self):
            return self.username
'''
#create a boat model for booking 
class Boat(models.Model):
    boat_name = models.CharField(max_length=100,primary_key=True,)
    boat_type = models.CharField(max_length=100)
    boat_location = models.CharField(max_length=100)
    boat_capacity = models.IntegerField()
    boat_price = models.IntegerField()
    def __str__(self):
        return self.boat_name+" "+self.boat_type

#create a event model
class Event(models.Model):
    event_name = models.CharField(max_length=50,primary_key=True,unique=False)
    boat = models.ForeignKey(Boat,on_delete=models.CASCADE,null=True,default=None)
    event_location = models.CharField(max_length=30)
    event_capacity = models.DecimalField(max_digits=10000, decimal_places=0)
    event_price = models.DecimalField(max_digits=100000, decimal_places=0)
    def __str__(self):
        return self.event_name+"-"+self.boat.boat_name+"-size:"+str(self.event_capacity)+" in "+self.event_location+" price:"+str(self.event_price)

'''
create a booking model for booking where for every one user can book many boats and the model must have a foreign key to the user and a foreign key to the boat
'''
class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date = models.DateField( auto_now=False, auto_now_add=False)
    booking_time = models.TimeField(auto_now=False, auto_now_add=False)
    #booking_status = models.CharField(max_length=50,default="pending")
    #total_price = models.DecimalField(max_digits=200000, decimal_places=0,default=0)
    def __str__(self):
        return self.event.event_name+" "+str(self.booking_date)+" "+str(self.booking_time)

'''
class Booking(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneno = models.ForeignKey(User, on_delete=models.CASCADE)
    boat_name = models.ForeignKey(Boat, on_delete=models.CASCADE)
    boat_type = models.ForeignKey(Boat, on_delete=models.CASCADE)
    boat_price = models.ForeignKey(Boat, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    event = models.CharField(max_length=100)
    def __str__(self):
        return self.user_name

'''