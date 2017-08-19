from setuptools import setup
from setuptools import find_packages

setup(name='gym_mazeexplorer',
    version='0.0.7',
    author='Mr-Yellow',
    author_email='mr-yellow@mr-yellow.com',
    description='A maze exploration environment for openai/gym',
    packages=find_packages(),
    url='https://github.com/mryellow/gym-mazeexplorer',
    license='MIT',
    install_requires=['gym', 'mazeexp'],
    keywords='maze, game, maze-explorer, openaigym, openai-gym',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)


#package_dir={'gym_mazeexplorer' : 'gym_mazeexplorer/envs'},
