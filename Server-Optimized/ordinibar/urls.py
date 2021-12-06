from ordinibar import admin_views
from . import views
from . import admin_views
from django.urls import path

app_name = 'ordinibar'
urlpatterns = [
    #Urls
    path("login", views.loginView, name = "login"),
    path("logout", views.logoutView, name = "logout"),
    path("", views.indexView, name = "index"),
    path("ordine",views.ordineView, name = "ordine"),
    path("ordine/addordine", views.addOrdineView, name = "add_ordine"),
    path("ordineconfirmed", views.ordineConfirmedView, name="ordine_confirmed"),
    path("account", views.accountView, name = "account"),
    path("cronologia", views.cronologiaView, name ="cronologia"),
    #ADMIN URLS
    path("bivio", admin_views.bivioView, name = "bivio"),
    path("listaordini",admin_views.listaOrdiniView, name = "lista_ordini"),
]