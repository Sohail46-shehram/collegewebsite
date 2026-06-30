from django.db import models


# ==========================
# Principal Model
# ==========================

class Principal(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='principal/')
    message = models.TextField()

    def __str__(self):
        return self.name


# ==========================
# Notice Model
# ==========================

class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf = models.FileField(upload_to='notices/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# ==========================
# Program Model
# ==========================

class Program(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='programs/')

    def __str__(self):
        return self.name


# ==========================
# Department Model
# ==========================

class Department(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='departments/')

    def __str__(self):
        return self.name


# ==========================
# Gallery Model
# ==========================

class Gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title
    
    # ==========================
# Hero Slider Model
# ==========================

class HeroSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    image = models.ImageField(upload_to='hero/')
    button_text = models.CharField(max_length=50, default="Explore")
    button_link = models.CharField(max_length=200, default="#")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    
    from django.db import models

class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name