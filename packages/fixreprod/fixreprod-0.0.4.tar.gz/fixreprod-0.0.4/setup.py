import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fixreprod",
    version="0.0.4",
    author="yoshiyasu takefuji",
    author_email="takefuji@keio.jp",
    description="A package for showing all seeds to be fixed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ytakefuji/fixreprod",
    project_urls={
        "Bug Tracker": "https://github.com/ytakefuji/fixreprod",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['fixreprod'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    entry_points = {
        'console_scripts': [
            'fixreprod = fixreprod:main'
        ]
    },
)
