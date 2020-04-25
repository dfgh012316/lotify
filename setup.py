import re
from os import path

from setuptools import setup, find_packages

version_file = path.join(
    path.dirname(__file__),
    'line_notify',
    '__version__.py'
)
with open(version_file, 'r') as fp:
    m = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        fp.read(),
        re.M
    )
    version = m.groups(1)[0]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='line-notify',
    version=version,
    description='Using Line Notify more easily',
    url='https://github.com/louis70109/line-notify',
    author='NiJia Lin',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='louis70109@gmail.com',
    keywords='line notify python',
    license='MIT',
    platforms='any',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests==2.22.0'
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    zip_safe=False,
    project_urls={
        'Bug Reports': 'https://github.com/louis70109/line-notify/issues',
        'Source': 'https://github.com/louis70109/line-notify',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
