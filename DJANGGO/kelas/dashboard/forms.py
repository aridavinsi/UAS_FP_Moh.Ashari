from django.forms import ModelForm
from dashboard.models import Barang, Member, Barang03, Member02
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widget = {
            'kodebrg': forms.TextInput({'class':'form-control'}),
            'nama':forms.TextInput({'class':'form-control'}),
            'stok':forms.NumberInput({'class':'form-control'}),
            'harga':forms.NumberInput({'class':'form-control'}),
            'link_gbr':forms.TextInput({'class':'form-control'}),
            'jenis_id':forms.Select({'class':'form-control'}),
        }

class FormMember(ModelForm):
    class Meta :
        model=Member
        fields='__all__'

        widget = {
            'idmember': forms.NumberInput({'class':'form-control'}),
            'nama':forms.TextInput({'class':'form-control'}),
            'alamat':forms.TextInput({'class':'form-control'}),
        }

class FormBarang03(ModelForm):
    class Meta :
        model=Barang03
        fields='__all__'

        widget = {
            'nama':forms.TextInput({'class':'form-control'}),
            'harga':forms.NumberInput({'class':'form-control'}),
            'jenis_id':forms.Select({'class':'form-control'}),
        }

class FormMember02(ModelForm):
    class Meta :
        model=Member02
        fields='__all__'

        widget = {
            'idmember': forms.NumberInput({'class':'form-control'}),
            'nama':forms.TextInput({'class':'form-control'}),
        }