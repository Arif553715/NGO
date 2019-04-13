from django.contrib import admin
from .models import Artical
# Register your models here.


class ArticalModel(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__"]
    list_per_page = 10

    class Meta:
        model=Artical

admin.site.register(Artical,ArticalModel)




