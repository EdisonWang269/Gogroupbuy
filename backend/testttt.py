from app.database import execute_query
from app.sendmess import send_message

query = """
            SELECT userid
            FROM `Order`
            WHERE group_buying_id = %s 
            AND receive_status = FALSE;
        """
userids = execute_query(query, (1,), True)

message = '您訂購的商品已送達，請盡快取貨。'

useridtype = ""
for userid in userids:
    send_message(userid, message)

print(type(userids))
