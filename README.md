Поиск станций ближайших к двум заданным 
Данные только по Москве, но сработает и если залить другой город в точно таком же формате
Может быть полезно если собираетесь снимать квартиру вместе   

**max_stations** - максимум остановок от каждой из заданных  
**max_time** - максимум времени в пути от каждой из заданных  
**max_price** - максимальная средняя цена в рублях(берется из rent.txt, набрана из интернета. Может отличаться от реальности)  
**exclude_lines** - id линий которые не рассматривать  

пример:

    main.print_stations(source=Station(158), target=Station(63))
    #Курская, Трубна
    
    Метро Щёлковская, до Трубная 11 остановок, 0:26:30 минут до Курская 8 остановок, 0:18:10 минут средняя цена 35319 руб.
    Метро Черкизовская, до Трубная 9 остановок, 0:19:05 минут до Курская 8 остановок, 0:26:50 минут средняя цена 37489 руб.
    Метро Братиславская, до Трубная 11 остановок, 0:28:10 минут до Курская 10 остановок, 0:25:50 минут средняя цена 38248 руб.
    Метро Кожуховская, до Трубная 7 остановок, 0:15:35 минут до Курская 6 остановок, 0:13:15 минут средняя цена 33835 руб.
    Метро Первомайская, до Трубная 10 остановок, 0:24:15 минут до Курская 7 остановок, 0:15:55 минут средняя цена 36218 руб.
    Метро Каширская, до Трубная 11 остановок, 0:26:30 минут до Курская 9 остановок, 0:24:05 минут средняя цена 39951 руб.
    Метро Партизанская, до Трубная 8 остановок, 0:18:15 минут до Курская 5 остановок, 0:09:55 минут средняя цена 39423 руб.
    Метро Новокосино, до Трубная 10 остановок, 0:25:50 минут до Курская 9 остановок, 0:23:30 минут средняя цена 38342 руб.
    Метро Владыкино, до Трубная 8 остановок, 0:17:15 минут до Курская 11 остановок, 0:26:50 минут средняя цена 35040 руб.
    Метро Бабушкинская, до Трубная 11 остановок, 0:24:10 минут до Курская 11 остановок, 0:27:25 минут средняя цена 38005 руб.
    Метро Новогиреево, до Трубная 9 остановок, 0:22:30 минут до Курская 8 остановок, 0:20:10 минут средняя цена 38031 руб.
    Метро Бульвар Рокоссовского, до Трубная 10 остановок, 0:22:15 минут до Курская 9 остановок, 0:30:00 минут средняя цена 38225 руб.
    
