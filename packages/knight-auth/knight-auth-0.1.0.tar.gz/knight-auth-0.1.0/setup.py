from setuptools import setup, find_packages

setup(
    name="knight-auth",
    version="0.1.0",
    description='Authentication for django-ninja, KNOX inspired',
    url='https://github.com/knightSarai/knight-auth',
    author='knightSarai',
    author_email='knight.sarai.dev@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Framework :: Django',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
    ],
    packages=find_packages(exclude=['core']),
    python_requires='>=3.11.4',
    install_requires=[
        'django>=4.2.4',
        'django-ninja>=0.22.2'
    ],
    extras_require={
        "dev": ["twine>=4.0.2"],
    }
)
