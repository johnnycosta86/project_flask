# project_flask

Projeto 'HelloWorld' utilizando o framework web Flask em python, consumindo um rest endpoint
que retorna a predição utilizando um modelo fashion mnist criado via tensorflow.

# (necessário ter o pip e o pipenv instalado na maquina)
# (caso não tenha, rodar: 
# 1 - wget https://bootstrap.pypa.io/get-pip.py
# 2 - sudo python get-pip.py
# 3 - pip install pipenv)

# Baixa Projeto
git clone https://github.com/johnnycosta86/project_flask.git

# Baixa Todas Dependencias do projeto.                   
pipenv install 
                 
# Roda a aplicacao no localhost:5000/
pipenv run python app.py

# Utilizando o postman, envia requisicoes post no endereco localhost:5000/api/v1/4.png
# O endpoint retorna qual tipo de imagem representa a imagem 4.png (salvo na pasta upload do projeto),

# O modelo utilizado e' o fashion mnist, que e' o hello world para modelos de visao computacional.
# Esse modelo possui 10 classes de saida. ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
# E tambem possui 70.000 imagens de 28x28, com 60.000 para treinamento e 10.000 para testes.
