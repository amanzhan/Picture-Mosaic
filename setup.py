from setuptools import setup

setup(
    name='PictureMosaic',
    version='0.1.0',
    packages=['PictureMosaic'],
    include_package_data=True,
    install_requires=[
        'arrow==0.15.5',
        'bs4==0.0.1',
        'Flask==1.1.1',
        'nodeenv==1.3.5',
        'requests==2.22.0',
        'selenium==3.141.0',
        'sh==1.12.14',
        'Pillow==8.1.1',
        'numpy==1.18.3',
        'progressbar2==3.51.3',
    ],
    entry_points={
        'console_scripts': [
            'PictureMosaic = PictureMosaic.__main__:main'
        ]
    },

)
