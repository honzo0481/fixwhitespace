from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='fixwhitespace',
      description='Fix whitespace in files',
      long_description=readme(),
      url='https://github.com/honzo0481/whitespace',
      author='honzo0481',
      author_email='gonzalesre@gmail.com',
      license='MIT',
      packages=['fixwhitespace'],
      include_package_data=True,
      entry_points={
        'console_scripts': [
            'trim=fixwhitespace.fixwhitespace:cli.trim',
            'tabs2spaces.fixwhitespace:cli.tabs2spaces'
            ]
      },
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      version='0.1',
      zip_safe=False,
      )
