from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Bangunan_bendung(models.Model):
    BANGUNANBENDUNG = 'Bangunan Bendung'
    Pilihan_Categori = ((BANGUNANBENDUNG, 'BANGUNAN BENDUNG'),)
    nama            = models.CharField(max_length=100)
    slug            = models.SlugField(blank=True, null=True)
    category        = models.CharField(max_length=100,blank=True, choices=Pilihan_Categori, default=BANGUNANBENDUNG)
    letak           = models.CharField(max_length=50)
    foto1           = models.ImageField(default='noPic.png', blank=True)
    foto2           = models.ImageField(default='noPic.png', blank=True)
    foto3           = models.ImageField(default='noPic.png', blank=True)
    latitude                   = models.FloatField(null=True)
    longitude                   = models.FloatField(null=True)

    def save(self):
        self.slug = slugify(self.nama)
        super(Bangunan_bendung, self).save()

    def __str__(self):
        return "{}.{}".format(self.id, self.nama)


class Bangunan_corong (models.Model):
    BANGUNANCORONG = 'Bangunan Corong'
    Pilihan_Categori = ((BANGUNANCORONG, 'BANGUNAN CORONG'),)
    nama 			= models.CharField(max_length=100)
    category 		= models.CharField(max_length=100,blank=True, choices=Pilihan_Categori, default=BANGUNANCORONG)
    slug 			= models.SlugField(blank=True, null=True)
    debit 			= models.CharField(max_length=20)
    luas_terairi 	= models.CharField(max_length=20)
    letak 			= models.CharField(max_length=50)
    foto1           = models.ImageField(default='noPic.png', blank=True)
    foto2           = models.ImageField(default='noPic.png', blank=True)
    foto3           = models.ImageField(default='noPic.png', blank=True)
    latitude                   = models.FloatField(null=True)
    longitude                   = models.FloatField(null=True)

    def save(self):
        self.slug = slugify(self.nama)
        super(Bangunan_corong, self).save()

    def __str__(self):
        return "{}.{}".format(self.id, self.nama)


class Bangunan_sadap (models.Model):
    BANGUNANSADAP = 'Bangunan Sadap'
    Pilihan_Categori 		= ((BANGUNANSADAP, 'BANGUNAN SADAP'),)
    nama	 				= models.CharField(max_length=100)
    category 				= models.CharField(max_length=100,blank=True, choices=Pilihan_Categori, default=BANGUNANSADAP)
    slug 					= models.SlugField(blank=True, null=True)
    debit 					= models.CharField(max_length=20)
    luas_terairi 			= models.CharField(max_length=20)
    letak 					= models.CharField(max_length=50)
    #letak = models.ForeignKey(Saluran, on_delete=models.CASCADE)
    foto1                   = models.ImageField(default='noPic.png', blank=True)
    foto2                   = models.ImageField(default='noPic.png', blank=True)
    foto3                   = models.ImageField(default='noPic.png', blank=True)
    latitude                   = models.FloatField(null=True)
    longitude                   = models.FloatField(null=True)
    #foto = models.CharField(max_length=500,null=True, blank=True)

    def save(self):
        self.slug = slugify(self.nama)
        super(Bangunan_sadap, self).save()

    def __str__(self):
        return "{}.{}".format(self.id, self.nama)

class LaporanKerusakan(models.Model):
    nama = models.CharField(max_length=100)
    noTelepon = models.CharField(max_length=20)
    alamat = models.TextField()
    lokasiKerusakan = models.CharField(max_length=50)
    deskripsiKerusakan = models.TextField()
    foto = models.ImageField(default='noPic.png')
    foto2 = models.ImageField(default='noPic.png', blank=True)

    def __str__(self):
        return self.nama
