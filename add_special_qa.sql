-- Run this in your Supabase SQL editor
CREATE TABLE special_qa (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  job_id uuid REFERENCES jobs(id),
  prompt text NOT NULL,
  answer text NOT NULL,
  created_at timestamptz DEFAULT now()
);
