from django.contrib import admin
from website.models import CategoriaModel, SubcategoriaModel, ImagemModel, ContactoModel

class ListCategoria(admin.ModelAdmin):
    list_display = ('tituloPT', 'ordem', 'visivel')
    ordering = ['ordem']

class ListSubcategoria(admin.ModelAdmin):
    list_display = ('tituloPT', 'categoria', 'ordem', 'visivel')
    ordering = ['categoria', 'ordem']

class ListImagem(admin.ModelAdmin):
    list_display = ('subcategoria', 'ordem', 'visivel')
    ordering = ['subcategoria', 'ordem']

class ListContactos(admin.ModelAdmin):
    list_display = ('nome', 'email', 'id')
    ordering = ['-id']

admin.site.site_header = 'Administração Kinasmart'
admin.site.site_title = 'Kinasmart'
admin.site.index_title = 'Administração'

admin.site.register(CategoriaModel, ListCategoria)
admin.site.register(SubcategoriaModel, ListSubcategoria)
admin.site.register(ImagemModel, ListImagem)
admin.site.register(ContactoModel, ListContactos)
