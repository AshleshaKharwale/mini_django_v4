from rest_framework.serializers import Serializer
from rest_framework import serializers
from .models import Portal, JobDescription, JobTitle


class PortalSerializer(Serializer):
    name = serializers.CharField(max_length=250, required=True)
    description = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return Portal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class JobDescriptionSerializer(Serializer):
    role = serializers.CharField(max_length=250)
    description_text = serializers.CharField(max_length=250)
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        return JobDescription.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.role = validated_data.get("role", instance.role)
        instance.description_text = validated_data.get("description_text", instance.description_text)
        instance.pub_date = validated_data.get("pub_date", instance.pub_date)
        instance.save()
        return instance


class JobTitleSerializer(Serializer):
    title = serializers.CharField(max_length=250)
    last_updated = serializers.DateTimeField()
    job_description = JobDescriptionSerializer(required=True)
    portal = PortalSerializer(required=True)

    def create(self, validated_data):
        return JobTitle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.last_updated = validated_data.get("last_updated", instance.last_updated)
        instance.job_description = validated_data.get("job_description", instance.job_description)
        instance.portal = validated_data.get("portal", instance.portal)
        instance.save()
        return instance
