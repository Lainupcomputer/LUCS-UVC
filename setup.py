# setup.py
from setuptools import setup, find_packages

setup(
    name='uvc',
    version='0.1.0.0',
    author='Sandro Kalett',
    author_email='sandrokalett@lainupcomputersolution.de',
    description='A version checking utility',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Lainupcomputer/vcs',  # Ersetze dies durch die URL deines Repositories
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
