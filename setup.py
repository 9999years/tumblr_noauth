from setuptools import setup, find_packages
from codecs import open
from os import path

long_description = 'https://github.com/9999years/tumblr_noauth'
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tumblr_noauth',
    version='0.1.0',
    description='A sneaky Tumblr API',
    url='https://github.com/9999years/tumblr_noauth',
    author='Rebecca Turner',
    author_email='637275@gmail.com',
    license='AGPL-3.0',

    long_description=long_description,
    long_description_content_type='text/markdown',

    # See https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3',
    ],

    keywords='tumblr api',

    packages=find_packages(),

    # Run-time dependencies
    install_requires=['requests', 'beautifulsoup4'],
)
