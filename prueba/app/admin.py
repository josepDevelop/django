from django.contrib import admin
from app.models import Question, Choice


admin.site.site_header = "Admin de mi blog"


admin.site.register(Question)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question')
