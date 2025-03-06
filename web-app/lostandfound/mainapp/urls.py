from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('items/',views.all_items,name='all-items'),
    path('items/<int:pk>',views.item_detail,name='item-detail'),
    path('unclaimed/',views.unclaimed_items,name='unclaimed-items'),
    path('filter/',views.search_items,name='filter'),
    path('about/',views.about,name='about'),
    path('search/',views.search,name='search'),
    path('report/',views.report,name='report')
]