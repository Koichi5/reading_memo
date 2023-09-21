# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

# from firebase_functions import firestore_fn, https_fn
# from firebase_admin import initialize_app, firestore
# import google.cloud.firestore
# import MeCab
# from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
# from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
# from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
# from pysummarization.nlp_base import NlpBase
# from pysummarization.similarityfilter.tfidf_cosine import TfIdfCosine

from firebase_functions import https_fn
# from pysummarization import AutoAbstractor
# from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
# from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
# from pysummarization.nlp_base import NlpBase
# from pysummarization.similarityfilter.tfidf_cosine import TfIdfCosine

@https_fn.on_request()
def sayHello(req: https_fn.Request) -> https_fn.Response:
    document = req.args.get("text")
    if not document:
        return https_fn.Response("No text provided", status=400)
    return https_fn.Response(f"Hello {document} !")

# @https_fn.on_request()
# def pysummarizationTest(req: https_fn.Request) -> https_fn.Response:
#     document = req.args.get("text")
#     if not document:
#         return https_fn.Response("No text provided", status=400)

#     nlp_base = NlpBase()
#     nlp_base.tokenizable_doc = MeCabTokenizer()
#     similarity_filter = TfIdfCosine()
#     similarity_filter.nlp_base = nlp_base
#     similarity_filter.similarity_limit = 0.25
#     auto_abstractor = AutoAbstractor()
#     auto_abstractor.tokenizable_doc = MeCabTokenizer()
#     abstractable_doc = TopNRankAbstractor()
#     result_dict = auto_abstractor.summarize(document, abstractable_doc, similarity_filter, top_n=5)

#     summarized_text = "\n".join(result_dict["summarize_result"])
#     return https_fn.Response(summarized_text)

# @https_fn.on_request()
# def changeToMemoWithPysummarization(req: https_fn.Request) -> https_fn.Response:
#     text = req.args.get("text")
#     if text is None:
#         return https_fn.Response("No text parameter provided", status=400)
    
#     firestore_client = google.cloud.firestore.Client = firestore.client()
#     # NLPのオブジェクト
#     nlp_base = NlpBase()
    
#     # トークナイザーを設定します。 これは、MeCabを使用した日本語のトークナイザーです
#     nlp_base.tokenizable_doc = MeCabTokenizer()
    
#     similarity_filter = TfIdfCosine()
    
#     # NLPのオブジェクトを設定します
#     similarity_filter.nlp_base = nlp_base
    
#     # 類似性がこの値を超えると、文は切り捨てられます
#     similarity_filter.similarity_limit = 0.25
    
#     # 自動要約のオブジェクト
#     auto_abstractor = AutoAbstractor()
    
#     # トークナイザーを設定します。 これは、MeCabを使用した日本語のトークナイザーです
#     auto_abstractor.tokenizable_doc = MeCabTokenizer()
    
#     # ドキュメントを抽象化およびフィルタリングするオブジェクト
#     abstractable_doc = TopNRankAbstractor()
    
#     # オブジェクトを委任し、要約を実行します
#     # similarity_filter機能追加
#     result_dict = auto_abstractor.summarize(text, abstractable_doc, similarity_filter)
    
#     # 出力
#     for sentence in result_dict["summarize_result"]:
#         print(sentence)
    
#     _, doc_ref = firestore_client.collection("formatted_text").add({
#         "text" : sentence
#     })

#     return https_fn.Response(f"Memo with ID {doc_ref.id} added.")

# @https_fn.on_request()
# def changeToMemoWithSudachi(req: https_fn.Request) -> https_fn.Response:
#     text = req.args.get("text")
#     if text is None:
#         return https_fn.Response("No text parameter provided", status=400)
#     firestore_client = google.cloud.firestore.Client = firestore.client()
#     tokenizer_obj = Dictionary().create()
#     mode = tokenizer.Tokenizer.SplitMode.C  # モードCを指定
    
#     words = [m.surface() for m in tokenizer_obj.tokenize(text, mode)]
    
#     formatted_text = []
#     append_bullet = True  # 「・」を追加するかどうかのフラグ
#     for word in words:
#         # 「・」を追加する条件
#         if append_bullet and word not in ["って", "、", "。", "んだ"]:
#             formatted_text.append("・")
#             append_bullet = False
            
#         # 「って」や「んだ」を除外する
#         if word in ["って", "んだ"]:
#             continue
        
#         formatted_text.append(word)
        
#         # 「って」や「は」や「が」の後、または句読点「、。」の前に改行を入れる
#         if word in ["は", "が", "、", "。"]:
#             formatted_text.append("\n")
#             append_bullet = True
    
#     print("".join(formatted_text))
#     joined_text = "".join(formatted_text)

#     _, doc_ref = firestore_client.collection("formatted_text").add({
#         "text" : joined_text
#     })

#     return https_fn.Response(f"Memo with ID {doc_ref.id} added.")

# @https_fn.on_request()
# def changeToMemo(req: https_fn.Request) -> https_fn.Response:
#     original = req.args.get("text")
#     if original is None:
#         return https_fn.Response("No text parameter provided", status=400)
    
#     firestore_client = google.cloud.firestore.Client = firestore.client()

#     tagger = MeCab.Tagger()
#     node = tagger.parseToNode(original)
#     while node:
#         surface = node.surface
#         pos = node.feature[0]
#         feature = node.feature
#         print(f"{surface} ({pos}, {feature})")

#     _, doc_ref = firestore_client.collection("memo_texts").add({
#         "surface" : surface,
#         "pos" : pos,
#         "feature" : feature,
#         "original" : original
#     })
    
#     return https_fn.Response(f"Memo with ID {doc_ref.id} added.")

# @https_fn.on_request()
# def addMessage(req: https_fn.Request) -> https_fn.Response:
#     original = req.args.get("text")
#     if original is None:
#         return https_fn.Response("No text parameter provided", status=400)
    
#     firestore_client = google.cloud.firestore.Client = firestore.client()

#     _, doc_ref = firestore_client.collection("messages").add(
#         {"original" : original}
#     )

#     return https_fn.Response(f"Message with ID {doc_ref.id} added.")

# @firestore_fn.on_document_created(document="messages/{pushId}")
# def makeuppercase(
#     event: firestore_fn.Event[firestore_fn.DocumentSnapshot | None],
# ) -> None:
#     """Listens for new documents to be added to /messages. If the document has
#     an "original" field, creates an "uppercase" field containg the contents of
#     "original" in upper case."""

#     # Get the value of "original" if it exists.
#     if event.data is None:
#         return
#     try:
#         original = event.data.get("original")
#     except KeyError:
#         # No "original" field, so do nothing.
#         return

#     # Set the "uppercase" field.
#     print(f"Uppercasing {event.params['pushId']}: {original}")
#     upper = original.upper()
#     event.data.reference.update({"uppercase": upper})

