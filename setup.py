from setuptools import setup, find_packages
from codecs import open
from os import path

import EasyImgConverter

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

req_path = path.join(here, 'requirements.txt')
with open(req_path, "r") as f:
    install_reqs = f.read().strip()
    install_reqs = install_reqs.split("\n")

setup(
    name='EasyImgConverter',
    version=EasyImgConverter.__version__,
    description='Python tool for easy and quick conversion of images between different formats.',
    long_description=long_description,
    url='https://github.com/alzaia/easy_img_converter',
    author='Aldo Zaimi',
    author_email='zaimialdo@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=install_reqs,
    package_dir={'EasyImgConverter': 'EasyImgConverter'},
    package_data={"EasyImgConverter": ['data_test/*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'easy_img_converter = EasyImgConverter.main:main'
        ],
    },
)