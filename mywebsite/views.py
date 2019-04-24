from django.shortcuts import render

def index(request):
	context = {
		'Tittle':'SISTEM INFORMASI JARINGAN IRIGASI',
		'Heading':'Selamat Datang',
		'Subheading':'Sistem Informasi Jaringan Irigasi Danayuda'
	}

	return render(request,'index.html', context)