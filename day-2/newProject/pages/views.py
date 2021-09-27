from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Answer

def homeView(requests): 
    # name - > david
    # youre from -> usa
    all_questions = Question.objects.all()
    all_answers = Answer.objects.all() 
    context = {
        "questionsList": all_questions,
        "answersList": all_answers
    }
    return render(requests, 'homePage.html', context)

def aboutView(requests): 
    return render(requests, 'aboutPage.html')

def searchView(requests):
    if requests.method == 'POST': 
        return HttpResponse(requests.POST['username'] + " searched for " + requests.POST['search'])
    return render(requests, 'searchResults.html')