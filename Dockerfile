FROM python:3.11-slim

RUN apt update && apt install -y make g++ git
RUN python3 -m venv /ve
ENV PATH="/ve/bin:$PATH"

RUN mkdir -p /usr/src/
COPY . /usr/src/

WORKDIR /usr/src/cDynAA
RUN make wheel
RUN for whl in pydynaa*.whl; do pip install "$whl" || :; done

WORKDIR /usr/src/nexussim
RUN pip install .

WORKDIR /usr/src
RUN pip install .

FROM python:3.11-slim
COPY --from=0 /ve /ve
COPY --from=0 /usr/src/nexussim/influx.ini.default /usr/src/influx.ini
ENV PATH="/ve/bin:$PATH"
ENV INFLUX_INI=/usr/src/influx.ini


EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "nexussim_server"]
