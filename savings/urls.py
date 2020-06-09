from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='savings_index'),
    path('stocks', views.stocks, name='savings_details'),
    path('stocks/<choice>', views.mlearning, name='savings_m_learning'),
    path('tips', views.tips, name='savings_tips')

]
