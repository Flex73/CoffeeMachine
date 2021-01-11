# Write your code here
print('Starting to make a coffee')
print('Grinding coffee beans')
print('Boiling water')
print('Mixing boiled water with crushed coffee beans')
print('Pouring coffee into the cup')
print('Pouring some milk into the cup')
print('Coffee is ready!')


class CoffeeMachine:
    def __init__(self, money, water, milk, beans, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.action = None

    def make_action(self):
        self.action = input('Write action (buy, fill, take, remaining, exit):')
        return self.action

    def print_state(self):
        print('The coffee machine has:', str(self.water) + ' of water', str(self.milk) + ' of milk', str(self.beans) + ' of coffee beans',
              str(self.cups) + ' of disposable cups', str(self.money) + ' of money', sep='\n')

    @staticmethod
    def resource_error(resource):
        print(f'Sorry, not enough {resource}!')

    @staticmethod
    def begin():
        print('I have enough resources, making you a coffee!')

    def reduce_supplies(self, n):
        if n == '1':
            if self.water >= 250 and self.beans >= 16:
                CoffeeMachine.begin()
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
            elif self.water < 250:
                CoffeeMachine.resource_error('water')
            elif self.beans < 16:
                CoffeeMachine.resource_error('beans')
        elif n == '2':
            if self.water >= 350 and self.beans >= 20 and self.milk >= 75:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
            elif self.water < 350:
                CoffeeMachine.resource_error('water')
            elif self.beans < 20:
                CoffeeMachine.resource_error('beans')
            elif self.milk < 75:
                CoffeeMachine.resource_error('milk')
        elif n == '3':
            if self.water >= 200 and self.beans >= 12 and self.milk >= 100:
                CoffeeMachine.begin()
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
            elif self.water < 200:
                CoffeeMachine.resource_error('water')
            elif self.beans < 12:
                CoffeeMachine.resource_error('beans')
            elif self.milk < 100:
                CoffeeMachine.resource_error('milk')

    def add_supplies(self):
        water = int(input('Write how many ml of water do you want to add:'))
        milk = int(input('Write how many ml of milk do you want to add:'))
        beans = int(input('Write how many grams of coffee beans do you want to add:'))
        cups = int(input('Write how many disposable cups of coffee do you want to add:'))

        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def get_money(self):
        print('I gave you $' + str(self.money))
        self.money = 0


machine = CoffeeMachine(550, 400, 540, 120, 9)
machine.make_action()

while machine.action:
    if machine.action == 'buy':
        num = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')

        if num != 'back':
            machine.reduce_supplies(num)

        machine.make_action()
    elif machine.action == 'fill':
        machine.add_supplies()
        machine.make_action()
    elif machine.action == 'take':
        machine.get_money()
        machine.make_action()
    elif machine.action == 'remaining':
        machine.print_state()
        machine.make_action()
    elif machine.action == 'exit':
        break
