from django.contrib import admin
from django.contrib import admin
from .models import categories,technologies,colors,countries,Project,Profile,Rating


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('technologies','categories','colors')


# Register your models here.
admin.site.register(categories)
admin.site.register(technologies)
admin.site.register(colors)
admin.site.register(countries)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Profile)
admin.site.register(Rating)
