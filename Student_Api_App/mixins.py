from django.core.serializers import serialize
import json
from django.http import HttpResponse


class HttpResponseMixin(object):

    def render_to_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type='application/json', status=status)


class SerializeMixin(object):

    def serialize(self, qs):
        json_data = serialize('json', qs)
        p_dict = json.loads(json_data)
        final_list = []
        for obj in p_dict:
            original_data = obj['fields']
            final_list.append(original_data)
        json_data = json.dumps(final_list)
        return json_data
