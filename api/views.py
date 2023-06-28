from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import status
import datetime
from optionscontract.serializers import OptionsContractSerializer
from optionscontract.models import OptionsContract


# Create your views here.

# View for displaying the options in the dropdown menus on the add and edit contract pages
class CreateNewContractDropDownOptions(APIView):
    def get(self, request):
        contract_type = OptionsContract.CONTRACT_CHOICES
        position_type = OptionsContract.POSITION_CHOICES

        data = {
            'contract_type': contract_type,
            'position_type': position_type
        }

        return Response(data=data, status=status.HTTP_200_OK)

# view for returning all unique years for date_opened field to populate in dropdown menu for filtering    
class FilteredOptionsDropdown(APIView):
    def get(self, request):
        unique_years = OptionsContract.objects.dates('date_opened', 'year', order='DESC')
        years = [str(year.year) for year in unique_years]
        return Response(years, status=status.HTTP_200_OK)
    

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
    def single_option(self, id_arg):
        try:
            queryset = OptionsContract.objects.get(id=id_arg)
            return queryset
        except:
            return None
        
    def delete(self, request, id_arg):
        option = self.single_option(id_arg)
        option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SingleOption(APIView):
    def single_option(self, id_arg):
        try:
            queryset = OptionsContract.objects.get(id=id_arg)
            return queryset
        except:
            return None

    def get(self, request, id_arg):
        option = self.single_option(id_arg)
        serializer = OptionsContractSerializer(option)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id_arg):
        option = self.single_option(id_arg)

        option.ticker = request.data.get("ticker")
        option.contract_type = request.data.get("contract_type")
        option.position_type = request.data.get("position_type")
        option.expiration = request.data.get("expiration")
        option.strike_price = request.data.get("strike_price")
        option.quantity = request.data.get("quantity")
        option.open_price = request.data.get("open_price")
        option.date_opened = request.data.get("date_opened")
        option.date_closed = request.data.get("date_closed")
        option.closing_price = request.data.get("closing_price")
        option.closed = request.data.get("closed")
        option.fees = request.data.get("fees")

        serializer = OptionsContractSerializer(option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view for filtering options data based on filter fields passed in
class FilteredOptions(APIView):
    def query(self):
        try:
            queryset = OptionsContract.objects.all()
            return queryset
        except:
            return None

    def filtered_options(self, filtered_argument, queryset):
        filtered_queryset = queryset
        if(filtered_argument.get('ticker') != ""):
            ticker = filtered_argument.get("ticker")
            filtered_queryset = queryset.filter(ticker=ticker)

        if(filtered_argument.get('date_opened_year') != ""):
            year = filtered_argument.get('date_opened_year')
            filtered_queryset = filtered_queryset.filter(date_opened__year=year)

        if(filtered_argument.get('closed') != ""):
            closed = filtered_argument.get('closed')
            filtered_queryset = filtered_queryset.filter(closed=closed)

        

        
        # for filtering dates
        # Sample.objects.filter(date__year='2011', 
        #               date__month='01')
        
        
        return filtered_queryset
        # try:
        #     filtered_queryset = queryset.filter(filtered_argument)
        #     return filtered_queryset
        # except:
        #     return None
        
    def get(self, request):
        filtered_arguments = request.data
        print(filtered_arguments)
        # return Response(status=status.HTTP_200_OK)
        queryset = self.query()
        filtered_queryset = self.filtered_options(filtered_arguments, queryset)
        print(filtered_queryset)
        serializer = OptionsContractSerializer(filtered_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FilteredOptionsForGraphs(APIView):
    pass