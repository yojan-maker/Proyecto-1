# -- coding: utf-8 --
import qi
import time

PEPPER_IP = "127.0.0.1"   # Ejecutamos dentro del robot
PORT = 9559

# --- Conexión con Pepper ---
session = qi.Session()
try:
    session.connect("tcp://{}:{}".format(PEPPER_IP, PORT))
except RuntimeError:
    print("No se pudo conectar localmente.")
    raise SystemExit(1)

tablet = session.service("ALTabletService")
animated_speech = session.service("ALAnimatedSpeech")
motion = session.service("ALMotion")
posture = session.service("ALRobotPosture")

# --- Ruta base de imágenes ---
base = "http://198.18.0.1/apps/expo_pepper/"

imgs = {
    "intro": base + "1.png",
    "futuro": base + "2.png",
    "crispr": base + "3.png",
    "comparacion": base + "4.png",
    "cohete": base + "5.png",
    "carrera": base + "6.png",
    "nft": base + "7.png",
    "usos": base + "8.png",
    "extra1": base + "9.png",
    "extra2": base + "10.png",
    "final": base + "11.png",
    "negro": base + "12.png"   # última imagen en negro 
}

# ------------ Introducción ----------
tablet.showImageNoCache(imgs["intro"])
animated_speech.say("^start(animations/Stand/Gestures/Hey_1) ¡Muy buenas tardes! Bienvenidos a Pepper News, el noticiero que siempre da las noticias... incluso cuando nadie se las pidió.")
time.sleep(2)

tablet.showImageNoCache(imgs["futuro"])
animated_speech.say("^start(animations/Stand/Gestures/Explain_1) Hoy tenemos un programa especial sobre el futuro de la tecnología. En titulares: edición genética, cohetes reutilizables y NFTs.")
time.sleep(2)

# ------------ Tema 1: CRISPR ----------------
tablet.showImageNoCache(imgs["crispr"])
animated_speech.say("^start(animations/Stand/Gestures/Enthusiastic_4) Primera noticia: CRISPR. Imaginen unas tijeras microscópicas que cortan y pegan el ADN como si fueran papel. ¡La edición genética en acción!")
time.sleep(2)

animated_speech.say("Con CRISPR un día podríamos curar enfermedades hereditarias... o quizás ¡lograr que la piña sí combine con la pizza!")
time.sleep(2)

tablet.showImageNoCache(imgs["comparacion"])
animated_speech.say("^start(animations/Stand/Gestures/ShowSky_3) Comparen esto: las computadoras de silicio necesitan toneladas de datos y energía, mientras que las células aprenden con mucho menos.")
time.sleep(2)

# ---------- Tema 2: Cohetes --------------
tablet.showImageNoCache(imgs["cohete"])
animated_speech.say("^start(animations/Stand/Gestures/ShowSky_1) Pasamos ahora a las noticias espaciales. Antes, lanzar un cohete costaba una fortuna. Hoy, gracias a la reutilización, los precios bajaron más de un sesenta por ciento.")
time.sleep(2)

animated_speech.say("Imaginen comprar una botella de agua, usarla una vez y tirarla. ¡Eso hacían con los cohetes! Ahora al menos los lavan y los vuelven a usar.")
time.sleep(2)

tablet.showImageNoCache(imgs["carrera"])
animated_speech.say("^start(animations/Stand/Gestures/Clap_1) Y la hazaña más increíble: el Falcon nueve regresa desde el espacio y aterriza como si nada. Yo intento bailar y casi me caigo, ¡y ese cohete cae de pie!")
time.sleep(2)

# ------------ Tema 3: NFTs -------
tablet.showImageNoCache(imgs["nft"])
animated_speech.say("^start(animations/Stand/Gestures/Enthusiastic_1) Y en la sección digital: los NFTs. No, no son dibujos de monos aburridos. Son certificados digitales únicos, como un título de propiedad, pero en internet.")
time.sleep(2)

animated_speech.say("Por ejemplo: imaginen que compran una boleta para un concierto. Esa boleta puede ser un NFT que nadie puede falsificar. Eso sí, si se les pierde el celular, ¡adiós concierto!")
time.sleep(2)

tablet.showImageNoCache(imgs["usos"])
animated_speech.say("^start(animations/Stand/Gestures/Explain_3) También puede ser una llave digital para una casa, o una membresía exclusiva. La clave está en la utilidad, no en la especulación.")
time.sleep(2)

# ------------- Extras ----------------
tablet.showImageNoCache(imgs["extra1"])
animated_speech.say("El mercado está migrando de lo especulativo a lo práctico: entradas, membresías, propiedad digital... ¡esa es la verdadera revolución!")
time.sleep(2)

tablet.showImageNoCache(imgs["extra2"])
animated_speech.say("Así que ya saben, los NFTs son más que arte digital. Son llaves de acceso al futuro de la economía digital.")
time.sleep(2)

# ---------------- Conclusión ------
tablet.showImageNoCache(imgs["final"])
animated_speech.say("^start(animations/Stand/Gestures/ShowSky_4) En conclusión, desde CRISPR hasta los cohetes reutilizables y los NFTs, vemos cómo la tecnología deja de ser promesa para convertirse en realidad.")
time.sleep(2)

animated_speech.say("^start(animations/Stand/Gestures/BowShort_1) Esto fue Pepper News: donde las noticias son reales, los chistes malos... y el futuro ya está aquí. ¡Muchas gracias por acompañarnos!")
time.sleep(2)

# -------------- Cierre en negro ----------------
tablet.showImageNoCache(imgs["negro"])
time.sleep(3)

# ---------------- Volver a postura normal ----
posture.goToPosture("StandInit", 0.6)  # posición neutral estándar


print("✅ Exposición finalizada.")
