from django.contrib import admin
from app.models import Services, Sections
# Register your models here.


admin.site.register([
    Services,
    Sections,
])
