from setuptools import setup, find_packages


setup(
    name='simple-ml-datastore-fetcher',
    version='1.0',
    author='Anikin Denis',
    author_email='ad@xfenix.ru',
    packages=find_packages(),
    install_requires = [
        'requests==2.22.0',
    ]
)
