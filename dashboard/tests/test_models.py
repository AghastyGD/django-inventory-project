from django.test import TestCase
from ..models import Product, Order
from django.contrib.auth.models import User

# Um simples teste para garantir a funcionalidade do codigo
class UsuarioTestCase(TestCase):
  def test_um_e_um(self):
    self.assertEqual(2,1)

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name='Xiaomi 12',
            category='Electrônicos',
            quantity=5
        )
        self.assertEqual(str(product), 'Xiaomi 12: 5')

class OrderModelTest(TestCase):
    def setUp(self):
        # Criar um usuário e um produto para serem usados nos testes
        self.user = User.objects.create_user(username='cleiton', password='1234')
        self.product = Product.objects.create(
            name='Xiaomi 12',
            category='Electrônicos',
            quantity=5
        )

    def test_order_creation(self):
        order = Order.objects.create(
            product=self.product,
            staff=self.user,
            order_quantity=5
        )
        self.assertEqual(str(order), 'Xiaomi 12: 5 ordered by cleiton')

    def test_order_date_auto_now_add(self):
        order = Order.objects.create(
            product=self.product,
            staff=self.user,
            order_quantity=5
        )
        self.assertIsNotNone(order.date)
        