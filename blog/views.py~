from django.shortcuts import render
from .models import Questions,person

# Create your views here.

def index(request):
	question_list = Questions.objects.all()
	context_dict = {'questions': question_list}

	return render(request, 'quiz_app/index.html', context_dict)

def submit(request):
   
    answer = Questions.objects.all()
    

    if answer.correct_ans == answer.option1:
       outcome = "correct"
    else:
       outcome = "incorrect"
    context_dict = {'correct': cor}

    return render(request, 'quiz_app/submit.html', context_dict)
       



# Create your views here.
