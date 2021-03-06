import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()


PACKAGE = 'code_reflector'
VERSION = '0.1.0'


def _get_requires(filepath):
    path = '{}/{}'.format(os.path.abspath(os.path.dirname(__file__)), filepath)
    with open(path) as reqs:
        return [req for req in reqs.read().split('\n') if req]

keywords = ['codereflector', 'code', 'html2css', 'css2html', 'htmlparser',
            'cssparser', 'pyquery', 'tinycss', 'css', 'stylesheet', 'html',
            'parser', 'cssparser']
description = ('A suite of python tools to parse and transform web formats '
               '(css/html, etc...), for web applications and automation')
setup(
    name='code_reflector',
    version=VERSION,
    description=description,
    author='Chris Tabor',
    author_email='dxdstudio@gmail.com',
    maintainer='Chris Tabor',
    maintainer_email='dxdstudio@gmail.com',
    url='https://github.com/christabor/codeReflector',
    keywords=keywords,
    license='Apache License 2.0',
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=_get_requires('requirements.txt'),
    setup_requires=[
        'setuptools>=0.8',
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ]
)
