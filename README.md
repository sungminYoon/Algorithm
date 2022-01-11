CODE PATH -> Algorithm/ArumiProject/arumi.py

![3](https://user-images.githubusercontent.com/19296155/148867315-1fdb9f6e-80eb-4d73-ae48-dd620ed43e28.png)
 
 결과

signal_list = [ 0, 11, 22, 32, 

                        12, 34, 34, 21, 

                        10, 22, 22, 30, 

                         40, 60, 40, 40,    <- 제일 높은 값인 60 이 있지만 완만한 구간이 아님 튀는값

                         30, 21, 55, 45,    <- 비교적 신호의 완만한 구간중 제일 높은 값인 55 를 찾는 아래 결과

                        12, 21, 44, 30, 21, 0]

​

diff_list = [0, 0, -2, 2, -1, -1, 0, 2, -1, 1, 0, 0, -2, 1, -1, 0, 2, -2, 0, 2,  0,-2,0, 0]

signal_count 26

diff_count 24

zero_index_list [0, 1, 6, 10, 11, 15, 18, 20, 22, 23]

value_index_list [0, 11, 34, 22, 30, 40, 55, 12, 44, 30]

max_value = 55

max_index = 6

------------------------------

result = 18 < - signal_list 인덱스 18 값 55
