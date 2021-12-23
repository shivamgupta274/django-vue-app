from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status, generics , viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PartnerInfo, DataSharing, DataSharingDocument, Contanct
from .serializers import PartnerSerailizer, DataSharingSerializer, DataSharingDocumentSerializer, ContactSerializer
from datetime import datetime 
import json
# Create your views here.

class PartnerList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format= None):
        partners = PartnerInfo.objects.all()
        serializer = PartnerSerailizer(partners, many = True)

        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        partner = PartnerInfo.objects.create(
            partner_name = request.data['partner_name'],
            status = request.data['status'],
            purchasing_owner = request.data['purchasing_owner'],
            is_name_approved = request.data['is_name_approved'],
            region= request.data['region'],
            country = request.data['country']
        )
        partner.save()
        response = {'message': 'Partner is created successfully', 'partner_id':partner.id}
        return Response(response, status= status.HTTP_200_OK)


class PartnerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PartnerInfo.objects.all()
    serializer_class = PartnerSerailizer

    def get(self, request, *args, **kwargs):
        partners = PartnerInfo.objects.get(id= self.kwargs['pk'])
        partners_serializer = PartnerSerailizer(partners)
        
        try:
            data_sharing = DataSharing.objects.get(partner= partners.id)
            data_sharing_serilaizer = DataSharingSerializer(data_sharing)

            contact = Contanct.objects.filter(partner= partners.id)
            
            if contact.exists():
                contact_serilaizer = ContactSerializer(contact , many = True)
                response = {'partner': partners_serializer.data, 'data_sharing' : data_sharing_serilaizer.data, 'contact': contact_serilaizer.data }
            
            else:
                response = {'partner': partners_serializer.data, 'data_sharing' : data_sharing_serilaizer.data }

            return Response(response, status= status.HTTP_200_OK)
        except:
            response = {'partner': partners_serializer.data}
            # response = {'message': 'data saved successfully'}
            return Response(response, status= status.HTTP_200_OK)


class DataSharingList(APIView):

    def get(self, request, format= None):

        datasharing = DataSharing.objects.all()
        serializer = DataSharingSerializer(datasharing, many = True)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     # print(request.data)
    #     rawdata = json.loads(request.data['rawdata'])

    #     partner = PartnerInfo.objects.get(id=int(rawdata['partner_id']))
        
    #     name = rawdata['name']
    #     consent_approach =rawdata['consent_approach']
    #     data_parameter = rawdata['data_parameter']
    #     agreement = request.data['file']
    #     data_share = rawdata['data_share']
    #     iab_tcf_version = rawdata['iab_tcf_version']
    #     data_sharing = DataSharing.objects.create(partner = partner,
    #         name = name, agreement = agreement, consent_approach = consent_approach,
    #         data_parameter = data_parameter, data_share = data_share,  iab_tcf_version = iab_tcf_version
    #     )
    #     data_sharing.save()

    #     response = {'message': 'sharing data saved successfully'}
    #     return Response(request.POST, status= status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        
        rawdata = json.loads(request.data['rawdata'])
        partner = PartnerInfo.objects.get(id=int(rawdata['partner_id']))
        agreement = DataSharingDocument.objects.get(id=int(rawdata['agreement']))
        
        name = rawdata['name']
        consent_approach =rawdata['consent_approach']
        data_parameter = rawdata['data_parameter']
        signed_date = datetime.strptime(rawdata['signed_date'], '%Y-%m-%d')
        data_share = rawdata['data_share']
        iab_tcf_version = rawdata['iab_tcf_version']
        data_sharing = DataSharing.objects.create(partner = partner,
            name = name, agreement = agreement, consent_approach = consent_approach,
            signed_date= signed_date,
            data_parameter = data_parameter, data_share = data_share,  iab_tcf_version = iab_tcf_version
        )
        data_sharing.save()

        response = {'message': 'sharing data saved successfully'}
        return Response(request.POST, status= status.HTTP_200_OK)

class DataSharingDocumentPost(APIView):
    def post(self, request, *args, **kwargs):
        # print(request.data)
        datadocument = DataSharingDocument.objects.create(
            agreement = request.data['agreement']
        )
        datadocument.save()
        response = {'message': 'data saved successfully', 'path': datadocument.__str__(), 'datadocid':datadocument.id}
        print(response)
        return Response(response, status= status.HTTP_200_OK)

class ContactList(APIView):
    def get(self, request, format= None):
        contacts = Contanct.objects.all()
        serializer = ContactSerializer(contacts, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        partner = PartnerInfo.objects.get(id=request.data['partner'])
        contact = Contanct.objects.create(
            partner = partner,
            contact_name = request.data['contact_name'],
            contact_title = request.data['contact_title'],
            contact_email = request.data['contact_email'],
            contact_phone = request.data['contact_phone'],
            contact_ext =  request.data['contact_ext'],
            contact_type = request.data['contact_type']
        )
        contact.save()
        contact_serilaizer = ContactSerializer(contact)

        response = {'message': request.data['contact_type'] +' Contact is created successfully', 'data':contact_serilaizer.data}
        return Response(response, status= status.HTTP_200_OK)


class DataSharingDocumentUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataSharingDocument.objects.all()
    serializer_class = DataSharingDocumentSerializer

class DataSharingUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataSharing.objects.all()
    serializer_class = DataSharingSerializer

class ContactUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contanct.objects.all()
    serializer_class = ContactSerializer
        