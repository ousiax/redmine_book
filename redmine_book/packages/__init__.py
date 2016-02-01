# -*- encoding:utf-8 -*-

from . import redmine

try:
    external_redmine = __import__('redmine', level=0)
except ImportError:
    pass
else:
    if redmine.__version__ < external_redmine.__version__:
        redmine = external_redmine
