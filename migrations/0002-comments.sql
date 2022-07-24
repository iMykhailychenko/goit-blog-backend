CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    content VARCHAR(1000) NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp with time zone,
    post_id integer NOT NULL REFERENCES posts(id) ON DELETE CASCADE REFERENCES posts(id) DEFERRABLE INITIALLY DEFERRED
);