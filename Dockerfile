FROM cloud.mathcrowd.cn:5001/tex2png

# Install pango,ffmpeg,git
RUN apt-get update && \
    apt install -y libpango1.0-dev pkg-config python3-dev && \
    apt install -y ffmpeg git &&\
    apt install -y freeglut3-dev freeglut3 libgl1-mesa-dev libglu1-mesa-dev libxext-dev libxt-dev && \
    apt install -y python3-opengl libgl1-mesa-glx libglu1-mesa

RUN git config --global http.proxy http://192.168.10.97:80

COPY . /opt/mathcrowd-manim
WORKDIR /opt/mathcrowd-manim

VOLUME /usr/local/share/fonts
VOLUME /opt/mathcrowd-manim/outputs

RUN pip install -r requirements.txt
RUN git submodule sync --recursive && git submodule update  --remote --recursive && cd manim && pip install -e .

CMD [ "/bin/bash" ]




