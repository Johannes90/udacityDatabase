# Udacity Full Stack Developer Database Project

This is the code repo of Johannes Herrmann for the Udacity Database project. To run the project you will need vagrant. To setup the project follow the steps below:

1. Run 'cd vagrant/' from the root repository folder
2. Run 'vagrant up' to start the virtual machine
3. Run 'vagrant ssh' to access the shell of the virtual machine
4. Run 'cd vagrant/tournament'
5. Run 'psql' to open the Postgresql console
6. Inside the console run '\i tournament.sql' to initialize the database and create the table schemas. Note that this sql file will drop the previously created database every time it is rerun.
7. Exit the Postgresql console qith \q
8. You can now run the tests for this project with 'python tournament_test.py' in the same directory.
