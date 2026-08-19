from setuptools import setup, find_packages

NAME = "nexussim_server"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion[swagger-ui,uvicorn]>=2.0.2, <3",
    "python-dateutil>=2.6.0",
    "Flask>=2.1.1, <2.3",
    "pint>=0.24",
    "pytimeparse>=1.1"
]

TESTING = [
    "pytest>=8.3.5",
    "pytest-cov>=5.0.0",
    "pytest-mock>=3.14",
    "Flask-Testing>=0.8"
]

setup(
    name=NAME,
    use_scm_version=True,
    description="MIRTO DynAA API",
    author_email="coen.vanleeuwen@tno.nl",
    url="https://github.com/TNO/nexussim-server",
    keywords=["OpenAPI", "MIRTO DynAA API"],
    install_requires=REQUIRES,
    extras_require={"testing": TESTING},
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['nexussim_server=nexussim_server.__main__:main']},
    long_description="""\
    This API offers an interface to the DynAA service. It takes descriptions of application service chains, and provides simulation results on the system performance
    """
)

