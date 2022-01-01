from django.contrib import admin
from boat.models import Boat, Event,Booking
# Register your models here.
@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ('boat_name','boat_type')
    search_fields = ('boat_name', 'boat_type')
'''   
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    search_fields = ('username', 'email')
'''
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name','event_price')
    search_fields = ('event_name', 'event_price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_date','booking_time')
    search_fields = ('booking_date', 'booking_time')
    