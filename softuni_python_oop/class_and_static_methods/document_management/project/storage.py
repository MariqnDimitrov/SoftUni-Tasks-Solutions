from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = next(category for category in self.categories if category_id == category.id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = next(topic for topic in self.topics if topic_id == topic.id)
        topic.storage_folder = new_storage_folder
        topic.topic = new_topic

    def edit_document(self, document_id: int, new_file_name: str):
        document = next(document for document in self.documents if document_id == document.id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = next(category for category in self.categories if category_id == category.id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = next(topic for topic in self.topics if topic_id == topic.id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = next(document for document in self.documents if document_id == document.id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = next(document for document in self.documents if document_id == document.id)
        return document

    def __repr__(self):
        return "\n".join([repr(document) for document in self.documents])








