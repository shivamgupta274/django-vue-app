from rest_framework import serializers

from .models import PartnerInfo, DataSharing, DataSharingDocument, Contanct
import json
class PartnerSerailizer(serializers.ModelSerializer):
    class Meta:
        model = PartnerInfo
        fields = '__all__'
        # fields= (
        #     "partner_name",
        #     "status",
        #     "purchasing_owner",
        #     "is_name_approved",
        #     "region",
        #     "country"
        # )
        # extra_kwargs = {'partner_name': {'required': True}}


class DataSharingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSharingDocument
        fields = '__all__'

class DataSharingSerializer(serializers.ModelSerializer):
    # agreement = serializers.StringRelatedField()
    agreement = DataSharingDocumentSerializer(many=False, read_only=True)

    class Meta:
        model = DataSharing
        fields = ('id', 'partner', 'signed_date','name', 'agreement', 'consent_approach', 'data_parameter', 'data_share', 'iab_tcf_version')
    
    #<developer> older style </developer>
    # agreement = serializers.SerializerMethodField('get_agreement_path')
    # def get_agreement_path(self, obj):
    #     return obj.agreement.agreement
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contanct
        fields = '__all__'