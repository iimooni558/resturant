from django.db import models

# Create your models here.
class storetype(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class items(models.Model):
    nameitems=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/',null=True)
    price=models.FloatField()
    price_increase_per_unit=models.FloatField(default=0.0)
    st=models.ForeignKey(storetype,on_delete=models.CASCADE,null=True)
    def __str__(self):
        template='{0.nameitems} {0.description}{0.image}{0.price}'
        return template.format(self)



class itemsdetails(models.Model):
     qty=models.FloatField()
     tax=models.FloatField()
     items=models.ForeignKey(items,on_delete=models.CASCADE,null=True)

     def __str__(self):
        template='{0.qty}{0.tax}'
        return template.format(self)

class cart(models.Model):
    itemsid=models.IntegerField()
