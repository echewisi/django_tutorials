from django.db import models

class Author(models.Model):
    name= models.CharField(max_length= 255, null= False, blank= False)

    def __str__(self):
        return self.name
        

class Books(models.Model):
    title= models.CharField(max_length= 255, null= False, blank= False)
    author= models.ForeignKey(Author, on_delete= models.CASCADE)
    published_date= models.DateField()
    
    def __str__(self):
        return f'{self.title} by  {self.author}'
        

class Review(models.Model):
    book= models.ForeignKey(Books, on_delete= models.CASCADE)
    review= models.TextField()
    
    def __str__(self):
        return f'{self.book}  {self.review}'
        
# Create your models here.
