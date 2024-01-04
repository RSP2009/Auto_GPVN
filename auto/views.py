from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

# Create your views here.
menu = [{'title': "Путевые листы", 'url_name': 'putlist'},
        {'title': "Нормы расхода", 'url_name': 'normrashod'},
        {'title': "Отчеты", 'url_name': 'othets'},
        {'title': "Добавить автомобиль", 'url_name': 'addauto'},
        {'title': "Редактировать автомобиль", 'url_name': 'editauto'}
        ]


def index(request):
    park = Auto.objects.all()
    # cats = Category.objects.all()

    contex = {
        'park': park,
        # 'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, "auto/index.html", context=contex)


def about(request):
    return render(request, "auto/about.html", {'menu': menu, 'title': 'О сайте'})


def putlist(request):
    return HttpResponse('Страница обработки путевых листов')


def normrashod(request):
    return HttpResponse('Страница норм расхода')


def othets(request):
    return HttpResponse('Страница отчетов')


def addauto(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # try:
                # Auto.objects.create(**form.cleaned_data)
            form.save()
            return redirect('home')
            # except:
            #     form.add_error(None, 'Ошибка добавления информации')
    else:
        form = AddPostForm()

    return render(request, 'auto/addauto.html', {'form': form, 'menu': menu, 'marka': 'Добавление комментария'})


def editauto(request):
    return HttpResponse('Страница редактирования авто')


def show_post(request, post_slug):
    post = get_object_or_404(Auto, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'marka': post.marka,
        'cat_selected': post.cat_id,
    }
    return render(request, 'auto/post.html', context=context)
    # return HttpResponse(f'Отображение заметки о машине с id = {post_id}')


def show_category(request, cat_id):
    park = Auto.objects.filter(cat_id=cat_id)
    # cats = Category.objects.all()

    if len(park) == 0:
        raise Http404

    contex = {
        'park': park,
        # 'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, "auto/index.html", context=contex)
    # return HttpResponse(f'Отображение категории с id = {cat_id}')


def personal(request, perid):
    return HttpResponse(f"<h1>Страница конкретной машины</h1><p>Машина № {perid}</p><p>Пробег: 50000</p>")


def obslug(request, per):
    return HttpResponse(f"<h2>Страница истории ТОиР</h2><p>{per}</p>")


def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)
        # raise Http404()

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!!!</h1>')
