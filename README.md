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
![image](/home/alexander/Documents/images/Screenshot from 2022-04-11 23-43-13.png)
---
#### After that, we receive an email with a link to download file:
![image](/home/alexander/Documents/images/Screenshot from 2022-04-11 23-40-34.png)
---
#### All files are stored on the dropbox:

![image](/home/alexander/Pictures/Screenshot from 2022-04-11 23-52-34.png)
---
#### We use Celery and Flower to track tasks:
![image](/home/alexander/Pictures/Screenshot from 2022-03-17 15-08-06.png)
---
#### And for tracking errors/bugs, we use Sentry for the Backend and Frontend:
![image](/home/alexander/Pictures/Screenshot from 2022-03-17 14-36-07.png)
![image](/home/alexander/Pictures/Screenshot from 2022-03-17 14-35-39.png)