# Web Page Generator
### Service for generating web pages to PDF files

---
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django)
![PyPI - Django Version](https://img.shields.io/pypi/djversions/djangorestframework)
![GitHub](https://img.shields.io/github/license/AlexanderPoleshchuk/web_to_page)
---

## QuickStart
Get the latest version of the project:
```bash
git clone https://github.com/AlexanderPoleshchuk/web_to_page.git
```
Move into your project folder \
Decrypt files with environment variables
```bash
gpg -d dev.gpg > dev
```
To install, you need to run:
```bash
docker-compose up -d --build
```

To put containers, it is enough to write:
```bash
docker-compose down -v
```

To see the logs write:
```bash
docker-compose logs -f
```

To start using go to:
```bash
http://localhost:3001
```
---
## Technology stack

- **Sentry**
- **Flower**
- **React**
- **Javascript**
- **Python**
- **Django**
- **Django Rest Framework**
- **Celery**
- **Redis**
- **PostgreSQL**
---

## Using 

#### The main page with input fields for a link to a website and email:
![Screenshot from 2022-04-11 23-43-13](https://user-images.githubusercontent.com/53741871/162834886-b1c7b2f3-fdca-4e99-978e-f3d5694dd829.png)

---
#### After that, we receive an email with a link to download file:
![Screenshot from 2022-04-11 23-40-34](https://user-images.githubusercontent.com/53741871/162834905-3a5e313e-895f-45c2-abdb-c4f1077a4a6b.png)
---
![Screenshot from 2022-04-12 00-19-01](https://user-images.githubusercontent.com/53741871/162835203-fb7a3233-cd70-44c9-a45b-ed4e32948a99.png)

---
#### All files are stored on the dropbox:
![Screenshot from 2022-04-11 23-52-34](https://user-images.githubusercontent.com/53741871/162834919-16a2871f-bd03-4df2-ae0e-54e62d617b6d.png)


---
#### We use Celery and Flower to track tasks:
![Screenshot from 2022-03-17 15-08-06](https://user-images.githubusercontent.com/53741871/162834958-d9804108-97a4-40d3-949f-00d712ca0874.png)

---
#### And for tracking errors/bugs, we use Sentry for the Backend and Frontend:
![Screenshot from 2022-03-17 14-35-39](https://user-images.githubusercontent.com/53741871/162834998-d2215bb1-6218-4e79-9afa-46f0292ad64a.png)
---
![Screenshot from 2022-03-17 14-36-07](https://user-images.githubusercontent.com/53741871/162835023-ec15161b-4314-47b3-8633-0973e97578ea.png)
