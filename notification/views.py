from rest_framework import generics, permissions, mixins, status, views
from notification.serializers import TokenSerializer
from notification.models import DeviceToken
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from notification.Notify import EventTrigger 
from . import models 
import datetime

class ListToken(generics.ListAPIView):
    queryset = DeviceToken.objects.all()
    serializer_class = TokenSerializer

class CreateToken(generics.CreateAPIView):
    queryset = DeviceToken.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class DeleteToken(generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset = DeviceToken.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def get_queryset(self):
        try:
            token = DeviceToken.objects.get(pk=self.kwargs['pk'])
        except:
            token = None
        return token

    def delete(self, request, *args, **kwargs):
        if self.get_queryset():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('Token have not created already!')

class DeleteTokens(generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset = DeviceToken.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def get_queryset(self):
        tokens = DeviceToken.objects.filter(creator=self.request.user)
        return tokens

    def delete(self, request, *args, **kwargs):
        if len(self.get_queryset()) > 0:
            for token in self.get_queryset():
                token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('The user has not created any token already!')

class SendTestMessage(views.APIView):
    serializer_class = TokenSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        to_email = ['rastavatest@gmail.com' , 'kiarashezadpanah@gmail.com' ]
        to_phone = ['+989399162041','+9890288899663']
        template_data = [{'name' : 'rastava' , 'site' :'rastava.co'} ,{'name' : 'kiarash' , 'age' : '' }]
        multinotification = models.MultiNotify.objects.get(notify_name = 'Phone')
        date_time=datetime.datetime(2021, 12, 29, 18, 33, 9, 210065)
        notify = EventTrigger(multinotification,date_time,to_email , to_phone , None,template_data )
        response = notify.trigger()
        return Response(data=response, status=status.HTTP_200_OK)
#---


