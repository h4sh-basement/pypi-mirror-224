from distutils.core import setup
setup(
  name = 'TearRouting',         # How you named your package folder (MyLib)
  packages = ['TearRouting'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Trainable, efficient, autonomous routing.',   # Give a short description about your library
  author = 'John Kessler',                   # Type in your name
  author_email = 'johncolekessler@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/kesile/tear',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kesile/tear/archive/refs/tags/publish.tar.gz',    # I explain this later on
  keywords = ['OpenAI', 'Routing', 'Router'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'openai',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)