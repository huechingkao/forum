# -*- coding: utf8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TopicListView.as_view()),
    path('topic/<int:pk>', views.TopicDetailView.as_view()),
    path('topic/create/', views.TopicCreate.as_view()),  
    path('topic/<int:pk>/delete/', views.TopicDelete.as_view()),   
    path('reply/<int:topic_id>/create/', views.ReplyCreate.as_view()),  
    path('reply/<int:topic_id>/<int:pk>/delete/', views.ReplyDelete.as_view()),    
]