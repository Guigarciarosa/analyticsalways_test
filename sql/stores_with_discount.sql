select st.stor_id,
st.stor_name 'store_name',
count(s.discount) 'has_discount'

from stores st
	left join discounts s on s.stor_id = st.stor_id
group by st.stor_id,st.stor_name