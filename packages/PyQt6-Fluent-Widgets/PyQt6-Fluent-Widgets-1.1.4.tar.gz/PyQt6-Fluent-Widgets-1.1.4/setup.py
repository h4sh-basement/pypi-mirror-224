import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="PyQt6-Fluent-Widgets",
    version="1.1.4",
    keywords="pyqt6 fluent widgets",
    author="zhiyiYo",
    author_email="shokokawaii@outlook.com",
    description="A fluent design widgets library based on PyQt6",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPLv3",
    url="https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PyQt6",
    packages=setuptools.find_packages(),
    install_requires=[
        "PyQt6>=6.3.1",
        "PyQt6-Frameless-Window>=0.3.1",
        "darkdetect",
    ],
    extras_require = {
        'full': ['scipy', 'pillow<=9.4.0', 'colorthief']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'Documentation': 'https://pyqt-fluent-widgets.readthedocs.io/',
        'Source Code': 'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PyQt6',
        'Bug Tracker': 'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/issues',
    }
)
