# processing activities

![License](https://img.shields.io/github/license/cedricbonhomme/processing-activities.svg?style=flat-square)
![Contributors](https://img.shields.io/github/contributors/cedricbonhomme/processing-activities.svg?style=flat-square)
![Stars](https://img.shields.io/github/stars/cedricbonhomme/processing-activities.svg?style=flat-square)
[![Say thanks to cedric](https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg?style=flat-square)](https://saythanks.io/to/cedricbonhomme)


## Presentation

Create, edit and share JSON objects.

## Installation


```bash
$ git clone https://github.com/cedricbonhomme/processing-activities.git
$ cd processing-activities/
$ npm install --prefix node_modules/v3 bootstrap@3.3.7
$ npm install
$ pipenv install
$ pipenv shell
$ python src/manager.py db_create
$ python src/manager.py db_init
$ python src/manager.py create_admin <username> <password>
$ python src/runserver.py
```

Generating the UML graph of the database:

```bash
$ python src/manager.py uml_graph
```


## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)
