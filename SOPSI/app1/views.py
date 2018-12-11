from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Choice, Question
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'app1/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Devuelve las 5 últimas preguntas publicadas."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'app1/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'app1/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app1/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('app1:results', args=(question_id,)))

