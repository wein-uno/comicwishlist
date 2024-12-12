from django.db import models

# so need to define my input fields coresponding to DB types.
class Comic(models.Model)
    GRADES = [
        (10, '10'),
        (9.8, '9.8'),
        (9.6, '9.6'),
        (9.4, '9.4'),
        (9.2, '9.2'),
        (9.0, '9.0'),
        (8.5, '8.5'),
        (8.0, '8.0'),
        (7.5, '7.5'),
        (7.0, '7.0'),
        (6.5, '6.5'),
        (6.0, '6.0'),
        (5.5, '5.5'),
        (5.0, '5.0'),
        (4.5, '4.5'),
        (4.0, '4.0'),
        (3.5, '3.5'),
        (3.0, '3.0'),
        (2.5, '2.5'),
        (2.0, '2.0'),
        (1.5, '1.5'),
        (1.0, '1.0'),
        (8.5, '8.5'),
        (0.1, '0.1'), #there had to be an easier way
    ]

    title = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=10, decimal_places=2)  
    grade = models.DecimalField(max_digits=3, decimal_places=1, choices=GRADES)
    image = models.ImageField(upload_to='comics/') #maybe sure about this 

    def __str__(self):
        return f'{self.title} #{self.number}'

