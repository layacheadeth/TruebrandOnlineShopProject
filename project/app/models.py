from django.db import models
from django.contrib.auth.models import User


#create the database of product to store data and fetch it for later use
# to make the site dynamic depending on the backend
# choice can be embedded  into the charfield using choice property which accepts only turple(if one element must end with ',')
#when ever there is an error in migration, go to the migration folder and delete the error, then makemigrations and migrate again, it will work.
class product(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    type_demand = (
        ('long-sleeve', 'អាវដៃវែង'),
        ('short-sleeve', 'អាវដៃខ្លី'),
        ('trouser', 'ខោជេីងវែង'),
        ('short', 'ខោជេីងខ្លី'),
        ('bag', 'កាបូប'),
        ('shoe', 'ស្បែកជេីង'),
        ('pajamas', 'រ៉ូប'),
        ('suit', 'ឈុត'),
        ('t-shirt', 'អាវយឹត'),
        ('man', 'បុរស​'),
        ('woman', 'ស្រ្តី'),
        ('child', 'កុមារ'),
        ('sport', 'ឈុតស្ព័រ'),
    )
    Image=models.ImageField(upload_to='product/%Y/%m/%d/')
    name=models.CharField(max_length=20, unique=True)
    # slug=models.SlugField(max_length=20,unique=True,null = True, blank = True)
    type=models.CharField(max_length=20, choices=type_demand,default='Shirt')
    arrive_date=models.DateTimeField()
    price=models.CharField(max_length=10)
    description = models.TextField(default="detail of product")
    size = models.CharField(max_length=20, choices=SHIRT_SIZES,default='M')
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.name














# Create your models here.
