from setuptools import setup, find_packages

setup(
    name='ptt-follower',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'urwid',
        'beautifulsoup4',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        ptt-follower=src.core:App
    ''',
)
