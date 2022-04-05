# GDSC-BSUM-OCRS
An online crime reporting system for Benue State University, developed by its GDSC community developers.

# How to Use this code
1. Clone the repository
2. Install django, Pillow, django-crispy-forms, django-ckeditor, pyrebase, crispy-bootstrap5
3. Run migrations with "python manage.py makemigrations" then migrate with "python manage.py migrate" commands.
4. Create a super user with the "python manage.py createsuperuser" command to access the django admin panel
5. Use the registration form to create new user
6. A new user can be given the staff status from the admin panel to make him a security(Security get to see reports)
7. Otherwise the new user is a student.
8. Student can report crimes or make blog post
