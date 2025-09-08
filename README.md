# 🤖 Proyecto 1: Exposicion con Pepper y Dashboard Didactico

## 📌 Descripción
Este proyecto integra el **robot Pepper**, un **chatbot educativo con personalidad inspirada en Thanos** y un **dashboard interactivo** desarrollado en **Streamlit**.  

El objetivo es combinar **interacción robótica**, **novedades tecnológicas** y **visualización en la nube**, logrando una experiencia educativa innovadora y accesible desde cualquier dispositivo.  

---

## 📝 Contenido del Proyecto

### 🔹 1. Conexión con Pepper
- Acceso al robot mediante **SSH**.  
- Creación y gestión de carpetas para imágenes.  
- Transferencia y verificación de archivos en Pepper.  
- Ejecución de código en Python para controlar voz, gestos e imágenes.  

### 🔹 2. Chatbot Personalizado
- Chatbot con **personalidad de Thanos** 🟣.  
- Responde exclusivamente sobre:
  - 🧬 **CRISPR y biocomputación**  
  - 🚀 **Cohetes reutilizables**  
  - 💠 **NFTs de utilidad**  
- Interacción por **texto** y **voz**.  
- Implementado con **LangChain, gTTS y Streamlit**.  

### 🔹 3. Dashboard Integrado
- Creado con **Streamlit** e integrado en **Hugging Face**.  
- Interfaz de **3 columnas**:
  - 🎥 Videos educativos (CRISPR, Cohetes, NFTs).  
  - 📑 Información y resúmenes de cada tema.  
  - 💬 Chatbot interactivo (texto + voz).  
- Estilizado con CSS y mensajes destacados.  

### 🔹 4. Documentación en Overleaf
- Desarrollo de un documento completo en LaTeX.  
- Paso a paso con capturas de pantalla y explicaciones detalladas.  

### 🔹 5. Control de Versiones con GitHub
- Uso de **git** y **GitHub** para control de versiones.  
- Creación de ramas por cada integrante.  
- Subida de videos y unificación del trabajo en `main`.  

---

## ⚙️ Herramientas Utilizadas
- 🐍 **Python 3.12**  
- 🎛 **Streamlit** + `streamlit-mic-recorder`  
- 🧩 **LangChain** + `langchain-deepseek`  
- 🔊 **gTTS (Google Text-to-Speech)**  
- ☁️ **Hugging Face** (despliegue en la nube)  
- 📝 **Overleaf (LaTeX)**  
- 🖥 **Git & GitHub**  

---

## 🚀 Instalación y Ejecución

### 1️⃣ Clonar el repositorio
git clone (URL del repositorio)
cd pepper-chatbot

### 2️⃣ Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

### 3️⃣ Instalar dependencias
pip install -r requirements.txt

### 4️⃣ Ejecutar el chatbot
streamlit run chatbot.py
