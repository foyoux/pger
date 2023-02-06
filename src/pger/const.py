import os
from pathlib import Path

MANIFEST = 'MANIFEST.in'
PYPROJECT = 'pyproject.toml'
PUBLISH = 'python-publish.yml'
README = 'README.md'
REQUIREMENTS = 'requirements.txt'
STARTED = 'started-notify.yml'
UPDATE = 'update-version.py'
MAIN = '__main__.py'
INIT = '__init__.py'
TEMPLATES = 'templates'

templates = Path(os.path.join(os.path.dirname(__file__), TEMPLATES))
