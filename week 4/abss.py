from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via credit card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

def make_payment(processor, amount):
    print(processor.process_payment(amount))
credit_card = CreditCardProcessor()

make_payment(CreditCardProcessor(), 100)
make_payment(PayPalProcessor(), 50)