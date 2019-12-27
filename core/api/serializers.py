from rest_framework.serializers import ModelSerializer, SerializerMethodField, StringRelatedField
from core.models import Item, Order, OrderItem


class StringSerializer(StringRelatedField):
    def to_internal_value(self, value):
        return value


class ItemSerializer(ModelSerializer):
    category = SerializerMethodField()
    label = SerializerMethodField()

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'price',
            'discount_price',
            'category',
            'label',
            'slug',
            'description',
            'image',
        )

    def get_category(self, obj):
        return obj.get_category_display()

    def get_label(self, obj):
        return obj.get_label_display()


class OrderItemSerializer(ModelSerializer):
    item = StringSerializer()

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'item',
            'quantity',
        )


class OrderSerializer(ModelSerializer):
    order_items = SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'order_items'
        )

    def get_order_items(self, obj):
        return OrderItemSerializer(obj.items.all(), many=True).data
