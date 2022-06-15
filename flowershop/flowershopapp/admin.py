from django.contrib import admin
from .models import  Flower
from .models import Branches
from .models import Subbranches
# Register your models here.
admin.site.register(Flower)
admin.site.register(Branches)
admin.site.register(Subbranches)