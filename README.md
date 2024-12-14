Cyber Security Project-1 Course. The purpose of the app is to let users save secrets. Once a user logs in, they can use a form to create secrets that are only visible to them. Additionally, the apps lets users view one secret at a time.

NOTE: This project uses the 2021 list of vulnerabilities (`https://owasp.org/www-project-top-ten/`)!


INSTALL INSTRUCTIONS (After cloning the repo):

1. Install required libraries according to `https://cybersecuritybase.mooc.fi/installation-guide`
   
2. Install dotenv: 
  	`pip install python-dotenv`

3. Run:
  	for Windows: `'setup.bat'`
  	for Unix: `'setup.sh'`

4. Run: 
  	on Windows: `python manage.py runserver` 
  	on Unix: `python3 manage.py runserver`


The web app can be accessed by going to: `http://localhost:8000/`

The app has 2 regular users and 1 superuser - (username : password)
	`beep : saysboop` (regular user)
	`boop : saysbeep` (regular user)
  	`admin : admin` (superuser)
