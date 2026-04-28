-- Run this in your Supabase SQL editor
CREATE TABLE profile (
  id text PRIMARY KEY DEFAULT 'default',
  first_name text,
  last_name text,
  email text,
  phone text,
  street text,
  city text,
  state text,
  country text,
  zip text,
  race text,
  veteran text,
  disability text,
  desired_salary text
);
