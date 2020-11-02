# from __future__ import absolute_import, unicode_literals
# import os
# import random
# from celery import Celery, shared_task
#
# from celery.signals import task_failure, after_task_publish
#
#
# @shared_task
# def demo_task(num):
#     print(" Entered in demo_task")
#     n = random.randint(1,9)
#     i = 1000000000
#     while i > 0:
#         i = i - 1
#     print(" Exit from demo_task")
#     x = num * n
#     from web.books_app.views import BooksListTemplateView
#     BooksListTemplateView.last_value = x
#     return x
#
# @after_task_publish.connect(sender='apis.authors.tasks.demo_task')
# def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
#     info = headers if 'task' in headers else body
#     print('after_task_publish for task id {info[id]}'.format(
#         info=info,
#     ))
#
#
# @task_failure.connect(sender=demo_task)  # FIXME by name it doesn't work
# def task_failure_handler(sender=None, headers=None, body=None, **kwargs):
#     print('This will be executed after if `my task` fails')