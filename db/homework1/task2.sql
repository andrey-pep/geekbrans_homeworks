update users set created_at = convert(datetime, created_at, 104), updated_at = convert(datetime, updated_at, 104);
