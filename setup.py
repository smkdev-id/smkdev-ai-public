from pathlib import Path
from setuptools import setup
from setuptools.command.install import install as _install
import subprocess

class CustomInstallCommand(_install):
  def run(self):
    subprocess.check_call(['python', 'install_dependencies.py'])
    _install.run(self)

directory = Path(__file__).resolve().parent
with open(directory / 'README.md', encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='smkdev-ai-public',
  version='1.0',
  description='AI Development and Prompt Engineering Guide for SMKDEV Community. Claude 3, GPT-4, Gemini, RAG, n8n',
  author='SMKDEV',
  license='MIT',
  long_description=long_description,
  long_description_content_type='text/markdown',
  install_requires=["langchain", "langgraph"],
  extras_require={
    'linting':["nbqa[toolchain]", "pre-commit"],
    'docs':["mkdocs-material", "mkdocstrings[python]", "markdown-callouts", "markdown-exec[ansi]", "black"]
  },
  cmdclass={'install': CustomInstallCommand,},
  entry_points={"console_scripts": ["my_script=my_python_project.main:main"]},
  include_package_data=True
)