
Documentation for Restaurant Catalog Project
-------------
Release v0.1 on January 2016


Files:
------------------------------------------------------------------------
Main entry --> /main-catalog.py

Methods --> /methods

DB --> /database_setup.py

Helpers --> /helpers

HTML -> /templates

CSS -> /static


Description:
------------------------------------------------------------------------
The program generates employment catalog app using Flask

The primary function is a demenstration of create, read, update, and delete (CRUD) operations for a given employer, category,
and job.



Getting started:
------------------------------------------------------------------------



To run locally:

Please note this runs in the Vagrant environment, included in /vagrant

1) ** Important  **
Place your client_secrets.json file for both google and facebook logins in the /catalog directory.

2) from the console, cd to /vagrant directory, then type "vagrant up" and hit enter   #This starts the virtual machine

3) type "vagrant ssh" and hit enter   #Log in to machine

4) cd to /vagrant/catalog (yes you have to cd again)   #Get to shared directory

5) type "ls" and hit enter, you should see a list of files

6) run database_setup.py to create the database

7) run data-populator.py to populate the database

8) run main-catalog.py to start server

9) navigate to localhost:5000 in your browser



License:
------------------------------------------------------------------------

Portions from Udacity Full-Stack Engineer course and are copyright Udacity

Otherwise,

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


Authors:
------------------------------------------------------------------------
Udacity
Anthony Sarkis


Contact:
------------------------------------------------------------------------
my firstnamelastname@protonmail.com 

