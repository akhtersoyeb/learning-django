from django.db import models

class Question(models.Model): 
    text = models.CharField(max_length=150)

    def __str__(self):
        return self.text
class Answer(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    answer_text = models.CharField(max_length=150)

    def __str__(self): 
        return self.answer_text

# every question can have many answers some of them can
# be right others can be wrong

# every right answer has exactly question