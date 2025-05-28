from setuptools import setup, find_packages

setup(
    name='jamaica_pto',
    version='0.0.1',
    description='Jamaica PTO Custom App',
    author='Ankit',
    author_email='loharankit08@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe'],
)
