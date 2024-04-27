from fastapi import APIRouter, Depends, HTTPException

from .strategy import BankTransferGateway, PayPalGateway, RouteStrategyGateway, StripeGateway

from enum import Enum

class Gateway(Enum):
    PAYPAL = "paypal"
    STRIPE = "stripe"
    BANKTRANSFER = "banktransfer"

def get_strategy_gateway(gateway: Gateway) -> RouteStrategyGateway:
    if gateway == Gateway.PAYPAL:
        return PayPalGateway()
    elif gateway == Gateway.STRIPE:
        return StripeGateway()
    elif gateway == Gateway.BANKTRANSFER:
        return BankTransferGateway()
    else:
        raise HTTPException(status_code=400, detail="Invalid gateway")

router = APIRouter()

@router.get("/payment")
def payment(amount: float, gateway: RouteStrategyGateway = Depends(get_strategy_gateway)) -> str:
    return gateway.process_payment(amount = amount)

@router.get("/transfer_fee")
def payment(amount: float, gateway: RouteStrategyGateway = Depends(get_strategy_gateway)) -> float:
    return gateway.charge_transfer_fee(amount = amount)
