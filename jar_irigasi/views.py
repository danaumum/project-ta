from django.shortcuts import render, redirect
from .models import *
from .forms import LaporanForm
from django.core.serializers import serialize
#from rest_framework.renderers import JSONRenderer
import json
from django.forms.models import model_to_dict


# Create your views here.
def index(request):
	corongs	= Bangunan_corong.objects.all()
	sadaps 	= Bangunan_sadap.objects.all()
	bendungs = Bangunan_bendung.objects.all()
	corong_seri = serialize('json', corongs)
	sadap_seri = serialize('json', sadaps)
	bendung_seri = serialize('json', bendungs)
	#obj_as_dict = json.loads(sadap_seri)[0]['fields']
	context = {
		'Tittle':'Sistem Informasi Jaringan Irigasi Danayuda',
		'Heading':'Selamat Datang',
		'Subheading':'Menampilkan informasi bangunan irigasi',
		'Corongs': corongs,
		'Sadaps': sadaps,
		'sadap_json': json.dumps(sadap_seri),
		'corong_json': json.dumps(corong_seri),
		'bendung_json': json.dumps(bendung_seri),
		'Bendungs' : bendungs
	}
	return render(request,'jar_irigasi/index.html', context)

def listBangunan(request):
	corongs	= Bangunan_corong.objects.all()
	sadaps 	= Bangunan_sadap.objects.all()
	bendungs = Bangunan_bendung.objects.all()
	corong_seri = serialize('json', corongs)
	sadap_seri = serialize('json', sadaps)
	bendung_seri = serialize('json', bendungs)
	#obj_as_dict = json.loads(sadap_seri)[0]['fields']
	context = {
		'Tittle':'Sistem Informasi Jaringan Irigasi Danayuda',
		'Heading':'Selamat Datang',
		'Subheading':'Menampilkan informasi bangunan irigasi',
		'Corongs': corongs,
		'Sadaps': sadaps,
		'sadap_json': json.dumps(sadap_seri),
		'corong_json': json.dumps(corong_seri),
		'bendung_json': json.dumps(bendung_seri),
		'Bendungs' : bendungs
	}
	return render(request,'jar_irigasi/list_bangunan.html', context)

def skema(request):
	corongs	= Bangunan_corong.objects.all()
	sadaps 	= Bangunan_sadap.objects.all()
	bendungs = Bangunan_bendung.objects.all()
	corong_seri = serialize('json', corongs)
	sadap_seri = serialize('json', sadaps)
	bendung_seri = serialize('json', bendungs)
	#obj_as_dict = json.loads(sadap_seri)[0]['fields']
	context = {
		'Tittle':'Sistem Informasi Jaringan Irigasi Danayuda',
		'Heading':'Selamat Datang',
		'Subheading':'Menampilkan informasi bangunan irigasi',
		'Corongs': corongs,
		'Sadaps': sadaps,
		'sadap_json': json.dumps(sadap_seri),
		'corong_json': json.dumps(corong_seri),
		'bendung_json': json.dumps(bendung_seri),
		'Bendungs' : bendungs
	}
	return render(request,'jar_irigasi/skema.html', context)

def laporan(request):
	if request.method == 'POST':
		form = LaporanForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	

	form = LaporanForm()
	context = {
		'form':form,
		'Tittle':'SISTEM INFORMASI JARINGAN IRIGASI',
		'Heading':'Sistem Informasi Jaringan Irigasi Danayuda',
		'Subheading':'Form Laporan Kerusakan',

	}
	return render(request, 'jar_irigasi/form.html', context)



def detailCorong(request, slugInput):
	corong	= Bangunan_corong.objects.get(slug=slugInput)
	context = {
		'Tittle':'SISTEM INFORMASI JARINGAN IRIGASI',
		'Heading':'Sistem Informasi Jaringan Irigasi Danayuda',
		'Subheading':'Menampilkan informasi bangunan irigasi',
		'Corong': corong
	}

	return render(request,'jar_irigasi/detailCorong.html', context)

def detailSadap(request, slugInput):
	sadap	= Bangunan_sadap.objects.get(slug=slugInput)
	context = {
		'Tittle':'SISTEM INFORMASI JARINGAN IRIGASI',
		'Heading':'Sistem Informasi Jaringan Irigasi Danayuda',
		'Subheading':'Menampilkan informasi bangunan irigasi',
		'Sadap': sadap
	}

	return render(request,'jar_irigasi/detailSadap.html', context)

def detailBendung(request, slugInput):
	bendung	= Bangunan_bendung.objects.get(slug=slugInput)
	context = {
		'Tittle':'SISTEM INFORMASI JARINGAN IRIGASI',
		'Heading':'Sistem Informasi Jaringan Irigasi Danayuda',
		'Subheading':'Menampilkan informasi bangunan irigasi',
		'Bendung': bendung
	}

	return render(request,'jar_irigasi/detailBendung.html', context)