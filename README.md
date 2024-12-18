# Hospital Website API

This project is a **RESTful API** built using **Django** and **Django REST Framework** for managing hospital-related data, including doctors, departments, specialties, and educational qualifications. It is designed to serve as the backend for a hospital website.

---

## Features 🚀

- **Doctors Management**: Add, view, update, and delete doctor profiles.
- **Specialties and Departments**: Manage hospital specialties and departments.
- **Education**: Store and manage doctor educational qualifications.
- **Image Upload**: Support for uploading and displaying doctor images.
- **Search and Filter**: Retrieve specific data using search parameters.
- **RESTful Endpoints**: Standardized API design for ease of integration.

---

## Tech Stack 💻

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **Language**: Python 3.11
- **Tools**: Django Admin, DRF Browsable API

---

## Installation 🛠️

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/hospital-api.git
cd hospital-api
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On MacOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root to store sensitive configurations:
```bash
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run Development Server
```bash
python manage.py runserver
```
Access the API at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---


## API Endpoints 🔗

### Doctor Endpoints
| Method | URL                       | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/doctors/`               | Retrieve a list of all doctors     |
| POST   | `/doctors/`               | Add a new doctor                   |

### Specialty Endpoints
| Method | URL                       | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/specialties/`           | Retrieve all specialties           |
| POST   | `/specialties/`           | Add a new specialty                |

### Department Endpoints
| Method | URL                       | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/departments/`           | Retrieve all departments           |
| POST   | `/departments/`           | Add a new department               |

### Staff Endpoints
| Method | URL                       | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/staff/`                 | Retrieve a list of all staff       |
| POST   | `/staff/`                 | Add new staff                      |
| GET    | `/staff/<int:pk>/`        | Retrieve a specific staff member   |
| PUT    | `/staff/<int:pk>/`        | Update a specific staff member     |
| DELETE | `/staff/<int:pk>/`        | Delete a specific staff member     |

### Review Endpoints
| Method | URL                       | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/reviews/`               | Retrieve all reviews               |
| POST   | `/reviews/`               | Add a new review                   |
| GET    | `/reviews/<int:pk>/`      | Retrieve a specific review         |
| PUT    | `/reviews/<int:pk>/`      | Update a specific review           |
| DELETE | `/reviews/<int:pk>/`      | Delete a specific review           |

### Hospital Information Endpoint
| Method | URL                       | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/hospital-info/`         | Retrieve hospital information      |

### Patient Contact Endpoint
| Method | URL                       | Description                        |
|--------|---------------------------|------------------------------------|
| POST   | `/contact/`               | Submit patient contact information |

---


## Admin Panel 🎛️

Access the Django Admin interface to manage data manually:
- URL: `/admin/`
- Login: Use the superuser credentials.

To create a superuser:
```bash
python manage.py createsuperuser
```

---

## Media Files 📷

Uploaded doctor images are stored in the `media/` directory. During development, ensure that `MEDIA_URL` and `MEDIA_ROOT` are correctly configured in your `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Add the following to your `urls.py` to serve media files locally:
```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## Testing ✅

Run tests using the following command:
```bash
python manage.py test
```

---

## Deployment 🚀

For production, use a server like **Gunicorn** with **Nginx**. Switch the database to PostgreSQL or MySQL for better performance.

1. **Collect Static Files**:
   ```bash
   python manage.py collectstatic
   ```

2. **Use `.env` for production settings** (set `DEBUG=False`).

---

## Contributing 🤝

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your message"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## License 📄

This project is licensed under the MIT License.

---

## Contact 📧

For questions or suggestions, contact:

- **Your Name**: [reshadmajumder365.com](mailto:reshadmajumder365@gmail.com)
- **GitHub**: [https://github.com/reshadMajumder](https://github.com/reshadMajumder)

