import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'pami',
    version = '2023.08.04',
    author = 'Takahiro Yokoi',
    author_email = 's1270147@u-aizu.ac.jp',
    description = 'This softwear is being developed at the University of Aizu, Aizu-Wakamatsu, Fukushima, Japan',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    url = 'https://github.com/TakahiroYokoi/s1270147_learn',
    license = 'GPLv3',
    install_requires=[
        'psutil',
        'pandas',
        'plotly',
        'matplotlib',
        'resource',
        'validators',
        'urllib3',
        'Pillow',
        'numpy',
    ],
    extras_require={
        'gpu':['cupy', 'pycuda'],
        'spark':['pyspark'],
        'dev':['twine', 'setuptools', 'build'],
        'all':['cupy', 'pycuda', 'pyspark', 'twine', 'setuptools', 'build']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Lamguage :: Python :: 3',
        'License :: OSI Approved :: GUN General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires = '>=3.5',
)