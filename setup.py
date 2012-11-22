#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "django-verbatim",
    version = "0.1",
    packages = find_packages(),
    include_package_data = True,
    author = "Aljosa Mohorovic",
    author_email = "aljosa.mohorovic@gmail.com",
    description = "Django template block tag which renders template syntax characters within the block as normal text.",
    long_description = \
"""
Template block tag which renders template syntax characters within the block as normal text. This serves as an escape hatch to avoid syntax collisions when using a template language meant to be rendered on the client, not the server.

This repo is just a package for PyPI, original code:
https://gist.github.com/629508

Django v1.5 should have compatible code included:
https://code.djangoproject.com/ticket/14502
""",
    license = "MIT License",
    keywords = "django template tag verbatim",
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms = ['any'],
    url = "https://github.com/aljosa/django-verbatim",
)
