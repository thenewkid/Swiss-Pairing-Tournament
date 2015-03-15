# Swiss-Pairing-Tournament
Second Project on the Udacity Full Stack Web Developer NanoDegree.

To run this application you need to clone this git repository on your computer. From the command line, the command would be -> git clone this-repo-url. Once that is working you need to have postgresql installed. Once thats done you can type in the command psql -l and see your default databases and the default owners.

To start the psql interactive prompt you would type psql database-name. Once you are in the prompt you can start writing queries like create table table1 (col1 data-type, col2 data-type); or select * from table-name, or delete from table-name.

In this example you want to create a database called tournament. So in your psql prompt you type create database tournament; If it works then hit ctrl-z and exit out of the prompt. Then type psql -l and you should see your tournament database there. Now we want to get in the prompt of our tournament database so type in the command psql tournament. Now there are two create table statements in our tournament.sql file. type those statements into the tournament database prompt. Then once those tables are completed we can now run our tournament_test.py to test our code.

Exit out of the prompt and change directories into the folder of this repo that you cloned onto your computer. Then cd into the tournament folder. Then run the command python tournament_test.py.

These instructions are for the unix command line/terminal. If you are using windows then download wubi so you can dual boot windows and ubuntu. 



