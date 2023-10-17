from django.urls import path
from .views import (
	home,
	PostDetail,
	category,
	CreateArticle,
	ListArticle,
	ArticleUpdate,
	ArticleDeleteView,
	search,
	tickView,
	chat_ai_jetwrie,

		)
urlpatterns = [
	path('',home,name="home"),
	path('<int:pk>/',PostDetail.as_view(),name='detail'),
	path('category/<slug:slug>/',category,name='category'),
	path('my/',ListArticle.as_view(),name="list"),
    path('create/',CreateArticle.as_view(),name='create'),
    path('update/<int:pk>/',ArticleUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',ArticleDeleteView.as_view(),name="delete"),
    path('search/',search,name="search"),
  	path('verified/',tickView,name="tick"),
  	path('aria-ai/',chat_ai_jetwrie,name="chatbot"),

]
