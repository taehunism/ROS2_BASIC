from setuptools import setup

package_name = 'basic_code'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='unicon',
    maintainer_email='ktaeh524@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'topic_publish = basic_code.topic_publish:main',
            'topic_subscribe = basic_code.topic_subscribe:main',
        ],
    },
)
