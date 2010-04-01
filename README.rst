django-registration-defaults
============================

James Bennet's `django-registration
<http://bitbucket.org/ubernostrum/django-registration/>_` is awesome.  But it
doesn't come with any of the 15 templates required to implement the workflow of
registration, login/logout, and password changing and resetting.  This
application simply provides a set of default templates for this to avoid the
repetition of rewriting them.

This app is supplemental to ``django-registration``, which must also be
installed.

Installation
~~~~~~~~~~~~

Install using your preferred method for python modules.  The folder
``registration_defaults`` must end up in your python path.  You could do this
by copying or symlinking the folder into your path, or with::

    python setup.py install

My preferred method (and that of many django developers) is `pip
<http://pip.openplans.org/>`_ with `virtualenv
<http://pypi.python.org/pypi/virtualenv>`_ from the git source.  The
requirements file entry for this (and the dependency ``django-registration``)
is as follows::

    django-registration
    -e git://github.com/yourcelf/django-registration-defaults.git#egg=django-registration-defaults

Setup
~~~~~

Configuration parameters required by ``django-registration`` are set in the
module ``registration_defaults.settings``.  Add these by importing them into
your settings file::

    from registration_defaults.settings import *

Add ``registration_defaults`` to your Django project's ``INSTALLED_APPS``
setting::

    INSTALLED_APPS = (
        ...
        "registration",
        "registration_defaults",
        ...
    )

In order for the login and password changing templates to take precedence over
the default templates provided by ``django.contrib.admin`` (and thus use your a
consistent base template for all login and password views), you must either add
``registration_defaults`` before ``django.contrib.admin`` in the INSTALLED_APPS
list, or add the ``registration_defaults`` template dir to the
``TEMPLATE_DIRS`` setting explicitly.  For example::

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
inherit from, or override ``registration/registration_base.html``.

Bugs, improvements
==================

Please contribute any improvements or bugs to the `github project page
<http://github.com/yourcelf/django-registration-defaults>_`

Thanks!


