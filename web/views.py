# -*- coding: utf8 -*-
from django.shortcuts import render
from django.views import generic
from .models import Topic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reply
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class TopicListView(generic.ListView):
    model = Topic
    ordering = ['-id']  
    paginate_by = 3    
    
class TopicDetailView(generic.DetailView):
    model = Topic
    
    def get_object(self):      
        topic = Topic.objects.get(id=self.kwargs['pk'])
        # 將瀏覽人次加1
        topic.hit = topic.hit + 1
        topic.save()
        return topic
    
    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['reply_list'] = Reply.objects.filter(topic_id= self.kwargs['pk']).order_by("-id")
        return context
    
class TopicCreate(CreateView):
    model = Topic
    fields = ['subject', 'content', 'poster']
    success_url = "/"   
    template_name = 'form.html'   
    
class ReplyCreate(CreateView):
    model = Reply
    fields = ['content', 'poster']
    template_name = 'form.html' 
    
    def form_valid(self, form):
        reply = form.save(commit=False)
        reply.topic_id = self.kwargs['topic_id']
        topic = Topic.objects.get(id=self.kwargs['topic_id'])
        topic.reply_date = datetime.now()
        topic.save()
        return super().form_valid(form) 
      
    def get_success_url(self):
        success_url =  '/web/topic/'+ str(self.kwargs['topic_id'])
        return success_url

@method_decorator(login_required, name='dispatch')      
class TopicDelete(DeleteView):
    model = Topic
    success_url = "/"
    template_name = 'confirm_delete.html'
    
@method_decorator(login_required, name='dispatch')      
class ReplyDelete(DeleteView):
    model = Reply
    template_name = 'confirm_delete.html'    
    
    def get_success_url(self):
        success_url =  '/web/topic/'+ str(self.kwargs['topic_id'])
        return success_url