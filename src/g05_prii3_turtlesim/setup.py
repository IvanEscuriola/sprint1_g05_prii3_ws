from glob import glob
import os

from setuptools import setup

package_name = 'g05_prii3_turtlesim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py'),
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ivan',
    maintainer_email='exarx444@gmail.com',
    description='Dibujo del 0 del grupo G05 con ROS 2 y turtlesim',
    license='TODO= License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dibujar_0 = g05_prii3_turtlesim.dibujar_0:main',
        ],
    },
)
