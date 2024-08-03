from . import models


class GetLinkInfoMixin:
      
    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except:
            context = {}
        
        if (self.request.user.access_level == 2):
            colleges = [self.request.user.college, ]
            groups = [self.request.user.group, ]
        else:
            groups = models.Group.objects.all()
            colleges = models.College.objects.all()

        terms = models.Term.objects.all()
            
        context['link_info'] = {"terms": terms, "colleges": colleges, 'groups': groups}

        if self.request.session.has_key('active_term'):
            active_term = self.request.session['active_term']
        else:
            active_term = False
        
        if active_term:
            active_term = models.Term.objects.get(id=active_term)
        
        if (self.request.user.access_level == 2):
            active_college = self.request.user.college
            active_group = self.request.user.group
        else:
            if self.request.session.has_key('active_college'):
                active_college = self.request.session['active_college']
            else:
                active_college = False
                
            if self.request.session.has_key('active_group'):
                active_group = self.request.session['active_group']
            else:
                active_group = False
       
            if active_group:
                active_group = models.Group.objects.get(id=active_group)

            if active_college:
                active_college = models.College.objects.get(id=active_college)

        context['active_info'] = {"term": active_term, "college": active_college, 'group': active_group}

        return context
