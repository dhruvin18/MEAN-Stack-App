#setup virtual environment env
py venv env
.\env\Scripts\activate

pip install -r requirements.txt

git clone https://github.com/LexPredict/lexpredict-lexnlp.git
cd lexpredict-lexnlp
py setup.py install

py -m spacy download en_core_web_sm
