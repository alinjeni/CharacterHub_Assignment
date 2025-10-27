# Backend - Infinite Scroll Posts API (Django REST Framework)

## Overview
This project implements an API endpoint for an **infinite scrolling posts feed**, where each post displays up to **3 latest comments**, along with total comment count and user details.

---

## Features
- List, Create Posts.
- List and Create Comments for specific posts.
- Paginated Posts (infinite scroll style).
- Shows latest 3 comments for each post.
- Authenticated users can create posts and comments.
- Anonymous users can only view posts and comments.

---

## Models

### **Post**
| Field | Type | Description |
|--------|------|-------------|
| id | UUID | Unique identifier |
| text | Text | Post content |
| timestamp | DateTime | Auto-added when created |
| user | ForeignKey(User) | Post author |

### **Comment**
| Field | Type | Description |
|--------|------|-------------|
| id | UUID | Unique identifier |
| text | Text | Comment content |
| timestamp | DateTime | Auto-added when created |
| post | ForeignKey(Post) | Linked post |
| user | ForeignKey(User) | Comment author |

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <project_directory>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Authentication
The API uses **Token Authentication**.

1. Obtain a token (after logging in from the admin panel or via API).  
2. Add it to your Postman headers:
   ```text
   Key: Authorization
   Value: Token <your_token_here>
   ```

---

## API Endpoints

### **Posts**
| Method | Endpoint | Description | Auth Required |
|---------|-----------|--------------|---------------|
| GET | `/api/posts/` | List all posts (paginated) | ❌ |
| POST | `/api/posts/` | Create a new post | ✅ |
| GET | `/api/posts/<id>/` | Retrieve a post | ❌ |
| PUT/PATCH | `/api/posts/<id>/` | Update a post | ✅ |
| DELETE | `/api/posts/<id>/` | Delete a post | ✅ |

#### Example Response (`GET /api/posts/`)
```json
{
  "count": 10,
  "next": "http://localhost:8000/api/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": "f3e9...",
      "text": "My first post!",
      "timestamp": "2025-10-27T08:00:00Z",
      "user": "admin",
      "comment_count": 2,
      "comments": [
        {
          "id": "b4d...",
          "text": "Nice post!",
          "timestamp": "2025-10-27T08:05:00Z",
          "user": "testuser"
        }
      ]
    }
  ]
}
```

### **Comments**
| Method | Endpoint | Description | Auth Required |
|---------|-----------|--------------|---------------|
| GET | `/api/posts/<post_id>/comments/` | List all comments for a post | ❌ |
| POST | `/api/posts/<post_id>/comments/` | Add a comment to a post | ✅ |

---

## Follow-up Question (Answer)
> Instead of sorting comments by timestamp, how would you fetch 3 random comments associated to a given post?

In `serializers.py` → `PostSerializer.get_comments` method, replace:
```python
latest_comments = obj.comments.order_by('-timestamp')[:3]
```
with:
```python
random_comments = obj.comments.order_by('?')[:3]
```

---


# Frontend - 