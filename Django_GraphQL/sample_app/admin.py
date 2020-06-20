from django.contrib import admin
from sample_app.models import Snippet
# Register your models here.


class AdminSnippet(admin.ModelAdmin):
    admin.site.register(Snippet)