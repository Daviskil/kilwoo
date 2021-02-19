from django.contrib import admin
from .models import Introduction, Subcategory, Team, Services

admin.site.register(Introduction)
admin.site.register(Team)
admin.site.register(Subcategory)
admin.site.register(Services)