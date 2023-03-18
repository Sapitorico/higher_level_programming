-- script that lists all genres displays the number of shows linked to each
SELECT tv_genres.genre AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.genre
HAVING COUNT(tv_show_genres.genre_id) > 0
ORDER BY number_of_shows DESC;