from project import Category
from project import Document
from project import Topic


class Storage:

    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    # DONT REPEAT YOURSELF
    def __edit_object(self, uid, collections, *args):
        obj = self.__get_object(uid, collections)
        if obj:
            obj.edit(*args)

    @staticmethod
    def __get_object(objects, collections: list):
        return next((o for o in collections if o.id == objects))

    def edit_category(self, category_id: int, new_name: str):
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.__edit_object(document_id, self.documents, new_file_name)

    # DONT REPEAT YOURSELF
    def __delete_objects(self, uid, collection: list):
        obj = self.__get_object(uid, collection)
        if obj:
            collection.remove(obj)

    def delete_category(self, category_id):
        self.__delete_objects(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.__delete_objects(topic_id, self.topics)

    def delete_document(self, document_id):
        self.__delete_objects(document_id, self.documents)

    def get_document(self, document_id):
        return self.__get_object(document_id, self.documents)

    def __repr__(self):
        result = '\n'.join([str(d) for d in self.documents])
        return result
