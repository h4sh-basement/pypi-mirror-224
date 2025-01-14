from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='luckywood',
    version='0.6.1',
    description='Package of helper classes.',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='LGPL-3.0',
    packages=find_packages(),
    author='Frederik Glücks, Christian Wald-von der Lahr',
    author_email='frederik@gluecks-gmbh.de, christian@waldvonderlahr-it.de',
    keywords=[],
    url='https://github.com/gluecks-gmbh/luckywood',
    download_url='https://pypi.org/project/luckywood/',
    python_requires='>=3.8'
)

install_requires = [
    "mysql-connector-python~=8.1.0",
    "requests~=2.31.0",
    "boto3==1.28.25"
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
