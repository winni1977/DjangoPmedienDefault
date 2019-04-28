import inspect
import os

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.template.defaultfilters import safe
from django.urls import reverse


class PmedienDefaults(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if not kwargs:
            my_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))

            self.message_user(
                request,
                safe(
                    '<div class="special_settings"><script>{}</script></div>'.format(
                        open(os.path.join(my_dir, 'main.js')).read()
                    )
                )
            )
        return super(PmedienDefaults, self).get_form(request, obj, **kwargs)

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.all().count() == 1:
            obj = self.model.objects.first()
            return HttpResponseRedirect(
                reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.model_name),
                        args=(obj.id,)))
        else:
            return HttpResponseRedirect(
                reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.model_name)))

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        if getattr(request.resolver_match, 'func', None).__name__ == 'add_view':
            return True
        return False
