# Sample Flask Project

Please ensure that MySQL and its development libraries are installed.

And Suggesting to use Virtual Environment.

$pip install virtualenv
$virtualenv venv
$venv\Scripts\activate

Expecting venv to be parallel to app folder.

### Install thre required plugins using below comand
pip install -r requirements.txt

Update config.py with mysql database configuration details. (Make sure specified database is already created)

### Run Below to create/migrate schema.
$python db.py db init

$python db.py db migrate

$python db.py db upgrade

### Run below to start the Server
$python run.py
