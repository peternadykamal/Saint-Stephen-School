from django.db import models

import uuid


class Address(models.Model):
  building = models.CharField(max_length=50, null=True, blank=True)
  street = models.CharField(max_length=50, null=True, blank=True)
  branches_from = models.CharField(max_length=50, null=True, blank=True)
  floor = models.CharField(max_length=50, null=True, blank=True)
  apartment_number = models.CharField(max_length=50, null=True, blank=True)
  residential_complexes = models.CharField(
      max_length=50, null=True, blank=True)
  district = models.CharField(max_length=50, null=True, blank=True)
  additional_details = models.TextField(max_length=500, null=True, blank=True)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    details = []
    if self.building:
      details.append(f"مبنا: {self.building}")
    if self.street:
      details.append(f"شارع: {self.street}")
    if self.branches_from:
      details.append(f"متفرع من: {self.branches_from}")
    if self.floor:
      details.append(f"الطابق: {self.floor}")
    if self.apartment_number:
      details.append(f"رقم الشقة: {self.apartment_number}")
    if self.residential_complexes:
      details.append(f"مجمع سكني: {self.residential_complexes}")
    if self.district:
      details.append(f"الحي: {self.district}")
    if self.additional_details:
      details.append(f"تفاصيل إضافية: {self.additional_details}")

    return ', '.join(details)

  def getAddressFromRequset(request, oldAddress=None):

    building = request.POST.get("building")
    street = request.POST.get("street")
    branches_from = request.POST.get("branches_from")
    floor = request.POST.get("floor")
    apartment_number = request.POST.get("apartment_number")
    residential_complexes = request.POST.get("residential_complexes")
    district = request.POST.get("district")
    additional_details = request.POST.get("additional_details")

    if oldAddress:
      oldAddress.building = building
      oldAddress.street = street
      oldAddress.branches_from = branches_from
      oldAddress.floor = floor
      oldAddress.apartment_number = apartment_number
      oldAddress.residential_complexes = residential_complexes
      oldAddress.district = district
      oldAddress.additional_details = additional_details

      oldAddress.save()
      return oldAddress
    else:
      address = Address.objects.create(
          building=building,
          street=street,
          branches_from=branches_from,
          floor=floor,
          apartment_number=apartment_number,
          residential_complexes=residential_complexes,
          district=district,
          additional_details=additional_details
      )
      return address

  def getAddressAttributesInContext(self, context):

    context['building'] = self.building
    context['street'] = self.street
    context['branches_from'] = self.branches_from
    context['floor'] = self.floor
    context['apartment_number'] = self.apartment_number
    context['residential_complexes'] = self.residential_complexes
    context['district'] = self.district
    context['additional_details'] = self.additional_details
