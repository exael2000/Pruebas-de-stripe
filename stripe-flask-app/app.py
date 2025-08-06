# Importación de librerías necesarias
import os  # Para acceder a variables del sistema
from flask import Flask, render_template, redirect, url_for, request  # Funciones principales de Flask
from dotenv import load_dotenv  # Para cargar variables desde un archivo .env
import stripe  # SDK de Stripe para Python

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Crear instancia de la aplicación Flask
app = Flask(__name__, template_folder="templates")

# Obtener la clave secreta de Stripe desde las variables de entorno
stripe_api_key = os.getenv("STRIPE_SECRET_KEY")
if not stripe_api_key:
    raise ValueError("La variable STRIPE_SECRET_KEY no está definida en el archivo .env")

# Configurar la clave de Stripe
stripe.api_key = stripe_api_key
print(f"🔐 Clave Stripe cargada: {stripe.api_key[:12]}...")  # Mostrar solo los primeros caracteres para verificar

# Lista de productos disponibles en la tienda
PRODUCTOS = [
    {"id": "prod_1", "nombre": "Camisa", "precio": 2500},   # $25.00 (el precio va en centavos)
    {"id": "prod_2", "nombre": "Gorra", "precio": 1500},    # $15.00
    {"id": "prod_3", "nombre": "Sudadera", "precio": 4000}, # $40.00
]

# Ruta principal (página de inicio)
@app.route("/")
def index():
    # Renderiza la plantilla HTML y le pasa la lista de productos
    return render_template("index.html", productos=PRODUCTOS)

# Ruta para crear la sesión de pago con Stripe
@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    # Obtener los datos enviados desde el formulario HTML
    producto_id = request.form.get("producto_id")
    cantidad = request.form.get("cantidad", type=int)

    # Validar que la cantidad sea válida (entre 1 y 10)
    if not cantidad or cantidad < 1 or cantidad > 10:
        return "Cantidad inválida", 400

    # Buscar el producto seleccionado por su ID
    producto = next((p for p in PRODUCTOS if p["id"] == producto_id), None)
    if not producto:
        return "Producto no encontrado", 400

    try:
        # Crear una sesión de pago con Stripe Checkout
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],  # Aceptar solo tarjetas
            line_items=[{
                'price_data': {
                    'currency': 'usd',  # Moneda en dólares
                    'unit_amount': producto["precio"],  # Precio en centavos
                    'product_data': {
                        'name': producto["nombre"],  # Nombre del producto
                    },
                },
                'quantity': cantidad,  # Cantidad elegida
            }],
            mode='payment',  # Tipo de sesión: pago único
            success_url=url_for('success', _external=True),  # URL si el pago fue exitoso
            cancel_url=url_for('cancel', _external=True),    # URL si el pago fue cancelado
        )
        # Redirigir al usuario a la página de pago de Stripe
        return redirect(session.url, code=303)

    except Exception as e:
        # Mostrar error en consola y devolverlo en la respuesta
        app.logger.error(f"Error creando sesión de Stripe: {e}")
        return f"<pre>Error al crear la sesión de pago:\n{e}</pre>", 500

# Ruta para mostrar página de éxito tras el pago
@app.route("/success")
def success():
    return render_template("success.html")

# Ruta para mostrar página si el usuario cancela el pago
@app.route("/cancel")
def cancel():
    return render_template("cancel.html")

# Ejecutar la aplicación en modo desarrollo, en el puerto 4242
if __name__ == "__main__":
    app.run(port=4242, debug=True)
