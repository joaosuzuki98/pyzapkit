from setuptools import find_packages, setup
from os import path


root_path = path.abspath(path.dirname(__file__))

with open(path.join(root_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyzapkit',
    packages=find_packages(include=['pyzapkit']),
    version='0.1.0',
    description='Automatically send Whatsapp messages and files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='João Suzuki',
    license='MIT',
    install_requires=[
        'selenium',
        'PyAutoGUI',
    ],
    url='https://github.com/joaosuzuki98/pyzapkit',
    keywords='Automation, Whatsapp',
)
