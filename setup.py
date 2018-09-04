from setuptools import setup


setup(name='slurm_cloudwatch',
      version='1.0.0',
      packages=['slurm_cloudwatch'],
      entry_points={
          'console_scripts': [
              'slurm_cloudwatch = slurm_cloudwatch.__main__:main'
              ]
      },
      install_requires=['boto3>=1.7.79'],
      zip_safe=False
      )
