from django.db import models


class Server(models.Model):

    name = models.CharField('name', max_length=255)
    ip_address = models.GenericIPAddressField('IP', max_length=16, default='0.0.0.0')
    description = models.TextField('description', max_length=255, default='no_description')
    server_is_active = models.BooleanField(default=False)
    

    class Meta:
        managed = True
        verbose_name = 'Server'
