from django.urls import path, include
from food import views


app_name ="food"

urlpatterns = [
    # function based index view.
    # path('index/', views.index, name='index'),
    # class based index view
    path('index/',views.IndexClassView.as_view(),name='index'),
    
    
    #function based detail view    
    path('detail/<int:item_id>/',views.detail,name='detail'),
    
    #function based create_item view
    path('add/', views.create_item, name='create_item'),
    
    #function based update_item view
    path('update/<int:id>/',views.update_item,name='update_item'),
    
    
    #function based delete_item view
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
    
]
