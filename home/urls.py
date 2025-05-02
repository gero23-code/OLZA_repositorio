from django.urls import path
from home.views import inicio, buscar_skin, listado_de_skins, detalle_skin, VistaDetalleSkin, VistaModificarSkin, VistaEliminarSkin

urlpatterns = [
    path("", inicio, name ="inicio"),
    path("skins/", buscar_skin, name ="buscar_skin"),
    path("skins/buscar/", listado_de_skins, name ="listado_de_skins"),
    path("skins/<int:pk>/", VistaDetalleSkin.as_view(), name ="detalle_skins"), 
    path("skin/<int:pk>/modificar/", VistaModificarSkin.as_view(), name ="modificar_skin"),
    path("skin/<int:pk>/eliminar/", VistaEliminarSkin.as_view(), name ="eliminar_skin"),
]

