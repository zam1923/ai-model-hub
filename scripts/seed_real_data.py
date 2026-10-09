import os
import yaml
from datetime import datetime

MODELS = [
    {
        "id": "gpt-4o",
        "title": "GPT-4o (Omni)",
        "lab": "OpenAI",
        "releaseDate": "2024-05-13",
        "contextWindow": "128k",
        "license": "Proprietary",
        "description": "テキスト、視覚、音声をリアルタイムで統合処理するOpenAIの画期的なフラッグシップモデル。",
        "modalities": ["Text", "Image", "Audio"],
        "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=800&auto=format&fit=crop",
        "sourceUrl": "https://openai.com/index/hello-gpt-4o/",
        "sourceTitle": "Hello GPT-4o | OpenAI 公式リリース",
        "body": "人工知能の歴史において、「マルチモーダル」という言葉は長くバズワードとして消費されてきた。しかし、OpenAIが発表した『GPT-4o（オムニ）』は、その概念を真の意味で体現した初めてのモデルかもしれない。\n\n従来の音声AIシステムは、音声をテキストに変換し、テキストで推論し、再び音声に変換するという3段階のプロセスを経る必要があった。これにより、対話には避けられない遅延（レイテンシ）が生じ、感情やトーンのニュアンスは途中で欠落してしまっていた。GPT-4oの最大のブレイクスルーは、テキスト、視覚、音声を「単一のニューラルネットワーク」でネイティブに入出力処理する点にある。\n\nこれにより、平均応答速度は人間の会話とほぼ同等の232ミリ秒を達成。ユーザーの呼吸のペースを読み取り、感情的な声色で応答し、さらには会話の途中で人間が割り込んだ場合でも自然に対応を切り替えることができる。\n\n「これはまるで映画の世界のAIだ」とサム・アルトマンCEOが語るように、GPT-4oはコンピューターと人間のインタラクションにおけるパラダイムシフトを提示している。スマートフォンを通じた同時翻訳や、視覚障害者向けのリアルタイムな環境描写アシスタントなど、APIの解放によって世界中の開発者がこの新たな知覚機能をプロダクトに組み込み始めている。もはやAIは「画面の中のテキストジェネレーター」ではなく、我々と同じ世界を見聞きし、反応する同僚へと進化を遂げたのだ。"
    },
    {
        "id": "llama-3-1-405b",
        "title": "Llama 3.1 405B",
        "lab": "Meta",
        "releaseDate": "2024-07-23",
        "contextWindow": "128k",
        "license": "Llama 3.1 Community License",
        "description": "オープンソースAIの頂点。クローズドな最先端モデルと同等以上の推論能力を持つ超巨大モデル。",
        "modalities": ["Text"],
        "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=800&auto=format&fit=crop",
        "sourceUrl": "https://ai.meta.com/blog/meta-llama-3-1/",
        "sourceTitle": "Llama 3.1 405Bのリリース | Meta AI Blog",
        "body": "シリコンバレーで長らく議論されてきた「オープン vs クローズド」のAI開発競争において、Metaは決定的な一手を打った。4050億パラメータという途方もない規模を持つ『Llama 3.1 405B』のオープンソース化である。\n\nこのモデルは、1万6000個ものH100 GPUを用いて学習され、数学、プログラミング、多言語推論など、ほぼすべての主要ベンチマークにおいてGPT-4oやClaude 3.5 Sonnetといったクローズドなトップモデルと互角、あるいはそれ以上の成績を記録している。マーク・ザッカーバーグCEOは「AIの力は少数の巨大企業によって独占されるべきではない」と明言し、このモデルのウェイト（重みデータ）を世界中の開発者に向けて無償で公開した。\n\nこれにより、何が起きるのか。最も重要なのは「合成データ（Synthetic Data）」の生成と、小規模モデルへの「蒸留（Distillation）」が可能になったことだ。企業や研究機関は、高価なAPI利用料を支払い続けることなく、Llama 3.1 405Bという「教師」を用いて、自社専用の高性能かつ軽量なローカルAIモデルを構築できるようになった。これは単なる一企業のプロダクト発表ではなく、世界のソフトウェアインフラストラクチャに対する巨大なオープンソースの贈り物であり、AIエコシステム全体の進化を数年分加速させる起爆剤となるだろう。"
    },
    {
        "id": "claude-3-5-sonnet",
        "title": "Claude 3.5 Sonnet",
        "lab": "Anthropic",
        "releaseDate": "2024-06-20",
        "contextWindow": "200k",
        "license": "Proprietary",
        "description": "圧倒的なコーディング能力と推論速度を両立し、実務においてGPT-4を凌駕すると評されるAnthropicの最高傑作。",
        "modalities": ["Text", "Image"],
        "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=800&auto=format&fit=crop",
        "sourceUrl": "https://www.anthropic.com/news/claude-3-5-sonnet",
        "sourceTitle": "Claude 3.5 Sonnetの発表 | Anthropic",
        "body": "AI業界の進化スピードは残酷だ。前世代のフラッグシップモデルが数ヶ月で陳腐化するこの世界において、Anthropicがリリースした『Claude 3.5 Sonnet』は、中量級モデル（Sonnet）でありながら、彼ら自身の重量級モデル（Opus）や競合他社の最高峰モデルを圧倒する性能を見せつけた。\n\nこのモデルが最も高く評価されているのは、その「ソフトウェア・エンジニアリング能力」だ。複雑なコードのリファクタリング、バグの発見と修正、そして難解なドキュメントからの要件定義において、Claude 3.5 Sonnetは人間のシニアエンジニアのように振る舞う。ユーザーの指示を正確に汲み取る能力（インストラクション・フォローイング）が極めて高く、「もうコーディングアシスタントはこれ以外考えられない」と公言する開発者が続出している。\n\nさらにAnthropicは、新しいUI機能「Artifacts（アーティファクト）」を同時に導入した。これは、AIが生成したコードやドキュメント、ベクターグラフィックスを対話画面の横に専用ウィンドウとして独立させ、リアルタイムに編集・プレビューできる機能だ。AIはもはや単なる「チャットボット」ではなく、人間と共同作業を行うための「ワークスペース」へと進化したのである。安全性（アライメント）に厳しいことで知られるAnthropicが、性能と実用性の面でも世界の頂点に立った瞬間だった。"
    }
]

def save_data(dir_name, items):
    os.makedirs(f"src/content/{dir_name}", exist_ok=True)
    for item in items:
        body = item.pop("body")
        filepath = f"src/content/{dir_name}/{item['id']}.md"

        # Parse dates to objects so pyyaml formats them unquoted
        if "releaseDate" in item and isinstance(item["releaseDate"], str):
            try:
                item["releaseDate"] = datetime.strptime(item["releaseDate"], "%Y-%m-%d").date()
            except Exception:
                pass

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("---\n")
            yaml.dump(item, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
            f.write("---\n\n")
            f.write(body + "\n")
        print(f"Created {filepath}")

def main():
    save_data("models", MODELS)

if __name__ == "__main__":
    main()
