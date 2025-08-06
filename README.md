# 🛍️ Tienda Web con Stripe Checkout - Flask

Este proyecto es una aplicación web simple hecha con **Flask** que permite a los usuarios comprar productos y realizar pagos seguros usando **Stripe Checkout**.

---

## 🚀 Características

- ✅ Selección dinámica de productos y cantidad  
- 💳 Integración con Stripe Checkout  
- 🎯 Páginas personalizadas de éxito y cancelación  
- 🔐 Variables de entorno para proteger tus claves  
- 🧼 Código limpio, comentado y modular  

---

## 🧰 Requisitos

- Python 3.7 o superior  
- pip (gestor de paquetes de Python)  
- Cuenta en [Stripe](https://dashboard.stripe.com/register) con claves activas  

---

## ⚙️ Instalación

1. **Clona este repositorio:**
2. **Crea y activa un entorno virtual (opcional pero recomendado):**
    python -m venv venv
    
    En Windows  
    venv\Scripts\activate
    
    En macOS/Linux  
    source venv/bin/activate
4. **Instala las dependencias:**
   pip install -r requirements.txt
5. **Crea un archivo .env en la raíz del proyecto con tu clave secreta de Stripe:**
   STRIPE_SECRET_KEY=sk_test_tu_clave_aqui
📝 Usa la clave secreta que encuentras en tu Dashboard de Stripe.

## Ejecución
# *Inicia la aplicación localmente con:*
  python app.py
# *Luego abre tu navegador y visita:*
  http://127.0.0.1:4242/

## 📁 Estructura del proyecto
    app.py: Aplicación Flask principal
    .env: Variables de entorno (no se sube al repo)
    requirements.txt: Lista de dependencias
    templates/:
        index.html
        success.html
        cancel.html

## 📦 Dependencias principales
1. Flask
2. python-dotenv
3. stripe

## 💡 Uso
  Selecciona un producto y cantidad.
  
  Haz clic en Pagar con Stripe para ser redirigido al Checkout.
  
  Completa el pago con una tarjeta de prueba.
  
  Serás redirigido a una página de éxito o cancelación.

## 🛠️ Consejos para producción
  Usa claves reales (sk_live_...) desde el modo "Live" de Stripe.
  
  Configura tu servidor con HTTPS.
  
  Implementa webhooks de Stripe para verificar pagos.
  
  Considera usar Stripe Elements para un checkout embebido.

## 📄 Licencia
  Este proyecto es libre para uso personal o comercial. Puedes modificarlo según tus necesidades.

## 📬 Contacto
  Para dudas o sugerencias: exaelyoandavid@gmail.com
```bash
git clone https://tu-repositorio.git
cd Pruebas-de-stripe
