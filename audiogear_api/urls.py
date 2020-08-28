from django.urls import path
from .views import audiogear_list, audiogear_detail, AudioGearAPIView, AudioGearDetails, GenericAPIView


urlpatterns = [
    # path('audiogear/', audiogear_list),
    path('audiogear/', AudioGearAPIView.as_view()), #From Class view, call 'as_view()'
    #path('detail/<int:pk>/', audiogear_detail) #<int:pk> is parameter
    path('detail/<int:id>/', AudioGearDetails.as_view()),
    path('generic/audiogear/<int:id>/', GenericAPIView.as_view())

]