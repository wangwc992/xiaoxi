from sentence_transformers import SentenceTransformer


class BgeLargeZhV15():
    model_path = "D:\\LLM\\BAAI\\bge-large-zh-v1.5"
    # model_name = "BAAI/bge-large-zh-v1.5"
    model = SentenceTransformer(model_path)

    def __init__(self):
        pass

    def embed_documents(self, documents):
        doc_vecs = [
            self.model.encode(doc, normalize_embeddings=True)
            for doc in documents
        ]
        return doc_vecs

    def embed_query(self, sentence):
        return self.model.encode(sentence, normalize_embeddings=True).tolist()


if __name__ == "__main__":
    e = BgeLargeZhV15()
    print(e.embed_query("澳国立申请费多少钱"))
