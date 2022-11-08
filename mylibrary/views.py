import logging

from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Document
from .forms import InquiryForm, DocumentCreateForm

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = 'index.html'
    
class InquiryForm(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('mylibrary:inquiry')
    
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Message is sent successfully.')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
    
class DocumentListView(LoginRequiredMixin, generic.ListView):
    model = Document
    template_name = 'doc_list.html'
    paginate_by = 2
    
    def get_queryset(self):
        documents =Document.objects.filter(
            user=self.request.user
        ).order_by('-created_at')
        return documents
    
class DocumentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Document
    template_name = 'doc_detail.html'
    
class DocumentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Document
    template_name = 'doc_create.html'
    form_class = DocumentCreateForm
    success_url = reverse_lazy('mylibrary:document_list')
    
    def form_valid(self, form):
        document = form.save(commit=False)
        document.user = self.request.user
        document.save()
        messages.success(self.request, 'Document is recoded successfully.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Failed to create new record.')
        return super().form_invalid(form)
    
class DocumentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Document
    template_name = 'doc_update.html'
    form_class = DocumentCreateForm
    
    def get_success_url(self):
        return reverse_lazy('mylibrary:document_detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        messages.success(self.request, 'Record is updated.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update record.')
        return super().form_invalid(form)
    
class DocumentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Document
    template_name = 'doc_delete.html'
    success_url = reverse_lazy('mylibrary:document_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Record is deleted.")
        return super().delete(request, *args, **kwargs)