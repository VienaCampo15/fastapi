from abc import ABC, abstractmethod

class RouteStrategyGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

    @abstractmethod
    def charge_transfer_fee(self, amount: float) -> float:
        pass

class PayPalGateway(RouteStrategyGateway):
    def process_payment(self, amount: float) -> str:
        return(f"Procesando el pago de ${amount} usando PayPal.")

    def charge_transfer_fee(self, amount: float) -> float:
        fee = 2.5
        print(f"Cobrando tarifa por transferencia con PayPal: ${fee}")
        return fee

class StripeGateway(RouteStrategyGateway):
    def process_payment(self, amount: float) -> str:
        return(f"Procesando el pago de ${amount} usando Stripe.")


    def charge_transfer_fee(self, amount: float) -> float:
        fee_percentage = 0.03
        fee = amount * fee_percentage
        print(f"Cobrando tarifa por transferencia con Stripe: ${fee}")
        return fee

class BankTransferGateway(RouteStrategyGateway):
    def process_payment(self, amount: float) -> str:
        return(f"Procesando el pago de ${amount} mediante Transferencia Bancaria.")


    def charge_transfer_fee(self, amount: float) -> float:
        fee = 0
        print("Transferencia Bancaria no cobra tarifa adicional.")
        return fee

