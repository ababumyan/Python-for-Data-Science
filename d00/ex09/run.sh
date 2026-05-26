#!/bin/bash
if [ -d "venv" ]; then
    echo "Virtual environment already exists"
    source venv/bin/activate
else
    echo "Creating virtual environment"
    python3 -m venv venv
    source venv/bin/activate
fi

echo "Installing dependencies"
pip install --upgrade pip
pip install setuptools wheel
pip install -e .
python setup.py sdist bdist_wheel
pip install dist/*.whl
pip show -v ft_package