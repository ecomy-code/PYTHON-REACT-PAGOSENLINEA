from flask import Blueprint, request
import stripe
from os import getenv


myapp = Blueprint("stripe_routes", __name__)


@myapp.route("/")
def main():
    return "Proceso iniciado"


@myapp.route("/pagar", methods=["POST"])
def pagar():
    try:
        data = request.json

        charge = stripe.Charge.create(
            amount=data['amount'],
            currency="usd",
            description=data['description'],
            source="tok_visa",
            idempotency_key=data['id'],
            api_key=getenv("SECRET_KEY")
        )
        print(charge)
        print('')
        print('Paquete cancelado con exito')

        return 'respuesta en json para validar compra en la app cliente'
    except stripe.error.StripeError as e:
        print(e)
        ero = str(e)
        mensaje = f"Se produjo un error::> {ero}"
        return mensaje