import abc

class PaymentProcessor(abc.ABC):
    def take_payment(self):
        raise BaseException("take_payment must be implemented")

class PointOfSaleProcessor(PaymentProcessor):
    def take_payment(self):
        if(self.valid_card()):
            print("Payment taken!")
        else:
            print("Card declined")

    def valid_card(self):
        return True


if __name__ == "__main__":
    pos = PointOfSaleProcessor()
    pos.take_payment()