select a.au_id as 'id',
concat(a.au_lname,' ',a.au_fname) as 'name',
sto.state as 'state',
count(sto.state) as 'qtd_sales_per_state'

from authors a
	inner join titleauthor ta on ta.au_id = a.au_id
	left join titles t on t.title_id = ta.title_id
	left join sales s on s.title_id = t.title_id
	left join stores sto on sto.stor_id = s.stor_id
group by a.au_id, a.au_lname,au_fname, sto.state