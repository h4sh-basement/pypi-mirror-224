name: Unit tests

on:
  push:
    branches: [ '**' ]

jobs:
  linting:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python 3.11
        uses: actions/setup-python@v3
        with:
          python-version: "3.11"

      - name: Install required packages
        run: pip install pre-commit

      - name: Run pre-commit hooks
        run: pre-commit run --all-files --hook-stage push

  build:
    name: Python ${% raw %}{{ matrix.python-version }}{% endraw %}, django ${% raw %}{{ matrix.django-version }}{% endraw %}
    runs-on: ubuntu-22.04
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', '3.11']
        django-version: [22, 30, 31, 32, 40, 41, 42]

        exclude:
          - python-version: '3.11'
            django-version: 40
          - python-version: '3.11'
            django-version: 32
          - python-version: '3.10'
            django-version: 32
          - python-version: '3.11'
            django-version: 31
          - python-version: '3.10'
            django-version: 31
          - python-version: '3.11'
            django-version: 30
          - python-version: '3.10'
            django-version: 30
          - python-version: '3.11'
            django-version: 22
          - python-version: '3.10'
            django-version: 22

    steps:
      - uses: actions/checkout@v3
      - name: setup python
        uses: actions/setup-python@v3
        with:
          python-version: ${% raw %}{{ matrix.python-version }}{% endraw %}
      - name: Install tox
        run: pip install tox
      - name: Run Tests
        env:
          TOXENV: django${% raw %}{{ matrix.django-version }}{% endraw %}
        run: tox
