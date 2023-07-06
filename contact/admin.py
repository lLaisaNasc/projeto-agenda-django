from django.contrib import admin
from contact import models
from contact.models import Contact

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',
    ordering = '-id', 

    # ---- opções de filtrar por data ----
    #list_filter = 'created_date',

    # ---- pesquisar ----
    search_fields = 'id', 'first_name', 'last_name',

    # ---- quantos por página ----
    list_per_page = 10

    list_max_show_all = 200

    # ---- deixa os campos editáveis ----
    list_editable = 'first_name', 'last_name', 'show'

    list_display_links = 'id', 'phone',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id', 