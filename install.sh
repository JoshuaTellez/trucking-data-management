set -e
set -x

sudo apt-get install python3-venv

python3 -m venv tdm-env
source tdm-env/bin/activate
pip install -r pip_requirements.txt
