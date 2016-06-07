from setuptools import setup, find_packages

version = '0.0.7'

def do_setup():
    setup(
        name='pyxmex',
        description='Parse American Express EPTRN files',
        license='MIT',
        version=version,
        packages=find_packages(),
        zip_safe=False,
        install_requires=['pyyaml'],
        package_data={'': ['pyxmex/config/eptrn.yml']},
        include_package_data=True,
        author='Rob Froetscher',
        author_email='rfroetscher@lumoslabs.com',
        url='https://github.com/lumoslabs/pyxmex',
        download_url=('https://github.com/lumoslabs/pyxmex/tarball/' + version)
    )

if __name__ == "__main__":
    do_setup()
