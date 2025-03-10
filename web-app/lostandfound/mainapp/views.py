from django.shortcuts import render, get_object_or_404, redirect
from .forms import ItemForm
from .forms import SearchForm
from .models import Category,Item,Tag,ItemTag

def index(request):
    return render(request,'index.html')

def all_items(request):
    items = Item.objects.all()
    return render(request,'mainapp/item-list.html',{"items":items})

def item_detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    context = {
        'item':item
    }
    return render(request,'mainapp/item-detail.html',context)

def unclaimed_items(request):
    items = Item.objects.filter(claimed_status = False)
    return render(request,'mainapp/unclaimed-items.html',{'items':items})

def search_items(request):
    categories = Category.objects.all()
    category = request.GET.get('category')

    if category:
        items = Item.objects.filter(category__name = category)
    else:
        items = Item.objects.all()

    context = {
        'categories': categories,
        'items': items,
        'category': category
    }

    return render(request,'mainapp/filter.html',context)

def about(request):
    all_items = Item.objects.count()
    unclaimed_items = Item.objects.filter(claimed_status = False).count()
    context = {
        'all_items': all_items,
        'unclaimed_items': unclaimed_items
    }
    return render(request, 'mainapp/about.html', context)


def search(request):
    search_text = request.GET.get("search")
    items = []
    form = SearchForm(request.GET)
    if form.is_valid() and len(form.cleaned_data['search'])>=1:
        search = form.cleaned_data['search']
        items = Item.objects.filter(name__icontains = search)

    return render(request,'mainapp/search.html',{"form":form,"items":items,"search_text":search_text})



def report(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all-items")
        else:
            print(form.errors)
    else:
        form = ItemForm()

    return render(request,'mainapp/report.html',{"form":form})

