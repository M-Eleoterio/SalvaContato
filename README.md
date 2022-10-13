# SalvaContato

https://salvacontato.rj.r.appspot.com

RODAR LOCALMENTE========================================

- Abra a pasta "SalvaContato" no seu editor de código

- Instale no seu editor de código todas as 
bibliotecas externas do código pelo terminal 
(pip install flask / pip install flask_sqlalchemy)

- use o comando "flask --app main run" para dar 
início ao server.

- aparecerá no terminal "Running on 
http://xxx.x.x.x:xxxx", é este link que você deve
 acessar para utilizar o site  localmente.

=========================================================

PROCESSO DE DEPLOY=======================================

- Abra o Google Cloud Shell                             
(https://shell.cloud.google.com/?show=ide%2Cterminal)

- Arraste a pasta SalvaContato para dentro do editor

- Rode no terminal o comando "gcloud config set project 
NOMEDOPROJETO" para definir em qual projeto o site será 
lançado.

- Rode também o comando "cd SalvaContato" para ir a pasta

- Faça o upload do site com "gcloud app deploy"
=========================================================
