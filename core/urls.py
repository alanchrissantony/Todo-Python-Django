
from django.urls import path

from core.views import delete, home, update








urlpatterns = [
    path('', home, name='home'),
    path('update/<int:todo_id>/', update, name='update'),
    path('delete/<int:todo_id>/', delete, name='delete')
]
