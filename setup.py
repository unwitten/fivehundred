from setuptools import setup, find_packages

version = "0.1.0.dev0"

requirements = [
]

entry_points = {
    'console_scripts': [
        # 'fivehundred = fivehundred.main:main',
    ]
}

setup(
    name="fivehundred",
    version=version,
    packages=find_packages(exclude=['tests']),
    description="An implementation of the card game Five Hundred in Python",
    author='unwitten, kyluca',
    license="MIT",
    url="https://github.com/unwitten/fivehundred",
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    entry_points=entry_points,
    package_data={
        'fivehundred': [],
    },
    data_files=[
    ],
)
