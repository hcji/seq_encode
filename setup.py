from setuptools import setup, find_packages

setup(name='seq_encode',
      version='0.0.2',
      description='Convert SMILES to one hot matrix',
      license='MIT',
      author='Ji Hongchao',
      author_email='ji.hongchao@foxmail.com',
      url='https://github.com/hcji/seq_encode',
      packages=find_packages(),
	  classifiers=[
	  'Development Status :: 4 - Beta',
	  'Programming Language :: Python :: 3.6',
	  'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8'
	  ]
     )