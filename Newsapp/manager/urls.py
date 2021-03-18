
from django.urls import path
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('panel/manager/list/', views.manager_list, name='manager_list'),
    path('panel/manager/1del/<int:id>', views.manager_del, name='manager_del'),
    path('panel/manager/group/', views.manager_group, name='manager_group'),
    path('panel/manager/perms/', views.manager_perms, name='manager_perms'),
    path('panel/manager/perms/del/<str:name>', views.manager_perms_del, name='manager_perms_del'),
    path('panel/manager/perms/add', views.manager_perms_add, name='manager_perms_add'),
    path('panel/manager/group/add', views.manager_group_add, name='manager_group_add'),
    path('panel/manager/group/del/<str:name>', views.manager_group_del, name='manager_group_del'),
    path('panel/manager/group/show/<int:id>', views.user_group, name='user_group'),
    path('panel/manager/perms/show/<int:id>', views.user_perms, name='user_perms'),
    path('panel/manager/addusertogroup/<int:id>', views.add_user_to_groups, name='add_user_to_groups'),
    path('panel/manager/delusertogroup/<int:id>/<str:name>', views.del_user_to_groups, name='del_user_to_groups'),
    path('panel/manager/delusertoperm/<int:id>/<str:name>', views.user_perms_del, name='user_perms_del'),
    path('panel/manager/addusertoperm/<int:id>', views.user_perms_add, name='user_perms_add'),
    path('panel/manager/addgroupstoperms/<str:name>', views.groups_perms, name='groups_perms'),
    path('panel/manager/gorup/delperms/<str:gname>/<str:name>', views.groups_perms_del, name='groups_perms_del'),
    path('panel/manager/gorup/addperms/<str:name>', views.groups_perms_add, name='groups_perms_add'),

]

