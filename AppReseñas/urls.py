from django.urls import path
from AppReseñas import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('about', views.about, name='Acerca de mí'),
    path('addReseña', views.addReseña, name='Añadir Reseña'),
    path('buscar/', views.buscar),
    path('addEstrenos',views.addEstrenos, name='Añadir Estrenos'),
    path('Estrenos', views.estrenos, name='Estrenos'),
    path("editarEstreno/<estreno_nombre>", views.editarEstreno, name="Editar Estreno"),

    path('login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='AppReseñas/Autenticar/logout.html'), name='Logout'),
    path('register', views.register, name = 'Register'),
    path("editarUsuario", views.editarUsuario, name="Editar Usuario"),

]
