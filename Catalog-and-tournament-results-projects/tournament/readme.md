
Documentation for Tournament PSQL database.
-------------
Release v0.1 Novemeber 2016


Files:
------------------------------------------------------------------------
SQL database setup --> /tournament.sql
Functions --> /tournament.py
Unit tests --> /tournament_test.py


Description:
------------------------------------------------------------------------
The program generates a swiss-tournament style tournament database using
    psql.

The primary functions are:
-> Create database, tables, and views
-> Manage tournament including players, matches, and pairings. 


Getting started:
------------------------------------------------------------------------

To run locally:
1. Clong the files using github. This includes a pre-setup (by Udacity)
    version of vagrant virtual machine and psql:
	https://github.com/swirlingsand/fullstack-nanodegree-vm
2. Install Python 2.7
	https://www.python.org/downloads/
3. Open a terminal window (ie GitBash) in admin mode
4. Change directory (cd) to your local copy of the above repository
5. Start the virtual machine using the command: vagrant up
6. Secure shell into the machine using: vagrant ssh
7. Access PSQL using: psql
8. Import tournament file using: \i tournament.sql
9. Exit psql using: \q
10: Check you are in the tournament folder director, if not cd to that
    directory.
11: To run unit tests: python tournament_test.py


License:
------------------------------------------------------------------------

Portions from Udacity Full-Stack Engineer course and are copyright Udacity

Inspiration for parts of the view format and usage of zip function
    and views from internet help.

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
anthonysarkis@gmail.com


