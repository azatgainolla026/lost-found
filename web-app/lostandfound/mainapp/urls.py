from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('items/',views.all_items,name='all-items'),
    path('items/<int:pk>',views.item_detail,name='item-detail'),
    path('unclaimed/',views.unclaimed_items,name='unclaimed-items'),
    path('search/',views.search_items,name='search'),
    path('about/',views.about,name='about'),
]