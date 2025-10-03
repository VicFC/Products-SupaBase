import os
from supabase import create_client, Client

URL = os.getenv("SUPABASE_URL", "https://yijapvjwuhfihszjjomf.supabase.co")
KEY = os.getenv("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o")
EMAIL = os.getenv("USER_EMAIL", "usuarioCR@example.com")
PWD = os.getenv("USER_PASSWORD", "cr1234")

def login() -> Client:
    sb: Client = create_client(URL, KEY)
    auth = sb.auth.sign_in_with_password({"email": EMAIL, "password": PWD})
    
    if not auth.session:
        raise SystemExit("Login failed.")
    
    print("Logged in:", auth.user.email)
    return sb


def list_my_products(sb: Client):
    res = sb.table("products").select("*").execute()
    print("Products (RLS applied):", res.data)


def list_my_customers(sb: Client):
    res = sb.table("customers").select("*").execute()
    print("Customers (RLS applied):", res.data)


def create_invoice(sb: Client, customer_id: int):
    inv = sb.table("invoices").insert({"customer_id": customer_id}).select("*").execute()
    print("Invoice:", inv.data)
    return inv.data[0]["id"]


def add_line(sb: Client, invoice_id: int, product_id: int, qty: float, unit_price: float):
    line_total = round(qty * unit_price, 2)
    line = {
        "invoice_id": invoice_id,
        "product_id": product_id,
        "quantity": qty,
        "unit_price": unit_price,
        "line_total": line_total
    }
    res = sb.table("invoice_lines").insert(line).select("*").execute()
    print("Line:", res.data)


def show_invoice_with_lines(sb: Client, invoice_id: int):
    inv = sb.table("invoices").select("*").eq("id", invoice_id).execute()
    lines = sb.table("invoice_lines").select("*").eq("invoice_id", invoice_id).execute()
    print("Invoice:", inv.data)
    print("Lines:", lines.data)


if __name__ == "__main__":
    
    sb = login()

    while True:
        print("\n--- MENU ---")
        print("1. List my products")
        print("2. List my customers")
        print("3. Create invoice")
        print("4. Add line to invoice")
        print("5. Show invoice with lines")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_my_products(sb)
        elif choice == "2":
            list_my_customers(sb)
        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            invoice_id = create_invoice(sb, customer_id)
        elif choice == "4":
            invoice_id = int(input("Enter invoice ID: "))
            product_id = int(input("Enter product ID: "))
            qty_str = input("Enter quantity (default 1): ")
            qty = float(qty_str) if qty_str else 1
            price_str = input("Enter unit price (or leave blank to use product price): ")
            unit_price = float(price_str) if price_str else None
            add_line(sb, invoice_id, product_id, qty, unit_price)
        elif choice == "5":
            invoice_id = int(input("Enter invoice ID: "))
            show_invoice_with_lines(sb, invoice_id)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")