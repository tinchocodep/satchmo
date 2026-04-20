"""Generador de 7 landings HORECA para Satchmo.

Genera 1 archivo HTML por segmento con contenido específico
(hero, productos destacados, caso de uso, formulario).
Corré:  python3 _landings_generator.py
"""
import pathlib
import html

OUT_DIR = pathlib.Path(__file__).parent

# ===================== DATA =====================
LANDINGS = {
    "hoteles": {
        "title": "Hotelería",
        "nav_label": "Hoteles",
        "hero_pre": "Para hoteles y resorts",
        "hero_h1_a": "La panera que <em>tu huésped</em>",
        "hero_h1_b": "recuerda al desayunar.",
        "hero_sub": "Croissants de manteca, medialunas, lactales y multicereales. Producción diaria para buffets y room service, con entrega antes de las 7 AM.",
        "hero_img": "img/hero/hero.jpg",
        "diferencial": "Desde hoteles boutique hasta cadenas, armamos la panera exacta para tu servicio. Calidad consistente todos los días del año.",
        "productos": [
            ("Croissant de Manteca",            "Facturas",       "facturas"),
            ("Docena de Medialunas de Manteca", "Facturas",       "facturas"),
            ("Pan Lactal Brioche",              "Panes Especiales","panes-especiales"),
            ("Pan Lactal Blanco XL",            "Panes Especiales","panes-especiales"),
            ("Molde Multicereal",               "Panes Especiales","panes-especiales"),
            ("Baguetín Soft Grande",            "Panes Especiales","panes-especiales"),
        ],
        "caso_title": "Cómo armamos la panera de un hotel",
        "caso_steps": [
            ("Mapeamos tu servicio", "Cantidad de habitaciones, tipo de desayuno (buffet o room service), horario de mayor demanda."),
            ("Definimos el surtido", "Selección de productos por tipo de huésped y servicio: clásico, premium, integral, sin TACC a pedido."),
            ("Entregamos antes de las 7 AM", "Logística propia en CABA y GBA para que la panera esté lista cuando abrís el salón."),
        ],
        "form_cta": "Armar la panera de tu hotel",
        "form_fields": [
            ("hab",  "Cantidad de habitaciones", "text",   "Ej: 80 habitaciones"),
            ("serv", "Servicio de desayuno",     "select", ["Buffet", "Room service", "Ambos"]),
            ("hora", "Horario preferido de entrega", "text", "Ej: antes de las 6:30 AM"),
        ],
    },
    "hamburgueserias": {
        "title": "Hamburgueserías y Cervecerías",
        "nav_label": "Hamburgueserías",
        "hero_pre": "Para hamburgueserías y cervecerías",
        "hero_h1_a": "El pan puede hacer",
        "hero_h1_b": "la <em>mejor hamburguesa</em>.",
        "hero_sub": "Pan hamburguesa premium en 12 variantes. Clásico, black, green, papa, queso, salvado, vegano, multicereal, celeste. Todos con consistencia de producción industrial.",
        "hero_img": "img/hero/hero.jpg",
        "diferencial": "De smash burgers de barrio a cervecerías con 10 sucursales: el mismo pan premium, el mismo día, todo el año.",
        "productos": [
            ("Pan Hamburguesa Premium",             "Panes de Viena", "panes-viena"),
            ("Pan Hamburguesa Premium Black",       "Panes de Viena", "panes-viena"),
            ("Pan Hamburguesa Premium Green",       "Panes de Viena", "panes-viena"),
            ("Pan Hamburguesa Premium Papa",        "Panes de Viena", "panes-viena"),
            ("Pan Hamburguesa Premium Queso",       "Panes de Viena", "panes-viena"),
            ("Pan Hamburguesa Premium Multicereal", "Panes de Viena", "panes-viena"),
        ],
        "caso_title": "Cómo trabajamos con hamburgueserías",
        "caso_steps": [
            ("Probás nuestro pan", "Te mandamos muestra sin costo de las variantes que te interesan."),
            ("Definimos volumen y variantes", "Pedido base + flex semanal. Te entregamos 1 a 3 veces por semana según rotación."),
            ("Escalamos con tu negocio", "Si abrís sucursal, el mismo pan está disponible sin set-up nuevo."),
        ],
        "form_cta": "Probar nuestros panes premium",
        "form_fields": [
            ("vol",  "Volumen semanal estimado", "text",   "Ej: 500 panes/semana"),
            ("var",  "Variantes de interés",     "text",   "Ej: premium, black, papa"),
            ("zona", "Zona del local",           "text",   "Ej: Palermo / La Plata / Zona Sur"),
        ],
    },
    "buffets-cafeterias": {
        "title": "Buffets y Cafeterías",
        "nav_label": "Buffets y cafeterías",
        "hero_pre": "Para buffets y cafeterías",
        "hero_h1_a": "Desayunos que",
        "hero_h1_b": "<em>vuelven a pedir</em>.",
        "hero_sub": "Medialunas, facturas, croissants, budines, cookies. Producción diaria para que tu mostrador nunca quede vacío en hora pico.",
        "hero_img": "img/hero/hero.jpg",
        "diferencial": "Desayuno y merienda son la batalla diaria de tu cafetería. Te damos el surtido y la consistencia para ganarla.",
        "productos": [
            ("Docena de Medialunas de Manteca", "Facturas",         "facturas"),
            ("Docena de Facturas Surtidas",     "Facturas",         "facturas"),
            ("Croissant de Manteca",            "Facturas",         "facturas"),
            ("Budín de Limón",                  "Budines",          "budines"),
            ("Cookies de Vainilla con Chips",   "Pastelería por Kilo","pasteleria-kg"),
            ("Rosquitas Españolas",             "Pastelería por Kilo","pasteleria-kg"),
        ],
        "caso_title": "Cómo trabajamos con buffets y cafeterías",
        "caso_steps": [
            ("Entendemos tu flujo", "Cuántos desayunos/día, hora pico, qué se vende más y qué querés probar."),
            ("Armamos surtido + freezer", "Una parte fresca del día, otra congelada para extender stock sin merma."),
            ("Reabastecemos semanal o diario", "Elegís la frecuencia. Te avisamos si vemos que te estás quedando corto."),
        ],
        "form_cta": "Pedir muestra de desayunos",
        "form_fields": [
            ("pers", "Personas/día aproximadas",   "text",   "Ej: 200 desayunos/día"),
            ("frec", "Frecuencia deseada",         "select", ["Diaria", "Día por medio", "3x semana", "Semanal"]),
            ("hora", "Horario preferido de entrega","text", "Ej: antes de las 6 AM"),
        ],
    },
    "catering": {
        "title": "Catering y Eventos",
        "nav_label": "Catering",
        "hero_pre": "Para catering y eventos",
        "hero_h1_a": "Volumen alto,",
        "hero_h1_b": "<em>fecha clavada</em>.",
        "hero_sub": "Sándwiches de miga, copetines, surtidos de facturas, tarteletas y masas finas. Producción pensada para eventos de 50 a 2.000 personas.",
        "hero_img": "img/hero/hero.jpg",
        "diferencial": "El catering no tiene segundas chances. Producción dedicada para el día del evento, sin romper tu margen.",
        "productos": [
            ("Docena de Facturas Surtidas", "Facturas",          "facturas"),
            ("Masas Finas",                 "Pastelería por Kilo","pasteleria-kg"),
            ("Pan de Lomito",               "Panes de Viena",     "panes-viena"),
            ("Pebete Chico",                "Panes de Viena",     "panes-viena"),
            ("Tarta Individual Caprese",    "Empanadas y Tartas", "empanadas-tartas"),
            ("Brownie",                     "Porciones",          "porciones"),
        ],
        "caso_title": "Cómo trabajamos con caterings",
        "caso_steps": [
            ("Cotizamos tu evento", "Pasaje un brief: tipo de evento, personas, fecha, hora. Te devolvemos propuesta en 24-48 hs."),
            ("Producción dedicada", "Reservamos planta para tu fecha. Entregamos el día, en el horario que definas."),
            ("Post-evento", "Feedback corto: qué funcionó, qué ajustar. Sos cliente, no un pedido único."),
        ],
        "form_cta": "Cotizar para tu evento",
        "form_fields": [
            ("tipo",  "Tipo de evento",        "text",   "Ej: casamiento, corporativo, fiesta"),
            ("pers",  "Cantidad de personas",  "text",   "Ej: 150 personas"),
            ("fecha", "Fecha del evento",      "text",   "Ej: 15/09/2026"),
            ("pres",  "Presupuesto orientativo","text",  "Opcional"),
        ],
    },
    "canchas-clubes": {
        "title": "Canchas y Clubes",
        "nav_label": "Canchas y clubes",
        "hero_pre": "Para canchas, clubes y gimnasios",
        "hero_h1_a": "Día de partido,",
        "hero_h1_b": "<em>pan que no falla</em>.",
        "hero_sub": "Super pancho soft 30cm y 60cm, pan hamburguesa premium, prepizzas. Packs pensados para el pico de venta de los fines de semana y partidos.",
        "hero_img": "img/hero/hero.jpg",
        "diferencial": "Fines de semana y partidos son el 70% de tu facturación. No te la podemos fallar — por eso tenemos línea dedicada.",
        "productos": [
            ("Super Pancho 30 cm",           "Panes de Viena",    "panes-viena"),
            ("Super Pancho 60 cm",           "Panes de Viena",    "panes-viena"),
            ("Super Pancho Soft",            "Panes de Viena",    "panes-viena"),
            ("Pan Hamburguesa Premium",      "Panes de Viena",    "panes-viena"),
            ("Prepizza de Tomate",           "Empanadas y Tartas","empanadas-tartas"),
            ("Pan Hamburguesa Premium Maxi", "Panes de Viena",    "panes-viena"),
        ],
        "caso_title": "Cómo armamos el pack para tu cancha",
        "caso_steps": [
            ("Mapeamos tu semana", "Qué días tenés más gente, qué se vende (pancho, hamburguesa, pizza), qué querés sumar."),
            ("Pack base + refuerzo de fin de semana", "Entrega diaria de fresco + congelado de reserva para picos."),
            ("Campaña Mundial", "Con el Mundial 2026 garantizamos stock en semana de partidos con entrega reforzada."),
        ],
        "form_cta": "Armar tu pack para la cancha",
        "form_fields": [
            ("act",  "Tipo de actividad",     "select", ["Cancha fútbol 5", "Club deportivo", "Gimnasio", "Otro"]),
            ("pico", "Días de mayor demanda", "text",   "Ej: viernes a domingo"),
            ("vol",  "Volumen estimado",      "text",   "Ej: 300 panchos/fin de semana"),
        ],
    },
    "restaurantes": {
        "title": "Restaurantes",
        "nav_label": "Restaurantes",
        "hero_pre": "Para restaurantes",
        "hero_h1_a": "La panera",
        "hero_h1_b": "<em>que te representa</em>.",
        "hero_sub": "Pan de campo, chapatta, figazzas, trenzas, baguetines soft. Variedad artesanal con consistencia industrial para tu mesa.",
        "hero_img": "img/hero/hero.jpg",
        "diferencial": "La panera es la primera impresión. Un pan correcto no alcanza: tiene que alinear con la identidad de tu cocina.",
        "productos": [
            ("Pan de Campo 500 g",            "Panes Especiales", "panes-especiales"),
            ("Chapatta",                      "Panes Especiales", "panes-especiales"),
            ("Figaza con Sésamo 170 g",       "Panes Especiales", "panes-especiales"),
            ("Trenza de Sésamo",              "Panes Especiales", "panes-especiales"),
            ("Baguetín Soft con Corte",       "Panes Especiales", "panes-especiales"),
            ("Mini Baguette Soft con Semilla","Panificados Horneados", "panificados-horno"),
        ],
        "caso_title": "Cómo armamos la panera de tu restó",
        "caso_steps": [
            ("Probamos 3 paneras", "Te mandamos tres combinaciones posibles para que elijas la que va con tu cocina."),
            ("Afinamos el surtido", "Ajustamos según feedback del equipo y los comensales durante 2-3 semanas."),
            ("Entrega diaria o día por medio", "Fresco del día. Logística propia en CABA y GBA."),
        ],
        "form_cta": "Armar la panera de tu restó",
        "form_fields": [
            ("cocina","Tipo de cocina",         "text",   "Ej: cocina de autor / italiana / bistró"),
            ("cub",   "Cantidad de cubiertos",  "text",   "Ej: 80 cubiertos/turno"),
            ("frec",  "Frecuencia preferida",   "select", ["Diaria", "Día por medio", "3x semana"]),
        ],
    },
    "panaderias": {
        "title": "Panaderías y Distribuidores",
        "nav_label": "Panaderías",
        "hero_pre": "Para panaderías y distribuidores",
        "hero_h1_a": "Catálogo completo,",
        "hero_h1_b": "<em>precio mayorista</em>.",
        "hero_sub": "Crudo por lata (medialunas, vigilantes, sacramentos, scones), congelados y pre-cocidos. Toda nuestra planta al servicio de tu mostrador.",
        "hero_img": "img/hero/hero.jpg",
        "diferencial": "Si tenés mostrador propio, te damos catálogo mayorista y logística regular para que no dependas del proveedor del barrio.",
        "productos": [
            ("Lata de Medialunas de Manteca 40/60 (36u)", "Facturas", "facturas"),
            ("Lata de Vigilante Sacramento 40/60 (66u)",  "Facturas", "facturas"),
            ("Lata de Surtido de Hojaldre 40/60 (40u)",   "Facturas", "facturas"),
            ("Miñón Pre-cocido — Bolsa 3 kg",             "Panificados Crudo/Pre-cocido", "panificados-crudo"),
            ("Baguette Pre-cocida — Bolsa 3 kg",          "Panificados Crudo/Pre-cocido", "panificados-crudo"),
            ("Medialunas de Manteca Congeladas — Bolsa 12 unidades", "Línea Congelado", "congelados"),
        ],
        "caso_title": "Cómo trabajamos con panaderías",
        "caso_steps": [
            ("Te mostramos el catálogo mayorista", "220 productos disponibles: crudo, pre-cocido, horneado y congelado."),
            ("Definimos líneas y volumen mensual", "Precio escalonado por volumen. Logística propia en CABA/GBA, coordinada para interior."),
            ("Reposición regular sin fricción", "Te reabastecemos semanal o quincenal, con alertas si se viene rotura de stock."),
        ],
        "form_cta": "Ver catálogo completo mayorista",
        "form_fields": [
            ("zona", "Zona de distribución", "text", "Ej: CABA / GBA / Mar del Plata"),
            ("vol",  "Volumen mensual estimado", "text", "Ej: 40 latas/mes"),
            ("lin",  "Líneas de interés", "text", "Ej: facturas, congelados, pre-cocidos"),
        ],
    },
}

# ===================== HTML PIECES =====================
COMMON_CSS = """*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{--dark:#0f0f0f;--cream:#f7f6f3;--mid:#e8e6e1;--accent:#b8975a;--accent-light:#d4b87a;--text:#1a1a1a;--text-s:#888;--text-inv:#f7f6f3;--serif:'Cormorant Garamond',Georgia,serif;--sans:'Outfit',system-ui,sans-serif}
html{scroll-behavior:smooth}
body{font-family:var(--sans);color:var(--text);background:var(--cream);-webkit-font-smoothing:antialiased;overflow-x:hidden}
::selection{background:var(--accent);color:#fff}
img{display:block;max-width:100%}a{color:inherit;text-decoration:none}
[data-a]{opacity:0;transform:translateY(28px);transition:opacity .8s cubic-bezier(.16,1,.3,1),transform .8s cubic-bezier(.16,1,.3,1)}
[data-a].v{opacity:1;transform:none}
[data-a][data-d="1"]{transition-delay:.12s}[data-a][data-d="2"]{transition-delay:.24s}[data-a][data-d="3"]{transition-delay:.36s}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:6px 24px;display:flex;align-items:center;justify-content:space-between;transition:all .4s}
nav.s{background:rgba(247,246,243,.92);backdrop-filter:blur(20px);padding:4px 24px}
.nav-logo{height:72px;width:auto;transition:all .4s;position:relative;z-index:101}
nav.s .nav-logo{height:56px}
.nk{display:none;gap:28px;list-style:none}
.nk a{font-family:var(--sans);font-size:12px;font-weight:400;letter-spacing:.15em;text-transform:uppercase;color:var(--text);opacity:.5;transition:opacity .3s}.nk a.inv{color:var(--text-inv)}nav.s .nk a{color:var(--text)!important}.nk a:hover{opacity:1}
.nh{display:flex;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:6px}
.nh span{width:20px;height:1px;background:var(--text);transition:all .4s}.nh.inv span{background:var(--text-inv)}nav.s .nh span{background:var(--text)!important}
@media(min-width:900px){.nk{display:flex}.nh{display:none}nav{padding:8px 40px}nav.s{padding:4px 40px}}

/* HERO */
.hero{position:relative;min-height:560px;height:70vh;overflow:hidden;display:flex;align-items:flex-end}
.hero__img{position:absolute;inset:0;background:center/cover no-repeat}
.hero__ov{position:absolute;inset:0;background:linear-gradient(to top,rgba(15,15,15,.78) 0%,rgba(15,15,15,.22) 55%,rgba(15,15,15,.35) 100%)}
.hero__c{position:relative;z-index:2;padding:0 32px 64px;width:100%;max-width:920px}
.hero__pre{font-family:var(--sans);font-size:11px;font-weight:400;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);margin-bottom:20px;opacity:0;animation:fu .8s .4s forwards}
.hero__h1{font-family:var(--serif);font-size:clamp(36px,6vw,68px);font-weight:300;color:var(--text-inv);line-height:1.08;margin-bottom:20px;opacity:0;animation:fu .8s .6s forwards}.hero__h1 em{font-style:italic}
.hero__sub{font-family:var(--sans);font-size:15px;font-weight:300;color:rgba(247,246,243,.7);line-height:1.75;max-width:520px;margin-bottom:32px;opacity:0;animation:fu .8s .8s forwards}
.hcta{display:inline-flex;align-items:center;gap:10px;padding:14px 0;font-family:var(--sans);font-size:12px;font-weight:400;letter-spacing:.15em;text-transform:uppercase;color:var(--text-inv);border-bottom:1px solid rgba(247,246,243,.3);transition:all .4s;opacity:0;animation:fu .8s 1s forwards}
.hcta:hover{border-color:var(--accent);color:var(--accent)}.hcta svg{width:16px;height:16px;transition:transform .3s}.hcta:hover svg{transform:translateX(4px)}
@keyframes fu{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
@media(min-width:900px){.hero__c{padding:0 48px 80px}}

/* BREADCRUMB */
.bc{padding:12px 32px;font-family:var(--sans);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--text-s);border-bottom:1px solid var(--mid)}
.bc a{color:var(--text-s);transition:color .3s}.bc a:hover{color:var(--text)}
.bc span{margin:0 10px;color:var(--accent)}
@media(min-width:900px){.bc{padding:14px 48px}}

/* SECTIONS */
.sec{padding:90px 32px}.sec--d{background:var(--dark);color:var(--text-inv)}
.si{max-width:1000px;margin:0 auto}
.pre{font-family:var(--sans);font-size:11px;font-weight:400;letter-spacing:.2em;text-transform:uppercase;color:var(--text-s);margin-bottom:18px}.sec--d .pre{color:rgba(247,246,243,.3)}
.h2{font-family:var(--serif);font-size:clamp(28px,4.5vw,44px);font-weight:300;line-height:1.2;margin-bottom:20px}
.pp{font-family:var(--sans);font-size:15px;font-weight:300;line-height:1.8;color:var(--text-s);max-width:520px}.sec--d .pp{color:rgba(247,246,243,.55)}
@media(min-width:900px){.sec{padding:120px 48px}}

/* PRODUCTOS GRID */
.prods{display:grid;gap:1px;margin-top:48px;background:var(--mid);border:1px solid var(--mid)}
.pcard{background:var(--cream);padding:28px;transition:background .4s;display:flex;flex-direction:column;gap:6px}
.pcard:hover{background:#fff}
.pcard .pcat{font-family:var(--sans);font-size:10px;font-weight:500;letter-spacing:.15em;text-transform:uppercase;color:var(--accent)}
.pcard .pn{font-family:var(--serif);font-size:22px;font-weight:400;line-height:1.25;color:var(--text)}
.pcard .plk{font-family:var(--sans);font-size:12px;letter-spacing:.08em;color:var(--text-s);margin-top:10px;display:inline-flex;align-items:center;gap:6px;transition:color .3s,gap .3s}
.pcard:hover .plk{color:var(--accent);gap:10px}
@media(min-width:640px){.prods{grid-template-columns:1fr 1fr}}
@media(min-width:900px){.prods{grid-template-columns:1fr 1fr 1fr}}

/* STEPS */
.steps{display:grid;gap:48px;margin-top:56px}
.sn{font-family:var(--serif);font-size:clamp(48px,6vw,72px);font-weight:300;color:var(--accent);opacity:.25;line-height:1;margin-bottom:8px}
.st{font-family:var(--sans);font-size:12px;font-weight:500;letter-spacing:.15em;text-transform:uppercase;color:var(--text-inv);margin-bottom:10px}
.sp{font-family:var(--sans);font-size:14px;font-weight:300;line-height:1.8;color:rgba(247,246,243,.55);max-width:340px}
@media(min-width:768px){.steps{grid-template-columns:repeat(3,1fr);gap:32px}}

/* FORM */
.cg{display:grid;gap:48px}
.cwa{display:inline-flex;align-items:center;gap:10px;padding:14px 0;font-family:var(--sans);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);border-bottom:1px solid var(--accent);transition:all .3s;margin-bottom:24px}.cwa:hover{color:var(--text);border-color:var(--text)}
.fg{margin-bottom:20px}.fg label{display:block;font-family:var(--sans);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--text-s);margin-bottom:8px}
.fg input,.fg select,.fg textarea{width:100%;padding:12px 0;border:none;border-bottom:1px solid var(--mid);background:transparent;font-family:var(--sans);font-size:14px;font-weight:300;color:var(--text);transition:border-color .3s;border-radius:0;-webkit-appearance:none}
.fg input:focus,.fg select:focus,.fg textarea:focus{outline:none;border-color:var(--text)}.fg textarea{min-height:80px;resize:vertical}
.fr{display:grid;gap:20px}
.fbtn{padding:14px 0;background:transparent;border:none;border-bottom:1px solid var(--text);font-family:var(--sans);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--text);cursor:pointer;transition:all .3s}.fbtn:hover{border-color:var(--accent);color:var(--accent)}
.fnote{font-family:var(--sans);font-size:12px;color:var(--text-s);margin-top:16px;font-weight:300}
@media(min-width:768px){.cg{grid-template-columns:1fr 1fr;gap:72px;align-items:start}.fr{grid-template-columns:1fr 1fr}}

/* OTHER SEGMENTS */
.other{padding:64px 32px;background:var(--cream);border-top:1px solid var(--mid)}
.other__t{font-family:var(--sans);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--text-s);margin-bottom:18px}
.other__g{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px}
.other__l{padding:14px 18px;border:1px solid var(--mid);background:#fff;font-family:var(--sans);font-size:13px;color:var(--text);transition:all .3s;text-align:left}
.other__l:hover{border-color:var(--text);color:var(--accent)}
@media(min-width:900px){.other{padding:72px 48px}}

/* FOOTER */
footer{background:var(--dark);color:var(--text-inv);padding:64px 32px 32px}
.fi{max-width:1000px;margin:0 auto}.fgr{display:grid;gap:36px;margin-bottom:48px}
.ft{font-family:var(--sans);font-size:10px;letter-spacing:.15em;text-transform:uppercase;color:rgba(247,246,243,.3);margin-bottom:14px}
.flogo{font-family:var(--sans);font-size:13px;font-weight:500;letter-spacing:.25em;text-transform:uppercase;margin-bottom:10px}
.ftag{font-family:var(--sans);font-size:13px;font-weight:300;color:rgba(247,246,243,.4);line-height:1.6}
.flk{list-style:none}.flk li+li{margin-top:10px}.flk a{font-family:var(--sans);font-size:13px;font-weight:300;color:rgba(247,246,243,.45);transition:color .3s}.flk a:hover{color:var(--accent)}
.fbot{border-top:1px solid rgba(255,255,255,.06);padding-top:24px;font-family:var(--sans);font-size:11px;font-weight:300;color:rgba(247,246,243,.2)}
@media(min-width:768px){.fgr{grid-template-columns:2fr 1fr 1fr 1fr}footer{padding:72px 48px 32px}}

/* WA */
.waf{position:fixed;bottom:28px;right:28px;z-index:90;width:52px;height:52px;border-radius:50%;background:var(--accent);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 24px rgba(184,151,90,.3);transition:transform .3s}.waf:hover{transform:scale(1.08)}.waf svg{width:24px;height:24px;fill:#fff}
@media(max-width:767px){.waf{width:48px;height:48px;bottom:20px;right:20px}}
"""

WA_SVG = '<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347zM12 0C5.373 0 0 5.373 0 12c0 2.625.846 5.059 2.284 7.034L.789 23.492a.5.5 0 00.611.611l4.458-1.495A11.94 11.94 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-2.326 0-4.48-.764-6.219-2.055l-.435-.334-2.998 1.005 1.005-2.998-.334-.435A9.96 9.96 0 012 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/></svg>'

ARROW_SVG = '<svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def render_product_card(name, cat_label, cat_slug):
    wa_text = f"Hola Satchmo, consulto por {name}"
    wa_url = "https://wa.me/5491126952459?text=" + _url_encode(wa_text)
    cat_link = f"productos.html#{cat_slug}"
    return f"""      <div class="pcard">
        <a class="pcat" href="{cat_link}">{html.escape(cat_label)}</a>
        <div class="pn">{html.escape(name)}</div>
        <a class="plk" href="{wa_url}" target="_blank" rel="noopener">Pedir muestra {ARROW_SVG}</a>
      </div>"""


def render_form_field(fid, label, ftype, placeholder_or_options):
    if ftype == "select":
        opts = "".join(f'<option>{html.escape(o)}</option>' for o in placeholder_or_options)
        return f'<div class="fg"><label>{html.escape(label)}</label><select id="{fid}"><option value="">Seleccioná</option>{opts}</select></div>'
    return f'<div class="fg"><label>{html.escape(label)}</label><input type="text" id="{fid}" placeholder="{html.escape(placeholder_or_options)}"></div>'


def render_other_segments(current_slug):
    items = []
    for slug, data in LANDINGS.items():
        if slug == current_slug:
            continue
        items.append(f'<a class="other__l" href="{slug}.html">{html.escape(data["nav_label"])} →</a>')
    return "\n        ".join(items)


def _url_encode(s):
    from urllib.parse import quote
    return quote(s)


def render_landing(slug, d):
    page_title = f"{d['title']} — Satchmo Panificados"
    meta_desc = d["hero_sub"]
    products_html = "\n".join(render_product_card(n, c, cs) for n, c, cs in d["productos"])
    steps_html = ""
    for i, (t, p) in enumerate(d["caso_steps"], start=1):
        steps_html += f'<div><div class="sn">{i:02d}</div><div class="st">{html.escape(t)}</div><p class="sp">{html.escape(p)}</p></div>\n        '
    form_fields_html = "\n        ".join(render_form_field(*f) for f in d["form_fields"])
    others_html = render_other_segments(slug)
    wa_prefill = _url_encode(f"Hola Satchmo, vengo desde la landing de {d['title']} y quiero consultar.")

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(page_title)}</title>
<meta name="description" content="{html.escape(meta_desc)}">
<link rel="icon" type="image/x-icon" href="img/favicon.ico">
<link rel="apple-touch-icon" sizes="180x180" href="img/favicon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Outfit:wght@300;400;500&display=swap" rel="stylesheet">
<style>
{COMMON_CSS}
</style>
</head>
<body>

<nav id="nav">
  <a href="index.html" class="nl inv"><img src="img/logo.png" alt="Satchmo" class="nav-logo"></a>
  <ul class="nk"><li><a href="index.html#nosotros" class="inv">Nosotros</a></li><li><a href="productos.html" class="inv">Catálogo</a></li><li><a href="index.html#como-trabajamos" class="inv">Proceso</a></li><li><a href="#contacto" class="inv">Contacto</a></li></ul>
  <button class="nh inv" id="ham" aria-label="Menú"><span></span><span></span><span></span></button>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero__img" style="background-image:url('{d['hero_img']}')"></div>
  <div class="hero__ov"></div>
  <div class="hero__c">
    <p class="hero__pre">{html.escape(d['hero_pre'])}</p>
    <h1 class="hero__h1">{d['hero_h1_a']}<br>{d['hero_h1_b']}</h1>
    <p class="hero__sub">{html.escape(d['hero_sub'])}</p>
    <a href="#contacto" class="hcta">{html.escape(d['form_cta'])} {ARROW_SVG}</a>
  </div>
</section>

<!-- BREADCRUMB -->
<div class="bc"><a href="index.html">Satchmo</a><span>/</span>Segmentos<span>/</span>{html.escape(d['title'])}</div>

<!-- PRODUCTOS DESTACADOS -->
<section class="sec">
  <div class="si">
    <div data-a>
      <p class="pre">Productos destacados</p>
      <h2 class="h2">Lo que más se lleva tu segmento.</h2>
      <p class="pp">{html.escape(d['diferencial'])}</p>
    </div>
    <div class="prods" data-a data-d="1">
{products_html}
    </div>
    <p style="margin-top:32px;font-family:var(--sans);font-size:13px;color:var(--text-s);font-weight:300"><a href="productos.html" style="color:var(--accent);border-bottom:1px solid var(--accent);padding-bottom:2px">Ver catálogo completo — 220 productos →</a></p>
  </div>
</section>

<!-- COMO TRABAJAMOS -->
<section class="sec sec--d">
  <div class="si">
    <div data-a>
      <p class="pre">Proceso</p>
      <h2 class="h2">{html.escape(d['caso_title'])}</h2>
    </div>
    <div class="steps" data-a>
        {steps_html.rstrip()}
    </div>
  </div>
</section>

<!-- CONTACTO -->
<section class="sec" id="contacto">
  <div class="si">
    <div class="cg">
      <div data-a>
        <p class="pre">Contacto</p>
        <h2 class="h2">{html.escape(d['form_cta'])}.</h2>
        <p class="pp" style="margin-bottom:36px">Contanos un poco sobre tu operación y te armamos una propuesta en menos de 24 hs. Sin compromiso.</p>
        <a href="https://wa.me/5491126952459?text={wa_prefill}" class="cwa" target="_blank" rel="noopener">Escribinos por WhatsApp →</a>
      </div>
      <div data-a data-d="2">
        <div class="fr"><div class="fg"><label>Nombre y apellido</label><input type="text" id="fn" placeholder="Tu nombre"></div><div class="fg"><label>Empresa / local</label><input type="text" id="bn" placeholder="Nombre de tu negocio"></div></div>
        <div class="fr"><div class="fg"><label>Email</label><input type="email" id="em" placeholder="tu@email.com"></div><div class="fg"><label>Teléfono</label><input type="tel" id="tl" placeholder="+54 11..."></div></div>
        <div class="fr">{form_fields_html}</div>
        <div class="fg"><label>Mensaje (opcional)</label><textarea id="ms" placeholder="Contanos qué necesitás..."></textarea></div>
        <input type="hidden" id="seg" value="{html.escape(d['title'])}">
        <button type="button" class="fbtn" id="sendBtn">Enviar consulta →</button>
        <p class="fnote">Te respondemos en menos de 24 horas hábiles.</p>
      </div>
    </div>
  </div>
</section>

<!-- OTROS SEGMENTOS -->
<section class="other">
  <div class="si">
    <div class="other__t">Ver otras landings por segmento</div>
    <div class="other__g">
        {others_html}
    </div>
  </div>
</section>

<footer>
  <div class="fi">
    <div class="fgr">
      <div><div class="flogo">Satchmo</div><p class="ftag">Proveedor de panificados<br>para gastronomía<br>Buenos Aires, Argentina</p></div>
      <div><div class="ft">Navegación</div><ul class="flk"><li><a href="index.html#nosotros">Nosotros</a></li><li><a href="productos.html">Catálogo</a></li><li><a href="index.html#como-trabajamos">Proceso</a></li><li><a href="index.html#contacto">Contacto</a></li></ul></div>
      <div><div class="ft">Segmentos</div><ul class="flk"><li><a href="buffets-cafeterias.html">Buffets y cafeterías</a></li><li><a href="hamburgueserias.html">Hamburgueserías</a></li><li><a href="hoteles.html">Hoteles</a></li><li><a href="catering.html">Catering</a></li></ul></div>
      <div><div class="ft">Contacto</div><ul class="flk"><li><a href="tel:+5491126952459">+54 9 11 2695-2459</a></li><li><a href="mailto:satchmopanificados@gmail.com">satchmopanificados@gmail.com</a></li><li><a href="https://wa.me/5491126952459" target="_blank">WhatsApp</a></li></ul></div>
    </div>
    <div class="fbot">© 2026 Satchmo — Panificadora Satchmo S.A.</div>
  </div>
</footer>

<a href="https://wa.me/5491126952459?text={wa_prefill}" class="waf" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>

<script>
const nv=document.getElementById('nav');
window.addEventListener('scroll',()=>{{nv.classList.toggle('s',scrollY>80);const inv=scrollY<=80;document.querySelectorAll('.nl,.nk a').forEach(el=>el.classList.toggle('inv',inv));document.querySelector('.nh')?.classList.toggle('inv',inv)}});

const obs=new IntersectionObserver(es=>{{es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('v');obs.unobserve(e.target)}}}})}},{{threshold:.1}});
document.querySelectorAll('[data-a]').forEach(el=>obs.observe(el));
setTimeout(()=>document.querySelectorAll('[data-a]').forEach(el=>el.classList.add('v')),3000);

document.getElementById('sendBtn').addEventListener('click',()=>{{
  const g=id=>document.getElementById(id).value;
  const seg=g('seg'),fn=g('fn'),bn=g('bn'),em=g('em'),tl=g('tl'),ms=g('ms');
  const extra=Array.from(document.querySelectorAll('.fr .fg input, .fr .fg select')).filter(i=>!['fn','bn','em','tl'].includes(i.id)).map(i=>{{
    const lbl=i.previousElementSibling?.textContent||i.id;
    return lbl+': '+i.value;
  }}).filter(s=>!s.endsWith(': ')).join('\\n');
  const txt=`Hola Satchmo, consulta desde landing ${{seg}}:\\n\\nNombre: ${{fn}}\\nEmpresa: ${{bn}}\\nEmail: ${{em}}\\nTel: ${{tl}}\\n${{extra}}\\n\\nMensaje: ${{ms}}`;
  window.open('https://wa.me/5491126952459?text='+encodeURIComponent(txt),'_blank');
}});
</script>
</body>
</html>
"""


def main():
    for slug, data in LANDINGS.items():
        out = OUT_DIR / f"{slug}.html"
        out.write_text(render_landing(slug, data), encoding="utf-8")
        print(f"✓ {out.name}")
    print(f"\nGenerated {len(LANDINGS)} landings.")


if __name__ == "__main__":
    main()
