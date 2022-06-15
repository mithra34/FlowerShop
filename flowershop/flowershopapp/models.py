from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()

    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):

        return self.name


class Branches(models.Model):
    bname = models.CharField(max_length=250,unique=True)

    class Meta:
        ordering = ('bname',)
        verbose_name = 'bname'
        verbose_name_plural ='bnames'

    def __str__(self):


         return self.bname



class Subbranches(models.Model):
        subname = models.CharField(max_length=250)
        branch = models.ForeignKey(Branches, on_delete=models.CASCADE)

        def __str__(self):
            return self.subname