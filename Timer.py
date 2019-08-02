from time import *
start_timer = time()
struct = localtime(start_timer)
print('\nStarting Countdown At:', strftime('%X', struct))
i = 12 #Количество секунд в таймере
while i>-1:
    print(i)
    i -= 1
    sleep(1) #Пауза. В данном случае, каждый отстчёт через введённое кол-во времени (для одной секунды = 1)
end_timer = time()
difference = round(end_timer - start_timer)
print('\nRuntime:', difference, 'Seconds')
