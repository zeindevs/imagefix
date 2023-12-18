from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='imagefix',
    version='0.0.1',
    description='Image Fixer CLI application.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Image :: Image Processing',
    ],
    keywords='imagefix',
    url='https://github.com/zeindevs/imagefix',
    author='zeindevs',
    author_email='zeindevs@gmail.com',
    license='MIT',
    packages=['imagefix'],
    zip_safe=False,
    scripts=['bin/imagefix'],
    entry_points={
        'console_scripts': ['imagefix=imagefix.command_line:main']
    }
)
