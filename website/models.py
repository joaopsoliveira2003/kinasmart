from django.db import models

class CategoriaModel(models.Model):
    tituloPT = models.TextField()
    tituloEN = models.TextField()
    ordem = models.PositiveIntegerField(unique=True)
    imagem = models.ImageField()
    imagem_topo = models.ImageField()
    visivel = models.BooleanField(default=True)

    def __str__(self):
        return self.tituloPT

    class Meta: 
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class SubcategoriaModel(models.Model):
    tituloPT = models.TextField()
    tituloEN = models.TextField()
    categoria = models.ForeignKey(to=CategoriaModel, on_delete=models.CASCADE)
    ordem = models.PositiveIntegerField()
    visivel = models.BooleanField(default=True)

    def __str__(self):
        return self.tituloPT

    class Meta: 
        verbose_name = "Subcategoria"
        verbose_name_plural = "Subcategorias"

class ImagemModel(models.Model):
    subcategoria = models.ForeignKey(to=SubcategoriaModel, on_delete=models.CASCADE)
    ordem = models.PositiveIntegerField()
    imagem = models.ImageField()
    visivel = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

class ContactoModel(models.Model):
    nome = models.TextField()
    email = models.EmailField()
    mensagem = models.TextField()

    class Meta: 
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"