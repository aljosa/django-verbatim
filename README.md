django-verbatim
===
Template block tag which renders template syntax characters within the block as normal text. This serves as an escape hatch to avoid syntax collisions when using a template language meant to be rendered on the client, not the server.

This repo is just a package for PyPI, original code:
https://gist.github.com/629508 (w/ permission)

Django v1.5 should have compatible code included:
https://code.djangoproject.com/ticket/14502

Quickstart
---
Install using `pip`:

    $ pip install django-verbatim

Use in template:

    {% load verbatim %}

    {% verbatim %}

    My name is {{ name }}.

    {% endverbatim %}

Documentation
---
None (except quickstart).

Support and updates
---
You can contact me directly at aljosa.mohorovic@gmail.com, track updates at https://twitter.com/maljosa or use github issues.
Be persistent and bug me, I often find myself lost in time so ping me if you're still waiting for me to answer.

License
---
MIT (see LICENSE)
