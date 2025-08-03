#!/bin/bash

# Exit on error
set -e

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Build the mock data
echo "Building mock data..."
python3 main.py

# Start the web server
echo "Starting web server..."
echo "Please navigate to: http://localhost:8000/index.html"
python3 -m http.server

# Deactivate virtual environment
deactivate
