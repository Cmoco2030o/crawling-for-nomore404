from setuptools import setup, find_packages

setup(
    name='no404vj-wordpress',
    version='0.1.4',
    author='Kenji Nagahashi',
    author_email='kenji@archive.org',
    description=("application to read wordpress update feed and schedule"
                 " permalink to crawler"),
    #packages=find_packages(),
    scripts=['process-firehose.py'],
    install_requires=[
        # requires libevent
        'gevent>=0.13.6',
        ]
    )
