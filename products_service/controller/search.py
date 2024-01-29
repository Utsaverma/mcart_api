from products_service.open_search.util import get_document_util


def search_by_title(title, start_index=0, size=20, filters=None):
    if title:
        documents_util = get_document_util()
        items = documents_util.get_documents_by_title(title, size, start_index, filters)
        return items


def search_by_id(id):
    if id:
        documents_util = get_document_util()
        return documents_util.get_document_by_id(id)


def get_all_categories_util():
    documents_util = get_document_util()
    return documents_util.get_all_categories()


def search_by_category(category, size=20, start_index=0):
    documents_util = get_document_util()
    return documents_util.get_documents_by_category(category, size, start_index)