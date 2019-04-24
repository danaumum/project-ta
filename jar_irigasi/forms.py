from django import forms
from .models import LaporanKerusakan

class LaporanForm(forms.ModelForm):
    class Meta:
        model = LaporanKerusakan
        fields = ('nama','alamat','noTelepon','lokasiKerusakan','deskripsiKerusakan','foto', 'foto2')
        labels = {
        	'nama':'Nama Pelapor',
        	'alamat':'Alamat',
        	'noTelepon':'Nomer telepon',
        	'lokasiKerusakan':'Koordinat Lokasi Kerusakan',
        	'deskripsiKerusakan':'Deskripsi Kerusakan',
        	'foto':'Foto 1',
        	'foto2':'Foto 2'
        }
    



