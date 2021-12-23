from django.db import models

STATUS= (
    ('new_partner', 'NEW PARTNER'),
    ('old_partner', 'OLD PARTNER'),
    ('assistant_partner', 'ASSISTANT PARTNER')
)
REGION = [
    ('{"key": "GL", "value": "GLOBAL"}', 'GLOBAL'),
    ('{"key": "EN", "value": "ENGLISH"}', 'ENGLISH'),
    ('{"key": "AR", "value": "ARABIC"}', 'ARABIC'),
    ('{"key": "FR", "value": "FRENCH"}','FRENCH')
]
COUNTRY = (
    ('brazil', 'BRAZIL'),
    ('united_arab_emirates', 'UNITED ARAB EMIRATES'),
    ('united_stats_of_america', 'UNITED STATES OF AMERICA'),
    ('china', 'CHINA'),
    ('germany', 'GERMANY')
)
CONSENT_APPROACHS =(
    ('manager', 'MANAGER'),
    ('product_owner', 'PRODUCT OWNER'),
    ('product_manager', 'PRODUCT MANAGER')
)
IAB_TCF_VERSIONS =(
    ('v1.1', 'TCF v1.1'),
    ('v2.0', 'TCF v2.0')
)
DOCUMENTS =(
    ('description_document', 'DESCRIPTION DOCUMENT'),
    ('high_level_design_document', 'HIGH LEVEL DESIGN DOCUMENT'),
    ('diagram_document', 'DIAGRAM DOCUMENT')
)
DATA_PARAMETERS =(
    ('update_report', 'UPDATE REPORT'),
    ('remove_params_from_report', 'REMOVE PARAMETERS FROM REPORT')
)

class PartnerInfo(models.Model):
    partner_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS)
    purchasing_owner = models.CharField(max_length=25)
    is_name_approved = models.CharField(max_length= 10)
    region = models.CharField(max_length= 255)
    country = models.CharField(max_length=50, choices= COUNTRY)

    def __str__(self):
        return self.partner_name + ' '+ self.status

class DataSharingDocument(models.Model):
    agreement = models.FileField(upload_to='uploaded_doc1/', blank= True)

    def __str__(self):
        return self.agreement.url

class DataSharing(models.Model):
    partner = models.ForeignKey(PartnerInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    agreement = models.ForeignKey(DataSharingDocument, on_delete= models.CASCADE)
    consent_approach = models.CharField(max_length=50, choices=CONSENT_APPROACHS)
    data_parameter = models.CharField(max_length=50, choices=DATA_PARAMETERS)
    data_share = models.CharField(max_length=50, choices=DOCUMENTS)
    signed_date = models.DateField(blank=True, null=True)
    iab_tcf_version = models.CharField(max_length=50, choices=IAB_TCF_VERSIONS)

    class Meta:
        unique_together = (('partner'),)

    def __str__(self):
        return self.name + ' '+ self.consent_approach

class Contanct(models.Model):
    partner = models.ForeignKey(PartnerInfo, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=50)
    contact_title = models.CharField(max_length= 50)
    contact_email = models.EmailField(max_length=254)
    contact_phone = models.CharField(max_length=12)
    contact_ext =  models.CharField(max_length=4)
    contact_type = models.CharField(max_length=10)

    def __str__(self):
        return self.contact_name + '' + self.contact_type






