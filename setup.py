import os

from pip.req import parse_requirements
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
install_reqs = parse_requirements("requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='djabout',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
    license='MIT License',
    description='Add a / about endpoint to your app to show some components\' health',
    long_description=README,
    author='Mattia Procopio',
    author_email='promat85@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: End users',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
