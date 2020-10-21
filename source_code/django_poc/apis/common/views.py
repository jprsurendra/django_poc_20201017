from rest_framework import viewsets

from apis.common.data_wrapper import format_data


class GenericDataWrapper(object):

    def dispatch(self, *args, **kwargs):
        result =  super(GenericDataWrapper, self).dispatch(*args, **kwargs)
        data = format_data(result)
        return data
