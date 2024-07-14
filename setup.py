from setuptools import setup, find_packages

setup(
    name='soti_mobicontrol_api',
    version='0.1.0',
    description='A Python wrapper for the SOTI MobiControl API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Bo Snitkjaer Nielsen',
    author_email='snitkjaer@gmail.com',
    url='https://github.com/snitkjaer/soti-mobicontrol-python',
    packages=find_packages(),
    install_requires=[
        'requests',  # Add other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers'
    ],
    python_requires='>=3.6',
)
