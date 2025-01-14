# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['azpipeline', 'azpipeline.libs']

package_data = \
{'': ['*']}

install_requires = \
['azure-devops>=7.1.0b3,<8.0.0']

setup_kwargs = {
    'name': 'azpipeline',
    'version': '0.0.1',
    'description': 'Interact with azure pipelines using python',
    'long_description': "# azpipeline\n\n[![PyPI](https://img.shields.io/pypi/v/azpipeline?style=flat-square)](https://pypi.python.org/pypi/azpipeline/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/azpipeline?style=flat-square)](https://pypi.python.org/pypi/azpipeline/)\n[![PyPI - License](https://img.shields.io/pypi/l/azpipeline?style=flat-square)](https://pypi.python.org/pypi/azpipeline/)\n\n\n---\n\n**Documentation**: [https://azpipeline.readthedocs.io/en/latest/](https://azpipeline.readthedocs.io/en/latest/)\n\n**Source Code**: [https://github.com/nidhaloff/azpipeline](https://github.com/nidhaloff/azpipeline)\n\n**PyPI**: [https://pypi.org/project/azpipeline/](https://pypi.org/project/azpipeline/)\n\n---\n\nInteract with azure pipelines using python\n\n## Installation\n\n```sh\npip install azpipeline\n```\n\n## Development\n\n* Clone this repository\n* Requirements:\n  * [Poetry](https://python-poetry.org/)\n  * Python 3.7+\n* Create a virtual environment and install the dependencies\n\n```sh\npoetry install\n```\n\n* Activate the virtual environment\n\n```sh\npoetry shell\n```\n\n### Testing\n\n```sh\npytest\n```\n\n### Documentation\n\nThe documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings\n of the public signatures of the source code. The documentation is updated and published as a [Github project page\n ](https://pages.github.com/) automatically as part each release.\n\n### Releasing\n\nTrigger the [Draft release workflow](https://github.com/nidhaloff/azpipeline/actions/workflows/draft_release.yml)\n(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.\n\nFind the draft release from the\n[GitHub releases](https://github.com/nidhaloff/azpipeline/releases) and publish it. When\n a release is published, it'll trigger [release](https://github.com/nidhaloff/azpipeline/blob/master/.github/workflows/release.yml) workflow which creates PyPI\n release and deploys updated documentation.\n\n### Pre-commit\n\nPre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality\n checks to make sure the changeset is in good shape before a commit/push happens.\n\nYou can install the hooks with (runs for each commit):\n\n```sh\npre-commit install\n```\n\nOr if you want them to run only for each push:\n\n```sh\npre-commit install -t pre-push\n```\n\nOr if you want e.g. want to run all checks manually for all files:\n\n```sh\npre-commit run --all-files\n```\n",
    'author': 'Nidhal Baccouri',
    'author_email': 'nidhalbacc@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://nidhaloff.github.io/azpipeline',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
