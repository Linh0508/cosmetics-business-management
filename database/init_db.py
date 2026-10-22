from .database import Base, engine
from .models import (
    Brand,
    Category,
    Customer,
    Inventory,
    Order,
    OrderItem,
    Payment,
    Product,
    ProductReview,
    Promotion,
    Role,
    User,
)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    init_db()
