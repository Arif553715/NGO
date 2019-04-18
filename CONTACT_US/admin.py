from django.contrib import admin
from .models import Artical,Contact_list
# Register your models here.




class ArticalModel(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__"]
    list_per_page = 10

    class Meta:
        model=Artical

admin.site.register(Artical,ArticalModel)


class Contact_listModel(admin.ModelAdmin):
    # list_display = ["__str__","posted_on"]
    search_fields = ["__str__"]
    list_per_page = 10
    list_display = [ 'name', 'mail', 'message','posted_on']

    class Meta:
        model=Contact_list

admin.site.register(Contact_list,Contact_listModel)

