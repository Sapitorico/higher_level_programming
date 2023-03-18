-- SELECT tv_shows.title, tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = show_id ORDER BY title, genre_id;