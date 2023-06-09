import re

from aiogram import types
from dispatcher import dp
from bot import BotDB
import config


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if not BotDB.user_exists(message.from_user.id):
        BotDB.add_user(message.from_user.id)

    await message.bot.send_message(message.from_user.id, "Добро пожаловать!")


@dp.message_handler(commands=('spent', 's', 'earned', 'e'), commands_prefix='!/')
async def record(message: types.Message):
    command_variants = (('/spent', '/s', '!spent', '!s'), ('/earned', '/e', '!earned', '!e'))
    operation = '-' if message.text.startswith(command_variants[0]) else '+'

    value = message.text

    for i in command_variants:
        for command in i:
            value = value.replace(command, '').strip()

    if len(value):
        x = re.findall(r'\d+(?:.\d+)?', value)
        if len(x):
            value = float(x[0].replace(',', '.'))

            BotDB.add_record(message.from_user.id, operation, value)

            if operation == '-':
                await message.reply('✅Запись о <u><b>расходе</b></u> успешно внесена!')
            else:
                await message.reply('✅Запись о <u><b>доходе</b></u> успешно внесена!')
        else:
            await message.reply('Не удалось определить сумму')
    else:
        await message.reply('Не введена сумма!')



@dp.message_handler(commands=('history', 'h'), commands_prefix='!/')
async def history(message: types.Message):
    command_variants = ('/history', '/h', '!history', '!h')
    within_all = {
        'day': ('today', 'day', 'сегодня', 'день'),
        'month': ('month', 'месяц'),
        'year': ('year', 'год')
    }

    command = message.text
    for cmd in command_variants:
        command = command.replace(cmd, '').strip()

    within = 'day'

    if len(command):
        for key in within_all:
            for value in within_all[key]:
                if command == value:
                    within = key

    records = BotDB.get_history(message.from_user.id, within)

    if len(records):
        answer = f'История записей за {within_all[within][-1]}\n\n'

        for r in records:
            answer += '<b>' + ('➖ Расход' if not r[2] else '➕ Доход') + '</b>'
            answer += f' - {r[3]}'
            answer += f'<i>({r[4]})</i>\n'

        await message.reply(answer)
    else:
        await message.reply('Записей нет!')
