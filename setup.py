from setuptools import setup


setup(
    name='cldfbench_szetosinitic',
    py_modules=['cldfbench_szetosinitic'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'szetosinitic=cldfbench_szetosinitic:Dataset',
        ]
    },
    install_requires=[
        'cldfbench[glottolog]',
        'lxml',
        'beautifulsoup4',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
