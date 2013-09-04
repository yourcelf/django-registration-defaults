django-registration-defaults
============================

James Bennet's `django-registration <http://bitbucket.org/ubernostrum/django-registration/>`_ 
is awesome.  But it doesn't come with any of the 15 templates required to
implement the workflow of registration, login/logout, and password changing and
resetting.  This application simply provides a set of default templates for
this to avoid the repetition of rewriting them.

This app is supplemental to ``django-registration``, which must also be
installed.

Installation
~~~~~~~~~~~~

Install using your preferred method for python modules.  The folder
``registration_defaults`` must end up in your python path.  You could do this
by copying or symlinking the folder into your path, or with::

    python setup.py install

My preferred method (and that of many django developers) is to install from the
git source using `pip <http://pip.openplans.org/>`_ with `virtualenv
<http://pypi.python.org/pypi/virtualenv>`_.  The `requirements file
<http://pip.openplans.org/#requirements-files>`_ entry for this (and the
dependency ``django-registration``) is as follows::

    django-registration
    django-registration-defaults

Setup
~~~~~

Configuration parameters required by ``django-registration`` are set in the
module ``registration_defaults.settings``.  Add these by importing them into
your settings file::

    from registration_defaults.settings import *

You can add the templates in one of two ways:

    1.  If you're using the ``django.template.loaders.app_directories.Loader``
        template loader (it is enabled by default), you can include the
        templates by adding ``"registration_defaults"`` to your project's
        ``INSTALLED_APPS`` setting.  Keep in mind that ``admin`` defines some
        templates for changing and retrieving passwords, so if you want to use
        consistent base templates and styling for all registration and
        login/logout functions, you should add ``registration_defaults`` before
        ``django.contrib.admin`` so that it will take precedence::

            INSTALLED_APPS = (
                ...
                "registration_defaults",
                "django.contrib.admin",
                ...
                "registration",
            )

    2. Alternatively, if ``django.template.loaders.filesystem.Loader`` is
       listed before the app directories loader, you can add
       ``REGISTRATION_TEMPLATE_DIR`` to your ``TEMPLATE_DIRS`` setting.  If you
       do this, it is not necessary to include ``registration_defaults`` as an
       installed app::

            from registration_defaults.settings import *

            TEMPLATE_DIRS = (
                ...
                REGISTRATION_TEMPLATE_DIR,
            )

Base templates
~~~~~~~~~~~~~~

All ``registration_defaults`` templates inherit from
``registration/registration_base.html``.  The default template provided for
this is simply::

    {% extends "base.html" %}

You must either provide a ``base.html`` for the registration templates to
inherit from, or override ``registration/registration_base.html``.  The base
template should provide a ``title`` block for the content of the HTML title,
and a ``content`` block for content (NOTE: this has changed from previously
using ``body`` to be more in line with `reusable app standards 
<http://django-reusable-app-docs.readthedocs.org/en/latest/index.html>`_ ).  For example::

    <!doctype html>
    <html>
        <head>
            <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
            {% block content %}{% endblock %}
        </body>
    </html>

Bugs, improvements
==================

Please contribute any improvements or bugs to the `github project page
<http://github.com/yourcelf/django-registration-defaults>`_

Thanks!

Copying
=======

Copyright (c) 2010 Charlie DeTar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
