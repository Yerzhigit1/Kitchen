from django.urls import path
from main.views import IndexView, index, category_view
from kitchen import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('', index, name='index'),
    path('category/<slug:category_slug>', category_view, name='category')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)