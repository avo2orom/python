# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import decimal

ZERO = 0
CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXID = 'в'
MULTIPLICITY = 50
PERSENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MAX_REMOVAL = decimal.Decimal(600)
MIN_REMOVAL = decimal.Decimal(30)
PERSENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER_4_PERCENTAGES = 3
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_PERSENT = decimal.Decimal(10) / decimal.Decimal(100)

bank_account = decimal.Decimal(ZERO)
count = ZERO

def screen_input():
    action = 1
    while action not in (CMD_DEPOSIT, CMD_WITHDRAW, CMD_EXID):
        action = input(f'Введите значение:\n'
                       f'{CMD_DEPOSIT} - пополнить\n'
                       f'{CMD_WITHDRAW} - снять\n'
                       f'{CMD_EXID} - выйти:  ')

def exid():
    print(f'Заберите карту')
    print(f'Текущий баланс = {bank_account} у.е.')

def check_richness():
    persent = bank_account * RICHNESS_PERSENT
    bank_account -= persent
    print(f'Вычтен налог на высокую сумму - {RICHNESS_PERSENT} % в размере {persent}')
    print(f'Текущий баланс = {bank_account} у.е.')






while True:
    action = 1
    while action not in (CMD_DEPOSIT, CMD_WITHDRAW, CMD_EXID):
        action = input(f'Введите значение:\n'
                       f'{CMD_DEPOSIT} - пополнить\n'
                       f'{CMD_WITHDRAW} - снять\n'
                       f'{CMD_EXID} - выйти:  ')
        if action == CMD_EXID:
            print(f'Заберите карту')
            print(f'Текущий баланс = {bank_account} у.е.')
            break

        if bank_account > RICHNESS_SUM:
            persent = bank_account * RICHNESS_PERSENT
            bank_account -= persent
            print(f'Вычтен налог на высокую сумму - {RICHNESS_PERSENT} % в размере {persent}')
            print(f'Текущий баланс = {bank_account} у.е.')

        amount = 1
        while amount % MULTIPLICITY != ZERO:
            amount = decimal.Decimal(input('Введите сумму кратную {MULTIPLICITY}'))

        if action == CMD_DEPOSIT:
            count += 1
            bank_account += amount
            result = f'Пополнение карты на {amount}'

        elif action == CMD_WITHDRAW:
            persent = amount ** PERSENT_REMOVAL
            persent = MIN_REMOVAL if persent < MIN_REMOVAL else MAX_REMOVAL if persent > MAX_REMOVAL else persent
            amount_persent = amount + persent

            if bank_account >= amount_persent:
                count += 1
                bank_account -= amount_persent
                result = f'Cнятие с карты - {amount}. Процент за снятие составит {PERSENT_REMOVAL} в сумме {persent}'
            else:
                result = f'Недостаточно средств. Сумма с комиссией {amount_persent}'

        if count % COUNTER_4_PERCENTAGES == ZERO:
            amount_persent = bank_account * PERSENT_DEPOSIT
            bank_account += amount_persent
            result = f'{result}\nНачислено {PERSENT_DEPOSIT}% за {COUNTER_4_PERCENTAGES} операции, в сумме {amount_persent}'
        print(result)
        print(f'Текущий баланс = {bank_account} у.е.')
