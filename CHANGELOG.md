Changelog
=========


v0.13 (2020-04-23)
------------------

Changes
~~~~~~~
- [views] schemas are not filtered for not authenticated users. [Cédric
  Bonhomme]

Other
~~~~~
- Updated CHANGELOG and bumped version in pyproject.toml. [Cédric
  Bonhomme]
- Updated wtforms. [Cédric Bonhomme]
- Updated jquery. [Cédric Bonhomme]
- Updated flask-admin and jinja2. [Cédric Bonhomme]
- Bounded Force Layout. [Cédric Bonhomme]
- Using local version of D3 version 4. [Cédric Bonhomme]
- Working digraph with D3 version 4. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Wip: graph generation. [Cédric Bonhomme]
- Added button to return to the schema. [Cédric Bonhomme]
- Jsoneditor is useless here. [Cédric Bonhomme]
- Added a view which is rendering a graph with the relations between
  schemas. Concerns #19. [Cédric Bonhomme]
- Display the email address of the user in the admin dashboard. [Cédric
  Bonhomme]


v0.12 (2020-04-09)
------------------

New
~~~
- Added a view which returns (text/plain) the definition of a schema.
  [Cédric Bonhomme]

Fix
~~~
- Platform_url is now instance_url. [Cédric Bonhomme]
- Forgot to concatente the last part of the URL for the URL definition
  of the JSON schema to create. [Cédric Bonhomme]
- The website attribute of an organization was not given to the
  constructor when creating a new one. [Cédric Bonhomme]

Other
~~~~~
- Updated relases notes. [Cédric Bonhomme]
- Rephrazing. [Cédric Bonhomme]
- Updated accountr recovery email template. [Cédric Bonhomme]
- Added comments. [Cédric Bonhomme]
- Improved login form. [Cédric Bonhomme]
- Check if the user exist. [Cédric Bonhomme]
- Added generation and verification of token for account recovery.
  [Cédric Bonhomme]
- Added template for the account recovery. [Cédric Bonhomme]
- Added sending of an email with a token to recover an account. [Cédric
  Bonhomme]
- Added email template for password recovery. [Cédric Bonhomme]
- Added functions to send emails. [Cédric Bonhomme]
- The name of the generated galaxy now containes the name of the
  original object. [Cédric Bonhomme]
- Fixed tests with the new required email field for users. [Cédric
  Bonhomme]
- Added email attribute for users. [Cédric Bonhomme]
- Fixed initialization of Flask-Migrate. [Cédric Bonhomme]
- Fixed documentation and Heroku deployment. [Cédric Bonhomme]
- Updated Heroku Procfile. [Cédric Bonhomme]
- Migrate form Flask-Script to the built-in integration of the click
  command line interface of Flask. [Cédric Bonhomme]
- Improved generation of cluster from an object: all values (properties)
  not directly useful for the context of the current schema in MONARC
  are assigned to the key 'meta' [Cédric Bonhomme]
- Display an error message when the user forgot to specify an
  organization during the creation of a news JSON schema. [Cédric
  Bonhomme]
- The JSON editor now by default enforces no_additional_properties and
  required_by_default. [Cédric Bonhomme]
- Updated JSON editor. [Cédric Bonhomme]
- Updated poetry.lock. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/MOSP. [Cédric Bonhomme]
- Provide more help to the user in order to create a valid JSON schema.
  [Cédric Bonhomme]
- Initializes an empty schema when the user wants to create a new one.
  [Cédric Bonhomme]
- Removed bin/pre_compile which is now useless. [Cédric Bonhomme]
- Fixed an issue when editing an existing schema. [Cédric Bonhomme]
- Add a way to create new schemas from the page which is listing the
  schemas. [Cédric Bonhomme]
- Uses the local version of the CSS fro code-prettify (sunburst).
  [Cédric Bonhomme]
- Removed useless Heroku configuration file. [Cédric Bonhomme]
- It is now possible to get the definition of a schema by its absolute
  UUID (URL) or by its id. [Cédric Bonhomme]
- Improved the JSON schema editor. [Cédric Bonhomme]
- Provice a better way to edit JSON schemas. [Cédric Bonhomme]
- Added Access-Control-Allow-Origin: * for the resources /schema/def/*
  [Cédric Bonhomme]
- Issue with JSON-editor 2.1.0. [Cédric Bonhomme]
- Updated JSON-editor. [Cédric Bonhomme]
- Deleted now useless conf file. [Cédric Bonhomme]
- Added some missing translations. [Cédric Bonhomme]
- Fixed broken translation system and completed translations. [Cédric
  Bonhomme]
- Use new buildpack for Poetry. [Cédric Bonhomme]
- Updated Flask-Login, [Cédric Bonhomme]
- Fixed some issues introduces after the update to the new version of
  Werkzeug. [Cédric Bonhomme]
- Updated JavaScript dependencies. [Cédric Bonhomme]
- Updated Python dependencies. [Cédric Bonhomme]
- Updated copyright years. [Cédric Bonhomme]
- Updated Python dependencies. [Cédric Bonhomme]
- Updated pyproject.toml. [Cédric Bonhomme]
- Updated JSON editor. [Cédric Bonhomme]


v0.11 (2020-02-03)
------------------
- Updated CHANGELOG. [Cédric Bonhomme]
- Simplify the pre-processor used to check if a user is authenticated.
  [Cédric Bonhomme]
- Updated CHANGELOG. [Cédric Bonhomme]
- Fixed an issue when authenticating a user via the API. [Cédric
  Bonhomme]
- Fixed UnboundLocalError issue in processor.py for the API. [Cédric
  Bonhomme]
- Added shebang. [Cédric Bonhomme]
- Deleted bin/README.md. [Cédric Bonhomme]
- Added pre-compile hook for Heroku. [Cédric Bonhomme]


v0.10 (2019-12-19)
------------------
- Updated CHANGELOG and bumped version number. [Cédric Bonhomme]
- Updated test for User objects. [Cédric Bonhomme]
- Updated auth-func preprocessor to take into account token sent in HTTP
  headers. [Cédric Bonhomme]
- Improved display. [Cédric Bonhomme]
- Added link to the documentation of the API. [Cédric Bonhomme]
- Let the user re-generate the API key. [Cédric Bonhomme]
- Added new apikey property for user objects. [Cédric Bonhomme]
- Fixed errors introduced by pycodestyle. [Cédric Bonhomme]
- Specify the address of the current Git repository for the project.
  [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated configuration for Heroku and fixed some warnings. [Cédric
  Bonhomme]
- Format style with black. [Cédric Bonhomme]
- Improved setting of the version for the /about/more page and in the
  setup.py file (based on git describe --tags) [Cédric Bonhomme]
- Updated README with poetry. [Cédric Bonhomme]
- Switch to poetry. Testing it with GitHub actions. [Cédric Bonhomme]
- Fix some indentation and removes useless stuff. [Cédric Bonhomme]
- Updated GitHub templates. [Cédric Bonhomme]


v0.9 (2019-12-12)
-----------------
- Updated JS dependencies. [Cédric Bonhomme]
- Bumped version number. [Cédric Bonhomme]
- Updated CHANGELOG. [Cédric Bonhomme]
- Cleaned tests fixtures. Updated CHANGELOG. [Cédric Bonhomme]
- Using app from bootstrap in the tests. [Cédric Bonhomme]
- Cleaning tests. [Cédric Bonhomme]
- Fixed bad path to runserver for Heroku. [Cédric Bonhomme]
- Typo. [Cédric Bonhomme]
- Typo. [Cédric Bonhomme]
- Chain postdeploy commands. [Cédric Bonhomme]
- Cleaned test_user test file. [Cédric Bonhomme]
- Updated Python application workflow. [Cédric Bonhomme]
- Replaced deprecated werkzeug.check_password_hash function. [Cédric
  Bonhomme]
- Updated Python application action file. [Cédric Bonhomme]
- Updated default wsgi. [Cédric Bonhomme]
- Updated manager. [Cédric Bonhomme]
- Moves instance folder. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Install dev dependencies. [Cédric Bonhomme]
- Testing Postgresql with GitHub actions. [Cédric Bonhomme]
- Fixed imports. [Cédric Bonhomme]
- Redoing something close to be working. [Cédric Bonhomme]
- Added simmple pytest test. [Cédric Bonhomme]
- Added setup.py file. [Cédric Bonhomme]
- Merge branch 'master' into reorganization. [Cédric Bonhomme]
- Added GitHub pull request template. [Cédric Bonhomme]
- Merge branch 'master' into reorganization. [Cédric Bonhomme]
- Update issue templates. [Cédric]
- Updated Help page. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Auto import of licenses from spdx. [Cédric Bonhomme]
- Auto initialization of the database on Heroku. [Cédric Bonhomme]
- Simply create symbolink with ln command. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/MOSP. [Cédric Bonhomme]
- Fixed deployment on Herokyu. [Cédric Bonhomme]
- Explain how to create first user. [Cédric Bonhomme]
- Fixed app.json. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Added a Contributing section to the README. [Cédric Bonhomme]
- Updated Heroku Python runtime. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Added pytest as a dev dependency. [Cédric Bonhomme]
- Removed deprecated generate_password_hash. [Cédric Bonhomme]
- Refactored models classes. [Cédric Bonhomme]
- Updated gigignore. [Cédric Bonhomme]
- Project reorganization. [Cédric Bonhomme]
- Fixed symlink. [Cédric Bonhomme]
- Updated path to source files. [Cédric Bonhomme]
- Added new configuration files. [Cédric Bonhomme]
- Cleaned old now useless files. [Cédric Bonhomme]
- Added shortlink to objects. [Cédric Bonhomme]
- Updated pipfile. [Cédric Bonhomme]
- Added defaut configuration files. [Cédric Bonhomme]
- Added mosp/bootstrap file. [Cédric Bonhomme]
- Renamed files. [Cédric Bonhomme]
- Renamed project folder. [Cédric Bonhomme]
- Removed useless logging module. [Cédric Bonhomme]
- Lint with flake8. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- No tests yet. [Cédric Bonhomme]
- No tests yet. [Cédric Bonhomme]
- Uses pipenv insteal of pip. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/MOSP. [Cédric Bonhomme]
- Improved preprocessors to check information of created and updated
  objects. [Cédric Bonhomme]
- Access values of the dictionary with get. [Cédric Bonhomme]
- Fixed typo. [Cédric Bonhomme]
- Testig GitHub actions. [Cédric Bonhomme]


v0.8 (2019-11-28)
-----------------

New
~~~
- Export an object to a MISP galaxy. Work in progress concerning #15.
  [Cédric Bonhomme]
- [template] Added a button in order to help the user generate a UUID
  easily. Closes #16. [Cédric Bonhomme]
- [views] added dashboard (WIP) [Cédric Bonhomme]

Changes
~~~~~~~
- Improved the perforamnces on JsonObject GET many by removing useless
  attributes from the result. [Cédric Bonhomme]
- [template] factorizes the template for the list of users. [Cédric
  Bonhomme]
- [views] improved iew to manage the users of the platform. [Cédric
  Bonhomme]
- [view] order by desc then put the nulls at last position. [Cédric
  Bonhomme]
- [view] Order the list of schemas by schema wich validates the most
  JSON objects. [Cédric Bonhomme]

Fix
~~~
- [template] wrong icon was used. [Cédric Bonhomme]
- [template] fixed an issue with the icon to delete a user (in the admin
  dashboard) [Cédric Bonhomme]

Other
~~~~~
- Updated CHANGELOG. [Cédric Bonhomme]
- Updated few Python dependencies with pipenv. Just took 10 minutes with
  pipenv...time to switch to poetry. [Cédric Bonhomme]
- Updated Bootstrap to version 4.4.1. [Cédric Bonhomme]
- Replace the call to JsonObject GET LIST to a JsonObject Get element.
  [Cédric Bonhomme]
- Removed useless import. [Cédric Bonhomme]
- Improved CHANGELOG. [Cédric Bonhomme]
- Authors default value is a list. [Cédric Bonhomme]
- Added link to MISP schemas for clusters and galaxies. [Cédric
  Bonhomme]
- Updated CHANGELOG. [Cédric Bonhomme]
- Updated translations, [Cédric Bonhomme]
- Updated links title in view_object. [Cédric Bonhomme]
- Added module description. [Cédric Bonhomme]
- Bumped version number and updated CHANGELOG. [Cédric Bonhomme]
- Let assume that for us the source is the organization name and the
  category is the schema which is validating the object. [Cédric
  Bonhomme]
- Add a warning when the UUID of new object is already taken. Closes
  #14. [Cédric Bonhomme]
- Increased the number of results per page for the Organization API.
  [Cédric Bonhomme]
- Call datetime.utcnow onely one time. [Cédric Bonhomme]
- Updated French translations. [Cédric Bonhomme]
- Minor update to the admin dashboard. [Cédric Bonhomme]
- Updated Python dependencies. [Cédric Bonhomme]
- Added a way to list the recently created/updated objects for an
  administrator. [Cédric Bonhomme]
- Updated JavaScript dependencies. [Cédric Bonhomme]
- Removes version checking functionality. [Cédric Bonhomme]
- Updated JavaScript dependencies and removed node-forge. [Cédric
  Bonhomme]
- Added shortcuts to create new users and organizations. [Cédric
  Bonhomme]
- Updated .gitignore. [Cédric Bonhomme]
- Added a link to the user profile from the list of users available to
  the admininstator. [Cédric Bonhomme]
- The number of memberships of the users. [Cédric Bonhomme]
- Updated JavaScript dependencies. [Cédric Bonhomme]
- Updated Python dependencies. [Cédric Bonhomme]
- Improved forms to create users and organizations. [Cédric Bonhomme]
- New [core]: it is now possible to create a new user and to link this
  user to one or several organization(s) in the same time. [Cédric
  Bonhomme]
- Added a break line between the tables of the admin page. [Cédric
  Bonhomme]
- Removed useless code. [Cédric Bonhomme]
- Removed SHA256 variable from the view_object Jinja template. [Cédric
  Bonhomme]
- Removed useless evaluation of the SHA256 of the JSON objects. [Cédric
  Bonhomme]
- Typo. [Cédric Bonhomme]
- Fixed pagination of the tables for the /organization page. [Cédric
  Bonhomme]
- Improved list of schemas view. [Cédric Bonhomme]
- Cosmethic change. [Cédric Bonhomme]
- Removed list-group-flush. [Cédric Bonhomme]
- Fixes and improvements to the user profile page. [Cédric Bonhomme]
- Typo. [Cédric Bonhomme]
- Updated dependencies. [Cédric Bonhomme]


v0.7 (2019-09-12)
-----------------

New
~~~
- It is now possible to download all JSON objects validated by a schema.
  Objects are returned in a flattened list. [Cédric Bonhomme]

Other
~~~~~
- Bumped version number. [Cédric Bonhomme]
- Added package-lock.json. [Cédric Bonhomme]
- Fixed an issue when one JSON object is not in a list. [Cédric
  Bonhomme]
- Removed Python version requirement. [Cédric Bonhomme]
- Updated Python dependencies. [Cédric Bonhomme]
- Updated json-editor. [Cédric Bonhomme]
- Updated configuration file. [Cédric Bonhomme]
- Excludes objects columns from the schema GET list result. [Cédric
  Bonhomme]
- Removed attribute is_public from the JsonObject objects. Closes #12.
  [Cédric Bonhomme]
- Updated Pipfile.lock. [Cédric Bonhomme]
- Removed Jinja safe filter for the schema description. [Cédric
  Bonhomme]
- Added multiple pagination objects for the organization page. [Cédric
  Bonhomme]
- Added server side pagination for objects created by users. [Cédric
  Bonhomme]
- Updated urllib3. [Cédric Bonhomme]
- [API] Updated max_results_per_page value for the json_object endpoint
  of the API. [Cédric Bonhomme]
- Added the possibility to filter objects of a schema based on some
  properties of this related schema (actually property of type interger,
  string and boolean). [Cédric Bonhomme]
- Added pagination for the list of objects validated by schema. [Cédric
  Bonhomme]
- Solved conflict. [Cédric Bonhomme]
- Updated urllib3 - CVE-2019-11324. [Cédric Bonhomme]
- Updated Pipfile.lock. [Cédric Bonhomme]
- Internationalization. [Cédric Bonhomme]
- Fixed typo. [Cédric Bonhomme]
- Is is now possible to acces to an object with its id or with the UUID
  of the JSONB object attribute of this object. [Cédric Bonhomme]
- Customized max_results_per_page and results_per_page. [Cédric
  Bonhomme]
- Minor fixes in the models. [Cédric Bonhomme]
- Change type of some String SQLALchemy columns to TEXT. [Cédric
  Bonhomme]
- Updated the default ordering of tables. [Cédric Bonhomme]
- Display the object id instead of displaying the loop index. [Cédric
  Bonhomme]
- Display the object id instead of displaying the loop index. [Cédric
  Bonhomme]
- Fix the taget column which is not sortable for the list of users in
  the admin section. [Cédric Bonhomme]
- Added a shortcut icon in order to delete an object. [Cédric Bonhomme]
- Renamed fork to copy. [Cédric Bonhomme]
- Renamed fork to copy. [Cédric Bonhomme]
- Hide useless icons. [Cédric Bonhomme]
- Improved layout of the organization page. [Cédric Bonhomme]
- Improved layout. [Cédric Bonhomme]
- Disable fork object button when user is not authenticated. [Cédric
  Bonhomme]
- It is now possible to fork an object from one organization to an
  other. Closes #11. [Cédric Bonhomme]
- Updated icon library used by the JSON editor. [Cédric Bonhomme]
- Updated development configuration file. [Cédric Bonhomme]
- Updated version of font-awesome. [Cédric Bonhomme]
- The contact e-mail address from the terms page is now using the one
  defined in the configuration file. [Cédric Bonhomme]
- Added an option in order to be able to remove version checking.
  [Cédric Bonhomme]
- Added a link to version.monarc.lu to check if MOSP is up-to-date.
  [Cédric Bonhomme]
- Replaced JavaScript aler message by a bootstrap toast. [Cédric
  Bonhomme]
- Updated comments. [Cédric Bonhomme]
- Added the new check_single_object_edit_permission pre-processor in
  order to check in the server side if the object send by the JSON
  editor is validated by the schema. [Cédric Bonhomme]
- Set ensure_ascii to False when converting the JSON to a string.
  [Cédric Bonhomme]
- Added management of members of organizations via the admin page to
  edit orgs. Closes #10. [Cédric Bonhomme]
- Updated links to the object/view page (from the view to create/edit an
  object). [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/MOSP. [Cédric Bonhomme]
- Updated terms. [Cédric Bonhomme]
- Delete the account of a user (and all its data). [Cédric Bonhomme]
- Updated french translations. [Cédric Bonhomme]
- Added new section in the edit object form. [Cédric Bonhomme]
- Updated french translations. [Cédric Bonhomme]
- Updated comments. [Cédric Bonhomme]
- Fixed a typo. [Cédric Bonhomme]
- Removed useless import. Added more comments. [Cédric Bonhomme]
- Added instructions in the README on how to compile translations.
  [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Improved layout of the object/view view. [Cédric Bonhomme]
- It is now possible to specify linkgs between objects when creating a
  new one. [Cédric Bonhomme]
- Updated label of the sha 256 footprint. [Cédric Bonhomme]


v0.6 (2019-03-11)
-----------------

Changes
~~~~~~~
- Minor update to the text of the help page. [Cédric Bonhomme]

Other
~~~~~
- Updated CHANGELOG. [Cédric Bonhomme]
- Updated the form the create/edit object in order to be able to manager
  referred objects. [Cédric Bonhomme]
- Removed useless tag for the list. [Cédric Bonhomme]
- Typo. [Cédric Bonhomme]
- Also provide a link to the schema of the related objects. [Cédric
  Bonhomme]
- Typo. [Cédric Bonhomme]
- Updated title of tabs in the related object section. [Cédric Bonhomme]
- Added the possibility to link objects. Closes #8. [Cédric Bonhomme]
- Updated dependencies. [Cédric Bonhomme]
- Fixed btn-group. [Cédric Bonhomme]
- COpy object to clipboard. [Cédric Bonhomme]
- Dsplays the SHA256 of the prettified object. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/MOSP. [Cédric Bonhomme]
- Updated about_more page. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/MOSP. [Cédric Bonhomme]
- Organization page now list the objects of an orgs. [Cédric Bonhomme]
- Improved users API page. [Cédric Bonhomme]
- Change the color of disabled features for not authenticated users.
  [Cédric Bonhomme]
- Fixed link the the running version of the software. [Cédric Bonhomme]
- Added about more page. [Cédric Bonhomme]
- Typo. [Cédric Bonhomme]
- Updated organization form. [Cédric Bonhomme]
- Last column of the table for the list of organizations is not
  sortable. [Cédric Bonhomme]
- Creation and basic edition of organizations. [Cédric Bonhomme]
- Added terms page. [Cédric Bonhomme]
- Added a link to the help page form the login page. [Cédric Bonhomme]
- Rephrasing. [Cédric Bonhomme]
- Added example of wsgi. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]


v0.5 (2019-02-23)
-----------------

Changes
~~~~~~~
- Updated dependencies. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated help page. [Cédric Bonhomme]
- Added logo from tebriz159. Closes #7. [Cédric Bonhomme]
- Added a public HTML template to list all the schemas. [Cédric
  Bonhomme]
- It is now possible to get an organization page with its name. [Cédric
  Bonhomme]
- Edited about page. [Cédric Bonhomme]
- Simply about page. [Cédric Bonhomme]
- Cosmetic change. [Cédric Bonhomme]
- Updated about page. [Cédric Bonhomme]

Fix
~~~
- Fixed style of the button in the view_object template. [Cédric
  Bonhomme]
- Bad name for the new human view. [Cédric Bonhomme]
- Misplaced HTML p tag. [Cédric Bonhomme]

Other
~~~~~
- Updated README. [Cédric Bonhomme]
- Updated CHANGELOG and README. [Cédric Bonhomme]
- Disable actually useless HTTP methods on the Organization endpoint for
  the API. [Cédric Bonhomme]
- Disable actually useless HTTP methods. [Cédric Bonhomme]
- PEP style. [Cédric Bonhomme]
- Renamed check_rights to pre_get_many. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Improved check_object_edit_permission decorator used by the API.
  [Cédric Bonhomme]
- Removed useless print. [Cédric Bonhomme]
- Is is now possible to create new objects via the API validated by the
  server. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/MOSP. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Removed useless line in the list of schemas. [Cédric Bonhomme]
- List only public objects for the user page. [Cédric Bonhomme]
- Minor UI improvement for the organization page. [Cédric Bonhomme]
- Added more sharing options. [Cédric Bonhomme]
- Testing sunburst skin for code-prettify. [Cédric Bonhomme]
- Using dropdown-menu-right class for dropdown menus. [Cédric Bonhomme]
- Updated background color. [Cédric Bonhomme]
- Renamed view_json template. [Cédric Bonhomme]
- Improved shema HTML template. [Cédric Bonhomme]
- Cleaned template. [Cédric Bonhomme]
- Improved object view page with new dropdown menu. [Cédric Bonhomme]
- Now using the name of organizations instead of their ids. [Cédric
  Bonhomme]
- Improved back redirect form. [Cédric Bonhomme]
- Cleaned indentation. [Cédric Bonhomme]
- Added a page to display shemas definition. [Cédric Bonhomme]
- Changed how is handled the management of configuration file. [Cédric
  Bonhomme]
- Added link to edit JSON schema from the preview of a schema (in object
  edition mode) [Cédric Bonhomme]
- Updated users profile and CSS. [Cédric Bonhomme]
- Updated CSS for the schema edtion button. [Cédric Bonhomme]
- Updated secondary style for buttons. [Cédric Bonhomme]
- Src/web/templates/edit_schema.html. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/MOSP. [Cédric Bonhomme]
- Added bootstrap spinner for the main page. [Cédric Bonhomme]
- Human.txt content type is text/plain. [Cédric Bonhomme]
- Update human.txt. [Cédric Bonhomme]
- Added human.txt file and icon for iOS devices. [Cédric Bonhomme]
- Improved layout and logos for apple-touch. [Cédric Bonhomme]
- Added bigger favicon. [Cédric Bonhomme]
- Updated AUTHORS file. [Cédric Bonhomme]
- Updated template in order to use the name of organizations instead of
  using the ids. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Typo. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated Python dependencies. [Cédric Bonhomme]
- Updated gitignore. [Cédric Bonhomme]
- Started a little documentation page. [Cédric Bonhomme]
- Started a little documentation page. [Cédric Bonhomme]
- Fixed main title in nav-bar brand. [Cédric Bonhomme]
- Renamed main title in nav-bar brand. [Cédric Bonhomme]
- Updated colors. [Cédric Bonhomme]
- Fixed CSV export for the measures of referentials. [Cédric Bonhomme]
- Renable export of CSV. [Cédric Bonhomme]
- Merge branch 'master' of github.com:CASES-LU/MOSP. [Cédric Bonhomme]
- Rempved link to the JavaScript library papaparse. [Cédric Bonhomme]
- It is no more possible to export the values of an object, useless.
  Consequently depency to papaparse has been removed. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Now using Heroku Python 3.7.1 runtime. [Cédric Bonhomme]
- Now using Heroku Python 3.7.2 runtime. [Cédric Bonhomme]
- Updated JSON-Editor. [Cédric Bonhomme]
- Updated Python minimum version and Python Heroku runtime. [Cédric
  Bonhomme]
- Updated some dependencies. [Cédric Bonhomme]
- Updated JavaScript dependencies (json-editor) [Cédric Bonhomme]
- Updated flask-admin due to security issue. [Cédric Bonhomme]
- Updated Pipfile.lock. [Cédric Bonhomme]


v0.4 (2018-10-05)
-----------------
- Updated CHANGELOG. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Added some sanity checks and comments. [Cédric Bonhomme]
- Simplify the table of the schema.html page. [Cédric Bonhomme]
- Improved the new user profile page. [Cédric Bonhomme]
- Return the user given in parameter with the objects created by this
  user. [Cédric Bonhomme]
- Changed the place of the button to edit the JSON definition of an
  object. [Cédric Bonhomme]
- Added a event listener for changes on JsonObject and Schema objects.
  [Cédric Bonhomme]
- Fixed a typo in the french translations. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Added missing bootstrap-select library. [Cédric Bonhomme]
- Improved the edit object page. [Cédric Bonhomme]
- Updated the form to edit objects in order to let users select on or
  several licenses. [Cédric Bonhomme]
- The view_json template now displays the license(s) atrributed to an
  object. [Cédric Bonhomme]
- Added a script to import licenses from spdx.org. [Cédric Bonhomme]
- Added migration script for the license. [Cédric Bonhomme]
- Objects are displayed in the first column. [Cédric Bonhomme]
- Let the user download values of an object to CSV of JSON. [Cédric
  Bonhomme]
- WIP: Export value fron JSON to a CSV file. [Cédric Bonhomme]
- Updated Python dependencies. [Cédric Bonhomme]
- Sort the table of objects by last updated. [Cédric Bonhomme]
- Updated dependencies. [Cédric Bonhomme]
- Updated dependencies. [Cédric Bonhomme]
- Added a statement about the licensing of the contributions. [Cédric
  Bonhomme]
- Updated WT-Forms. [Cédric Bonhomme]
- Updated json-editor. [Cédric Bonhomme]
- Updated README.md. [Cédric Bonhomme]
- Updated AUTHORS.md. [Cédric Bonhomme]
- Typo. [Cédric Bonhomme]
- Updated some URLs. [Cédric Bonhomme]
- Improved dropdown-menu. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Flix conflict. [Cédric Bonhomme]
- Minor update to the navbar. [Cédric Bonhomme]
- Improved dropdown-menu. [Cédric Bonhomme]
- Cosmethic changes for the navbar. [Cédric Bonhomme]
- Remmoved debug print. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Improved menu. [Cédric Bonhomme]
- Restored admin menu. [Cédric Bonhomme]
- Added profile edition page. [Cédric Bonhomme]
- Display creation nickname if profile is public. [Cédric Bonhomme]
- Bug fix. [Cédric Bonhomme]
- Check the permissions when edition objects. [Cédric Bonhomme]
- Added missing import. [Cédric Bonhomme]
- Update the NPM engine, just to silence a Heroku warning. [Cédric
  Bonhomme]
- Updated translaltions. [Cédric Bonhomme]
- Harmonize messages. [Cédric Bonhomme]
- Temporally remove this link. [Cédric Bonhomme]
- Fixed a bug where previously created JSON schema weren't editable via
  the custom web form. [Cédric Bonhomme]
- Fix. Convert the string from the form to a JSON object. [Cédric
  Bonhomme]


v0.3.0 (2018-06-01)
-------------------
- Improved translations. Bump version number. [Cédric Bonhomme]
- Fix. [Cédric Bonhomme]
- Directly add a schema in the selected organizations. [Cédric Bonhomme]
- Added link to create new schemas. [Cédric Bonhomme]
- Let the user create/edit new schemas. [Cédric Bonhomme]
- Fixed columns in templates. [Cédric Bonhomme]
- Clean layout template. [Cédric Bonhomme]
- Improved management of users. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Simplify the footer. [Cédric Bonhomme]


v0.2.0 (2018-05-30)
-------------------
- Updated CHANGELOG for the new release. [Cédric Bonhomme]
- Added a tab in order to see the corresponding JSON schema. [Cédric
  Bonhomme]
- Various improvements to the UI to edit JSON. [Cédric Bonhomme]
- Various improvements to the UI to edit JSON. [Cédric Bonhomme]
- Use a container-fluid for the editor. [Cédric Bonhomme]
- Rever test. [Cédric Bonhomme]
- Test. [Cédric Bonhomme]
- Uses bootstrap 4 with JSON-editor. [Cédric Bonhomme]
- Use a more stable version of json-editor. [Cédric Bonhomme]
- Updated SQLAlcheny and babel. [Cédric Bonhomme]
- Better use of DataTables. [Cédric Bonhomme]
- Added missing import of flask_babel. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Renamed the view which lists schemas related to a user. [Cédric
  Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Updated translations. [Cédric Bonhomme]
- Improved login page. [Cédric Bonhomme]
- Internationalization of dates. [Cédric Bonhomme]
- Updated Procfile. [Cédric Bonhomme]
- Updated Procfile. [Cédric Bonhomme]
- Skeleton for the internationalization. [Cédric Bonhomme]
- Improved deletion of accounts. [Cédric Bonhomme]
- Cosmethic changes, [Cédric Bonhomme]
- Exclude creator related information in the API. [Cédric Bonhomme]
- Added Flasj success message for objects creation. [Cédric Bonhomme]
- Editor -> definition. [Cédric Bonhomme]
- Improved the form to create objects. [Cédric Bonhomme]
- Updated footer. [Cédric Bonhomme]
- Merge branch 'master' of github.com:cedricbonhomme/MOSP. [Cédric
  Bonhomme]
- Now using JSONB instead of JSON. Default value is {}. [Cédric
  Bonhomme]
- Added some tests. [Cédric Bonhomme]
- Improvement. [Cédric Bonhomme]
- Rephrasing. [Cédric Bonhomme]
- Better management of users. [Cédric Bonhomme]
- Added a link to the validating schenas from the view object view.
  [Cédric Bonhomme]


v0.1.0 (2018-05-13)
-------------------
- First beta release of MOSP. [Cédric Bonhomme]
- Updated list of objects. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Fix for Heroku. [Cédric Bonhomme]
- Updated Heroku config. [Cédric Bonhomme]
- Updated Heroku config. [Cédric Bonhomme]
- Updated Heroku config. [Cédric Bonhomme]
- Updated Heroku config. [Cédric Bonhomme]
- Updated Heroku cocnfiguration. [Cédric Bonhomme]
- Fix. [Cédric Bonhomme]
- Added buildpak for heroku. [Cédric Bonhomme]
- Added configuration file for Heroku. [Cédric Bonhomme]
- Removed validation functions. [Cédric Bonhomme]
- Database improvements. [Cédric Bonhomme]
- Merge branch 'master' of github.com:cedricbonhomme/MOSP. [Cédric
  Bonhomme]
- Display more information in the view object page. [Cédric Bonhomme]
- Wip. [Cédric Bonhomme]
- Improved permissions management. [Cédric Bonhomme]
- Check permissions of objects with a decorator. [Cédric Bonhomme]
- Updated comments. [Cédric Bonhomme]
- Fix when the user is not connected. [Cédric Bonhomme]
- Load only private objects that are managed by the organizations the
  user is affiliated to. [Cédric Bonhomme]
- Improved user page. [Cédric Bonhomme]
- This view is public. [Cédric Bonhomme]
- Improved organization page. [Cédric Bonhomme]
- Previsualization of a JSON object. [Cédric Bonhomme]
- Fix typo. [Cédric Bonhomme]
- Fix. [Cédric Bonhomme]
- Cosmethic change. [Cédric Bonhomme]
- Improved navigation. [Cédric Bonhomme]
- Improved the editor view. [Cédric Bonhomme]
- Added a link to organization details page. [Cédric Bonhomme]
- Forgot to import abort. [Cédric Bonhomme]
- CSS customization. [Cédric Bonhomme]
- Adjust size of columns. [Cédric Bonhomme]
- Minor improvements in the JSON editor view. [Cédric Bonhomme]
- Added templates and views for organizations. [Cédric Bonhomme]
- Typo. [Cédric Bonhomme]
- More serious. [Cédric Bonhomme]
- Export a the JSON part of a JsonObject as a clean JSON file. [Cédric
  Bonhomme]
- Let's use the color of the year. [Cédric Bonhomme]
- Cosmethic change. [Cédric Bonhomme]
- Cosmethic change. [Cédric Bonhomme]
- A new page displays now JSON schemas and objects related to the
  currently connected user. [Cédric Bonhomme]
- Fix. [Cédric Bonhomme]
- Cosmethic change. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Specify the org related to an object during the creation. [Cédric
  Bonhomme]
- Updated footer. [Cédric Bonhomme]
- Updated About page and README file. [Cédric Bonhomme]
- Improved access rights for JsonObject objects throught the API.
  [Cédric Bonhomme]
- Updated index.html. [Cédric Bonhomme]
- All schemas are public. [Cédric Bonhomme]
- Returns only public JsonObject objects. [Cédric Bonhomme]
- Changed default color of the navbar. [Cédric Bonhomme]
- Edit attribute of a JsonObject object. [Cédric Bonhomme]
- Update layout. [Cédric Bonhomme]
- New table to list the JsonObjects. [Cédric Bonhomme]
- Better list of the objects related to a schema. [Cédric Bonhomme]
- Relads an object and edit it. [Cédric Bonhomme]
- Fix. [Cédric Bonhomme]
- Prettry print of information displayed in Flask-Admin. [Cédric
  Bonhomme]
- Updated README. [Cédric Bonhomme]
- Save a json object. [Cédric Bonhomme]
- Select a schema to create a new object. Display the org owner of a
  schema. [Cédric Bonhomme]
- Minor changes for the admin panel. [Cédric Bonhomme]
- Display details about a schema. Added a view to create a new object
  validated by a schema. [Cédric Bonhomme]
- Updated package.json. [Cédric Bonhomme]
- Updated Flask version number. [Cédric Bonhomme]
- Added a list which displays the list of recent schemas. [Cédric
  Bonhomme]
- Merge branch 'master' of github.com:cedricbonhomme/MOSP. [Cédric
  Bonhomme]
- Update to Flask 1.0. [Cédric Bonhomme]
- A user can be part of several organizations. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Added a boolean is_public in order to let the user set the visibility
  of an object or a schema. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- At least, a "proper" name. [Cédric Bonhomme]
- Added custom CSS file. [Cédric Bonhomme]
- Updated index page. [Cédric Bonhomme]
- Login required in order to access to the editor. [Cédric Bonhomme]
- Integrate the JSON editor in the overall layout (Bootstrap 4.0.1 is
  overwritten by Bootstrap 3.3.7). [Cédric Bonhomme]
- README.md. [Cédric Bonhomme]
- Initializes the JSON editor with the schema from the database (via the
  webservice). [Cédric Bonhomme]
- WIP. Simple web service to manage shemas. Will be used by json-editor
  to load the good schema. [Cédric Bonhomme]
- Added simple views in order to manage organizations and JSON schema.
  [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Added a script in order to create users. [Cédric Bonhomme]
- Added a simple form and a template for the authentication, [Cédric
  Bonhomme]
- Wip. Bootstrap 4 for the whole UI and 3.3.7 for the editor. [Cédric
  Bonhomme]
- Generate uml graph of the db model with sqlalchemy_schemadisplay (as a
  dev dependency) [Cédric Bonhomme]
- Link between orgs, schemas and objects validated by the schemas.
  [Cédric Bonhomme]
- Added license file. [Cédric Bonhomme]
- Removed ogp attribute. [Cédric Bonhomme]
- Update package.json with better key for json-editor. [Cédric Bonhomme]
- Updated .gitignore. [Cédric Bonhomme]
- Manager for the various scripts. [Cédric Bonhomme]
- Default user roles. [Cédric Bonhomme]
- Database. [Cédric Bonhomme]
- Useless here. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Updated installation instructions. [Cédric Bonhomme]
- My current favorite Flask skeleton. [Cédric Bonhomme]
- Update gitignore. [Cédric Bonhomme]
- Added Python dependencies with Pipfile. [Cédric Bonhomme]
- Switch branch for json-editor. [Cédric Bonhomme]
- Removed useless link to bootstrap js. [Cédric Bonhomme]
- Added README. [Cédric Bonhomme]
- Now using bootstrap 3. And improved deployment. [Cédric Bonhomme]
- Test. [Cédric Bonhomme]
