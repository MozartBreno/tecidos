from rest_framework.serializers import ModelSerializer
from cliente.models import Cliente

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao', 'horario_func', 'idade_minima')