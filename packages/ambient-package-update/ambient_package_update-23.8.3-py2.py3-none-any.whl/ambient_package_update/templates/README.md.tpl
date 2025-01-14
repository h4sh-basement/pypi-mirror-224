[![PyPI release](https://img.shields.io/pypi/v/{{ package_name|replace("_", "-") }}.svg)](https://img.shields.io/pypi/v/{{ package_name|replace("_", "-") }}.svg)
[![Downloads](https://pepy.tech/badge/{{ package_name|replace("_", "-") }})](https://pepy.tech/project/{{ package_name|replace("_", "-") }})
[![Documentation Status](https://readthedocs.org/projects/{{ package_name|replace("_", "-") }}/badge/?version=latest)](https://{{ package_name|replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest)

{{ readme_content.tagline }}

* [PyPI](https://pypi.org/project/{{ package_name|replace("_", "-") }}/)
* [GitHub](https://github.com/ambient-innovation/{{ package_name|replace("_", "-") }})
* [Full documentation](https://{{ package_name|replace("_", "-") }}.readthedocs.io/en/latest/index.html)
* Creator & Maintainer: [Ambient Digital](https://ambient.digital)

{{ readme_content.content }}

## Installation

{% if readme_content.installation %}
  {{ readme_content.installation }}
{% else %}
- Install the package via pip:

  `pip install {{ package_name|replace("_", "-") }}`

  or via pipenv:

  `pipenv install {{ package_name|replace("_", "-") }}`

- Add module to `INSTALLED_APPS` within the main django `settings.py`:

    ````
    INSTALLED_APPS = (
        ...
        '{{ package_name }}',
    )
     ````
{% endif %}

## Contribute

### Setup package for development

- Create a Python virtualenv and activate it
- Install "pip-tools" with `pip install pip-tools`
- Compile the requirements with `pip-compile --extra {% for area, dependency_list in optional_dependencies.items() %}{{ area }},{% endfor %} -o requirements.txt pyproject.toml --resolver=backtracking`
- Sync the dependencies with your virtualenv with `pip-sync`

### Add functionality

- Create a new branch for your feature
- Change the dependency in your requirements.txt to a local (editable) one that points to your local file system:
  `-e /Users/workspace/{{ package_name|replace("_", "-") }}` or via pip  `pip install -e /Users/workspace/{{ package_name|replace("_", "-") }}`
- Ensure the code passes the tests
- Create a pull request

### Run tests

- Run tests
  ````
  pytest --ds settings tests
  ````

### Git hooks (via pre-commit)

We use pre-push hooks to ensure that only linted code reaches our remote repository and pipelines aren't triggered in
vain.

To enable the configured pre-push hooks, you need to [install](https://pre-commit.com/) pre-commit and run once:

    pre-commit install -t pre-push -t pre-commit --install-hooks

This will permanently install the git hooks for both, frontend and backend, in your local
[`.git/hooks`](./.git/hooks) folder.
The hooks are configured in the [`.pre-commit-config.yaml`](templates/.pre-commit-config.yaml.tpl).

You can check whether hooks work as intended using the [run](https://pre-commit.com/#pre-commit-run) command:

    pre-commit run [hook-id] [options]

Example: run single hook

    pre-commit run ruff --all-files --hook-stage push

Example: run all hooks of pre-push stage

    pre-commit run --all-files --hook-stage push

### Update documentation

- To build the documentation run: `sphinx-build docs/ docs/_build/html/`.
- Open `docs/_build/html/index.html` to see the documentation.

### Translation files

If you have added custom text, make sure to wrap it in `_()` where `_` is
gettext_lazy (`from django.utils.translation import gettext_lazy as _`).

How to create translation file:

* Navigate to `{{ package_name|replace("_", "-") }}`
* `python manage.py makemessages -l de`
* Have a look at the new/changed files within `{{ package_name }}/locale`

How to compile translation files:

* Navigate to `{{ package_name|replace("_", "-") }}`
* `python manage.py compilemessages`
* Have a look at the new/changed files within `{{ package_name }}/locale`

### Publish to ReadTheDocs.io

- Fetch the latest changes in GitHub mirror and push them
- Trigger new build at ReadTheDocs.io (follow instructions in admin panel at RTD) if the GitHub webhook is not yet set
  up.

### Publish to PyPi

- Update documentation about new/changed functionality

- Update the `Changelog`

- Increment version in main `__init__.py`

- Create pull request / merge to master

- This project uses the flit package to publish to PyPI. Thus publishing should be as easy as running:
  ```
  flit publish
  ```

  To publish to TestPyPI use the following ensure that you have set up your .pypirc as
  shown [here](https://flit.readthedocs.io/en/latest/upload.html#using-pypirc) and use the following command:

  ```
  flit publish --repository testpypi
  ```

### Maintenance

Please note that this package supports the [ambient-package-update](https://pypi.org/project/ambient-package-update/).
So you don't have to worry about the maintenance of this package. All important configuration and setup files are
being rendered by this updater. It works similar to well-known updaters like `pyupgrade` or `django-upgrade`.

To run an update, refer to the [documentation page](https://pypi.org/project/ambient-package-update/)
of the "ambient-package-update".
