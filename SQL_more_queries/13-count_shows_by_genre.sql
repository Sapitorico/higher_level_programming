-- script that lists all genres displays the number of shows linked to each
SELECT genres.name AS genre, COUNT(id) AS number_of_shows FROM tv_genres INNER JOIN tv_show_genres ON genres_id = id
GROUP BY genres.name ORDER BY number_of_shows DESC;