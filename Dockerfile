FROM python:3-bullseye

RUN apt update
RUN apt install mariadb-client -y
RUN pip install --no-cache-dir --upgrade web.py mysqlclient
COPY ./server.py /server.py
COPY ./main.py /main.py
COPY ./genre.py /genre.py
COPY ./DB.py /DB.py
COPY ./home.py /home.py
COPY ./artist.py /artist.py
COPY ./album.py /album.py
COPY ./media_type.py /media_type.py
COPY ./track.py /track.py
COPY ./playlist.py /playlist.py
COPY ./nav.py /nav.py
COPY ./navH.py /navH.py
CMD [ "python", "/server.py" ]
