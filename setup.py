from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

import os

VERSION = '0.4'

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

template_dir = "registration_defaults/templates/registration"
templates = [os.path.join(template_dir, f) for f in os.listdir(template_dir)]

setup(
    name='django-registration-defaults',
    version=VERSION,
    description="Default templates and settings for James Bennett's"
                "django-registration application.",
    long_description="This module provides a full set of default templates"
        " and settings for ``django-registration`` to ease the process of"
        " creating Django apps that require user registration.  It depends"
        " on ``django-registration``.",
    author="Charlie DeTar",
    author_email="cfd@media.mit.edu",
    url="http://github.com/yourcelf/django-registration-defaults",
    license="MIT License",
    platforms=["any"],
    packages=['registration_defaults'],
    package_data={'registration_defaults': templates},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
