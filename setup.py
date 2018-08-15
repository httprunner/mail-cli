import os
import re

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'mailcli.py')) as f:
    version = re.compile(r"__version__\s+=\s+'(.*)'", re.I).match(f.read()).group(1)

with open('README.md') as f:
    long_description = f.read()

setup(
    name='mail-cli',
    version=version,
    description="Encapsulation for email senders, include mailgun service and SMTP mailer.",
    long_description=__doc__,
    author="Leo Lee",
    author_email='mail@debugtalk.com',
    url='https://github.com/debugtalk/mail-cli.git',
    license="MIT license",
    keywords='Email STMP Mailgun',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
