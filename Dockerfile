FROM python:3.9.0
RUN pip install flask
RUN pip install requests
COPY teste_tecnico_captalys.py /teste_tecnico_captalys.py
CMD ["python3","teste_tecnico_captalys.py"]