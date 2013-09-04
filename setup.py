from distutils.core import setup

VERSION = '0.4.2'

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
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
    zip_safe=False,
)
