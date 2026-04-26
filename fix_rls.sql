-- Option A: Disable RLS entirely (simplest for single-user MVP)
alter table users         disable row level security;
alter table jobs          disable row level security;
alter table cover_letters disable row level security;


-- Option B: Keep RLS on but allow all operations (safer habit for later)
-- Run these instead of Option A if you prefer:

-- create policy "allow all" on users         for all using (true) with check (true);
-- create policy "allow all" on jobs          for all using (true) with check (true);
-- create policy "allow all" on cover_letters for all using (true) with check (true);
