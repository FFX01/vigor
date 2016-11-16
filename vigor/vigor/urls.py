"""vigor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

from users.api import UserResource
from programs.api import (
    ProgramResource, PeriodResource, SessionResource,
    ExerciseResource
)
from styles.api import StyleResource

urlpatterns = [
    url(
        r'^$',
        TemplateView.as_view(template_name='index.html'),
        name='home'
    ),
    url(r'^admin/', admin.site.urls),
    url(
        r'^api/users/',
        include(UserResource.urls())
    ),
    url(
        r'^api/programs/',
        include(ProgramResource.urls())
    ),
    url(
        r'^api/periods/',
        include(PeriodResource.urls())
    ),
    url(
        r'^api/sessions/',
        include(SessionResource.urls())
    ),
    url(
        r'^api/exercises/',
        include(ExerciseResource.urls())
    ),
    url(
        r'^api/styles/',
        include(StyleResource.urls())
    )
]
