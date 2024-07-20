from django.contrib import admin
from .models import Project, Skill, Contact

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'url')
    search_fields = ('title', 'description', 'technology')
    list_filter = ('technology',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name', 'level')
    list_filter = ('level',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
    list_filter = ('email',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Contact, ContactAdmin)
