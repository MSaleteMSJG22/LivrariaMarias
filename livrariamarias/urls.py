from django.contrib import admin
from django.urls import path
from principal.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',index, name='index'),
    path ('produtos/', produtos , name='produtos'),
    path ('detalhes/<int:id>',detalhes, name='detalhes'),
    path ('sobrenos/',sobrenos, name='sobrenos'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






