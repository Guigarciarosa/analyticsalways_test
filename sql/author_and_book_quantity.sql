select a.au_id as 'id',
concat(a.au_lname,' ',a.au_fname) as 'name',
count(t.title) as 'book_written'

from authors a
	inner join titleauthor ta on ta.au_id = a.au_id
	left join titles t on t.title_id = ta.title_id
group by a.au_id, a.au_lname,au_fname
