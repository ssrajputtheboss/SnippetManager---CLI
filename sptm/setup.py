from setuptools import setup , find_packages

def get_requirements():
    with open('requirements.txt' , 'r') as f:
        return f.read().split('\n')


setup(
    name = 'sptm',
    version = '0.1',
    packages = find_packages(),
    include_package_data = True,
    install_requires = get_requirements(),
    entry_points = '''
    [console_scripts]
    sptm=sptm.cli:cli
    '''
)