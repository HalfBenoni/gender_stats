import vk_api
import matplotlib.pyplot as plt

# авторизация
vk_session = vk_api.VkApi('логин', 'пароль')
vk_session.auth()

# получаем доступ к api
vk = vk_session.get_api()

# список анализируемых групп
group_list = ['bookflow', 'tproger', 'proglib', 'nuancesprog', 'habr']


# получаем список подписчиков групп, выделяем уникальных подписчиков по id
members_list = []  # общий список участников групп
count = 0  # счетчик участников
offset = 1000  # необходимо увеличивать на 1000, пока не достигнем общего числа подписчиков
# потому что метод getMembers() возвращает максимум 1000 участников


# составляем список уникальных участников групп
for group in group_list:
    # получаем количество участников каждой группы (counter_list['count']) для параметра offset
    counter_list = vk.groups.getMembers(group_id=group)

    while offset < counter_list['count']:
        members = vk.groups.getMembers(group_id=group, fields='sex', offset=offset)
        for m in members['items']:
            # TODO классифицировать уникальных польщователей
            members_list.append(m)
            count += 1
            print(count)
        offset += 1000
    offset = 1000

male, female, alien = 0, 0, 0  # мальчики, девочки и те, кому не кайф было пол указывать
# сортируем по гендерной принадлежности
for member in members_list:
    # print(member)
    if member['sex'] == 1:
        female += 1
    elif member['sex'] == 2:
        male += 1
    else:
        alien += 1
print(f'мужчин: {male}')
print(f'женщин: {female}')
print(f'непонято кто: {alien}')

# строим гистограмму по полученным данным
plt.title('График')
plt.xlabel('Гендерное распределение')
plt.ylabel('Количество лиц')
plt.grid(True)

x = [1, 1.2, 1.4]  # чтоб эстетика глаз радовала (как минимум мой)
plt.xticks(x, ('женщины', 'мужчины', 'непонято кто'))
y = [female, male, alien]
plt.bar(x, y, width=0.1, align='center')
plt.show()
