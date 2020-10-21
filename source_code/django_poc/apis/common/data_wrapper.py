from rest_framework.response import Response

def data_wrapper_response(data=None, status_code=None):
	if status_code in [200,201,204]:
		status = True
	else:
		status = False

	data = {
		'status':status,
		'status_code':status_code,
		'data':data
	}
	
	return Response(data, status=status_code)


def format_data(result):
	if result.status_code in [200,201]:
		status = True
	else:
		status = False

	data = {
		'status':status,
		'status_code':result.status_code,
		'data':result.data
	}
	result.data = data

	return result