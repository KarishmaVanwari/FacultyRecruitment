from django.db import models
from django.conf import settings 
from django.utils import timezone



class Applicant(models.Model):
    ''' Model for applicants personal data '''
    application_no = models.CharField(primary_key=True, max_length=20)
    date = models.DateField(default=timezone.now())
    post = models.CharField(max_length=100)
    department = models.CharField(max_length=20)
    Research_Domain=models.TextField(default=None)
    
    def __str__(self):
        return str(self.application_no)

class Research_Exp(models.Model):
    '''Model for the research experience of the applicant''' 
    From = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='research_exp',
                )
    duration = models.CharField(max_length=20)
    def __str__(self):
        return str(self.applicant)

class Seminar_Articles(models.Model):
    '''Model for the details of seminars taken by the applicant'''
    article_title = models.TextField()
    seminar_subject = models.TextField()
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    published = models.TextField()
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='seminar_articles',
                )
    duration = models.CharField(max_length=20)
    def __str__(self):
        return str(self.applicant)

class Newspaper_Article(models.Model):
    article_title = models.TextField()
    journal_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_published = models.CharField(max_length=20)
    referred = models.TextField()
    level=models.CharField(max_length=20)
    naas = models.TextField()
    isbn_issn = models.TextField()
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='newspaper_article',
                )
    def __str__(self):
        return str(self.applicant)

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    date_publish = models.CharField(max_length=20)
    isbn= models.TextField()
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='books',
                )
    def __str__(self):
        return str(self.applicant)

class Chapters(models.Model):
    book_title = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    date_of_publisher = models.CharField(max_length=100)
    isbn_issn = models.TextField()
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='applicant',
                )
    def __str__(self):
        return str(self.applicant)

class Academic_detail(models.Model):
    ''' Model for academic details of applicant.'''
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='academic_detail',
                )
    degree = models.CharField(max_length=200)
    area_of_qualification = models.CharField(max_length=200)
    category_of_university = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    status = models.CharField(max_length=200, 
                            choices=[
                                    ('Completed', 'Completed'),
                                    ('ResultAwaited', 'ResultAwaited'),
                                    ('FinalAwaited', 'FinalAwaited'),
                                    ('Ongoing', 'Ongoing'),
                                ],
            )
    year_of_passing = models.IntegerField()
    percentage = models.FloatField()
    
    def __str__(self):
        return str(self.applicant.name)


class Professional_detail(models.Model):
    '''Model for professional details of applicant'''
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='professional_details',
                )
    organisation = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    role = models.CharField(max_length=250)
    pay_scale = models.IntegerField()
    emoluments = models.IntegerField()

    def __str__(self):
        return str(self.applicant.name)


class Teaching_and_research_detail(models.Model):
    '''Teaching details of applicants.'''
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='teaching_and_research_details',
                                null=True,
                                blank=True,
                )
    course_title = models.CharField(max_length=200)
    level = models.CharField(max_length=2,
                            choices=[
                                ('UG', 'Undergraduate'),
                                ('PG', 'Postgraduate'),
                                ],
                            null=True,
                            blank=True,
            )
    sole_instructor = models.CharField(max_length=1,
                                        choices=[
                                            ('Y','Yes'),
                                            ('N','No'),
                                            ],
                                        null=True,
                                        blank=True,
            )
    developer_of_course = models.CharField(max_length=1,
                                            choices=[
                                                ('Y','Yes'),
                                                ('N','No'),
                                                ],
                                            null=True,
                                            blank=True,
            )
    name_of_student = models.CharField(max_length=200, null=True)
    year_of_completion = models.IntegerField(null=True, blank=True)
    name_of_institute = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    guide = models.CharField(max_length=200, null=True, blank=True)
    period = models.CharField(max_length=200, null=True, blank=True)
    organisation = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    co_investigators = models.CharField(max_length=200, null=True, blank=True)
    period = models.CharField(max_length=100, null=True, blank=True)
    name_of_body = models.CharField(max_length=150, null=True, blank=True)
    status_of_membership = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.applicant.name)

class Other_important_details(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='other_details')
    awards_and_recognition = models.TextField()
    any_other_relevant_information = models.TextField()
    reference = models.TextField()
    statement_of_objective = models.TextField()


# class File(models.Model):
#     applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='files')
#     publications = models.FileField(upload_to='uploads/', null=True, blank=True)
#     image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    # caste_certificate = models.FileField(upload_to='uploads/', null=True, blank=True)