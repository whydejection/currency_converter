from setuptools import setup, find_packages

setup(
    name='main',
    version='0.0.1',
    packages=find_packages("../cource"),
    scripts=["bin/main"],
    url='https://github.com/whydejection/currency_converter',
    license='Apache-2.0',
    author='Lysenko Gleb Vladimirovich',
    author_email='lysenko.gv@edu.spbstu.ru',
    description='Пакет на Python для работы c валютами',
    include_package_data=True,
    install_requires=[
        'tabulate>=0.8.9',
    ],

)
