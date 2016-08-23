from django.contrib import admin

from econv.models import Codec

class CodecAdmin(admin.ModelAdmin):
    fields = ['name', 'aliases', 'languages']
admin.site.register(Codec, CodecAdmin)
