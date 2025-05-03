from setuptools import find_packages, setup

setup(name ="agentic-trading-system",
version = "0.0.1",
author= "Monika",
author_email= "moni_764@yahoo.com"
packages=find_packages(),
install_requires=['lancedb', 'langchain', 'langgraph', 'tavily-python', 'plygon']
)