CAT=cat
MYSQL=| mysql -hlocalhost -uroot -p
ECHOCREATE=echo "CREATE USER 'user_0d_1'@'localhost';"
ECHOGRANT=echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';"
DATABASE=hbtn_0d_2
DATABASE2=hbtn_0d_usa
DATABASE3=hbtn_0d_tvshows

TASK0=0-privileges.sql

TASK1=1-create_user.sql

TASK2=2-create_read_user.sql

TASK3=3-force_name.sql

TASK4=4-never_empty.sql

TASK5=5-unique_id.sql

TASK6=6-states.sql

TASK7=7-cities.sql

TASK8=8-cities_of_california_subquery.sql

TASK9=9-cities_by_state_join.sql

TASK10=10-genre_id_by_show.sql

TASK11=11-genre_id_all_shows.sql

TASK12=12-no_genre.sql

TASK13=13-count_shows_by_genre.sql

TASK14=14-my_genres.sql

TASK15=15-comedy_only.sql

TASK16=16-shows_by_genre.sql

all: 0

0:
	$(CAT) $(TASK0) $(MYSQL)

1:
	$(CAT) $(TASK1) $(MYSQL)

2:
	$(CAT) $(TASK2) $(MYSQL)
	$(CAT) $(TASK0) $(MYSQL)

3:
	$(CAT) $(TASK3) $(MYSQL) $(DATABASE)

4:
	$(CAT) $(TASK4) $(MYSQL) $(DATABASE)

5:
	$(CAT) $(TASK5) $(MYSQL) $(DATABASE)

6:
	$(CAT) $(TASK6) $(MYSQL)

7:
	$(CAT) $(TASK7) $(MYSQL)

8:
	$(CAT) $(TASK8) $(MYSQL) $(DATABASE2)

9:
	$(CAT) $(TASK9) $(MYSQL) $(DATABASE2)

10:
	$(CAT) $(TASK10) $(MYSQL) $(DATABASE3)

11:
	$(CAT) $(TASK11) $(MYSQL) $(DATABASE3)

12:
	$(CAT) $(TASK12) $(MYSQL) $(DATABASE3)

13:
	$(CAT) $(TASK13) $(MYSQL) $(DATABASE3)

14:
	$(CAT) $(TASK14) $(MYSQL) $(DATABASE3)

15:
	$(CAT) $(TASK15) $(MYSQL) $(DATABASE3)

16:
	$(CAT) $(TASK16) $(MYSQL) $(DATABASE3)
