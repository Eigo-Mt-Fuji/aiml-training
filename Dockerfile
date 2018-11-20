FROM python:3.6-slim
LABEL maintainer="efg.river"
ENV SRC_DIR /usr/local/opt/aiml-training
WORKDIR $SRC_DIR
RUN mkdir -p $SRC_DIR
ADD ./ $SRC_DIR/
RUN pip install -r requirements.txt
RUN jupyter notebook --generate-config
RUN echo "c.NotebookApp.password = u'sha1:f192a3018d9d:b010686da910ea6be26a307e7a1b95c2c05d1a6a'" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.token = u'test'" >> ~/.jupyter/jupyter_notebook_config.py
RUN cat ~/.jupyter/jupyter_notebook_config.py
EXPOSE 8888
CMD jupyter notebook --ip=0.0.0.0 --allow-root --no-browser

