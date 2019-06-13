from setuptools import setup, find_packages

setup(
    name='django_pmedien_export',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='General export for a complete model with languages',
    long_description=open('README.md').read(),
    install_requires=['django'],
    url='http://www.pmedien.com',
    author='pmedien GmbH',
    author_email='nomail@pmedien.com'
)