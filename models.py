from django.db import models
       from django.utils import timezone

       class User(models.Model):
           USER_ROLES = (
               ('student', 'Student'),
               ('faculty', 'Faculty'),
               ('librarian', 'Librarian'),
           )
           user_id = models.AutoField(primary_key=True)
           name = models.CharField(max_length=200)
           role = models.CharField(max_length=10, choices=USER_ROLES, default='student')
           email = models.EmailField(unique=True)
           department = models.CharField(max_length=100, blank=True, null=True)
           faculty_subjects = models.ManyToManyField('Subject', related_name='faculty_users', blank=True)

           def __str__(self):
               return self.name

       class Subject(models.Model):
           subject_id = models.AutoField(primary_key=True)
           subject_name = models.CharField(max_length=200)
           semester = models.IntegerField()
           total_books = models.IntegerField(default=0)

           def __str__(self):
               return self.subject_name

       class Book(models.Model):
           book_id = models.AutoField(primary_key=True)
           title = models.CharField(max_length=200)
           author = models.CharField(max_length=200)
           isbn = models.CharField(max_length=20, unique=True)
           subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='books')
           semester = models.IntegerField()
           total_copies = models.IntegerField(default=1)
           available_copies = models.IntegerField(default=1)

           def __str__(self):
               return self.title

       class Transaction(models.Model):
           transaction_id = models.AutoField(primary_key=True)
           user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
           book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transactions')
           borrow_date = models.DateField(default=timezone.now)
           return_date = models.DateField(null=True, blank=True)
           status = models.CharField(max_length=10, choices=[('borrowed', 'Borrowed'), ('returned', 'Returned'), ('overdue', 'Overdue')], default='borrowed')
           fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

           def __str__(self):
               return f"{self.user.name} - {self.book.title} - {self.status}"
