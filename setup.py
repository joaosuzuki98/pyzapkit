from setuptools import find_packages, setup

setup(
    name='pyzapkit',
    packages=find_packages(include=['pyzapkit']),
    version='0.1.0',
    description='Automatically send Whatsapp messages and files',
    author='João Suzuki',
    license='MIT',
    install_requires=[
        'selenium',
        'PyAutoGUI',
    ],
    url='https://github.com/joaosuzuki98/pyzapkit',
    keywords='Automation, Whatsapp',
)
