from django import forms
from django.contrib import admin
from .models import Article, Scope, Tag


class ScopeInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_count += 1

        if main_count == 0:
            raise forms.ValidationError('Должен быть указан один основной раздел.')

        super().clean()



class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
