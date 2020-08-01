from setuptools import setup, find_packages
name = "app"

setup(
    name=name,
    version="0.1",
    packages=find_packages(),
    package_data={'app': ['ui/web/static/**/*', 'ui/web/templates/*']},
    zip_safe=True,
    entry_points = {
        'console_scripts': [f'{name}-hello={name}:hello',
                            f'{name}-web={name}.ui.web.server:main'],
    }
)