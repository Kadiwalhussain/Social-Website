# Social Website

A full-featured social bookmarking web application built with Django. This project allows users to share and bookmark images from around the web, follow other users, and interact through a like system.

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [URL Endpoints](#-url-endpoints)
- [Models](#-models)
- [Authentication](#-authentication)
- [API Reference](#-api-reference)
- [Development](#-development)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### User Authentication
- **Traditional Registration**: Sign up with username, email, and password
- **Social Authentication**: Sign in with Google OAuth2
- **Email Authentication**: Login using email address instead of username
- **Password Management**: Change and reset passwords
- **User Profiles**: Customizable profiles with photo upload and personal information

### Image Bookmarking
- **Bookmarklet Tool**: Drag-and-drop bookmarklet to save images from any website
- **Image Gallery**: Browse all bookmarked images with infinite scroll pagination
- **Image Details**: View full image with description and user interactions
- **Like System**: Like/unlike images with AJAX-powered real-time updates

### Social Features
- **User Directory**: Browse and discover other users
- **User Profiles**: View other users' profiles and their bookmarked images
- **Activity Dashboard**: Personal dashboard showing bookmarking statistics

### Admin Panel
- **Django Admin**: Full administrative interface for managing users, profiles, and images
- **User Management**: Create, edit, and manage user accounts
- **Content Moderation**: Review and moderate bookmarked images

## 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| **Backend Framework** | Django 5.1+ |
| **Database** | SQLite (development) / PostgreSQL (production) |
| **Authentication** | Django Auth + Python Social Auth |
| **Image Processing** | Pillow |
| **Configuration** | python-decouple |
| **HTTPS Development** | django-extensions + Werkzeug + pyOpenSSL |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **AJAX** | Fetch API |
| **Cookie Management** | js-cookie |

## 📁 Project Structure

```
Social-Website/
├── account/                    # User account application
│   ├── migrations/            # Database migrations
│   ├── static/css/           # Account app stylesheets
│   ├── templates/            # Account templates
│   │   ├── account/          # Account-specific templates
│   │   │   ├── dashboard.html
│   │   │   ├── edit.html
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── register_done.html
│   │   │   └── user/         # User list/detail templates
│   │   ├── registration/     # Auth templates (login, password reset)
│   │   └── base.html         # Base template
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   ├── authentication.py     # Custom authentication backends
│   ├── forms.py              # User and profile forms
│   ├── models.py             # Profile model
│   ├── urls.py               # Account URL routing
│   └── views.py              # Account views
├── bookmarks/                 # Main project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # Root URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── images/                    # Image bookmarking application
│   ├── migrations/           # Database migrations
│   ├── static/               # Static files (CSS, JS)
│   ├── templates/images/     # Image templates
│   │   └── image/
│   │       ├── create.html
│   │       ├── detail.html
│   │       ├── list.html
│   │       └── list_images.html
│   ├── admin.py              # Image admin configuration
│   ├── apps.py               # App configuration
│   ├── forms.py              # Image creation form
│   ├── models.py             # Image model
│   ├── urls.py               # Image URL routing
│   └── views.py              # Image views
├── manage.py                  # Django management script
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kadiwalhussain/Social-Website.git
   cd Social-Website
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow python-decouple social-auth-app-django django-extensions werkzeug pyopenssl
   ```

4. **Create environment file**
   Create a `.env` file in the project root:
   ```env
   # Google OAuth2 (optional)
   GOOGLE_OAUTH2_KEY=your_google_client_id
   GOOGLE_OAUTH2_SECRET=your_google_client_secret
   
   # Email Configuration (optional)
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   # Standard HTTP server
   python manage.py runserver
   
   # HTTPS server (for social auth)
   python manage.py runserver_plus --cert-file cert.crt 0.0.0.0:8000
   ```

8. **Access the application**
   - HTTP: `http://127.0.0.1:8000/`
   - HTTPS: `https://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

## ⚙ Configuration

### Django Settings

Key settings in `bookmarks/settings.py`:

```python
# Security (change in production)
SECRET_KEY = 'your-secret-key'
DEBUG = True  # Set to False in production

# Allowed hosts
ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1', '0.0.0.0']

# Database (SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Authentication redirects
LOGIN_REDIRECT_URL = 'account:dashboard'
LOGIN_URL = 'account:login'

# Static and Media files
STATIC_URL = '/static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Google OAuth2 Configuration

To enable Google Sign-In:

1. **Create a Google Cloud Project**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one

2. **Enable OAuth2 Credentials**
   - Navigate to **APIs & Services** → **Credentials**
   - Click **Create Credentials** → **OAuth 2.0 Client IDs**
   - Select **Web application**

3. **Configure Redirect URIs**
   Add these authorized redirect URIs:
   ```
   https://127.0.0.1:8000/social-auth/complete/google-oauth2/
   https://localhost:8000/social-auth/complete/google-oauth2/
   ```

4. **Configure JavaScript Origins**
   Add these authorized JavaScript origins:
   ```
   https://127.0.0.1:8000
   https://localhost:8000
   ```

5. **Update Environment Variables**
   Add your credentials to `.env`:
   ```env
   GOOGLE_OAUTH2_KEY=your_client_id.apps.googleusercontent.com
   GOOGLE_OAUTH2_SECRET=your_client_secret
   ```

For detailed Google OAuth setup, see [GOOGLE_OAUTH_CONFIG.md](GOOGLE_OAUTH_CONFIG.md).

## 📖 Usage

### User Registration

1. Navigate to `/account/register/`
2. Fill in username, first name, email, and password
3. Click "Create my account"
4. A user profile is automatically created

### Logging In

1. Navigate to `/account/login/`
2. Enter username/email and password, OR
3. Click "Sign in with Google" for OAuth login

### Bookmarking Images

1. **Install the Bookmarklet**
   - Go to your Dashboard (`/account/`)
   - Drag the "Bookmark it" button to your browser's bookmarks bar

2. **Bookmark an Image**
   - Visit any website with images
   - Click the "Bookmark it" bookmarklet
   - Select an image to bookmark
   - Add a title and description
   - Click "Bookmark it!"

### Browsing Images

1. Navigate to `/images/` to see all bookmarked images
2. Click on any image to view details
3. Like/unlike images by clicking the Like button
4. Scroll down for infinite pagination

### Managing Your Profile

1. Navigate to `/account/edit/`
2. Update your first name, last name, and email
3. Upload a profile photo
4. Set your date of birth
5. Click "Save changes"

## 🔗 URL Endpoints

### Public URLs

| URL | View | Description |
|-----|------|-------------|
| `/` | Home redirect | Redirects to login page |
| `/admin/` | Django Admin | Administrative interface |
| `/account/login/` | Login | User login page |
| `/account/register/` | Register | User registration |
| `/account/password_reset/` | Password Reset | Request password reset |

### Protected URLs (Login Required)

| URL | View | Description |
|-----|------|-------------|
| `/account/` | Dashboard | User dashboard |
| `/account/edit/` | Edit Profile | Edit user profile |
| `/account/password_change/` | Change Password | Change user password |
| `/account/users/` | User List | Browse all users |
| `/account/users/<username>/` | User Detail | View user profile |
| `/images/` | Image List | Browse all images |
| `/images/create/` | Create Image | Bookmark a new image |
| `/images/detail/<id>/<slug>/` | Image Detail | View image details |

### Social Authentication URLs

| URL | Description |
|-----|-------------|
| `/social-auth/login/google-oauth2/` | Initiate Google OAuth |
| `/social-auth/complete/google-oauth2/` | Google OAuth callback |

### API Endpoints

| URL | Method | Description |
|-----|--------|-------------|
| `/images/like/` | POST | Like/unlike an image (AJAX) |

## 📊 Models

### Profile Model (`account/models.py`)

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
```

**Fields:**
- `user`: One-to-one relationship with Django's User model
- `date_of_birth`: Optional date of birth
- `photo`: Optional profile photo

### Image Model (`images/models.py`)

```python
class Image(models.Model):
    user = models.ForeignKey(User, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(User, related_name='images_liked', blank=True)
```

**Fields:**
- `user`: The user who bookmarked the image
- `title`: Image title
- `slug`: URL-friendly slug (auto-generated)
- `url`: Original image URL
- `image`: Downloaded and stored image file
- `description`: Optional description
- `created`: Creation timestamp
- `users_like`: Many-to-many relationship for likes

## 🔐 Authentication

### Authentication Backends

The application supports multiple authentication methods:

1. **Django ModelBackend**: Standard username/password authentication
2. **EmailAuthBackend**: Login using email address instead of username
3. **GoogleOAuth2**: Google social authentication

```python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.google.GoogleOAuth2',
]
```

### Social Auth Pipeline

When users authenticate via social providers, a custom pipeline ensures profile creation:

```python
SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'account.authentication.create_profile',  # Custom step
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
]
```

## 📚 API Reference

### Like/Unlike Image

**Endpoint:** `POST /images/like/`

**Request Body:**
```
id: <image_id>
action: "like" | "unlike"
```

**Response:**
```json
{
    "status": "ok"
}
```
or
```json
{
    "status": "error"
}
```

**Headers Required:**
- `X-CSRFToken`: CSRF token from cookies

## 🔧 Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files

```bash
python manage.py collectstatic
```

### Django Shell

```bash
python manage.py shell
```

### Common Commands

```bash
# Run development server
python manage.py runserver

# Run HTTPS development server
python manage.py runserver_plus --cert-file cert.crt 0.0.0.0:8000

# Create superuser
python manage.py createsuperuser

# Check for issues
python manage.py check

# Show URL patterns
python manage.py show_urls
```

## 🚢 Deployment

### Production Checklist

Before deploying to production:

1. **Security Settings**
   ```python
   DEBUG = False
   SECRET_KEY = os.environ.get('SECRET_KEY')
   ALLOWED_HOSTS = ['yourdomain.com']
   ```

2. **Database**
   - Switch to PostgreSQL or MySQL
   - Configure database credentials via environment variables

3. **Static Files**
   ```bash
   python manage.py collectstatic
   ```
   - Configure static file serving (nginx, WhiteNoise, etc.)

4. **HTTPS**
   - Use proper SSL certificates (Let's Encrypt)
   - Enable security middleware:
   ```python
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

5. **Environment Variables**
   - Move all sensitive data to environment variables
   - Use `.env` file or system environment

### Docker Deployment (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "bookmarks.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add tests for new functionality
   - Update documentation as needed

4. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```

5. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you encounter any issues or have questions:

1. Check the existing documentation files:
   - [SETUP_COMPLETE.md](SETUP_COMPLETE.md) - Setup completion guide
   - [GOOGLE_OAUTH_CONFIG.md](GOOGLE_OAUTH_CONFIG.md) - Google OAuth configuration
   - [SOCIAL_AUTH_PROFILE_CREATION.md](SOCIAL_AUTH_PROFILE_CREATION.md) - Social auth profile creation
   - [ALL_FIXED.md](ALL_FIXED.md) - Troubleshooting guide

2. Check Django documentation: https://docs.djangoproject.com/

3. Check Python Social Auth documentation: https://python-social-auth.readthedocs.io/

---

**Built with ❤️ using Django**
