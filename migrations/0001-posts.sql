CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(250) NOT NULL,
    content VARCHAR(1000) NOT NULL,
    image VARCHAR(250),
    preview_image VARCHAR(250),
    views INT DEFAULT 0 NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp with time zone
);