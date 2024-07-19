# FROM python:3.9

# # Set the Fontconfig cache directory and create it
# RUN mkdir -p /usr/share/fonts
# RUN mkdir -p /root/.cache/fontconfig

# # Set the FONTCONFIG_PATH environment variable
# ENV FONTCONFIG_PATH /root/.cache/fontconfig

# WORKDIR /app 
# COPY . /app 

# RUN pip install -r requirements.txt 

# # Set MPLCONFIGDIR
# ENV MPLCONFIGDIR=/tmp

# # Clean font cache
# ENV OSFONTDIR=/usr/share/fonts

# EXPOSE 8823

# CMD ["uvicorn", "app.views:app", "--host", "0.0.0.0", "--port", "8823"]


FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN useradd -m -u 1000 user

USER user

ENV HOME=/home/user \
 PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

CMD ["uvicorn", "app.views:app", "--host", "0.0.0.0", "--port", "7860"]