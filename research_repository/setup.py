# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in research_repository/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('research_repository/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='research_repository',
	version=version,
	description='A web based application to maintain the records related to research contribution of all faculty members in an institute, as a measure of research outcome',
	author='of the institute as a whole, departments and individual faculty member:ssn',
	author_email='sasirekhas@ssn.edu.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
