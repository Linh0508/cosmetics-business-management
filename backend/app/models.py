"""Backward-compatible model exports for the database schema.

The database schema now lives under the repository-level database package.
"""

from database.models import *

__all__ = [
    "Role",
    "User",
    "Category",
    "Brand",
    "Product",
    "Customer",
    "Order",
    "OrderItem",
    "Payment",
    "Inventory",
    "Promotion",
    "ProductReview",
]
