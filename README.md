# cryptohub
Detail of top 100 coins with prices and all the details

Install virtualenv via pip:
$ pip install virtualenv

Test your installation
$ virtualenv --version

Create a virtual environment for a project:
$ cd my_project_folder
$ virtualenv my_project

To begin using the virtual environment, it needs to be activated:
$ source my_project/bin/activate

Install packages as usual, for example:
$ pip install -r >requirements.txt

for database creation
python manage.py makemigrations
python manage.py migrate


to runserver
./manage.py runserver YOURIP:8000

to add cron job
open another terminal and then run this command along with server in virtualenv instance(another)
$ python manage.py crontab add               to add a new job
$ python manage.py crontab show              to show currently running jobs
$ python manage.py crontab remove            to remove jobs


