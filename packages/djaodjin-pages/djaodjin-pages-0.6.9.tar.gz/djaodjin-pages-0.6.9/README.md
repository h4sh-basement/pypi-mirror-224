djaodjin-pages is a Django application that allow live templates edition
and upload templates packages.

Major Features:

- Text edition (optional: markdown syntax)
- Media gallery (drag'n'drop in markdown or media placeholder)
- Upload template packages

Development
===========

After cloning the repository, create a virtualenv environment, install
the prerequisites, create the database then run the testsite webapp.

<pre><code>
    $ virtualenv <em>installTop</em>
    $ source <em>installTop</em>/bin/activate
    $ pip install -r testsite/requirements.txt
    $ make vendor-assets-prerequisites

    $ make initdb

    $ python manage.py runserver

    # Browse http://localhost:8000/
    # Start edit live templates

</code></pre>


Release Notes
=============

Tested with

- **Python:** 3.7, **Django:** 3.2 ([LTS](https://www.djangoproject.com/download/))
- **Python:** 3.10, **Django:** 4.2 (latest)
- **Python:** 2.7, **Django:** 1.11 (legacy) - use testsite/requirements-legacy.txt

0.6.9

  * adds tags into practice description
  * compatibles with Bootstrap5
  * publishes distribution using pyproject.toml

[previous release notes](changelog)

Version 0.4.3 is the last version that contains the HTML templates
online editor. This functionality was moved to [djaodjin-extended-templates](https://github.com/djaodjin/djaodjin-extended-templates/)
as of version 0.5.0.
