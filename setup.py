try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="async_foaas",
    version="0.3.0",
    description="Fuck Off As A Service",
    license="MIT",
    url="https://github.com/alexraskin/foaas-python",
    author="Alex Raskin",
    author_email="root@alexraskin.com",
    py_modules=["async_foaas"],
    install_requires=["httpx", "async-property"],
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
    ),
)
