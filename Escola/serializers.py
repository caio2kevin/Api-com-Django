from rest_framework import serializers
from Escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = [
            'id',
            'nome',
            'email',
            'cpf',
            'data_nascimento',
            'telefone'
                    ]



class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = [
            'codigo',
            'descricao',
            'nivel'

            #pode colocar tbm o filds = '__all__' pega todos os campos da tabela
                    ]


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []