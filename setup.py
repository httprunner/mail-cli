import os
import re

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'jenkins_mail_py', '__init__.py')) as f:
    version = re.compile(r"__version__\s+=\s+'(.*)'", re.I).match(f.read()).group(1)

with open('README.md') as f:
    long_description = f.read()

setup(
    name='jenkins-mail-py',
    version=version,
    description="Encapsulation for email senders, include mailgun service and SMTP mailer.",
    long_description=__doc__,
    author="Leo Lee",
    author_email='mail@debugtalk.com',
    url='https://github.com/debugtalk/jenkins-mail-py.git',
    packages=[
        'jenkins_mail_py',
    ],
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords='Email STMP Mailgun',
    classifiers=[
        'Development Status :: 4 - Beta',
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
