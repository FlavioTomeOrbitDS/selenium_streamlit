import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
from PIL import Image
import base64  # Adicione esta linha
import json
import time
import io
import os

def generate_qr_code():
    progress_text = "Abrindo o browser..."
    my_bar = st.progress(0, text=progress_text)
    # Iniciar o display virtual
    display = Display(visible=1, size=(1920, 1080))
    display.start()

    # Configurar o Selenium para usar o Firefox com um perfil específico
    profile_path = os.path.join(os.getcwd(), "profile", "whatsapp")
    options = Options()
    options.profile = profile_path
    
    driver = webdriver.Firefox(options = options)
    driver.get("https://web.whatsapp.com/")

    # Esperar um pouco para garantir que a página carregue completamente
    time.sleep(5)
    
    my_bar.progress(50, text="Capturando QR Code...")    
    # Tirar um screenshot da página
    screenshot_path = "/tmp/screenshot.png"
    driver.save_screenshot(screenshot_path)
    
    my_bar.progress(100, text="Qr Code Salvo .")    

    # Exibir o conteúdo do screenshot
    #image = Image.open(screenshot_path)
    #image.show()

    # print("convertendo para base64...")
    # # Converter a imagem para base64
    # with open(screenshot_path, "rb") as image_file:
    #     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    # # Criar um objeto JSON com os dados da imagem
    # screenshot_data = {
    #     "screenshot": encoded_string
    # }

    # # Converter o objeto para JSON
    # screenshot_json = json.dumps(screenshot_data)
    # print("Aguardando leitura do qrcode")

    # print(f"Dados do screenshot em JSON: {screenshot_json}")



    # time.sleep(120)

    # print("Encerrando a sessao")

    driver.quit()
    display.stop()
        

st.header("Gerar QR Code")
generate_button = st.button("Gerar")

try:
    st.image("/tmp/screenshot.png", caption="Sunrise by the mountains")
except:
    st.markdown("<h3> Nenhum código gerado ainda...</h3>", unsafe_allow_html=True)
    
if generate_button:
    #generate_qr_code()
    try:
        st.image("/tmp/screenshot.png", caption="Sunrise by the mountains")
    except:
        st.markdown("<h3> Erro ao gerar QR COde!</h3>", unsafe_allow_html=True)
