from setuptools import setup, find_packages

setup(
    name="maisaedu-utilities-prefect",
    version="1.1.1",
    description="Utilities for interaction with Prefect, for +A Education",
    license="MIT License",
    author="A+ Educação",
    author_email="dataeng@maisaedu.com.br",
    packages=find_packages(),
    scripts=[
        "maisaedu_utilities_prefect/scripts/refresh-secrets",
        "maisaedu_utilities_prefect/scripts/flow-mem-limit",
    ],
    install_requires=[
        "pandas",
        "scipy",
        "numpy",
        "wheel",
        "prefect",
        "papermill",
        "psycopg2-binary",
        "aiopg",
        "aiochannel",
        "gspread",
        "sshtunnel",
    ],  # external packages as dependencies
)
