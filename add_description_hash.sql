-- No migration needed — job lookup uses the existing `url` column only.
-- Optionally add an index if not already present:
CREATE INDEX IF NOT EXISTS idx_jobs_url ON jobs (url);
