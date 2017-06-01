from setuptools import setup, find_packages

version = '0.2.1'

def do_setup():
    setup(
        name='pyxmex',
        description='Parse American Express EPTRN and CBNOT files',
        license='MIT',
        version=version,
        packages=find_packages(),
        zip_safe=False,
        install_requires=['pyyaml'],
        package_data={'': ['pyxmex/config/*.yml']},
        include_package_data=True,
        author='Rob Froetscher, Joyce Lau',
        author_email='rfroetscher@lumoslabs.com',
        url='https://github.com/lumoslabs/pyxmex',
        download_url=('https://github.com/lumoslabs/pyxmex/tarball/' + version)
    )

if __name__ == "__main__":
    do_setup()
