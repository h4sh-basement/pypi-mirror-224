from setuptools import setup, find_packages

setup(
    name='hnu_quant_db',
    version='0.0.11',
    description='HNU Quant Association Database Query Tool',
    author='rikkaka',
    author_email='793329010@qq.com',
    
    packages=find_packages(),
    
    exclude_package_data={
        '': ['*.pyc', '*.pyo', '*.pyd'],
        'private': ["token"]
    },
    
    install_requires=[
        'pandas',
        'sqlalchemy',
        'psycopg2-binary'
    ],
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
    ],
)
    