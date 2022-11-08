from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Document(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='Title', max_length=40)
    summary = models.TextField(verbose_name='Summary', blank=True, null=True)
    keyword = models.CharField(verbose_name='Keywords', max_length=40, blank=True, null=True)
    photo = models.ImageField(verbose_name='Photo', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='CreatedDate', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='UpdatedDate', auto_now=True)

    class Meta:
        verbose_name_plural = 'Document'
        
    def __str__(self):
        return self.title