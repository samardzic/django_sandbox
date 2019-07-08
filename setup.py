"""-----------------------------------------------------------
Created By       : Nenad Samardzic
License          : GNU GENERAL PUBLIC LICENSE Version 3,
Date:            : Jun 2019
Powered          : Python-3.7

-----------------------------------------------------------"""

from setuptools import setup, find_packages

setup(
    name='auditor_client',
    version='0.0.0',
    description='Auditor client package',
    # long_description=read('README.md'),
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'astroid>=2.2.5',
        'certifi>=2019.3.9',
        'chardet>=3.0.4',
        'colorama>=0.4.1',
        'Django>=2.2.3',
        'django-crispy-forms>=1.7.2',
        'django-filter>=2.1.0',
        'djangorestframework>=3.9.4',
        'docutils>=0.14',
        'idna>=2.8',
        'isort>=4.3.17',
        'lazy-object-proxy>=1.3.1',
        'Markdown>=3.1.1',
        'mccabe>=0.6.1',
        'mysql-connector>=2.2.9',
        'mysql-connector-python>=8.0.15',
        'mysql-connector-python-rf>=2.2.2',
        'mysqlclient>=1.4.2.post1',
        'pep8>=1.7.1',
        'Pillow>=6.1.0',
        'protobuf>=3.7.1',
        'pylint>=2.3.1',
        'pytz>=2019.1',
        'requests>=2.21.0',
        'six>=1.12.0',
        'sqlparse>=0.3.0',
        'typed-ast>=1.3.1',
        'urllib3>=1.24.1',
        'wrapt>=1.11.1',
        ],
    # extras_require={'dev': ['flake8', 'flake8-docstrings', 'pytest', 'coverage', 'tox']},
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)