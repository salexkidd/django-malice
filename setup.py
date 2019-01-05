from setuptools import setup


setup(
    name='django-malice',
    author = "salexkidd",
    author_email = "salexkidd@gmail.com",
    url = "https://github.com/salexkidd/django_malice/",
    description='A simple Django app that enables own occuring error.',
    keywords = ["django", "testing",],
    version='0.1.5',
    packages=['malice'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
