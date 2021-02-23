from setuptools import setup, find_namespace_packages


description = """Utilities for the sphinx-kentigern theme."""
author = "Daniel Williams"
author_email = "mail@daniel-williams.co.uk"


with open("requirements.txt") as requires_file:
    requirements = requires_file.read().split("\n")

requirements = [requirement for requirement in requirements if not ("+" in requirement)]



setup(
    name='kentigern-ext',
    description=description,
    author=author,
    author_email=author_email,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_namespace_packages(include=['mynamespace.*']),
    zip_safe=True
)
