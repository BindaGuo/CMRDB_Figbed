from django.contrib import admin
from .models import Figure
from .models import Tag
from .models import FigTag

admin.site.register(Figure)
admin.site.register(Tag)
admin.site.register(FigTag)

