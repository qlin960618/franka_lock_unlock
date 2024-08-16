import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'franka_lock_unlock'

setup(
    name=package_name,
    version='4.2.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jk-ethz',
    maintainer_email='ethz@juliankeller.net',
    description='Lock or unlock the Franka Emika Panda joint brakes programmatically.',
    license='AGPLv3',
    entry_points={
        'console_scripts': [
            'run = franka_lock_unlock.run:main'
        ],
    },
)
