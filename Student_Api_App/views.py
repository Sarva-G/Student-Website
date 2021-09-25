import json
from django.shortcuts import render
from django.views.generic import View
from .utils import is_json
from .mixins import HttpResponseMixin, SerializeMixin
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import StudentForm


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentCRUDCBV(SerializeMixin, HttpResponseMixin, View):

    def get_object_by_id(self, id):
        try:
            emp = Student.objects.get(id=id)
        except Student.DoesNotExist:
            emp = None
        return emp

# ----------------------------------------------------------------------------------------------------------------------

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'Error Message': 'The given data is NOT a valid json. Please check!'})
            return self.render_to_http_response(json_data, status=404)
        else:
            p_data = json.loads(data)
            id = p_data.get('id', None)
            if id is not None:
                std = self.get_object_by_id(id)
                if std is None:
                    json_data = json.dumps({'Error Message': 'The given ID has NO matched student record. Please check!'})
                    return self.render_to_http_response(json_data, status=404)
                else:
                    json_data = self.serialize([std,])
                    return self.render_to_http_response(json_data)
            else:
                qs = Student.objects.all()
                json_data = self.serialize(qs)
                return self.render_to_http_response(json_data)

# ----------------------------------------------------------------------------------------------------------------------


    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'Error Message': 'The given data is NOT a valid json. Please check!'})
            return self.render_to_http_response(json_data, status=404)
        else:
            p_data = json.loads(data)
            form = StudentForm(p_data)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({'Message': 'The given data is Created Successfully'})
                return self.render_to_http_response(json_data)
            elif form.errors:
                json_data = json.dumps(form.errors)
                return self.render_to_http_response(json_data, status=404)

# ----------------------------------------------------------------------------------------------------------------------

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'Error Message': 'The given data is NOT a valid json. Please check!'})
            return self.render_to_http_response(json_data, status=404)
        else:
            p_data = json.loads(data)
            id = p_data.get('id', None)
            if id is None:
                json_data = json.dumps({'Error Message': 'The given id is NOT found. Please check!'})
                return self.render_to_http_response(json_data, status=404)
            else:
                std = self.get_object_by_id(id)
                original_data = {
                    's_name': std.s_name,
                    's_class': std.s_class,
                    's_city': std.s_city,
                    's_lover': std.s_lover
                }
                new_data = original_data.update(p_data)
                form = StudentForm(new_data, instance=std)
                if form.is_valid():
                    form.save(commit=True)
                    json_data = json.dumps({'Message': 'The given data is Updated Successfully'})
                    return self.render_to_http_response(json_data)
                if form.errors:
                    json_data = json.dumps(form.errors)
                    return self.render_to_http_response(json_data, status=404)

# ----------------------------------------------------------------------------------------------------------------------

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'Error Message': 'The given data is NOT a valid json. Please check!'})
            return self.render_to_http_response(json_data, status=404)
        else:
            p_data = json.loads(data)
            id = p_data.get('id', None)
            if id is None:
                json_data = json.dumps({'Error Message': 'The given ID is NOT found. Please check!'})
                return self.render_to_http_response(json_data, status=404)
            else:
                std = self.get_object_by_id(id)
                if std is None:
                    json_data = json.dumps({'Error Message': 'The given ID is has NO matched records. Please check!'})
                    return self.render_to_http_response(json_data, status=404)
                else:
                    deletion_status, deleted_item = std.delete()
                    if deletion_status == 1:
                        json_data = json.dumps({'Message': 'The given ID Deleted Successfully'})
                        return self.render_to_http_response(json_data)
                    else:
                        json_data = json.dumps({'Error Message': 'The given ID Not Deleted! Please try again'})
                        return self.render_to_http_response(json_data, status=404)

# ----------------------------------------------------------------------------------------------------------------------
