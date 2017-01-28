from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
        id_usuario = models.TextField(primary_key=True)
        username = models.TextField(unique=True)
        password = models.TextField(models.SET_NULL,blank=True,null=True)
        email = models.EmailField(unique=True)   
        fechaCreado = models.DateTimeField(auto_now_add=True)
        estatus = models.CharField(null=True)
        seguidor = models.ManyToManyField('self', symmetrical=False)
        seguidos = models.ManyToManyField('self', symmetrical=False)
        
        
class Perfil(models.Model):
        id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
        nombre = models.TextField()
        apellido = models.TextField()
        fechaNac = models.DateField()
        telefono = models.TextField()
        titulo = models.TextField()
        ocupacion = models.TextField()
        avatar = models.ImageField()
        
class Post(models.Model):
        id_post = models.TextField(primary_key=True)
        id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
        fecha = models.DateTimeField(auto_now_add=True)
        estatus =  models.CharField(null=True) #preguntar
        
class Comentario(models.Model):
        id_comentario = models.TextField(primary_key=True)
        id_post = models.ForeignKey(Post, on_delete=models.CASCADE, editable=True,
                                    related_name='comments')
        id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
        fecha = models.DateTimeField(auto_now_add=True)
        contenido = models.TextField()
        
class Like(models.Model):
        id_like = models.TextField(primary_key=True)
        id_post = models.ForeignKey(Post, on_delete=models.CASCADE, editable=True,
                                    related_name='likes')
        id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
        fecha = models.DateTimeField(auto_now_add=True)
        
class Resource(models.Model):
        id_post = models.ForeignKey(Post, editable=True,
                                    related_name='resources')    
        contenido = models.TextField()  # Base64 Content
        tipo = models.TextField()
        fecha = models.DateTimeField(auto_now_add=True)
        id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
        
class Canal(models.Model):
        id_canal = models.TextField(primary_key=True)
        id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
        nombre = models.TextField()
        descripcion = models.TextField()
        estatus =  models.CharField(null=True)
        miembros = models.ManyToManyField(Usuario, through='MiembrosCanal', through_fields=('id_usuario', 'id_canal'))
        
class Interes(models.Model):
        id_interes = models.TextField(primary_key=True)
        nombre =  models.TextField()
        descripcion =  models.TextField()
        miembros = models.ManyToManyField(Perfil, through='MiembrosInteres', through_fields=('id_usuario', 'id_interes'))
        
class MiembrosInteres(models.Model):
        id_usuario = models.ForeignKey(Perfil)
        id_interes = models.ForeignKey(Interes)
        
class MiembrosCanal(models.Model):
        id_usuario = models.ForeignKey(Usuario)
        id_canal = models.ForeignKey(Canal)
    