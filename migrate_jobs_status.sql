-- Run in Supabase SQL Editor
alter table jobs add column if not exists status text not null default 'Applied';
