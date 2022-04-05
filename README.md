# GDSC-BSUM-OCRS
An online crime reporting system for Benue State University, developed by its GDSC community developers.

# How to Use this code
1. Clone the repository
2. Open the python-team-contribution branch
3. Install django, Pillow, django-crispy-forms, django-ckeditor, pyrebase, crispy-bootstrap5
4. Run migrations with "python manage.py makemigrations" then migrate with "python manage.py migrate" commands.
5. Create a super user with the "python manage.py createsuperuser" command to access the django admin panel
6. Use the registration form to create new user
7. A new user can be given the staff status from the admin panel to make him a security(Security get to see reports)
8. Otherwise the new user is a student.
9. Student can report crimes or make blog post
