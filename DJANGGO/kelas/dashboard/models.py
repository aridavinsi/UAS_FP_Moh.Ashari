from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return "{}.{}".format(self.nama,self.ket)
        
class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True, default='img/')
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)
   
    def __str__(self):
        return "{}. {}".format(self.kodebrg,self.nama, self.stok, self.harga, self.link_gbr)

class Member(models.Model):
    idmember=models.CharField(max_length=10)
    nama=models.CharField(max_length=25)
    alamat=models.CharField(max_length=30)

    def __str__(self):
        return "{}. {}. {}" .format(self.idmember, self.nama, self.alamat)


class Barang03(models.Model):
    nama=models.CharField(max_length=50)
    harga=models.BigIntegerField()
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)
   
    def __str__(self):
        return "{}. {}".format(self.kodebrg,self.nama, self.stok, self.harga, self.link_gbr)

class Member02(models.Model):
    idmember=models.CharField(max_length=10)
    nama=models.CharField(max_length=25)

    def __str__(self):
        return "{}. {}" .format(self.idmember, self.nama)
