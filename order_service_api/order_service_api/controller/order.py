from order_service_api.utilities.util import get_table, get_logger

logger = get_logger()


def save_order(item):
    try:
        logger.info("inside save_order")
        table = get_table()
        table.put_item(Item=item)
        logger.info("item saved successfully")
        logger.info(item)
        return "Order details saved successfully"
    except Exception as err:
        logger.error(f"unable to save order {err}")
        return "Unable to save order"


def get_order_details_by_user_util(user_id):
    logger.info("inside get_order_details_by_user_util")
    table = get_table()
    logger.info(f"current table used {table}")

    response = table.scan(
        FilterExpression='begins_with(UserID_OrderID, :user_id)',
        ExpressionAttributeValues={':user_id': user_id},
    )

    items = response.get('Items', {})

    sorted_items = sorted(items, key=lambda x: x.get('OrderDate'))

    logger.info(f"item to be returned {sorted_items}")

    return sorted_items
