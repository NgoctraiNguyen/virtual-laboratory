#!/bin/bash

# This script sets up the virtual environment and runs the Virtual Laboratory app

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Run the main application
python src/main.py