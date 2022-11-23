from datetime import datetime

from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
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
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
