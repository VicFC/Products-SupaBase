# Supabase REST — Ejemplos de cURL


## Credenciales para usuario de pruebas
```bash
curl -X POST 'https://yijapvjwuhfihszjjomf.supabase.co/auth/v1/token?grant_type=password' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o"
-H "Content-Type: application/json" 
-d '{
  "email": "usuarioCR@example.com",
  "password": "cr1234"
}'
```

---

## Productos

### Seleccionar productos
```bash
curl 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/products?select=*' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o"
-H "Authorization: Bearer SUPABASE_KEY" 
```

### Insertar un producto
```bash
curl -X POST 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/products' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o"
-H "Authorization: Bearer SUPABASE_KEY" 
-H "Content-Type: application/json" 
-H "Prefer: return=minimal" 
-d '{ "some_column": "someValue", "other_column": "otherValue" }'
```

### Actualizar un producto
```bash
curl -X PATCH 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/products?some_column=eq.someValue' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o"
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY" 
-H "Content-Type: application/json" 
-H "Prefer: return=minimal" 
-d '{ "other_column": "otherValue" }'
```

### Eliminar un producto
```bash
curl -X DELETE 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/products?some_column=eq.someValue' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o"
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY"
```

---

## Customers

### Seleccionar customers
```bash
curl 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/customers?select=*' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY"
```

### Insertar customer
```bash
curl -X POST 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/customers' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY" 
-H "Content-Type: application/json" 
-H "Prefer: return=minimal" 
-d '{ "some_column": "someValue", "other_column": "otherValue" }'
```

### Actualizar customer
```bash
curl -X PATCH 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/customers?some_column=eq.someValue' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY" 
-H "Content-Type: application/json" 
-H "Prefer: return=minimal" 
-d '{ "other_column": "otherValue" }'
```

### Eliminar customer
```bash
curl -X DELETE 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/customers?some_column=eq.someValue' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY"
```

---

## Invoices

### Seleccionar invoices
```bash
curl 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/invoices?select=*' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY"
```

### Insertar invoice
```bash
curl -X POST 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/invoices' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY" 
-H "Content-Type: application/json" 
-H "Prefer: return=minimal" 
-d '{ "some_column": "someValue", "other_column": "otherValue" }'
```

### Actualizar invoice
```bash
curl -X PATCH 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/invoices?some_column=eq.someValue' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY" 
-H "Content-Type: application/json" 
-H "Prefer: return=minimal" 
-d '{ "other_column": "otherValue" }'
```

### Eliminar invoice
```bash
curl -X DELETE 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/invoices?some_column=eq.someValue' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY"
```

---

## Invoice Lines

### Seleccionar invoice_lines
```bash
curl 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/invoice_lines?select=*' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY"
```

### Insertar invoice_lines
```bash
curl -X POST 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/invoice_lines' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY"
-H "Content-Type: application/json" 
-H "Prefer: return=minimal" 
-d '{ "some_column": "someValue", "other_column": "otherValue" }'
```

### Actualizar invoice_lines
```bash
curl -X PATCH 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/invoice_lines?some_column=eq.someValue' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY" 
-H "Content-Type: application/json" 
-H "Prefer: return=minimal" 
-d '{ "other_column": "otherValue" }'
```

### Eliminar invoice_lines
```bash
curl -X DELETE 'https://yijapvjwuhfihszjjomf.supabase.co/rest/v1/invoice_lines?some_column=eq.someValue' 
-H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlpamFwdmp3dWhmaWhzempqb21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MzcwNTUsImV4cCI6MjA3NTAxMzA1NX0.ynbGR2aZYiHYa3oI2vMou_UwJ5jO_sLTr3x-AyGgQ6o" 
-H "Authorization: Bearer SUPABASE_CLIENT_ANON_KEY"
```
