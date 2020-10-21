from rest_framework import serializers

'''
This serializer fulfils multiple purpose such as adding user to created_by and updated by.
And fileds option to display field in serializer 
'''
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        try:
            if fields is None:
                req = kwargs['context']['request']
                fields =  req.query_params.get('fields')
                if fields:
                    fields = fields.split(',')
        except Exception as e:
            pass

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

