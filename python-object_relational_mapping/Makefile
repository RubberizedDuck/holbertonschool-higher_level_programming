EX=./
ROOT=root root
DB=hbtn_0e_0_usa
DB2=hbtn_0e_4_usa
DB3=hbtn_0e_6_usa
DB4=hbtn_0e_14_usa
CAT0=cat 0-select_states.sql | mysql -uroot -p
CAT4=cat 4-cities_by_state.sql | mysql -uroot -p
CAT6=cat 6-model_state.sql | mysql -uroot -p

TASK0=0-select_states.py

TASK1=1-filter_states.py

TASK2=2-my_filter_states.py

TASK3=3-my_safe_filter_states.py

TASK4=4-cities_by_state.py

TASK5=5-filter_cities.py

TASK6=6-model_state.py

TASK7=7-model_state_fetch_all.py

TASK8=8-model_state_fetch_first.py

TASK9=9-model_state_filter_a.py

TASK10=10-model_state_my_get.py

TASK11=11-model_state_insert.py

TASK12=12-model_state_update_id_2.py

TASK13=13-model_state_delete_a.py

TASK14=14-model_city_fetch_by_state.py

all: 0

0:
	$(EX)$(TASK0) $(ROOT) $(DB)

1:
	$(EX)$(TASK1) $(ROOT) $(DB)

2:
	$(EX)$(TASK2) $(ROOT) $(DB) 'Arizona'

3:
	$(EX)$(TASK3) $(ROOT) $(DB) 'Arizona'

4:
	$(EX)$(TASK4) $(ROOT) $(DB2)

5:
	$(EX)$(TASK5) $(ROOT) $(DB2) Texas
	$(EX)$(TASK5) $(ROOT) $(DB2) Hawaii

6:
	$(EX)$(TASK6) $(ROOT) $(DB3)
	$(CAT6)

7:
	$(EX)$(TASK7) $(ROOT) $(DB3)

8:
	$(EX)$(TASK8) $(ROOT) $(DB3)

9:
	$(EX)$(TASK9) $(ROOT) $(DB3)

10:
	$(EX)$(TASK10) $(ROOT) $(DB3) Texas
	$(EX)$(TASK10) $(ROOT) $(DB3) Illinois

11:
	$(EX)$(TASK11) $(ROOT) $(DB3)
	$(EX)$(TASK7) $(ROOT) $(DB3)

12:
	$(EX)$(TASK12) $(ROOT) $(DB3)
	$(EX)$(TASK7) $(ROOT) $(DB3)

13:
	$(EX)$(TASK13) $(ROOT) $(DB3)
	$(EX)$(TASK7) $(ROOT) $(DB3)

14:
	$(EX)$(TASK14) $(ROOT) $(DB4)
