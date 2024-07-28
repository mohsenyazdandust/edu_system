from . import models


class GetLinkInfoMixin:
      
    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except:
            context = {}
        
        if (self.request.user.access_level != 0):
            colleges = [self.request.user.college, ]
        else:
            colleges = models.College.objects.all()

        terms = models.Term.objects.all()
            
        context['link_info'] = {"terms": terms, "colleges": colleges}

        if self.request.session.has_key('active_term'):
            active_term = self.request.session['active_term']
        else:
            active_term = False
        
        if active_term:
            active_term = models.Term.objects.get(id=active_term)
        
        if (self.request.user.access_level != 0):
            active_college = self.request.user.college
        else:
            if self.request.session.has_key('active_college'):
                active_college = self.request.session['active_college']
            else:
                active_college = False
       
            if active_college:
                active_college = models.College.objects.get(id=active_college)

        context['active_info'] = {"term": active_term, "college": active_college}

        return context
