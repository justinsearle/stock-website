This is our python flask/connexion backend API to use for the stock website.

Useful commands:
pip install pipenv
python app.py
pipenv run python app.py
docker build --tag stonksback:1.0 .
docker run -d -p 8000:8000 --name stonks stonksback:1.0