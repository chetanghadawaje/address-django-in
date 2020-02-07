from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='address-django-in',
    version='0.0.1',
    description='Address Package',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
            'Development Status :: Production/Stable',
            'Environment :: Web',
            'License :: MIT License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
    ],
    url='',
    author='Chetan Ghadawaje',
    author_email='chetanghadawaje@gmail.com',
    keywords='',
    license='MIT',
    packages=['address-django-in'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)
