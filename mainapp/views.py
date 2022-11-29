from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from mainapp import models as mainapp_models


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 31f4ee1 (Lesson 3 (#2))
    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        context["news_title"] = "Громкий новостной заголовок"
        context["news_preview"] = "Предварительное описание, которое заинтересует каждого"
<<<<<<< HEAD
<<<<<<< HEAD
        context["range"] = range(5)
        context["datetime_obj"] = datetime.now()
<<<<<<< HEAD
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
=======
>>>>>>> de2bc33 (lesson_3 Template inhereting)
=======
        context["range"] = range(5)
>>>>>>> 8b40449 (lesson_3 Loops in templates)
=======
>>>>>>> 50e23b6 (lesson_3 Template's filters)
=======
=======
>>>>>>> 949da51 (Lesson 3 (#2))
        context["news_qs"] = mainapp_models.News.objects.all()[:5]
>>>>>>> 202c2e9 (lesson_4 Display model's data)
        return context
=======
=======
>>>>>>> 31f4ee1 (Lesson 3 (#2))
        context["news_title"] = "Громкий новостной заголовок"
        context["news_preview"] = "Предварительное описание, которое заинтересует каждого"
        context["range"] = range(5)
        context["datetime_obj"] = datetime.now()
=======
        context["news_qs"] = mainapp_models.News.objects.all()[:5]
>>>>>>> c323222 (lesson_4 Display model's data dotenv secretkey)
        return context


class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context

<<<<<<< HEAD
>>>>>>> 9044c7d (Lesson 3 (#2))


class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context

=======
>>>>>>> e422349 (Lesson 3 (#2))
=======
>>>>>>> 31f4ee1 (Lesson 3 (#2))

class CoursesListView(TemplateView):
    template_name = "mainapp/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = mainapp_models.Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lesson.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.CourseTeachers.objects.filter(course=context["course_object"])
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
