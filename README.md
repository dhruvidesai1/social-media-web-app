# social-media-web-app
A simple Django-based user authentication system with login, logout, registration, and profile creation features.
Thanks for sharing the project structure! Based on the file layout and features, here’s an enhanced README.md file for your Social Media Web App project, including useful badges and clean formatting:

⸻

📄 README.md

# 🧑‍🤝‍🧑 Social Media Web App

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-success?logo=django)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-active-brightgreen)]()

A simple yet functional Django-based social media web app that allows users to register, log in, create posts, like, comment, and manage their profiles.

---

## 🚀 Features

- 🔐 User Registration & Authentication
- 📝 Create, Edit, and View Posts
- ❤️ Like and Comment on Posts
- 👤 User Profile Pages
- 📧 Password Reset & Change Functionality
- 🎨 Custom Styles with Tailwind CSS and custom `style.css`

---

## 🗂️ Folder Structure

social/
├── env/                        # Virtual environment
├── socialproject/             # Project settings
│   ├── posts/                 # App for user-generated content
│   │   ├── templates/posts/   # Post views (feed, create)
│   │   └── views.py, models.py, forms.py, etc.
│   ├── users/                 # User management app
│   │   ├── templates/users/   # Auth pages (login, register, etc.)
│   │   ├── static/users/      # Images, CSS
│   │   └── views.py, models.py, forms.py
├── db.sqlite3                 # SQLite DB
├── manage.py


👩‍💻 Tech Stack
	•	Python 3.12
	•	Django 5.2
	•	HTML5, CSS3, Tailwind
	•	SQLite3 (default dev DB)

⸻

📬 License

This project is licensed under the MIT License.

⸻

🤝 Contributions

Pull requests are welcome! Feel free to fork and improve the project.

⸻

✨ Author
	•	Dhruvi Desai
