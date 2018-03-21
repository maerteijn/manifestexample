from setuptools import find_packages, setup

__version__ = "0.0.1"


setup(
    name='manifestexample',
    version=__version__,
    description=(
        "A manifest example to show that excluding files is not working "
        "with build / bdist / bdist_wheel"
    ),
    classifiers=[],
    keywords='',
    author='Martijn Jacobs',
    author_email='martijn@devopsconsulting.nl',
    url='https://github.com/maerteijn/manifestexample',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'wheel'
    ],
    entry_points={
        'console_scripts': [
            'manifest = manifestexample.cmd:command',
        ]
    },

)
