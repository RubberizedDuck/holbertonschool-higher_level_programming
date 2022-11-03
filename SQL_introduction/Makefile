CAT=cat
MYSQL=mysql -hlocalhost -uroot -p

TASK0=0-list_databases.sql

TASK1=1-create_database_if_missing.sql

TASK2=2-remove_database.sql

TASK3=3-list_tables.sql

TASK4=4-first_table.sql

TASK5=5-full_table.sql

TASK6=6-list_values.sql

TASK7=7-insert_value.sql

TASK8=8-count_89.sql

TASK9=9-full_creation.sql

TASK10=10-top_score.sql

TASK11=11-best_score.sql

TASK12=12-no_cheating.sql

TASK13=13-change_class.sql

TASK14=14-average.sql

TASK15=15-groups.sql

TASK16=16-no_link.sql

all: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

0:
	$(CAT) $(TASK0) | $(MYSQL)

1:
	$(CAT) $(TASK1) | $(MYSQL)

2:
	$(CAT) $(TASK2) | $(MYSQL)

3:
	$(CAT) $(TASK3) | $(MYSQL) mysql

4:
	$(CAT) $(TASK4) | $(MYSQL) hbtn_0c_0
	$(CAT) $(TASK3) | $(MYSQL) hbtn_0c_0

5:
	$(CAT) $(TASK5) | $(MYSQL) hbtn_0c_0

6:
	$(CAT) $(TASK6) | $(MYSQL) hbtn_0c_0

7:
	$(CAT) $(TASK7) | $(MYSQL) hbtn_0c_0

8:
	$(CAT) $(TASK8) | $(MYSQL) hbtn_0c_0 | tail -1

9:
	$(CAT) $(TASK9) | $(MYSQL) hbtn_0c_0

10:
	$(CAT) $(TASK10) | $(MYSQL) hbtn_0c_0

11:
	$(CAT) $(TASK11) | $(MYSQL) hbtn_0c_0

12:
	$(CAT) $(TASK12) | $(MYSQL) hbtn_0c_0
	$(CAT) $(TASK10) | $(MYSQL) hbtn_0c_0

13:
	$(CAT) $(TASK13) | $(MYSQL) hbtn_0c_0
	$(CAT) $(TASK10) | $(MYSQL) hbtn_0c_0

14:
	$(CAT) $(TASK14) | $(MYSQL) hbtn_0c_0

15:
	$(CAT) $(TASK15) | $(MYSQL) hbtn_0c_0

16:
	$(CAT) $(TASK16) | $(MYSQL) hbtn_0c_0
