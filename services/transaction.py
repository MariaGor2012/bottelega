from datetime import datetime

transactions= {}

def create_transaction(chat_id):
    transactions[chat_id]=get_templete_transaction()

def set_type_transaction(chat_id,type_):
    transactions[chat_id]["type"]=type_
    print(transactions)

def get_templete_transaction(type_=None,category=None,amount=None):

    """
    type - тип транзакции доход|расход
    .strftime("%d.%m.%Y)-> дата в формате день месяц год
    """
    
    return{
        "date": datetime.now().strftime("%d.%m.%Y"),
        "type": type_,
        "category": category,
        "amount":amount
    }

res=datetime.now().strftime("%d.%m.%Y")
print(res,type(res))






