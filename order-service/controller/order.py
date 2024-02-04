import logging
from utilities.util import get_table

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_order(item):
    try:
        table = get_table()
        table.put_item(Item=item)
        return "Order details saved successfully"
    except Exception as err:
        return "Unable to save order"


def get_order_details_by_user_util(user_id):
    table = get_table()

    response = table.scan(
        FilterExpression='begins_with(UserID_OrderID, :user_id)',
        ExpressionAttributeValues={':user_id': user_id},
    )

    items = response.get('Items', {})

    sorted_items = sorted(items, key=lambda x: x.get('OrderDate'))

    return sorted_items
