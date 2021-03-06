import logging

from flask import Flask

from metadataproxy import settings

log = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(settings)
app.debug = app.config['DEBUG']

if app.config['MOCK_API']:
    from metadataproxy.routes import mock  # NOQA
else:
    from metadataproxy.routes import proxy  # NOQA
