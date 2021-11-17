FROM cloud.mathcrowd.cn:5001/tex2png

# Install pango,ffmpeg,git
RUN apt-get update && \
    apt install -y libpango1.0-dev pkg-config python3-dev && \
    apt install -y ffmpeg git &&\
    apt install -y freeglut3-dev freeglut3 libgl1-mesa-dev libglu1-mesa-dev libxext-dev libxt-dev && \
    apt install -y python3-opengl libgl1-mesa-glx libglu1-mesa

WORKDIR /opt/mathcrowd-manim

COPY manim /opt/mathcrowd-manim/
COPY .gitmodules /opt/mathcrowd-manim/
COPY requirements.txt /opt/mathcrowd-manim/

RUN git config --global http.proxy http://192.168.10.97:80
RUN git submodule sync --recursive && git submodule update  --remote --recursive && cd manim && pip install -e .

RUN pip install -r requirements.txt

COPY . /opt/mathcrowd-manim

VOLUME /usr/local/share/fonts
VOLUME /opt/mathcrowd-manim/outputs



USER root

CMD [ "/bin/bash","./build.sh"]




