import vk_api
import matplotlib as mpl
import matplotlib.pyplot as plt

# авторизация
vk_session = vk_api.VkApi('login', 'password')
vk_session.auth()

# получаем доступ к api
vk = vk_session.get_api()

male, female, alien = 0, 0, 0
# получаем список подписчиков группы
# и сортируем по гендерной принадлежности
members = vk.groups.getMembers(group_id='ddosguardnet', fields='sex')
for item in members['items']:
    if item['sex'] == 1:
        female += 1
    elif item['sex'] == 2:
        male += 1
    else:
        alien += 1
# print(f'мужчин: {male}')
# print(f'женщин: {female}')
# print(f'непонято кто: {alien}')

# строим гистограмму по полученным данным
plt.title('График')
plt.xlabel('Гендерное распределение')
plt.ylabel('Количество лиц')
plt.grid(True)

x = [1, 1.2, 1.4]  # чтоб эстетика глаз радовала (как минимум мой)
plt.xticks(x, ('female', 'male', 'alien'))
y = [female, male, alien]
plt.bar(x, y, width=0.1, align='center')
plt.show()
