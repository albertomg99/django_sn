from django.contrib import admin

from django.contrib.auth.models import Group, User
from .models import Profile, AMGPost


class ProfileInLine(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInLine]


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(AMGPost)
# admin.site.register(Profile)
