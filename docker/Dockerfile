FROM python:3.11

RUN curl -LO https://nodejs.org/dist/v10.18.0/node-v10.18.0-linux-x64.tar.xz && \
  xz -d node-v10.18.0-linux-x64.tar.xz && \
  tar xvf node-v10.18.0-linux-x64.tar -C /opt

ENV PATH=$PATH:/node-v10.18.0-linux-x64/bin

CMD ["/bin/bash"]
