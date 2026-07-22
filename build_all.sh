#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "=== 1. Cleaning old build artifacts ==="
jupyter-book clean .

echo "=== 2. Building standard HTML website ==="
jupyter-book build .

echo "=== 3. Generating full book PDF ==="
python3 generate_pdf.py

echo "=== Build Process Completed Successfully! ==="
