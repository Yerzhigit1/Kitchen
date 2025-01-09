from django.urls import path
from main import views
app_name = 'main'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('category/<slug:category_slug>/', views.MainView.as_view(), name='category'),
    path('post/<slug:post_slug>/', views.DetailPage.as_view(), name='detail_page'),
    
    path("search/", views.SearchView.as_view(), name="search"),
    
    path("add_post/", views.PostAddView.as_view(), name="add_post"),
    path("post/<slug:post_slug>/update/", views.PostUpdateView.as_view(), name="update_post"),
    path("post/delete/<int:post_id>/", views.PostDeleteView.as_view(), name="delete_post"),
    path('delete_comment/<int:comment_id>/', views.delete_comment_view, name='delete_comment'),
    
    path('post/<int:post_id>/increment_views/', views.increment_views, name='increment_views'),
    
]