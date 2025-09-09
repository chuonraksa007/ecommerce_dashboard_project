from datetime import datetime
from sqlalchemy.future import select
from app.models.customer_model import Customer
from app.models.product_model import Product
from app.models.order_model import Order

async def seed_data(session):
    # Customers
    result = await session.execute(select(Customer))
    if result.first() is None:
        customers = [
            Customer(name="Alice", created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Customer(name="Bob", created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Customer(name="Charlie", created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Customer(name="Diana", created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Customer(name="Ethan", created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Customer(name="Fiona", created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Customer(name="George", created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Customer(name="Hannah", created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
        ]
        session.add_all(customers)

    # Products
    result = await session.execute(select(Product))
    if result.first() is None:
        products = [
            Product(name="iPhone 15", qty=50, amount=999.99, category_id=1,
                    created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Product(name="MacBook Pro", qty=20, amount=1999.99, category_id=1,
                    created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Product(name="AirPods Pro", qty=100, amount=249.99, category_id=2,
                    created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Product(name="Samsung Galaxy S23", qty=60, amount=899.99, category_id=1,
                    created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Product(name="Dell XPS 13", qty=30, amount=1499.99, category_id=1,
                    created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Product(name="Apple Watch Series 8", qty=100, amount=399.99, category_id=2,
                    created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Product(name="Sony Playstation 5", qty=50, amount=599.99, category_id=2,
                    created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Product(name="Nintendo Switch", qty=20, amount=1999.99, category_id=2,
                    created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
            Product(name="Xbox Series X", qty=100, amount=249.99, category_id=2,
                    created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        ]
        session.add_all(products)

    await session.commit()

    # Orders
    result = await session.execute(select(Order))
    if result.first() is None:
        orders = [
            Order(customer_id=1, product_id=1, category_id=1, qty=1, amount=999,
                  status="Completed", created_at=datetime.strptime("2025-05-01 12:00:00", "%Y-%m-%d %H:%M:%S"), updated_at=datetime.utcnow()),
            Order(customer_id=2, product_id=2, category_id=1, qty=1, amount=1999,
                  status="Pending", created_at=datetime.strptime("2025-06-02 12:00:00", "%Y-%m-%d %H:%M:%S"), updated_at=datetime.utcnow()),
            Order(customer_id=3, product_id=3, category_id=2, qty=2, amount=499,
                  status="completed", created_at=datetime.strptime("2025-07-01 12:00:00", "%Y-%m-%d %H:%M:%S"), updated_at=datetime.utcnow()),
            Order(customer_id=4, product_id=4, category_id=1, qty=1, amount=899,
                  status="Completed", created_at=datetime.strptime("2025-07-02 12:00:00", "%Y-%m-%d %H:%M:%S"), updated_at=datetime.utcnow()),
            Order(customer_id=5, product_id=5, category_id=1, qty=1, amount=1499,
                  status="Pending", created_at=datetime.strptime("2025-08-01 12:00:00", "%Y-%m-%d %H:%M:%S"), updated_at=datetime.utcnow()),
            Order(customer_id=6, product_id=6, category_id=2, qty=2, amount=399,
                  status="Completed", created_at=datetime.strptime("2025-09-01 12:00:00", "%Y-%m-%d %H:%M:%S"), updated_at=datetime.utcnow()),
            Order(customer_id=7, product_id=7, category_id=2, qty=2, amount=599,
                  status="Pending", created_at=datetime.strptime("2025-09-02 12:00:00", "%Y-%m-%d %H:%M:%S"), updated_at=datetime.utcnow()),
        ]
        session.add_all(orders)

    await session.commit()
