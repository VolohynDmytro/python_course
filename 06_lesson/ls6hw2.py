number = int(input('Введите количество секунд: '))
days = str(number // 86400)
hours = str((number % 86400) // 3600)
minutes = str((number % 3600) // 60)
seconds = str(number % 60)

if days.endswith('1') and days != '11':
    print(f'{days} День, {hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}')
elif days.endswith('2'):
    print(f'{days} Дні, {hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}')
elif days.endswith('3'):
    print(f'{days} Дні, {hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}')
elif days.endswith('4'):
    print(f'{days} Дні, {hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}')
else:
    print(f'{days} Днів, {hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}')
