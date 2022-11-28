from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("news/", views.NewsPageView.as_view(), name="news"),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
=======
>>>>>>> cb71671 (lesson_3 Urls in templates)
=======
    path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
>>>>>>> b00f658 (lesson_3 Args in url)
    path("courses/", views.CoursesPageView.as_view(), name="courses"),
=======
=======
>>>>>>> 949da51 (Lesson 3 (#2))
    path("news/<int:pk>/", views.NewsPageDetailView.as_view(), name="news_detail"),
    path("courses/", views.CoursesListView.as_view(), name="courses"),
    path(
        "courses/<int:pk>/",
        views.CoursesDetailView.as_view(),
        name="courses_detail",
    ),
<<<<<<< HEAD
>>>>>>> 202c2e9 (lesson_4 Display model's data)
=======
=======
    path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
    path("courses/", views.CoursesPageView.as_view(), name="courses"),
>>>>>>> 9044c7d (Lesson 3 (#2))
>>>>>>> 949da51 (Lesson 3 (#2))
=======
    path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
    path("courses/", views.CoursesPageView.as_view(), name="courses"),
>>>>>>> e422349 (Lesson 3 (#2))
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    path("login/", views.LoginPageView.as_view(), name="login"),
]
