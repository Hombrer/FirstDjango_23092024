from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
# Нужный тип исключения для функции get_item()
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_email@mail.ru"
    }
    return render(request, 'index.html', context)


def about(request):
    author = {
        "name": "Иван",
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru"
    }
    return render(request, 'about.html', {'author': author})


def get_item(request, item_id: int):
    """ Функция по item_id нужного элемента вернет имя и кол-во. """
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        # Если элемент не найден - нужно вернуть соотвествующий ответ(response)
        return render(request, "errors.html", {'error': f"Item with id={item_id} not found."})
    else:
        context = {
            "item": item,
            "colors": item.colors.all()
            }
        return render(request, "item_page.html", context)
    

def get_items(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)