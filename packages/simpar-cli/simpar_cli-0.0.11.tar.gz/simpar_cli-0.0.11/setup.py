#!/usr/bin/env python
from setuptools import setup



with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='simpar_cli',
    version='0.0.11',
    packages=['simpar_cli'],
    # install_requires=[
    #     'numpy', 'argparser', 'matplotlib', 'scikit-image', 'opencv_python'
    # ],
    license='MIT license',
    description="simple cli for paragraphe recognition",
    long_description= long_description,
    long_description_content_type="text/markdown",

    
    url='https://github.com/darixsamani/simpar_cli',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],    
    python_requires='>=3.6',                
    py_modules=["simpar_cli"],             
    package_dir={'':'./src'},     
    install_requires=['contourpy==1.1.0',
'cycler==0.11.0',
'fonttools==4.42.0',
'imageio==2.31.1',
'importlib-resources==6.0.1',
'kiwisolver==1.4.4',
'lazy_loader==0.3',
'matplotlib==3.7.2',
'networkx==3.1',
'numpy==1.25.2',
'opencv-python==4.8.0.74',
'packaging==23.1',
'Pillow==10.0.0',
'pyparsing==3.0.9',
'python-dateutil==2.8.2',
'PyWavelets==1.4.1',
'scikit-image==0.21.0',
'scipy==1.11.1',
'six==1.16.0',
'tifffile==2023.7.18',
'zipp==3.16.2'],

    entry_points={
        'console_scripts': [
            'simpar_cli = simpar_cli:main',
        ]
    }             
)
