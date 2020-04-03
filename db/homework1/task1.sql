UPDATE users set created_at = NOW(), updated_at = NOW()
where created_at is null or created_at = "";
