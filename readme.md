# WEC NITK GSDC Task ID: Web Scraper

<br>
<h2>Setting up the project:</h2>
<br>
<h3>Installing and using a Virtual Environment</h3>

`pip install virtualenvwrapper-win`<br>
`mkvirtualenv test` &nbsp; _test = name of virtual env_

<br>

<h3>Install required packages:</h3>

`pip install -r requirements.txt`<br>

<h3>To run project:</h3>

_After ensuring that we are in a virtual environment (If not, use `workon test`)_

`python manage.py makemigrations` <br>
`python manage.py migrate` <br>
`python manage.py runserver`<br>
<p>Visit development server http://127.0.0.1:8000/ </p>
<br>

<h3>Admin Site:</h3>

http://127.0.0.1:8000/admin

<br>
<h3>References:</h3>
<a href="https://docs.djangoproject.com/en/3.2/">Django's Official Documentation</a><br>
<a href="https://python-docx.readthedocs.io/en/latest/user/documents.html">Python Docx Documentation</a><br>
<a href="https://stackoverflow.com/">Stack Overflow</a><br>
<a href="https://www.youtube.com/watch?v=s6Xi7x4G7yg">Running a python script from Django</a><br>
