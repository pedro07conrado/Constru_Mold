# Constru_Mold
Sistema de gestão de estoque para um deposito de matérias de construção  👷🏽‍♂️🏗️ 

## Tecnologias

<p align="center">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" width="200"/>
</p>


> [!IMPORTANT]
> Se ainda não tiver o python instalado no seu sistema, execute
>```
>sudo apt install python3-venv
>```
>Crie um ambiente virtual, para isolar as dependências do projeto:
>```
>python3 -m venv venv
>```
>executando o ambiente virtual
>```
>source venv/bin/activate
>```

 ## Instale o Django e outras dependências listadas no arquivo `requirements.txt`
   
   ```
   pip install -r requirements.txt
   ```
>**Caso o arquivo requirements.txt não esteja presente, você pode instalar o Django e outras bibliotecas manualmente**
>```bash
>pip install django
>```

## Configure o banco de dados executando as migrações iniciais
```bash
python manage.py migrate
```

# *E finalmente rode a aplicação*
```
python manage.py runserver
```
