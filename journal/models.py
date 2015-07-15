from django.db import models

# Create your models here.
class Entry(models.Model):
    
    title = models.CharField(max_length=255)
    
    Void = ' '
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September'
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'
    
    month_choices = (
        (Jan, 'January'),
        (Feb, 'February'),
        (Mar, 'March'),
        (Apr, 'April'),
        (May, 'May'),
        (Jun, 'June'),
        (Jul, 'July'),
        (Aug, 'August'),
        (Sep, 'September'),
        (Oct, 'October'),
        (Nov, 'November'),
        (Dec, 'December'),
        (Void, '--'),
    )
    month = models.CharField(max_length=30,
                             choices=month_choices,
                             default=Void)
    
    day = models.CharField(max_length=2)
    content = models.TextField()
    
    def __unicode__(self):
        return (self.day + " " + self.month)
        
        
        