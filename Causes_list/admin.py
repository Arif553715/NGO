from django.contrib import admin
from .models import Author3,Catagory,Artical
# Register your models here.

class AuthorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        model=Author3
admin.site.register(Author3,AuthorModel)


class ArticalModel(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__"]
    list_per_page = 10
    list_filter = ["posted_on","catagory"]

    class Meta:
        model=Artical

admin.site.register(Artical,ArticalModel)



class CatagoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10

    class Meta:
        model=Catagory

admin.site.register(Catagory, CatagoryModel)


