# -*- coding:utf-8 -*-

from setuptools import setup

setup(
    name='neishaprocessing',
    version='0.1',
    packages=['','DB','model','service','util'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['mongoengine','tornado']
)