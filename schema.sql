-- Run this in your Supabase SQL editor

create table users (
  id text primary key default 'default',
  name text,
  email text,
  base_resume_text text not null
);

create table jobs (
  id uuid primary key default gen_random_uuid(),
  title text,
  company text,
  description text,
  url text,
  created_at timestamptz default now()
);

create table cover_letters (
  id uuid primary key default gen_random_uuid(),
  user_id text references users(id),
  job_id uuid references jobs(id),
  content text not null,
  created_at timestamptz default now()
);

-- Insert your resume so the backend can fetch it
insert into users (id, name, email, base_resume_text)
values (
  'default',
  'Your Name',
  'you@example.com',
  'Paste your full resume text here...'
);
