from setuptools import setup, find_packages

setup(
    name = 'pyonemap',
    version = '0.2.0',
    packages = find_packages(),
    install_requires = [
        'requests',
    ],
    author = 'Teo Cheng Guan',
    author_email = 'chengguan.teo@gmail.com',
    description = 'A Python package for interacting with OneMap API',
    url = 'https://github.com/yourusername/pyonemap',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
