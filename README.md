# To-Do List Application

## Project Overview
This is a comprehensive To-Do List Application built with Django (Python) for the backend and Django Templates, HTML, CSS, and JavaScript (with jQuery and Sortable.js) for the frontend. It provides robust user authentication, persistent task tracking, and a rich set of features designed to help users manage their tasks effectively.

## Features Implemented

1.  **Modern User Authentication & Flow:**
    *   Secure user registration, login, and logout via Django REST Framework API endpoints.
    *   Client-side JavaScript for asynchronous form submission, dynamic password strength meter, and show/hide password toggles.
    *   Detailed and user-friendly error messages during registration and login.
    *   Seamless redirection flow: Register -> Login -> Dashboard/Onboarding.
    *   Each user has their own private task list.

2.  **Public Home Page:**
    *   Welcoming landing page highlighting application features and call-to-action for registration.
    *   Consistent "glass panel" aesthetic.

3.  **Dashboard Overview:**
    *   A personalized dashboard displaying task summaries (total, pending, in-progress, completed, archived).
    *   Prominent task reminders for overdue, due today, due tomorrow, and due soon tasks.
    *   Quick action links to add new tasks or categories.

4.  **Task Management:**
    *   Create, view, update, and delete tasks.
    *   Tasks include `title`, `description` (with rich text editor), `due_date`, `priority` (High, Medium, Low), `status` (Pending, In Progress, Complete), `category`, and `attachment`.
    *   **Interactive Due Date Picker:** A calendar interface for easily selecting due dates on task creation/update forms.
    *   **File Attachments:** Users can attach files to tasks.

5.  **Task Prioritization, Categories, and Status:**
    *   Tasks can be assigned a `priority` (High, Medium, Low).
    *   Tasks can be assigned to user-defined `categories`.
    *   Tasks have a `status` (Pending, In Progress, Complete).

6.  **Advanced Filtering, Searching, and Sorting:**
    *   **Search:** Filter tasks by `title` or `description`.
    *   **Filtering:** Filter tasks by `status`, `priority`, `category`, and `due_date` ranges (Overdue, Today, This Week, Next Week).
    *   **Sorting:** Sort tasks by `due_date`, `created date`, `priority`, and `position` (for drag-and-drop).

7.  **Subtasks/Checklists:**
    *   Each main task can have multiple subtasks.
    *   Subtasks can be marked as complete or deleted.

8.  **Drag-and-Drop Task Reordering:**
    *   Tasks in the list can be reordered using drag-and-drop functionality, powered by `Sortable.js` and AJAX. The order is persisted in the database.

9.  **User Avatars/Profile Pictures:**
    *   Users can upload and manage their profile pictures.
    *   Includes a default placeholder image if no profile picture is set.

10. **In-App Reminders:**
    *   Notifications displayed prominently on every page for:
        *   Overdue tasks.
        *   Tasks due today.
        *   Tasks due tomorrow.
        *   Tasks due within the next 2-3 days.

11. **Task Commenting System:**
    *   Users can add comments to individual tasks, visible on the task detail page.

12. **Task Archiving:**
    *   Tasks can be archived to remove them from the active task list without deleting them.
    *   A "Show Archived" toggle is available to view archived tasks.
    *   Archived tasks can be unarchived.

13. **Unified "Glass Panel" Theme:**
    *   Consistent dark, semi-transparent design applied across public pages (Home, Register, Login) and authenticated pages (Dashboard, Tasks, Categories, Profile).
    *   Prominent gold-box styling for key action links and button-like appearance for navigation links.

## Installation and Setup

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository (if applicable)
If this project is hosted on a repository, clone it first:
```bash
git clone <repository_url>
cd To_Do_List_Application
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

*   **Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
*   **macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies
Install the required Python packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Create Static Files Directory and Placeholder Image
Ensure the static files directory for images exists and place a `default_profile.png` image there.
```bash
mkdir -p tasks/static/tasks/images/

```

### 6. Database Migrations
Apply the database migrations to create the necessary tables for models (Users, Tasks, Categories, Subtasks, UserProfiles, Comments).

```bash
python manage.py makemigrations tasks
python manage.py migrate
```

### 7. Run the Development Server
Start the Django development server.

```bash
python manage.py runserver
```
The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

### Public Pages
*   **Home:** The landing page provides an overview of the application.
*   **Register:** Create a new user account with enhanced client-side validation.
*   **Login:** Log in to your account with improved error feedback.

### Authenticated Pages
*   **Dashboard:** View your task summaries and reminders at a glance.
*   **Task List:** The main page to view, filter, sort, and reorder your active tasks.
*   **Adding and Updating Tasks:** Create new tasks, and view/edit existing task details including description, due date (with date picker), priority, category, subtasks, and attachments.
*   **Categories:** Manage your custom task categories.
*   **Profile Settings:** Upload or update your profile picture.
*   **Logout:** End your session.

## Technologies Used

*   **Backend:** Python 3.x, Django 5.x, Django REST Framework (DRF), `django-cors-headers`, `django-environ`.
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Libraries/Frameworks:**
    *   jQuery (for AJAX and DOM manipulation)
    *   jQuery UI Datepicker (for interactive date selection)
    *   Sortable.js (for drag-and-drop task reordering)
    *   `django-ckeditor` (for rich text editor)
    *   `Pillow` (for image processing with profile pictures and attachments)
*   **Database:** SQLite (default for Django development, easily configurable for others like PostgreSQL or MySQL)

---
Enjoy managing your tasks efficiently!
