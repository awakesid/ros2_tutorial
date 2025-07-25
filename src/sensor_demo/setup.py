from setuptools import find_packages, setup

package_name = 'sensor_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='awakesid',
    maintainer_email='youcrashall@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_reader = sensor_demo.sensor_reader:main',
        'led_controller = sensor_demo.led_controller:main',
        ],
    },
)
