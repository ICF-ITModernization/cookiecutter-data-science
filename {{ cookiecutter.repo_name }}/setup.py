from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
    install_requires=[
        "python-dotenv>=0.14.0",
        "sqlalchemy>=1.3.19",
        "pyodbc>=4.0.30",
    ],
    extras_require={
        "tests": "pytest>=6.0.2",
    },
)
