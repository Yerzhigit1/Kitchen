from django.urls import path
from main import views
app_name = 'main'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('category/<slug:category_slug>/', views.MainView.as_view(), name='category'),
    path('post/<slug:post_slug>/', views.DetailPage.as_view(), name='detail_page'),
    path("add_post/", views.PostAddView.as_view(), name="add_post"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("post/<slug:post_slug>/update/", views.PostUpdateView.as_view(), name="update_post"),
    path("post/<int:post_id>/delete/", views.PostDeleteView.as_view(), name="delete_post"),
    
]