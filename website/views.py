from django.shortcuts import render, get_object_or_404
from website.forms import ContactosForm
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from website.models import CategoriaModel, SubcategoriaModel, ImagemModel
from django.urls import reverse

def get_lang(request):
    try:
        lang = request.META['HTTP_ACCEPT_LANGUAGE']
    except:
        lang = "pt-PT"
    cookie = request.COOKIES.get('lang')
    if cookie is None:
        return "pt" if lang[:5] == "pt-BR" or lang[:5] == "pt-PT" else "en"
    else:
        return cookie

def copyright():
    if datetime.now().year != 2020:
        return f"2020 - {datetime.now().year}"
    else:
        return "2020"

def home(request, *args, **kwargs):
    lang = get_lang(request)
    title = "Pagina Principal" if lang == "pt" else "Main Page"
    return render(request, "index.html", {
        "title": title,
        "lang": lang,
        "copyright": copyright(),
        "categoria": CategoriaModel.objects.filter(visivel=True).order_by('ordem')
    })

def about(request, *args, **kwargs):
    lang = get_lang(request)
    title = "Sobre Nós" if lang == "pt" else "About Us"

    return render(request, "about.html", {
        "title": title,
        "lang": lang,
        "copyright": copyright()
    })

def services(request, *args, **kwargs):
    lang = get_lang(request)
    title = "Serviços" if lang == "pt" else "Services"
    
    return render(request, "services.html", {
        "title": title,
        "lang": lang,
        "copyright": copyright()
    })

def products(request, *args, **kwargs):
    try:
        id = kwargs["id"]
        cat = CategoriaModel.objects.filter(visivel=True, id=id).order_by('ordem')
    except:
        id = -1
    lang = get_lang(request)
    if id != -1: 
        if cat.count() == 0:
            return HttpResponseRedirect(reverse(products))
        title = cat[0].tituloPT if lang == "pt" else cat[0].tituloEN
        context = {
            "title": title,
            "lang": lang,
            "copyright": copyright(),
            "id": id,
            "categoria": cat,
            "subcategoria": SubcategoriaModel.objects.filter(visivel=True, categoria=id).order_by('ordem'),
            "imagem": ImagemModel.objects.filter(visivel=True).order_by('ordem')
        }
    else:
        title = "Produtos" if lang == "pt" else "Products"
        context = {
            "title": title,
            "lang": lang,
            "copyright": copyright(),
            "id": id,
            "categoria": CategoriaModel.objects.filter(visivel=True).order_by('ordem')
        }
    return render(request, "products.html", context)

def lang(request, *args, **kwargs):
    if request.POST:
        if request.POST['id_lang'] == "0":
            lang = "pt"
        else:
            lang = "en"
        response = HttpResponseRedirect(request.POST['redirect'])
        response.set_cookie('lang', lang)    
        return response

def contacts(request, *args, **kwargs):
    lang = get_lang(request)
    title = "Contactos" if lang == "pt" else "Contacts"
    erro = -1 #nao mostrar msg

    if request.method == 'POST':
        form = ContactosForm(request.POST)
        if form.is_valid():
            erro = 0 #mostrar msg sucesso
            form.save()
            form = ContactosForm()
        else:
            erro = 1 #mostrar msg erro
    else:
        form = ContactosForm()
        
    return render(request, "contacts.html", {
        "title": title,
        "lang": lang,
        "copyright": copyright(),
        "form": form,
        "erro": erro
    })