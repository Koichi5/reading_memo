from firebase_functions import https_fn
import sumy
import tinysegmenter
import Janome

def summaryWithSumy(req: https_fn.Request) -> https_fn.Response:
    text = req.args.get("text")
    if not text:
        return https_fn.Response("No text provided", status=400)

    # テキストを単語に分割する
    seg = tinysegmenter.TinySegmenter()
    words = seg.segment(text)

    # 分かち書きされたテキストを生成
    sentence = ""
    for word in words:
        sentence += word + " "

    # 要約を生成
    summarizer = sumy.summarizer.Summarization()
    summary = summarizer(sentence, ratio=0.5)

    return https_fn.Response(summary)

