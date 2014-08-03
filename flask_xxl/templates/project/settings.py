# -*- coding: utf-8 -*-

"""
    settings
    ~~~~~~~~
    Global settings for project.
"""
import os
from local_settings import LocalConfig

class BaseConfig(LocalConfig):
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    #ADMIN_PER_PAGE = 5
    #CODEMIRROR_LANGUAGES = ['python','python2','python3','php','javascript','xml']
    #CODEMIRROR_THEME = 'blackboard'#'vivid-chalk'#'3024-night'
    #SQLALCHEMY_ECHO = True
    #SQLALCHEMY_COMMIT_ON_TEARDOWN = True


    #####################################################
    # Define url modules with routes defined inside
    #
    #   in bp.urls.py file make routes
    #   routes = [
    #       ((bp_name),
    #           ('/url_rule',ViewClass.as_view('endpoint')),
    #           ('/next_url',view_func)),
    #       ]
    #
    #####################################################
    URL_MODULES = [
            '{{{project.url_module}}}.urls.routes',
            #'flask.ext.xxl.apps.admin.urls.routes',
            #'flask.ext.xxl.apps.auth.urls.routes',
            #'flask.ext.xxl.apps.page.urls.routes',
    ]
    
    #####################################################
    # define sub dirs as blueprints
    # in __init__.py file define blueprint like this:
    #   from flask import BluePrint
    #   blueprint = BluePrint('blueprint',__name__,
    #                           url_prefix='/blueprint',
    #                           template_dir='templates')
    #####################################################
    BLUEPRINTS = [
            '{{{project.name}}}.{{{project.name}}}',
            #'flask.ext.xxl.apps.admin.admin',
            #'flask.ext.xxl.apps.menu.menu',
            #'flask.ext.xxl.apps.page.page',
            #'flask.ext.xxl.apps.auth.auth',
    ]

    ####################################################
    # define flask extensions to use in your app
    # in ext.py import and create instance of extensions
    # from flask.ext.name import Extension
    #
    # extension = Extension()
    #####################################################

    EXTENSIONS = [
            'ext.db',
            #'ext.toolbar',
            #'ext.pagedown',
            #'ext.codemirror',
            #'ext.alembic',
    ]
    
    ###################################################
    # context processors add global variables or
    # functions to your templates
    #
    # define like this:
    # def my_processor_name():
    #   def the_func_to_add():
    #       #w/e you want to do
    #   return {name:the_func_to_add}
    # then in templates name is aviable
    ######################################################

    CONTEXT_PROCESSORS = [
            #'flask.ext.xxl.context_processors.add_is_page',
            #'flask.ext.xxl.context_processors.common_context',
            #'flask.ext.xxl.context_processors.common_forms',
            #'flask.ext.xxl.apps.menu.context_processors.frontend_nav',
            #'flask.ext.xxl.apps.menu.context_processors.admin_nav',
            #'flask.ext.xxl.apps.auth.context_processors.user_context',
    ]

    TEMPLATE_FILTERS = [
            'flask.ext.xxl.filters.date',
            'flask.ext.xxl.filters.date_pretty',
            'flask.ext.xxl.filters.datetime',
            'flask.ext.xxl.filters.pluralize',
            'flask.ext.xxl.filters.month_name',
            'flask.ext.xxl.filters.markdown',
    ]

    CONTACT_FORM_SETTINGS = {
    'HEADING':'Send Us a message',
    'SUBHEADING':'Or a Comment',
    'OPTIONS':(
        ('test','opt1'),
        ('test2','opt2'),
        ('test3','opt3'),
        ('test4','opt4'),
        ('test5','opt5'),
        ('test6','opt6'),
    ),
    'SUBMIT_TEXT':'Send to Us',
    'COMPANY_TITLE':'Level2designs',
    'COMPANY_ADDRESS':{
        'NAME':'level2designs',
        'STREET':'1045 w katella',
        'CITY':'Orange',
        'STATE':'CA',
        'ZIP':'92804',
    },
    'COMPANY_PHONE':'714-783-6369',
    'CONTACT_NAME':'Kyle Roux',
    'CONTACT_EMAIL':'kyle@level2designs.com',
    }

    #BLOG_SIDEBAR_LEFT = False
    #BLOG_SIDEBAR_RIGHT = True
    BLOG_SIDEBAR_LEFT = True
    #BLOG_SIDEBAR_RIGHT = False
    BLOG_TITLE = 'Dynamic'
    BLOG_CONTENT = 'some text to put into my<br />Blog'

def get_choices(option):
    return BaseConfig.DYNAMIC_SETTINGS[option]


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(BaseConfig):
    TESTING = True
