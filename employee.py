"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, contract_commission=0, bonus_commission=0, hours_worked=0, hourly_pay=0, monthly_pay=0, contracts_signed=0, bonus_amount=0, commission_per_contract=0):
        self.name = name
        self.contract_type = contract_type #salary or hourly
    
        self.contract_commission = contract_commission
        self.bonus_commission = bonus_commission
        self.hours_worked = hours_worked
        self.contracts_signed = contracts_signed
        self.bonus_amount = bonus_amount
        self.commission_per_contract = commission_per_contract
        self.monthly_pay = monthly_pay
        self.hourly_pay = hourly_pay

    def get_pay(self):
        return self.commission_money() + self.contract_money

    def commission_money(self):
        if self.bonus_commission:
            return self.bonus_amount
        if self.contract_commission:
            return (self.commission_per_contract * self.contracts_signed)

    def contract_money(self):
        if self.contract_type == "monthly salary":
            return self.monthly_pay
        if self.contract_type == "contract":
            return (self.hourly_pay * self.hours_worked)


    def __str__(self):
        description = f'{self.name} works on a {self.contract_type} of'
        description2 = f'{self.monthly_pay if self.contract_type=="monthly salary" else self.hours_worked + f"hours at {self.hourly_pay}/hour"}'
        if self.bonus_commission:
            description3 = f'and recieves a bonus commission for {self.bonus_amount}. Their total pay is {self.get_pay()}'
            return description + description2 + description3

        if self.contract_commission:
            description3 = f'annd recieves a commission for {self.contracts_signed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}'
            return description + description2 + description3
        
        else:
            description + description2 + f'. Their total pay is {self.get_pay()}'
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly salary", monthly_pay=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "contract", hours_worked=100, hourly_pay=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly salary", contract_commission=1, commission_per_contract=200, contracts_signed=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "contract", hours_worked=150, hourly_pay=25, contract_commission=1, contracts_signed=3, commission_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly salary", monthly_pay=2000, bonus_commission=1, bonus_amount=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "contract", hourly_pay=30, hours_worked=120, bonus_commission=1, bonus_amount=600)
