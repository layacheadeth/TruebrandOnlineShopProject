from django.contrib import admin
from .models import product

# this class does demonstrate of how we deal with the illustration of the admin page.


class admin_display(admin.ModelAdmin):
    list_display = ('name','arrive_date','price','is_available',)
    #display what shall be shown on the table of our admin page
    list_display_links = ('name','arrive_date',)
    #the one that we click and lead us to detail of each data
    list_filter = ('name','price','arrive_date')
    #filter by categories such as name, price, arrive_date
    list_editable =('is_available',)
    #to enable the user to published and unpublished it by clicking save
    search_fields = ('name','price',)
    #to create a search field based on name and price only
    list_per_page = 12
    #to make a list of 10 per page, more than that deal with paginaion


admin.site.register(product,admin_display)


# Register your models here.
