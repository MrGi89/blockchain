import json
import pyqrcode
from datetime import datetime
from blockchain import blockexplorer
from django.shortcuts import render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from .forms import AddressForm
from .models import Address, Transaction


class TransactionView(View):

    @staticmethod
    def get_object(address):
        '''Takes id, searches for object in base and returns object or None if object doesn't exists'''
        try:
            return Address.objects.get(address=address)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def transaction_search(address, start, end):
        '''Takes address, filters transactions by start_date and end_date and returns queryset with transactions.'''

        queryset = address.transactions.all()

        if start:
            queryset = queryset.filter(time__gte=datetime.timestamp(start))
        if end:
            queryset = queryset.filter(time__lte=datetime.timestamp(end))
        return queryset

    def get(self, request):

        form = AddressForm()
        return render(request, template_name='base.html', context={'form': form})

    def post(self, request):
        '''Takes given address and validates.
        If address is not in base - saves it create new Address object and saves all transactions.
        Creates QRcode and returns template.
        If address is in base - checks if all transactions are in base and returns template.
        If some transactions are missing deletes object from base and creates new one with all transactions.
        '''
        form = AddressForm(request.POST)
        if form.is_valid():
            form_address = form.cleaned_data['address']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            api_address = blockexplorer.get_address(form_address)
            base_address = TransactionView.get_object(form_address)
            img = pyqrcode.create(form_address)
            img.png('bc_app/static/QRcode.png', scale=3)
            
            if base_address:

                if len(base_address.transactions.all()) == len(api_address.transactions):

                    transactions = TransactionView.transaction_search(base_address, start_date, end_date)
                    return render(request, template_name='base.html', context={'address': base_address,
                                                                               'form': form,
                                                                               'start_date': start_date,
                                                                               'end_date': end_date,
                                                                               'transactions': transactions})
                else:
                    base_address.delete()

            base_address = Address.objects.create(
                address=api_address.address,
                hash160=api_address.hash160,
                final_balance=api_address.final_balance,
                n_tx=api_address.n_tx,
                total_received=api_address.total_received,
                total_sent=api_address.total_sent
            )

            for transaction in api_address.transactions:

                inputs_str = json.dumps(transaction.inputs, default=lambda o: o.__dict__)
                inputs_data = json.loads(inputs_str)

                outputs_str = json.dumps(transaction.outputs, default=lambda o: o.__dict__)
                outputs_data = json.loads(outputs_str)

                Transaction.objects.create(
                    block_height=transaction.block_height,
                    double_spend=transaction.double_spend,
                    hash=transaction.hash,
                    relayed_by=transaction.relayed_by,
                    size=transaction.size,
                    time=transaction.time,
                    tx_index=transaction.tx_index,
                    version=transaction.version,
                    inputs=inputs_data,
                    outputs=outputs_data,
                    address=base_address
                )

            transactions = TransactionView.transaction_search(base_address, start_date, end_date)
            return render(request, template_name='base.html', context={'address': base_address,
                                                                       'form': form,
                                                                       'start_date': start_date,
                                                                       'end_date': end_date,
                                                                       'transactions': transactions})

        return render(request, template_name='base.html', context={'form': form})
