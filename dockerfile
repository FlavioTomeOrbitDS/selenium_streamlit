FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

# Instalar dependências, limpar cache e remover arquivos desnecessários em uma única camada
RUN apt-get update && apt-get install -y \
    firefox \
    xvfb \
    wget \
    unzip \
    python3 \
    python3-pip \
    xserver-xephyr \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar o Selenium, PyVirtualDisplay, Pillow, e Streamlit
RUN pip3 install --no-cache-dir selenium pyvirtualdisplay pillow streamlit

# Baixar e instalar a versão recomendada do geckodriver
RUN wget -q https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz \
    && tar -xzf geckodriver-v0.35.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v0.35.0-linux64.tar.gz

# Definir a variável DISPLAY para usar com Xvfb
ENV DISPLAY=:99

ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501

# Copiar os scripts de web scraping e o script Streamlit para o contêiner
COPY home.py /home.py
COPY qrcode.py /qrcode.py

# Expor a porta padrão do Streamlit
EXPOSE 8501

# Comando para iniciar o Xvfb e o aplicativo Streamlit
CMD Xvfb :99 -screen 0 1920x1080x24 & streamlit run /home.py
