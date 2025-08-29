# To-Do List Application

## Project Overview
This is a comprehensive To-Do List Application built with Django (Python) for the backend and Django Templates, HTML, CSS, and JavaScript (with jQuery and Sortable.js) for the frontend. It provides robust user authentication, persistent task tracking, and a rich set of features designed to help users manage their tasks effectively.

## Features Implemented

1.  **User Authentication:**
    *   Secure user registration, login, and logout.
    *   Each user has their own private task list.

2.  **Task Management:**
    *   Create, view, update, and delete tasks.
    *   Tasks include `title`, `description` (with rich text editor), `due_date`, `priority` (High, Medium, Low), `status` (Pending, In Progress, Complete), `category`, and `attachment`.
    *   **Interactive Due Date Picker:** A calendar interface for easily selecting due dates on task creation/update forms.
    *   **File Attachments:** Users can attach files to tasks.

3.  **Task Prioritization, Categories, and Status:**
    *   Tasks can be assigned a `priority` (High, Medium, Low).
    *   Tasks can be assigned to user-defined `categories`.
    *   Tasks have a `status` (Pending, In Progress, Complete).

4.  **Advanced Filtering, Searching, and Sorting:**
    *   **Search:** Filter tasks by `title` or `description`.
    *   **Filtering:** Filter tasks by `status`, `priority`, `category`, and `due_date` ranges (Overdue, Today, This Week, Next Week).
    *   **Sorting:** Sort tasks by `due_date`, `created date`, `priority`, and `position` (for drag-and-drop).

5.  **Subtasks/Checklists:**
    *   Each main task can have multiple subtasks.
    *   Subtasks can be marked as complete or deleted.

6.  **Drag-and-Drop Task Reordering:**
    *   Tasks in the list can be reordered using drag-and-drop functionality, powered by `Sortable.js` and AJAX. The order is persisted in the database.

7.  **User Avatars/Profile Pictures:**
    *   Users can upload and manage their profile pictures.

8.  **In-App Reminders:**
    *   Notifications displayed prominently on every page for:
        *   Overdue tasks.
        *   Tasks due today.
        *   Tasks due tomorrow.
        *   Tasks due within the next 2-3 days.

9.  **Task Commenting System:**
    *   Users can add comments to individual tasks, visible on the task detail page.

10. **Task Archiving:**
    *   Tasks can be archived to remove them from the active task list without deleting them.
    *   A "Show Archived" toggle is available to view archived tasks.
    *   Archived tasks can be unarchived.

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
Install the required Python packages. If you don't have a `requirements.txt` file, you'll need to install them individually. The key packages used are `Django`, `django-ckeditor`, `Pillow`.

```bash
pip install Django django-ckeditor Pillow
```
(If you have a `requirements.txt` file, use `pip install -r requirements.txt`)

### 5. Database Migrations
Apply the database migrations to create the necessary tables for models (Users, Tasks, Categories, Subtasks, UserProfiles, Comments).

```bash
python manage.py makemigrations tasks
python manage.py migrate
```


### 6. Run the Development Server
Start the Django development server.

```bash
python manage.py runserver
```
The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

### User Authentication
*   **Register:** Click "Register" to create a new user account.
*   **Login:** Use your credentials to log in.
*   **Logout:** Click "Logout" to end your session.

### Task List
*   The homepage displays your active tasks.
*   Use the search bar to find tasks by title or description.
*   Use the dropdown filters to narrow down tasks by status, priority, category, or due date.
*   Use the sort dropdown to change the order of tasks.
*   **Drag-and-Drop:** Drag and drop tasks to reorder them directly on the list. The new order is saved automatically.

### Adding and Updating Tasks
*   **Add New Task:** Click "Add New Task" to create a new task.
*   **Update Task:** Click "View Details" on a task, then "Edit Task" to modify it.
*   **Due Date:** Use the interactive calendar to select due dates.
*   **Rich Text Description:** The description field supports rich text formatting.
*   **Attachments:** Upload files relevant to your tasks.

### Categories
*   **Add New Category:** Click "Add New Category" to create a custom category.
*   **View Categories:** Navigate to the "Categories" page to see all your categories.
*   **Edit/Delete Categories:** You can update or delete existing categories from the "Categories" page.

### Subtasks
*   On the "Update Task" page, you can add new subtasks, toggle their completion status, or delete them.

### Profile Settings
*   Navigate to "Profile Settings" to upload or update your profile picture.

### In-App Reminders
*   Check the top of any page for reminder messages regarding overdue tasks, tasks due today, due tomorrow, or due soon.

### Task Archiving
*   **Archive:** On the task list or task detail page, click "Archive" to move a task to the archive.
*   **Show Archived:** Use the "Show Archived" checkbox in the task list filters to display archived tasks.
*   **Unarchive:** On an archived task, click "Unarchive" to restore it to the active task list.

### Commenting
*   On the "Task Detail" page, you'll find a section to view existing comments and a form to add new comments.

## Technologies Used

*   **Backend:** Python 3.x, Django 5.x
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
