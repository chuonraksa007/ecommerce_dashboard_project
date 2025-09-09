from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.base.untility import app_success, app_server_error


async def index_ecom(db: AsyncSession):
    try:
        # Helper function to run queries
        async def fetch_scalar(query: str):
            result = await db.execute(text(query))
            return result.scalar() or 0

        async def fetch_all(query: str):
            result = await db.execute(text(query))
            return result.fetchall()

        # Metrics Queries
        total_revenue = await fetch_scalar("SELECT COALESCE(SUM(amount), 0) FROM ecom_order")
        total_orders = await fetch_scalar("SELECT COUNT(*) FROM ecom_order")
        total_customers = await fetch_scalar("SELECT COUNT(DISTINCT customer_id) FROM ecom_order")
        total_products_sold = await fetch_scalar("SELECT COALESCE(SUM(qty), 0) FROM ecom_order")

        metrics = [
            {"title": "Total Revenue", "value": f"${total_revenue:,.0f}", "change": "+12.5%", "isPositive": True, "icon": "DollarSign", "changeLabel": "Increase Vs Last Month"},
            {"title": "Orders", "value": f"{total_orders:,}", "change": "+8.3%", "isPositive": True, "icon": "ShoppingBag", "changeLabel": "Increase Vs Last Month"},
            {"title": "Customers", "value": f"{total_customers:,}", "change": "+15.2%", "isPositive": True, "icon": "Users", "changeLabel": "Increase Vs Last Month"},
            {"title": "Products Sold", "value": f"{total_products_sold:,}", "change": "-2.1%", "isPositive": False, "icon": "Package", "changeLabel": "Descrease Vs Last Month"}
        ]

        # Sales Overview
        sales_query = """
            SELECT TO_CHAR(created_at, 'Mon') AS month, SUM(amount) AS sales
            FROM ecom_order
            GROUP BY month, EXTRACT(MONTH FROM created_at)
            ORDER BY EXTRACT(MONTH FROM created_at)
        """
        sales_rows = await fetch_all(sales_query)
        sale_overview = [
            {"month": row[0], "sales": int(row[1]) if row[1] else 0}
            for row in sales_rows
        ]

        # Top Selling Products
        top_products_query = """
            SELECT p.id, p.name, p.category_id,
                   SUM(o.amount) AS sales, SUM(o.qty) AS units
            FROM ecom_order o
            INNER JOIN ecom_product p ON o.product_id = p.id
            GROUP BY p.id, p.name, p.category_id
            ORDER BY sales DESC
            LIMIT 5
        """
        product_rows = await fetch_all(top_products_query)
        emojis = ["💻", "📱", "📦", "🎨", "👨‍💻"]
        top_products = [
            {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "sales": f"${row[3]:,.0f}",
                "units": f"{row[4]} sold",
                "trend": "+0%",
                "image": emojis[i % len(emojis)],
            }
            for i, row in enumerate(product_rows)
        ]

        # Recent Orders
        recent_order_query = """
            SELECT o.id, c.name, p.name, o.amount, o.status, o.created_at
            FROM ecom_order o
            INNER JOIN ecom_customer c ON o.customer_id = c.id
            INNER JOIN ecom_product p ON o.product_id = p.id
            ORDER BY o.created_at DESC
        """
        order_rows = await fetch_all(recent_order_query)
        recent_order = [
            {
                "id": row[0],
                "customer_name": row[1],
                "product_name": row[2],
                "amount": f"${row[3]:,.0f}",
                "status": row[4],
                "date_time": row[5],
            }
            for row in order_rows
        ]

        return app_success(data={
            "metrics_card": metrics,
            "top_products": top_products,
            "sale_overview": sale_overview,
            "recent_order": recent_order,
        })

    except Exception as e:
        return app_server_error(msg=str(e))
