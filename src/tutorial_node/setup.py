from setuptools import find_packages, setup

package_name = 'tutorial_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/tutorial_node/launch', ['launch/pub_sub_launch.py']),
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
        'publisher_node = tutorial_node.publisher_node:main',
        'subscriber_node = tutorial_node.subscriber_node:main',
        ],
    },
)
