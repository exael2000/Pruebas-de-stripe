# Tienda Web con Stripe Checkout - Flask

Este proyecto es una aplicación web simple hecha con Flask que permite a los usuarios comprar productos y realizar pagos seguros usando Stripe Checkout.

---

## Características

- Selección de productos y cantidad
- Creación dinámica de sesiones de pago en Stripe
- Páginas de éxito y cancelación personalizadas
- Uso de variables de entorno para la configuración segura de claves
- Código limpio y modular

---

## Requisitos

- Python 3.7 o superior
- Cuenta de Stripe con clave secreta activa
- pip (gestor de paquetes de Python)

---

## Instalación

1. Clona este repositorio:
Crea y activa un entorno virtual (opcional pero recomendado):
bash
Copiar código
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

Instala las dependencias:
bash
Copiar código
pip install -r requirements.txt

Crea un archivo .env en la raíz del proyecto con tu clave secreta de Stripe:
env
Copiar código
STRIPE_SECRET_KEY=sk_test_tu_clave_aqui
Nota: Usa la clave secreta que aparece en tu Dashboard de Stripe.

Ejecución
Para iniciar la aplicación localmente:
bash
Copiar código
python app.py

Luego abre en tu navegador:
cpp
Copiar código
http://127.0.0.1:4242/

Estructura del proyecto
app.py: Archivo principal con la aplicación Flask y la lógica Stripe.
templates/: Carpeta con archivos HTML (index.html, success.html, cancel.html).
.env: Archivo para variables de entorno (no se sube a repositorios públicos).
requirements.txt: Dependencias del proyecto.

Dependencias principales
Flask
python-dotenv
stripe

Uso
Selecciona un producto y cantidad.
Haz clic en "Pagar con Stripe" para ir a la página de pago seguro.
Completa el pago con tarjeta (Stripe en modo prueba).
Al terminar, serás redirigido a página de éxito o cancelación.

Consejos
Para producción, usa claves sk_live_ y configura HTTPS.
Implementa webhooks para confirmar pagos y actualizar base de datos.
Considera usar Stripe Elements para un flujo integrado.

Licencia
Este proyecto es de uso libre. ¡Siéntete libre de adaptarlo y mejorarlo!

Contacto
Para dudas o sugerencias: exaelyoandavid@gmail.com

Si quieres, te ayudo a generar también el archivo `requirements.txt` o a preparar un `.gitignore`. ¿Quieres?








Preguntar a ChatGPT

git clone https://tu-repositorio.git
cd nombre-del-proyecto
