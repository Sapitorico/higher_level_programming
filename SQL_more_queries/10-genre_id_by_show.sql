-- import a databse and list all show conteinded in the have at leaest  genere linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;