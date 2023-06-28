from django.urls import path
from api import views

urlpatterns = [
    path('add', views.CreateNewContract.as_view(), name="add"),
    path('add-contracts/dropdown-options', views.CreateNewContractDropDownOptions.as_view(), name="add-contract/dropdown-options"),
    path('get-all-contracts/', views.RetrieveAllContracts.as_view(), name="get-all-contracts"),
    path('delete/<id_arg>', views.DeleteOption.as_view(), name="delete-option"),
    path('single-contract/<id_arg>', views.SingleOption.as_view(), name="single-contract"),
    path('get-filtered-options', views.FilteredOptions.as_view(), name="get-filtered-options"),
    path('trial-dropdowns', views.FilteredOptionsDropdown.as_view(), name="trial-dropdowns"),
]