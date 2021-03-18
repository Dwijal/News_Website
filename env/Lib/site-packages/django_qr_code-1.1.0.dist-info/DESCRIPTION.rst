This application provides tools for displaying QR codes on your `Django <https://www.djangoproject.com/>`_ site.

This application depends on the `qrcode <https://github.com/lincolnloop/python-qrcode>`_ python library which requires the `Pillow <https://github.com/python-pillow/Pillow>`_ library in order to support PNG image format. The Pillow library needs to be installed manually if you want to generate QR codes in PNG format; otherwise, only SVG is format is supported.

This app makes no usage of the Django models and therefore do not use any database.

Only Python >= 3.5 is supported.

