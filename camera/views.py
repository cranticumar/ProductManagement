'''
Created on Jan 30, 2016

@author: bkranthi
'''
from importlib import import_module
from rest_framework import views, reverse, response
from camera import settings
from collections import OrderedDict
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


class APIRoot(views.APIView):
    _ignore_model_permissions = True

    def __init__(self):
        views = {}

        for app_name in settings.INSTALLED_APPS:
            try:
                m = import_module('.rest.urls', app_name)
                if hasattr(m, 'router'):
                    list_name = m.router.routes[0].name
                    for prefix, viewset, basename in m.router.registry:
                        logger.debug('view set is: {vs}'.format(vs=viewset))
                        views[prefix] = list_name.format(basename=basename)
            except ImportError:
                pass

        self.api_root_dict = OrderedDict(
            sorted(views.items(), key=lambda t: t[0]))

    def get(self, request, frmt=None):
        ret = OrderedDict()
        for key, url_name in self.api_root_dict.iteritems():
            ret[key] = reverse.reverse(url_name, request=request, format=frmt)
        return response.Response(ret)
