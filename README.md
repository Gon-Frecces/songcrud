# Music Library API

A RESTful Music Library API built with **Django** and **Django REST Framework (DRF)**. This project demonstrates the implementation of a backend service for managing music-related data, including artists, songs, and song lyrics.

The API supports standard CRUD (Create, Read, Update, Delete) operations and showcases REST API development, model relationships, serialization, and database management using Django's ORM.

---

## Features

* Create new songs
* Retrieve all songs
* Retrieve a single song by ID
* Update song information
* Delete songs
* Manage artists and their songs
* Store song lyrics
* JSON-based API responses

---

## Data Model

The project consists of three related models:

### Artiste

Represents a music artist.

| Field      | Type         |
| ---------- | ------------ |
| first_name | CharField    |
| last_name  | CharField    |
| age        | IntegerField |

---

### Song

Represents an individual song.

| Field         | Type                 |
| ------------- | -------------------- |
| id            | AutoField            |
| title         | CharField            |
| date_released | DateField            |
| likes         | IntegerField         |
| artiste       | ForeignKey → Artiste |

Each song belongs to one artist.

---

### Lyric

Stores the lyrics associated with a song.

| Field   | Type              |
| ------- | ----------------- |
| content | CharField         |
| song    | ForeignKey → Song |

Each lyric is linked to a song through a foreign key relationship.

---

## API Endpoints

### Songs

| Method | Endpoint       | Description              |
| ------ | -------------- | ------------------------ |
| GET    | `/songs/`      | Retrieve all songs       |
| POST   | `/songs/`      | Create a new song        |
| GET    | `/songs/<id>/` | Retrieve a specific song |
| PUT    | `/songs/<id>/` | Update a song            |
| DELETE | `/songs/<id>/` | Delete a song            |

---

## Example JSON

### Create a Song

```json
{
    "title": "Shape of You",
    "date_released": "2017-01-06",
    "likes": 120,
    "artiste_id": 1
}
```

### Response

```json
{
    "id": 1,
    "title": "Shape of You",
    "date_released": "2017-01-06",
    "likes": 120,
    "artiste_id": 1
}
```

---

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite (default Django database)
* Django ORM

---

## Project Structure

```text
music-library-api/
│
├── musicapp/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── apps.py
│
├── manage.py
├── db.sqlite3
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/music-library-api.git
cd music-library-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

Install dependencies:

```bash
pip install django djangorestframework
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

The API will be available at:

```
http://127.0.0.1:8000/
```

---

## Concepts Demonstrated

* RESTful API development
* CRUD operations
* Django Models
* Foreign Key relationships
* Django ORM
* Serialization with Django REST Framework
* Function-based API views
* JSON request and response handling
* HTTP status codes

---

## Future Improvements

* User authentication with JWT
* Artist CRUD endpoints
* Lyrics CRUD endpoints
* Search and filtering
* Pagination
* API documentation with Swagger/OpenAPI
* Album and playlist management
* File uploads for album artwork
* Music streaming integration
* Unit and integration tests

---

## Author

**Damilola Ayinde**

This project was developed as an early exploration of backend API development with Django and Django REST Framework, providing hands-on experience with RESTful services, database modeling, and API design.
