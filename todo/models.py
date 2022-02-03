from django.db import models

# Create your models here.
#item is like the sheet in excel, class inheritance models.Model


class Item(models.Model): 
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

#Override the name from the generic class 
    def __str__(self):
        return self.name
        
