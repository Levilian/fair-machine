from django.urls import path
from django.views import generic

from . import views

"""polls URL Configuration
    
    The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
    Examples:
    Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    """

line_chart = generic.TemplateView.as_view(template_name='line_chart.html')
line_chart_json = views.LineChartJSONView.as_view()

line_chart2 = generic.TemplateView.as_view(template_name='line_chart.html')
line_chart_json2 = views.LineChartJSONView2.as_view()

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('decision', views.DecisionView.as_view(), name='decision'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('stats', views.StatsView.as_view(), name='stats'),
    path('line_chart_json', views.LineChartJSONView.as_view(), name='line_chart_json'),
    path('line_chart_json2', views.LineChartJSONView2.as_view(), name='line_chart_json2'),
    path('decision/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('decision/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('decision/<int:decision_group_id>/vote/', views.vote, name='vote'),
]
