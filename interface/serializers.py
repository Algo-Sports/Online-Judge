from rest_framework import serializers
from interface.models import Question, Contest


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionListSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'question_name': instance.question_name,
            'question_code': instance.question_code,
            'question_score': instance.question_score
        }

class ContestSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'contest_name': instance.contest_name,
            'contest_code': instance.contest_code,
            'start_time': instance.start_time.timestamp(),
            'end_time' : instance.end_time.timestamp()
        }