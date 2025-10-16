import sys
class Bank_account:
    def __init__(self, initial_balance):

        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0< amount <= self.__balance:
            self.__balance -= amount
        elif amount > self.__balance:
            print(f'Недостаточно средств на счёте')
    @property
    def balance(self):
        return self.__balance

def main ():
    account = Bank_account(100)
    question = input(f'Вы хотите пополнить баланс или снять со счета (пополнить / снять): ')
    if question.lower() == 'пополнить':
        new_balance = int(input(f'Введите сумму для пополнения баланса'))
        account.deposit(new_balance)
        print(f' Сейчас на счёте: {account.balance}')
    elif question.lower() == 'снять':
        new_withdraw = int(input(f'Введите сумму для снятия депозита'))
        account.withdraw(new_withdraw)
        print(f'Сейчас на счёте: {account.balance}')
    else:
        print(f'Введите пополнить или снять')
        return main()
main()
sys.exit()