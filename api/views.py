from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import status
import datetime
from optionscontract.serializers import OptionsContractSerializer
from optionscontract.models import OptionsContract


# Create your views here.
class CreateNewContractDropDownOptions(APIView):
    def get(self, request):
        contract_type = OptionsContract.CONTRACT_CHOICES
        position_type = OptionsContract.POSITION_CHOICES

        data = {
            'contract_type': contract_type,
            'position_type': position_type
        }

        return Response(data=data, status=status.HTTP_200_OK)
    

class CreateNewContract(APIView):
    def post(self, request):
        serializer = OptionsContractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class RetrieveAllContracts(APIView):
    def get(self, request):
        queryset = OptionsContract.objects.all()
        serializer = OptionsContractSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DeleteOption(APIView):
    def single_task(self, id_arg):
        try:
            queryset = OptionsContract.objects.get(id=id_arg)
            return queryset
        except:
            return None
        
    def delete(self, request, id_arg):
        option = self.single_task(id_arg)
        option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
