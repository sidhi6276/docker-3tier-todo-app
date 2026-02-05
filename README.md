# Docker 3-Tier Todo App on AWS 🚀

A production-style 3-tier architecture Todo application deployed on AWS EC2 using Docker & Docker Compose.

This project demonstrates real-world DevOps workflow including containerization, database integration, and cloud deployment.

---

## 🌐 Live Demo

👉 http://13.234.111.174

---

## 🏗 Architecture

This project follows **3-tier architecture**:

```
Client (Browser)
     ↓
Web Tier (Django + Gunicorn container)
     ↓
Database Tier (MySQL container)
```

Docker Compose manages communication between services using internal networking.

---

## 🧰 Tech Stack

- Python 3.11
- Django
- Gunicorn
- MySQL
- Docker
- Docker Compose
- AWS EC2 (Ubuntu)
- Linux CLI


---

## ⚙️ How It Works

- Django handles backend logic
- Gunicorn serves production WSGI server
- MySQL stores todo data
- Docker containers isolate each service
- Docker Compose connects them in one network
- EC2 hosts the entire stack

---

## 🚀 Deployment Steps (AWS EC2)

### 1. Launch EC2 Instance

- Ubuntu server
- Open port 80 in security group

### 2. Install Docker

```
sudo apt update
sudo apt install docker.io docker-compose -y
```

### 3. Clone Project

```
git clone https://github.com/YOUR-USERNAME/docker-3tier-todo-app.git
cd docker-3tier-todo-app
```

### 4. Run Containers

```
docker-compose up --build -d
```

App runs on:

```
http://<EC2-PUBLIC-IP>
```

---

## 📁 Project Structure

```
todo-app/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│
└── todos/
    ├── models.py
    ├── views.py
    ├── templates/
```

---

## 🔥 Key DevOps Concepts Used

- Containerization
- Multi-container architecture
- Persistent database storage
- Internal Docker networking
- Production WSGI server
- Cloud deployment
- Infrastructure as code mindset

---

## 🎯 Purpose of This Project

This project was built to:

- Learn Docker deeply
- Understand 3-tier architecture
- Deploy apps on AWS
- Practice real DevOps workflow
- Build resume-ready cloud project

---

## 👩‍💻 Author

Sidhi Goel  
Docker + AWS Learner 🚀

---

⭐ If you like this project, star the repo!
