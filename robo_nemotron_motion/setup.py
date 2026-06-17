import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'robo_nemotron_motion'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[xml|py]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='User',
    author_email='user@test.com',
    maintainer='User',
    maintainer_email='user@test.com',
    description='Motion package for robo_nemotron',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'trajectory_generator = robo_nemotron_motion.trajectory_generator:main',
        ],
    },
)
