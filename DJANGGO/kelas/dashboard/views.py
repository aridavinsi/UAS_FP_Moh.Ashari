from django.shortcuts import render,redirect
from dashboard.forms import FormBarang, FormMember, FormBarang03, FormMember02
from dashboard.models import Barang, Member
from dashboard.models import Barang03, Member02
from django.contrib import messages

def produk(request):
    titelnya="produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html', konteks)
# Create your views here.

def tambah_barang(request):
    if request.POST:
        form=FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        titelnya="Form"
        konteks={
            'form':form,
        }
    return render(request,'tambah_barang.html',konteks)

def tambah_member(request):
    if request.POST:
        form=FormMember(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormMember()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_member.html',konteks)
    else:
        form=FormMember()
        titelnya="Form"
        konteks={
            'form':form,
        }
    return render(request,'tambah_member.html',konteks)

def tambah_barang03(request):
    if request.POST:
        form=FormBarang03(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormBarang03()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_barang03.html',konteks)
    else:
        form=FormBarang03()
        titelnya="Form"
        konteks={
            'form':form,
        }
    return render(request,'tambah_barang03.html',konteks)

def tambah_member02(request):
    if request.POST:
        form=FormMember02(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormMember02()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_member02.html',konteks)
    else:
        form=FormMember02()
        titelnya="Form"
        konteks={
            'form':form,
        }
    return render(request,'tambah_member02.html',konteks)

def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs':barangs
        }
    return render(request,'ubah_brg.html',konteks)

def ubah_member(request,id_member):
    members=Member.objects.get(id=id_member)
    if request.POST:
        form=FormMember(request.POST,instance=members)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_member',id_member=id_member)
    else:
        form=FormMember(instance=members)
        konteks = {
            'form':form,
            'members':members
        }
    return render(request,'ubah_member.html',konteks)



def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data Terhapus")
    return redirect('Vbrg')

def hapus_member(request,id_member):
    members=Member.objects.filter(id=id_member)
    members.delete()
    messages.success(request,"Data Terhapus")
    return redirect('member')



def Barang_view(request):
    barangs=Barang.objects.all()
    titelnya="Tabel1"
    konteks={
        'barangs':barangs,
    }
    return render(request,'tabel1.html', konteks)

def member(request):
    members=Member.objects.all()
    titelnya="Member"
    konteks={
        'members':members,
        'titel':titelnya,
    }
    return render(request,'tabel2.html', konteks)

def Barang_03(request):
    barangs03=Barang.objects.all()
    titelnya="Tabel3"
    konteks={
        'barangs':barangs03,
    }
    return render(request,'tabel3.html', konteks)

def member_02(request):
    members02=Member.objects.all()
    titelnya="Member02"
    konteks={
        'members':members02,
        'titel':titelnya,
    }
    return render(request,'tabel4.html', konteks)
