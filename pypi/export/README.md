General export for a complete model with languages

Usage:

project/urls.py:

from django_pmedien_export import export


urlpatterns = [

url(r'^admin/', admin.site.urls),    
url(r'^export/((?P<appname>[\w-]+)/)?$', export.export),

]    


The appname should be an existing app. Otherwise hothing is returned.