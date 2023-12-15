from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "The Poll Mall"
admin.site.site_title = "Voting Admin Area"
admin.site.index_title = "Welcome to our Voting Admin Area"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]

# Register the models with the admin site
admin.site.register(Question, QuestionAdmin)
