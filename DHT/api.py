
from .models import Dht11
from .serializers import DHT11serialize

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response

from django.core.mail import send_mail
from django.conf import settings

import telebot


@api_view(["GET"])
def Dlist(request):
    all_data = Dht11.objects.all()
    data = DHT11serialize(all_data, many=True).data
    return Response({"data": data})


class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DHT11serialize

    def perform_create(self, serializer):
        # Enregistrer la mesure dans SQLite
        data = serializer.save()

        # Récupérer la température
        temperature = data.temp

        # Déclencher les alertes au-dessus de 25 °C
        if temperature is not None and temperature > 25:

            message = (
                f"ALERTE COLD CHAIN !\n"
                f"Temperature : {data.temp} °C\n"
                f"Humidite : {data.hum} %\n"
                f"Seuil depasse : 25 °C"
            )

            # Envoyer un email Gmail
            send_mail(
                subject="Alerte Temperature - Cold Chain",
                message=message,
                from_email="abdellahfadi002@gmail.com",
                recipient_list=["abdellahfadi002@gmail.com"],
                fail_silently=False
            )

            # Envoyer un message Telegram
            bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)
            bot.send_message(
                settings.TELEGRAM_CHAT_ID,
                message
            )
