from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='aquaaristonremotethermo',
    version='1.0.49',
    description='Aqua Ariston NET Remotethermo integration',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Oleh Pashchuk',
    author_email='chomu.nattsol@gmail.com',
    keywords=['Ariston NET', 'Remotethermo', 'Ariston'],
    url='https://github.com/chomupashchuk/aquaariston-remotethermo-api',
    download_url='https://pypi.org/project/aquaaristonremotethermo/'
)

install_requires = [
    'requests'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
