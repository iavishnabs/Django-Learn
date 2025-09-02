from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('show',views.show,name="showpage"),
    # path('status <int:aid>',views.statusView,name="statusView"),
    path('add',views.add,name="addpage"),
    path('remove <int:aid>',views.remove,name="removeitem"),
    path('edit <int:aid>',views.edit,name="edititem"),
    path('reg',views.Signup,name="regpage"),
    path('login',views.userlogin,name="loginpage"),
    path('logout',views.logoutuser,name="logout")
]
 