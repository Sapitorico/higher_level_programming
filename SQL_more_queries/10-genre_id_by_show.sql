-- import a databse and list all show conteinded in the have at leaest  genere linked
mysql -u root -p hbtn_0d_tvshows < hbtn_0d_tvshows.sql;
SELECT DISTINCT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id;