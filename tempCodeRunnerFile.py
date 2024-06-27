import os
import subprocess

# Install dependencies from requirements.txt
subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

# Run Streamlit application
os.system('streamlit run build/UI.py')