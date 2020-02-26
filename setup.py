from setuptools import setup

setup(
        name='listen',   
        version='1.0', 
        description='An command line app to find where the song can be downloaded', 
        author='Weilet',
        author_email='weilet_sun@outlook.com', 
        install_requires=[
			'requests>=2.0.0'
    	],
    	packages=['listen', 'listen.search', 'listen.utils']
)