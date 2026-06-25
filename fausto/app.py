import streamlit as st
import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración de la página
st.set_page_config(page_title="Mi Tienda de Ropa", layout="wide")
ARCHIVO = "inventario.json"

def guardar_datos():
    datos = {
        "productos_dama": st.session_state.productos_dama,
        "productos_caballero": st.session_state.productos_caballero
    }
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(
            datos,
            archivo,
            ensure_ascii=False,
            indent=4
        )

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos
    return None

# --- INICIALIZACIÓN DEL ESTADO GLOBAL (PERSISTENTE AL REFRESH) ---
datos_guardados = cargar_datos()

if "productos_dama" not in st.session_state:
    if datos_guardados and "productos_dama" in datos_guardados:
        st.session_state.productos_dama = datos_guardados["productos_dama"]
    else:
        # Valores iniciales por defecto si el archivo no existe
        st.session_state.productos_dama = [
            {"id": "d1", "nombre": "Vestido Corto de Verano", "precio": 599.00, "desc": "Vestido fresco con estampado floral ideal para días soleados.", "img": "https://i.pinimg.com/originals/8c/eb/0b/8ceb0b97c7731617958e1f608d5c08cc.jpg", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "d2", "nombre": "Blusa Elegante de Satín", "precio": 450.00, "desc": "Blusa satinada de cuello en V ideal para oficina o eventos.", "img": "https://litb-cgis.rightinthebox.com/images/640x853/202507/bps/product/inc/ztnxrd1753345211622.jpg?fmt=webp&v=1", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "d3", "nombre": "Jeans High Rise Slim", "precio": 699.00, "desc": "Pantalón de mezclilla tiro alto con ajuste cómodo moldeador.", "img": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "d4", "nombre": "Chaqueta de Mezclilla", "precio": 799.00, "desc": "Chaqueta denim clásica con lavado claro y botones metálicos.", "img": "https://images.unsplash.com/photo-1610591951231-58887328a2d5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "d5", "nombre": "Falda Plisada Midi", "precio": 480.00, "desc": "Falda plisada de cintura alta, tiro elegante y caída suave.", "img": "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=400", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "d6", "nombre": "Suéter de Punto Ligero", "precio": 520.00, "desc": "Suéter tejido ideal para las tardes frescas de otoño.", "img": "https://media.falabella.com/falabellaCL/143440147_01/public", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "d7", "nombre": "Ensamble Casual Largo", "precio": 399.00, "desc": "Cardigan ligero abierto, perfecto para combinar con básicos.", "img": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "d8", "nombre": "Top Corto Acanalado", "precio": 250.00, "desc": "Crop top básico elástico de cuello redondo.", "img": "https://detqhtv6m6lzl.cloudfront.net/HCLContenido/producto/FullImage/7506591000250-1.jpg", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "d9", "nombre": "Pantalón Sastrero Elegante", "precio": 650.00, "desc": "Pantalón formal de pinzas ideal para un look de negocios.", "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "d10", "nombre": "Vestido Elegante de Noche", "precio": 899.00, "desc": "Vestido largo de fiesta con caída refinada y ajuste estilizado.", "img": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=400", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}}
        ]
        guardar_datos()

if "productos_caballero" not in st.session_state:
    if datos_guardados and "productos_caballero" in datos_guardados:
        st.session_state.productos_caballero = datos_guardados["productos_caballero"]
    else:
        # Valores iniciales por defecto si el archivo no existe
        st.session_state.productos_caballero = [
            {"id": "c1", "nombre": "Camisa Oxford Casual", "precio": 499.00, "desc": "Camisa de algodón premium de corte slim fit para diario.", "img": "https://www.unitam.com/media/catalog/product/c/a/camisa_oxford_gris_doblada_1.jpg", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "c2", "nombre": "Pantalón Chino Slim negro", "precio": 650.00, "desc": "Pantalón de gabardina suave de corte moderno semi-formal.", "img": "https://images.jackjones.com/12174152/3375430/003/jackjones-pantalonchinoslimfit-noire.jpg?v=1e4372fb4feb8b0a31fbe37163e53509", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "c3", "nombre": "Playera Polo Clásica", "precio": 350.00, "desc": "Playera tipo polo de algodón con cuello texturizado.", "img": "https://martinspolo.co/data/martins-polo-camiseta-tipo-polo-tela-fria-hombre-ref-1006-3-1580x1975.webp", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "c4", "nombre": "Sudadera con Capucha", "precio": 599.00, "desc": "Sudadera hoodie cómoda con bolsillo canguro frontal.", "img": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "c5", "nombre": "Chaqueta Bomber Negra", "precio": 899.00, "desc": "Chaqueta ligera estilo bomber con cierres reforzados.", "img": "https://www.bolf.es/hpeciai/49b49f5d03110139c40db57ebb00db86/spa_pl_Chaqueta-bomber-de-cuero-para-hombre-negro-Bolf-6671-89467_2.jpg", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "c6", "nombre": "Jeans Rectos Clásicos", "precio": 620.00, "desc": "Pantalón de mezclilla azul tradicional de corte recto.", "img": "https://pantalonesdemezclilla.mx/cdn/shop/files/Jeans-de-pierna-recta-para-hombre-estilo-clasico.png?v=1705709803", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "c7", "nombre": "Suéter de Cuello Alto", "precio": 550.00, "desc": "Suéter fino tejido de cuello alto para un estilo sofisticado.", "img": "https://i5-mx.walmartimages.com/mg/gm/3pp/asr/00b2cf45-6bfe-48ac-bc52-7d4289ced381.ffc6c2e813acd287daeb5304184c201c.jpeg?odnHeight=2000&odnWidth=2000&odnBg=ffffff", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "c8", "nombre": "Bermuda Casual de Lino", "precio": 380.00, "desc": "Bermuda fresca ideal para vacaciones o días calurosos.", "img": "https://i.pinimg.com/originals/eb/7b/56/eb7b56541e583fb8723bf610154d2f9a.jpg", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "c9", "nombre": "Chaqueta Acolchada", "precio": 999.00, "desc": "Chaqueta térmica capitonada repelente al viento.", "img": "https://images.unsplash.com/photo-1544923246-77307dd654cb?w=400", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
            {"id": "c10", "nombre": "Camisa de Lino Manga Corta", "precio": 450.00, "desc": "Camisa relajada de lino transpirable de cuello campana.", "img": "https://dracko.ar/wp-content/uploads/2023/11/img_7057-600x750.jpg", "stock": {"Chico": 10, "Mediano": 10, "Grande": 10}},
        ]
        guardar_datos()

if "carrito" not in st.session_state:
    st.session_state.carrito = []

if "seccion" not in st.session_state:
    st.session_state.seccion = "Inicio"

if "origen_catalogo" not in st.session_state:
    st.session_state.origen_catalogo = "Catálogo Dama"

if "ultimo_agregado" not in st.session_state:
    st.session_state.ultimo_agregado = None

if "admin_autenticado" not in st.session_state:
    st.session_state.admin_autenticado = False

if "total_compra" not in st.session_state:
    st.session_state.total_compra = 0

if "nombre_cliente" not in st.session_state:
    st.session_state.nombre_cliente = ""

# --- FUNCIÓN PARA ENVIAR ALERTAS AL ADMINISTRADOR ---
def enviar_alerta_admin(nombre_cliente, correo_cliente, telefono_cliente, carrito, calle, cp, municipio, estado):
    correo_admin = "roaalex912@gmail.com"
    correo_emisor = "23307049@utfv.edu.mx"
    password = "vkui tfmw xvxm jgya"
    asunto = "🛒 Nueva compra realizada"

    total = 0
    detalle_compra = ""
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        detalle_compra += f"Producto: {item['nombre']} | Talla: {item['talla']} | Cant: {item['cantidad']} | Sub: ${subtotal:.2f}\n"

    mensaje = f"NUEVA COMPRA\n\nCliente: {nombre_cliente}\nCorreo: {correo_cliente}\nTel: {telefono_cliente}\n\nEnvío: {calle}, {cp}, {municipio}, {estado}\n\nDetalle:\n{detalle_compra}\nTOTAL: ${total:.2f}"

    try:
        email = MIMEMultipart()
        email["From"] = correo_emisor
        email["To"] = correo_admin
        email["Subject"] = asunto
        email.attach(MIMEText(mensaje, "plain"))
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(correo_emisor, password)
        servidor.send_message(email)
        servidor.quit()
    except Exception as e:
        st.error(f"Error al enviar correo de compra: {e}")

# --- FUNCIÓN PARA ENVIAR EL TICKET AL COMPRADOR ---
def enviar_ticket_comprador(nombre_cliente, correo_cliente, carrito, calle, cp, municipio, estado):
    correo_emisor = "23307049@utfv.edu.mx"
    password = "vkui tfmw xvxm jgya"
    asunto = "🧾 Tu Ticket de Compra - VOGUE & STYLE"

    total = 0
    detalle_compra = ""
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        detalle_compra += f"- {item['nombre']} ({item['talla']}) x {item['cantidad']}: ${subtotal:.2f}\n"

    mensaje = (
        f"Hola {nombre_cliente},\n\n"
        f"¡Muchas gracias por tu compra en VOGUE & STYLE!\n"
        f"A continuación, te compartimos el detalle de tu ticket:\n\n"
        f"--- RESUMEN DE COMPRA ---\n"
        f"{detalle_compra}\n"
        f"TOTAL A PAGAR: ${total:.2f} MXN\n"
        f"-------------------------\n\n"
        f"📍 Dirección de Envío:\n"
        f"{calle}, C.P. {cp}, {municipio}, {estado}.\n\n"
        f"💵 Recuerda que tu pago es CONTRA ENTREGA.\n\n"
        f"Si tienes alguna duda con tu pedido, puedes responder a este correo.\n\n"
        f"¡Que disfrutes tus prendas!\n"
        f"Atentamente, El equipo de VOGUE & STYLE."
    )

    try:
        email = MIMEMultipart()
        email["From"] = correo_emisor
        email["To"] = correo_cliente
        email["Subject"] = asunto
        email.attach(MIMEText(mensaje, "plain"))
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(correo_emisor, password)
        servidor.send_message(email)
        servidor.quit()
    except Exception as e:
        st.error(f"Error al enviar el ticket al cliente: {e}")

def verificar_y_alertar_stock(productos_dama, productos_caballero):
    correo_admin = "roaalex912@gmail.com"
    correo_emisor = "23307049@utfv.edu.mx"
    password = "vkui tfmw xvxm jgya"
    
    productos_bajos = []
    for p in productos_dama + productos_caballero:
        for talla, cantidad in p["stock"].items():
            if cantidad < 10: 
                productos_bajos.append(f"- {p['nombre']} (Talla {talla}): {cantidad} rest.")

    if productos_bajos:
        mensaje = "ALERTA DE STOCK BAJO:\n\n" + "\n".join(productos_bajos)
        try:
            email = MIMEMultipart()
            email["From"] = correo_emisor
            email["To"] = correo_admin
            email["Subject"] = "⚠️ Alerta de Stock"
            email.attach(MIMEText(mensaje, "plain"))
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(correo_emisor, password)
            servidor.send_message(email)
            servidor.quit()
        except Exception as e:
            st.warning(f"No se pudo enviar la alerta de stock: {e}")


# --- BARRA DE NAVEGACIÓN ---
col_n1, col_n2, col_n3, col_n4, col_n5 = st.columns(5)
with col_n1:
    if st.button("🏠 Inicio", use_container_width=True):
        st.session_state.seccion = "Inicio"
        st.rerun()
with col_n2:
    if st.button("👗 Dama", use_container_width=True):
        st.session_state.seccion = "Catálogo Dama"
        st.rerun()
with col_n3:
    if st.button("👔 Caballero", use_container_width=True):
        st.session_state.seccion = "Catálogo Caballero"
        st.rerun()
with col_n4:
    cant_items = sum(item["cantidad"] for item in st.session_state.carrito)
    if st.button(f"🛒 Carrito ({cant_items})", use_container_width=True):
        st.session_state.seccion = "Carrito"
        st.rerun()
with col_n5:
    if st.button("⚙️ Panel Admin", use_container_width=True):
        st.session_state.seccion = "Administrador"
        st.rerun()

st.markdown("---")

# --- FUNCIÓN DEL CATÁLOGO ---
def mostrar_catalogo(lista_productos, tipo_catalogo):
    st.session_state.origen_catalogo = tipo_catalogo
    if not lista_productos:
        st.info("No hay productos disponibles actualmente.")
        return

    for i in range(0, len(lista_productos), 2):
        col1, col2 = st.columns(2)
        
        # --- COLUMNA IZQUIERDA ---
        with col1:
            prod = lista_productos[i]
            st.image(prod["img"], width=200)
            stock_total = sum(prod["stock"].values())
            aviso_stock = f"Disponibles: {stock_total} pzs" if stock_total > 0 else "⚠️ AGOTADO"
            
            st.markdown(f"""
            <div style="background-color: #fdfdfd; padding: 15px; border-radius: 8px; border: 1px solid #eee; margin-top: 5px; margin-bottom: 5px;">
                <h3 style="margin: 0; min-height: 60px; color: #222;">{prod['nombre']}</h3>
                <p style="color: #666; min-height: 50px; font-size: 14px; margin-bottom: 10px;">{prod['desc']}</p>
                <p style="font-weight: bold; color: #111; margin: 0; display: inline-block;">Precio: ${prod['precio']:.2f} MXN</p>
                <span style="float: right; color: {'#2e7d32' if stock_total > 0 else '#c62828'}; font-size: 13px; font-weight: bold;">{aviso_stock}</span>
            </div>
            """, unsafe_allow_html=True)
            
            with st.popover("🛒 Agregar al carrito", use_container_width=True, disabled=(stock_total == 0)):
                st.write(f"**Configura tu pedido para:** {prod['nombre']}")
                talla = st.radio("Selecciona tu talla:", ["Chico", "Mediano", "Grande"], key=f"talla_{prod['id']}", horizontal=True)
                stock_talla_disponible = prod["stock"][talla]
                st.write(f"Disponibles en talla *{talla}*: **{stock_talla_disponible} piezas**")
                
                if stock_talla_disponible > 0:
                    cantidad = st.number_input("Cantidad:", min_value=1, max_value=stock_talla_disponible, value=1, step=1, key=f"cant_{prod['id']}")
                    if st.button("Confirmar y Añadir", key=f"conf_{prod['id']}", use_container_width=True):
                        item_pedido = prod.copy()
                        item_pedido["talla"] = talla
                        item_pedido["cantidad"] = cantidad
                        st.session_state.carrito.append(item_pedido)
                        st.session_state.ultimo_agregado = prod['id']
                        st.rerun()
                else:
                    st.error(f"⚠️ Sin stock en talla {talla}.")
                
                if st.session_state.ultimo_agregado == prod['id']:
                    st.markdown("---")
                    st.success(f"¡Añadido con éxito!")
                    col_pop1, col_pop2 = st.columns(2)
                    with col_pop1:
                        if st.button("🛍️ Seguir Comprando", key=f"seguir_{prod['id']}", use_container_width=True):
                            st.session_state.ultimo_agregado = None
                            st.rerun()
                    with col_pop2:
                        if st.button("💳 Finalizar Compra", key=f"finalizar_{prod['id']}", use_container_width=True):
                            st.session_state.ultimo_agregado = None
                            st.session_state.seccion = "Formulario de Envío"
                            st.rerun()
            st.markdown("<br><br>", unsafe_allow_html=True)
            
        #  COLUMNA DERECHA
        with col2:
            if i + 1 < len(lista_productos):
                prod = lista_productos[i+1]
                st.image(prod["img"], width=200)
                stock_total = sum(prod["stock"].values())
                aviso_stock = f"Disponibles: {stock_total} pzs" if stock_total > 0 else "⚠️ AGOTADO"
                
                st.markdown(f"""
                <div style="background-color: #fdfdfd; padding: 15px; border-radius: 8px; border: 1px solid #eee; margin-top: 5px; margin-bottom: 5px;">
                    <h3 style="margin: 0; min-height: 60px; color: #222;">{prod['nombre']}</h3>
                    <p style="color: #666; min-height: 50px; font-size: 14px; margin-bottom: 10px;">{prod['desc']}</p>
                    <p style="font-weight: bold; color: #111; margin: 0; display: inline-block;">Precio: ${prod['precio']:.2f} MXN</p>
                    <span style="float: right; color: {'#2e7d32' if stock_total > 0 else '#c62828'}; font-size: 13px; font-weight: bold;">{aviso_stock}</span>
                </div>
                """, unsafe_allow_html=True)
                
                with st.popover("🛒 Agregar al carrito", use_container_width=True, disabled=(stock_total == 0)):
                    st.write(f"**Configura tu pedido para:** {prod['nombre']}")
                    talla = st.radio("Selecciona tu talla:", ["Chico", "Mediano", "Grande"], key=f"talla_{prod['id']}", horizontal=True)
                    stock_talla_disponible = prod["stock"][talla]
                    st.write(f"Disponibles en talla *{talla}*: **{stock_talla_disponible} piezas**")
                    
                    if stock_talla_disponible > 0:
                        cantidad = st.number_input("Cantidad:", min_value=1, max_value=stock_talla_disponible, value=1, step=1, key=f"cant_{prod['id']}")
                        if st.button("Confirmar y Añadir", key=f"conf_{prod['id']}", use_container_width=True):
                            item_pedido = prod.copy()
                            item_pedido["talla"] = talla
                            item_pedido["cantidad"] = cantidad
                            st.session_state.carrito.append(item_pedido)
                            st.session_state.ultimo_agregado = prod['id']
                            st.rerun()
                    else:
                        st.error(f"⚠️ Sin stock en talla {talla}.")
                    
                    if st.session_state.ultimo_agregado == prod['id']:
                        st.markdown("---")
                        st.success(f"¡Añadido con éxito!")
                        col_pop1, col_pop2 = st.columns(2)
                        with col_pop1:
                            if st.button("🛍️ Seguir Comprando", key=f"seguir_{prod['id']}", use_container_width=True):
                                st.session_state.ultimo_agregado = None
                                st.rerun()
                        with col_pop2:
                            if st.button("💳 Finalizar Compra", key=f"finalizar_{prod['id']}", use_container_width=True):
                                st.session_state.ultimo_agregado = None
                                st.session_state.seccion = "Formulario de Envío"
                                st.rerun()
                st.markdown("<br><br>", unsafe_allow_html=True)

# --- CONTENIDO DE LAS SECCIONES ---
if st.session_state.seccion == "Inicio":
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align: center; color: #333333;'>VOGUE & STYLE</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #777777;'>Tu tienda de ropa favorita</h3>", unsafe_allow_html=True)
        imagen_url = "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=800&q=80"
        st.image(imagen_url, use_container_width=True)

elif st.session_state.seccion == "Catálogo Dama":
    st.title("👗 Catálogo de Dama")
    mostrar_catalogo(st.session_state.productos_dama, "Catálogo Dama")

elif st.session_state.seccion == "Catálogo Caballero":
    st.title("👔 Catálogo de Caballero")
    mostrar_catalogo(st.session_state.productos_caballero, "Catálogo Caballero")

elif st.session_state.seccion == "Carrito":
    st.title("🛒 Tu Carrito de Compras")
    
    if not st.session_state.carrito:
        st.info("Tu carrito está vacío. ¡Explora nuestros catálogos!")
        if st.button("Ir a ver productos"):
            st.session_state.seccion = "Catálogo Dama"
            st.rerun()
    else:
        col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
        col1.write("**Producto**")
        col2.write("**Talla**")
        col3.write("**Cant.**")
        col4.write("**Subtotal**")
        col5.write("**Acción**")
        
        st.markdown("---")
        total = 0.0
        for i, item in enumerate(st.session_state.carrito):
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
            subtotal_item = item['precio'] * item['cantidad']
            total += subtotal_item
            
            col1.write(f"{item['nombre']}")
            col2.write(f"{item['talla']}")
            col3.write(f"{item['cantidad']}")
            col4.write(f"${subtotal_item:.2f}")
            
            if col5.button("🗑️", key=f"del_{i}"):
                st.session_state.carrito.pop(i)
                st.rerun()
        
        st.markdown("---")
        st.subheader(f"Total a Pagar: ${total:.2f} MXN")
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🛍️ Seguir Comprando"):
                st.session_state.seccion = st.session_state.origen_catalogo
                st.rerun()
        with col_btn2:
            if st.button("💳 Finalizar Compra"):
                st.session_state.seccion = "Formulario de Envío"
                st.rerun()

elif st.session_state.seccion == "Formulario de Envío":
    st.title("📦 Datos de Envío")
    st.markdown("---")
    nombre_completo = st.text_input("Nombre Completo:")
    col_dir1, col_dir2 = st.columns([3, 1])
    with col_dir1:
        calle = st.text_input("Calle y Número (Dirección):")
    with col_dir2:
        codigo_postal = st.text_input("Código Postal (CP):")
    col_dir3, col_dir4 = st.columns(2)
    with col_dir3:
        municipio = st.text_input("Municipio / Alcaldía:")
    with col_dir4:
        estado = st.text_input("Estado:")
    col_contacto1, col_contacto2 = st.columns(2)
    with col_contacto1:
        correo = st.text_input("Correo Electrónico:")
    with col_contacto2:
        telefono = st.text_input("Número de Teléfono:")

    st.markdown("<br>", unsafe_allow_html=True)
    col_form_btn1, col_form_btn2 = st.columns(2)

    with col_form_btn1:
        if st.button("❌ Cancelar", use_container_width=True):
            st.session_state.seccion = "Carrito"
            st.rerun()

    with col_form_btn2:
        if st.button("✅ Confirmar compra", use_container_width=True):
            if nombre_completo and calle and codigo_postal and municipio and estado and correo and telefono:
                total_compra = sum(item["precio"] * item["cantidad"] for item in st.session_state.carrito)
                st.session_state.total_compra = total_compra
                st.session_state.nombre_cliente = nombre_completo

                for item_carrito in st.session_state.carrito:
                    id_producto = item_carrito["id"]
                    talla_comprada = item_carrito["talla"]
                    cantidad_comprada = item_carrito["cantidad"]

                    for p in st.session_state.productos_dama:
                        if p["id"] == id_producto:
                            p["stock"][talla_comprada] -= cantidad_comprada

                    for p in st.session_state.productos_caballero:
                        if p["id"] == id_producto:
                            p["stock"][talla_comprada] -= cantidad_comprada

                # Guardar el inventario descontado en el archivo JSON de inmediato
                guardar_datos()

                # Envío de correos
                enviar_alerta_admin(
                    nombre_completo, correo, telefono,
                    st.session_state.carrito, calle, codigo_postal, municipio, estado
                )
                enviar_ticket_comprador(
                    nombre_completo, correo, st.session_state.carrito,
                    calle, codigo_postal, municipio, estado
                )
                verificar_y_alertar_stock(
                    st.session_state.productos_dama, 
                    st.session_state.productos_caballero
                )

                st.session_state.carrito = []
                st.session_state.seccion = "Compra Exitosa"
                st.rerun()
            else:
                st.error("⚠️ Por favor, llena todos los campos de envío.")

elif st.session_state.seccion == "Compra Exitosa":
    st.balloons()
    st.success("✅ Compra realizada con éxito")
    st.markdown(f"### Gracias por tu compra, {st.session_state.nombre_cliente}")
    
    with st.container(border=True):
        st.write("### Total del pedido:")
        st.metric(label="", value=f"${st.session_state.total_compra:.2f} MXN")
        st.markdown("---")
        st.write("🛵 **Gracias por su compra.**")
        st.write("💵 **Recuerde que el pago es contra entrega.**")
        st.write("📩 **Te hemos enviado tu ticket de compra por correo electrónico.**")

    if st.button("🏠 Volver al inicio", use_container_width=True):
        st.session_state.seccion = "Inicio"
        st.rerun()

# --- PANEL DEL ADMINISTRADOR ---
elif st.session_state.seccion == "Administrador":
    if not st.session_state.admin_autenticado:
        st.title("🔒 Acceso Restringido - Panel Administrativo")
        st.markdown("---")
        col_log1, col_log2, col_log3 = st.columns([1, 2, 1])
        with col_log2:
            with st.form("formulario_login"):
                usuario = st.text_input("👤 Cuenta de Usuario:", placeholder="Ej. admin")
                contrasena = st.text_input("🔑 Contraseña:", type="password", placeholder="••••••••")
                boton_ingresar = st.form_submit_button("Ingresar al Sistema", use_container_width=True)
                if boton_ingresar:
                    if usuario == "admin" and contrasena == "12345":
                        st.session_state.admin_autenticado = True
                        st.rerun()
                    else:
                        st.error("❌ Credenciales incorrectas.")
                        
    else:
        col_tit, col_logout = st.columns([4, 1])
        with col_tit:
            st.title("⚙️ Panel de Administración de Inventario")
        with col_logout:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🚪 Cerrar Sesión", use_container_width=True):
                st.session_state.admin_autenticado = False
                st.rerun()
                
        st.markdown("---")
        
        total_dama_piezas = sum(sum(p["stock"].values()) for p in st.session_state.productos_dama)
        total_cab_piezas = sum(sum(p["stock"].values()) for p in st.session_state.productos_caballero)
        
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric("Total Piezas Dama", total_dama_piezas)
        with col_m2:
            st.metric("Total Piezas Caballero", total_cab_piezas)
        with col_m3:
            st.metric("Stock Físico Global", total_dama_piezas + total_cab_piezas)
            
        st.markdown("---")
        
        tab_nuevo, tab_inventario = st.tabs(["➕ Agregar Nueva Prenda", "📋 Ver Inventario Real"])
        
        with tab_nuevo:
            st.subheader("Registrar Artículo con Stock de Tallas")
            with st.form("form_alta_producto", clear_on_submit=True):
                categoria = st.selectbox("Destino del Catálogo:", ["Dama", "Caballero"])
                nombre_p = st.text_input("Nombre de la Prenda:")
                precio_compra = st.number_input("Precio de Compra (Costo):", min_value=1.0, value=100.0)
                desc_p = st.text_area("Descripción:")
                img_p = st.text_input("Enlace URL de la Imagen:", value="https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=400")
                
                st.write("**Definir Stock Inicial por Talla:**")
                c_ch = st.number_input("Cantidad Talla Chica:", min_value=0, value=3, step=1)
                c_m = st.number_input("Cantidad Talla Mediana:", min_value=0, value=3, step=1)
                c_g = st.number_input("Cantidad Talla Grande:", min_value=0, value=3, step=1)
                
                submit_alta = st.form_submit_button("✨ Guardar y Publicar Producto", use_container_width=True)
                
                if submit_alta:
                    if nombre_p and desc_p and img_p:
                        precio_venta = precio_compra * 1.20
                        nuevo_id = f"custom_{categoria.lower()}_{len(st.session_state.productos_dama) + len(st.session_state.productos_caballero) + 1}"
                        nuevo_item = {
                            "id": nuevo_id,
                            "nombre": nombre_p,
                            "precio": precio_venta,
                            "desc": desc_p,
                            "img": img_p,
                            "stock": {"Chico": c_ch, "Mediano": c_m, "Grande": c_g}
                        }
                        
                        if categoria == "Dama":
                            st.session_state.productos_dama.append(nuevo_item)
                        else:
                            st.session_state.productos_caballero.append(nuevo_item)

                        guardar_datos()
                        st.success(f"¡Éxito! Producto agregado. Precio de venta calculado: ${precio_venta:.2f} (20% añadido).")
                        st.rerun()
                    else:
                        st.error("⚠️ Completa todos los campos.")
                        
        with tab_inventario:
            st.subheader("📋 Editar Inventario de Dama")
            if st.session_state.productos_dama:
                df_dama = []
                for p in st.session_state.productos_dama:
                    df_dama.append({
                        "Producto": p["nombre"],
                        "Chico": p["stock"]["Chico"],
                        "Mediano": p["stock"]["Mediano"],
                        "Grande": p["stock"]["Grande"]
                    })
                
                edited_dama = st.data_editor(df_dama, key="editor_dama", use_container_width=True)
                
                if st.button("💾 Guardar cambios en Dama"):
                    for i, row in enumerate(edited_dama):
                        st.session_state.productos_dama[i]["stock"]["Chico"] = row["Chico"]
                        st.session_state.productos_dama[i]["stock"]["Mediano"] = row["Mediano"]
                        st.session_state.productos_dama[i]["stock"]["Grande"] = row["Grande"]
                    guardar_datos()
                    st.success("¡Inventario de Dama actualizado!")
                    st.rerun()

            st.markdown("---")
            
            st.subheader("📋 Editar Inventario de Caballero")
            if st.session_state.productos_caballero:
                df_cab = []
                for p in st.session_state.productos_caballero:
                    df_cab.append({
                        "Producto": p["nombre"],
                        "Chico": p["stock"]["Chico"],
                        "Mediano": p["stock"]["Mediano"],
                        "Grande": p["stock"]["Grande"]
                    })
                
                edited_cab = st.data_editor(df_cab, key="editor_cab", use_container_width=True)
                
                if st.button("💾 Guardar cambios en Caballero"):
                    for i, row in enumerate(edited_cab):
                        st.session_state.productos_caballero[i]["stock"]["Chico"] = row["Chico"]
                        st.session_state.productos_caballero[i]["stock"]["Mediano"] = row["Mediano"]
                        st.session_state.productos_caballero[i]["stock"]["Grande"] = row["Grande"]
                    guardar_datos()
                    st.success("¡Inventario de Caballero actualizado!")
                    st.rerun()