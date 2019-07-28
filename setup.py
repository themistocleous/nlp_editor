# -*- coding: utf-8 -*-
from setuptools import setup

APP = ['main.py']
APP_NAME = "Natural Language Processing"
DATA_FILES = []

OPTIONS = {'argv_emulation': True}
setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
