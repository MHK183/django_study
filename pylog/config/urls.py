from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from config.views import index
from blog.views import post_list, post_detail, post_add


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('posts/', post_list),
    path('posts/<int:post_id>/', post_detail),
    path('posts/add/', post_add)
]
urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)