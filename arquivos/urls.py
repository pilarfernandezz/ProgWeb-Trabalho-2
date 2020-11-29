from django.contrib import admin
from django.urls import include, path
from arquivos import views;
app_name = 'arquivos';
urlpatterns = [
    path('apaga/<int:pk>/', views.ArquivoDeleteView.as_view(), name='apaga-arquivo'),
    path('atualiza/<int:pk>/', views.ArquivoUpdateView.as_view(), name='atualiza-arquivo'),
    path('lista/', views.ArquivoListView.as_view(),   name='lista-arquivo'),
    path('cria/',  views.ArquivoCreateView.as_view(), name='cria-arquivo'),
]