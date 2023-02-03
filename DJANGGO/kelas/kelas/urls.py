"""kelas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import *
from dashboard.views import produk
from dashboard.views import produk, tambah_barang, Barang_view, member, Barang_03, member_02

def coba1(request):
    return HttpResponse('Selamat Datang')

def satu(request):
    titelnya="HOME"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'home.html', konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',satu),
    path('utama/',satu),
    path('produk/',produk),
    path('addbrg/',tambah_barang),
    path('addmember/',tambah_member),
    path('addbrg03/',tambah_barang03),
    path('addmember02/',tambah_member02),
    path('Vbrg/',Barang_view,name='Vbrg'),
    path('member/',member,name='member'),
    path('Vbrg02/',Barang_03,name='Vbrg02'),
    path('member02/',member_02,name='member02'),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('ubahmember/<int:id_member>',ubah_member,name='ubah_member'),   
    path('hapus/<int:id_barang>',hapus_brg,name='hapus_brg'),
    path('hapusmember/<int:id_member>',hapus_member,name='hapus_member'),
]
