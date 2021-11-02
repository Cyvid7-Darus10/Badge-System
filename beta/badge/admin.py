from django.contrib import admin
from .models import Badge, Guilder, Claimable, Claimed, Announcements

admin.site.register(Badge)
admin.site.register(Guilder)
admin.site.register(Claimable)
admin.site.register(Claimed)
admin.site.register(Announcements)