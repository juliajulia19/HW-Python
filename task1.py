
a = float(input('Оцените силу вашей душевной боли по шкале от 0 до 10: '))
if a < 0.7:
    print('Кажется, вы испытываете легкое огорчение. Как человек в короткой поездке в метро, забывший дома наушники')
elif 0.7 <= a <= 4.2:
    print('Вы встревожены - почти как человек, которому придется звонить по телефону, и это в эпоху мессенджеров! То самое чувство, когда начинаете нервно репетировать в голове диалог...')
elif 4.3 <= a <= 7:
    print('Кажется вы действительно расстроены, как человек который купил билеты на концерт любимой группы за несколько месяцев, ждал его с нетерпением, но не смог пойти')
elif 7.1 <= a <= 10:
    print('Похоже с вами приключилась серьезная неудача, сравнимая с расстованием с любимым человеком или увольнением с работы. Вам требуется обратится за поддержкой к другу или даже психологу')
elif a > 10:
    print('Понимаем, что вы испытываете сильнейшую душевную боль, но пожалуйста оцените ваше состояние именно по шкале от 0 до 10')
  