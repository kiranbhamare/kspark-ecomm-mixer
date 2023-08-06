# kspark-ecomm-mixer
# To create virtual environ
python -m venv .venv
# to activate virtual envron (run below command by command line)
.venv\Scripts\activate

# to install requirements
pip install -r requirements.txt

# to run the python script
uvicorn main:app --reload