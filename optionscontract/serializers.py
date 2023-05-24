from .models import OptionsContract
from rest_framework import serializers

class OptionsContractSerializer(serializers.ModelSerializer):
    profit = serializers.SerializerMethodField()
    

    class Meta:
        model = OptionsContract
        fields = '__all__'

    def get_profit(self, obj):
        closed = obj.closed

        if closed:
            open_price = obj.open_price
            closing_price = obj.closing_price
            fees = obj.fees
            contract_type = obj.contract_type
            position_type = obj.position_type
            quantity = obj.quantity

            if position_type == 'BUY':
                profit = ((closing_price - open_price) * quantity )- fees
            elif position_type == 'SELL':
                profit = ((open_price - closing_price) * quantity) - fees

            return profit
        else:
            return None
        
    def create(self, validated_data):
        # Calculate profit
        closed = validated_data.get('closed', False)
        open_price = validated_data.get('open_price')
        closing_price = validated_data.get('closing_price')
        fees = validated_data.get('fees')
        position_type = validated_data.get('position_type')
        quantity = validated_data.get('quantity')

        if closed and open_price is not None and closing_price is not None and fees is not None and position_type is not None:
            if position_type == 'BUY':
                profit = ((closing_price - open_price) * quantity) - fees
            elif position_type == 'SELL':
                profit = ((open_price - closing_price) * quantity) - fees

            validated_data['profit'] = profit

        return super().create(validated_data)

