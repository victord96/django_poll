from django.db.models.enums import Choices
from django.db.models.lookups import Contains
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models.query_utils import Q


filtered_question = Question.objects.filter(Q(pub_date__lte=timezone.now()) & Q(choice__isnull=False)).distinct()


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """Return the last five published questions.(not including those set to be
    published in the future or without choices)"""
        
        return filtered_question.order_by('-pub_date')[:5]


class AdminIndexView(generic.ListView):
    template_name = 'polls/superindex.html'
    context_object_name = 'latest_question_list'

    
    def get_queryset(self):
        """Return all the questions"""
        
        return Question.objects.all    


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet (and without choices)
        """
        return filtered_question


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet (and without choices)
        """
        return filtered_question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))   