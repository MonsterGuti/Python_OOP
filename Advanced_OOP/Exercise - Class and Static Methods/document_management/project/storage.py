from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def __edit_object(self, object_id, object_collection, *new_values):
        cur_object = self.__find_object(object_id, object_collection)
        if cur_object:
            cur_object.edit(*new_values)

    @staticmethod
    def __find_object(object_id, object_collection):
        cur_object = next((o for o in object_collection if o.id == object_id), None)
        return cur_object

    def edit_category(self, category_id: int, new_name: str):
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.__edit_object(document_id, self.documents, new_file_name)

    def __delete_object(self, object_id, object_collection):
        cur_object = self.__find_object(object_id, object_collection)
        if cur_object:
            object_collection.remove(cur_object)

    def delete_category(self, category_id):
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id):
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id):
        document = self.__find_object(document_id, self.documents)
        return document

    def __repr__(self):
        result = [repr(doc) for doc in self.documents]
        return '\n'.join(result)

   