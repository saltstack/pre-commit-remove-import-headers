from setuptools import setup

setup(
    name='pre-commit-remove-import-headers',
    version='1.0.0',
    packages=["remove_import_headers"],
    entry_points={
        "console_scripts": [
            "remove-import-headers = remove_import_headers.main:main"
        ]
    }
)
