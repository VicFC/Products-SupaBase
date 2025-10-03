-- DDL =======================================================================================================


-- EXTRA 1: Funciones =======================================================================================================

-- EXTRA 2: Vistas =======================================================================================================
-- 1. Todas las sales
create or replace view public.v_sales_fact as
select 
    il.id as invoice_line_id,
    i.id as invoice_id,
    i.invoice_date,
    i.total_amount,
    c.id as customer_id,
    c.name as customer_name,
    c.country_code,
    co.name as country_name,
    p.id as product_id,
    p.name as product_name,
    cat.id as category_id,
    cat.name as category_name,
    il.quantity,
    il.unit_price,
    il.line_total
from invoice_lines il
join invoices i on il.invoice_id = i.id
join customers c on i.customer_id = c.id
join countries co on c.country_code = co.code
join products p on il.product_id = p.id
join categories cat on p.category_id = cat.id;

-- 2. Por categoria
create or replace view public.v_sales_by_category as
select 
    cat.id as category_id,
    cat.name as category_name,
    sum(il.line_total) as total_sales,
    count(distinct i.id) as total_invoices,
    sum(il.quantity) as total_units
from invoice_lines il
join invoices i on il.invoice_id = i.id
join products p on il.product_id = p.id
join categories cat on p.category_id = cat.id
group by cat.id, cat.name
order by total_sales desc;

-- 3. Por country
create or replace view public.v_sales_by_country as
select 
    co.code as country_code,
    co.name as country_name,
    sum(il.line_total) as total_sales,
    count(distinct i.id) as total_invoices,
    count(distinct c.id) as total_customers
from invoice_lines il
join invoices i on il.invoice_id = i.id
join customers c on i.customer_id = c.id
join countries co on c.country_code = co.code
group by co.code, co.name
order by total_sales desc;

-- Top 5 en los ultimos 30 dias
create or replace view public.v_top_products_30d as
select 
    p.id as product_id,
    p.name as product_name,
    cat.name as category_name,
    sum(il.quantity) as total_units_sold,
    sum(il.line_total) as total_sales
from invoice_lines il
join invoices i on il.invoice_id = i.id
join products p on il.product_id = p.id
join categories cat on p.category_id = cat.id
where i.invoice_date >= (current_date - interval '30 days')
group by p.id, p.name, cat.name
order by total_sales desc limit 5;
