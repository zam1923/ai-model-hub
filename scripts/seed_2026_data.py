import os
import yaml
from datetime import datetime

MODELS = [
    {
        "id": "gpt-5",
        "title": "GPT-5 (Orion)",
        "lab": "OpenAI",
        "releaseDate": "2026-03-14",
        "contextWindow": "10M",
        "license": "Proprietary",
        "description": "OpenAIが放つ次世代の超巨大モデル。人間レベルの論理的推論と自律エージェント能力を標準搭載し、業界に衝撃を与えた。",
        "modalities": ["Text", "Image", "Audio", "Video", "3D"],
        "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=800&auto=format&fit=crop",
        "body": "オープンAIが長らく沈黙を破りリリースした「GPT-5（コードネーム：Orion）」は、単なるパラメータ数の暴力ではない。特筆すべきは、その『思考の深さ』だ。\n\n従来のモデルが反射的に回答を生成していたのに対し、GPT-5は内蔵されたSystem 2推論モジュールにより、複雑な数学的証明や数万行に及ぶコードベースのリファクタリングを、内部で数分かけて「思考」してから出力する。\n\n発表会見でCEOのサム・アルトマンは「これは情報の検索エンジンから、推論エンジンへの完全な移行を意味する」と語気を強めた。コンテキスト長は驚異の1000万トークンに達し、長編映画数本分の映像を一度に読み込ませて文脈を理解させることも可能だ。我々はついに、自律的にタスクを遂行する真のAIエージェントの時代に突入したと言えるだろう。"
    },
    {
        "id": "claude-4-opus",
        "title": "Claude 4 Opus",
        "lab": "Anthropic",
        "releaseDate": "2026-05-22",
        "contextWindow": "5M",
        "license": "Proprietary",
        "description": "安全性を極限まで高めつつ、最高峰のコーディング能力と分析力を持つAnthropicの最新フラッグシップモデル。",
        "modalities": ["Text", "Image"],
        "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=800&auto=format&fit=crop",
        "body": "「AIの安全性は性能の足枷ではない。むしろ、信頼という最大の武器になる」——Anthropicのダリオ・アモデイCEOの言葉を体現したのが、この『Claude 4 Opus』だ。\n\n本モデルは、これまでのConstitutional AI（憲法ベースのAI）の概念をさらに進化させ、モデル自身が推論過程で倫理的ジレンマを自己解決するメカニズムを搭載している。特に金融や医療といった、一回のミスが致命傷になるエンタープライズ領域において、圧倒的なシェアを獲得しつつある。\n\nプログラミング能力においても、競技プログラミングのトップランカーに匹敵するスコアを叩き出しており、複雑なシステムアーキテクチャの設計図から、セキュアなバックエンドコードを一瞬で生成する能力は圧巻の一言だ。"
    },
    {
        "id": "gemini-2-ultra",
        "title": "Gemini 2.0 Ultra",
        "lab": "Google DeepMind",
        "releaseDate": "2026-08-10",
        "contextWindow": "Infinite (Streaming)",
        "license": "Proprietary",
        "description": "Googleのエコシステムと完全に統合されたマルチモーダルの王者。リアルタイムストリーミング処理に特化。",
        "modalities": ["Text", "Image", "Audio", "Video", "Robotics"],
        "image": "https://images.unsplash.com/photo-1680868543815-b8666dba60f7?q=80&w=800&auto=format&fit=crop",
        "body": "検索の巨人Googleが、DeepMindの知力を結集して放った逆襲の切り札、それが『Gemini 2.0 Ultra』である。\n\n最大のブレイクスルーは「コンテキストの無限化」だ。従来のトークン制限の概念を取り払い、リアルタイムにストリーミングされる動画や音声データを永続的に記憶・参照しながら対話するアーキテクチャを実現した。これにより、スマートグラスを通じてユーザーの日常を常に横でアシストする、究極のパーソナルAIが現実のものとなった。\n\nまた、Robotics（ロボット工学）モダリティが標準で組み込まれており、本モデルを搭載した汎用ロボットが、視覚情報から物理法則を瞬時に推論し、未知の環境で自律的に動作するデモンストレーションは、世界中のロボット工学者の度肝を抜いた。"
    },
    {
        "id": "llama-4-400b",
        "title": "Llama 4 (400B)",
        "lab": "Meta FAIR",
        "releaseDate": "2026-07-15",
        "contextWindow": "1M",
        "license": "Open Weights",
        "description": "オープンソースの常識を覆す性能。クローズドなフラッグシップモデルと完全に互角に渡り合う巨獣。",
        "modalities": ["Text", "Image", "Audio"],
        "image": "https://images.unsplash.com/photo-1655635643532-fa9ba2648cbe?q=80&w=800&auto=format&fit=crop",
        "body": "マーク・ザッカーバーグのオープンソース戦略は、この『Llama 4』においてついに一つの頂点に達した。\n\n4000億パラメータという巨大なモデルでありながら、推論効率が劇的に最適化されており、一般的なデータセンターのGPUで現実的なコストで運用が可能だ。各種ベンチマークにおいてGPT-5やClaude 4に肉薄、あるいは一部で凌駕するスコアを記録しており、「もはやクローズドAPIに依存する必要はない」と考える企業が続出している。\n\n世界中のオープンソース・コミュニティがこのモデルをベースに無数のファインチューニング版を生み出しており、AIの民主化を決定づける歴史的なマイルストーンとして、後世に語り継がれるモデルになるだろう。"
    },
    {
        "id": "grok-3",
        "title": "Grok 3",
        "lab": "xAI",
        "releaseDate": "2026-09-01",
        "contextWindow": "2M",
        "license": "Proprietary",
        "description": "イーロン・マスク率いるxAIの最新モデル。X（旧Twitter）のリアルタイムデータと世界最大の計算資源で学習。",
        "modalities": ["Text", "Image"],
        "image": "https://images.unsplash.com/photo-1639322537228-f710d846310a?q=80&w=800&auto=format&fit=crop",
        "body": "テキサス州に構築された世界最大のAIスーパーコンピューター「Colossus」の強大な演算能力によって鍛え上げられたのが『Grok 3』である。\n\nイーロン・マスクが掲げる「宇宙の真理を探求するAI」という壮大なビジョンのもと、政治的妥協や過度な安全性フィルターを排除した、真に中立で好奇心旺盛な性格付けがなされている。\n\nX（旧Twitter）プラットフォーム上の数兆件におよぶリアルタイムの会話データを独占的に学習しており、世界のトレンドや突発的なニュースに対する状況把握能力においては、他のどのモデルの追随も許さない。ユーモアと皮肉を交えた独特のトーンも健在であり、多くの熱狂的な支持者を集めている。"
    }
]

LABS = [
    {
        "id": "openai",
        "name": "OpenAI",
        "location": "San Francisco, CA, USA",
        "description": "汎用人工知能（AGI）の実現に向け、業界のトップランナーとしてAIの進化を牽引し続ける巨大研究機関。",
        "website": "https://openai.com/",
        "image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=800&auto=format&fit=crop",
        "body": "2022年末のChatGPTリリース以来、世界の覇権を握り続けるOpenAI。サム・アルトマン率いるこの組織は、近年ではハードウェア開発や独自のAIチップ設計にも乗り出し、単なるソフトウェア企業から「AI時代のインフラ企業」へと変貌を遂げつつある。\n\n彼らが目指すAGI（汎用人工知能）のロードマップは着実に進行しており、社内の秘密裏のプロジェクト「Q*（キュースター）」から派生したとされる高度な推論技術は、現在のGPT-5の基盤となっている。優秀な人材の流出やガバナンスの問題を幾度も乗り越えながら、依然としてAI業界の中心（オメガポイント）であり続けている。"
    },
    {
        "id": "anthropic",
        "name": "Anthropic",
        "location": "San Francisco, CA, USA",
        "description": "AIの安全性とアライメントを最重要視し、暴走しない堅牢なAIシステム「Claude」シリーズを開発する気鋭の企業。",
        "website": "https://www.anthropic.com/",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop",
        "body": "OpenAIから独立したダリオ・アモデイらが立ち上げたAnthropicは、「AIが人類の脅威にならないこと」を絶対的な至上命題として掲げている。\n\n彼らの開発手法である『Constitutional AI（憲法ベースのAI）』は、人間のフィードバック（RLHF）への過度な依存から脱却し、AI自身に基本原則を与えて自己採点・自己修正させるという画期的なアプローチだ。この安全性への徹底したこだわりが、結果的にエンタープライズ市場における圧倒的な信頼に繋がり、AmazonやGoogleからの巨額の投資を引き出している。"
    },
    {
        "id": "google-deepmind",
        "name": "Google DeepMind",
        "location": "London, UK / Mountain View, CA, USA",
        "description": "Google BrainとDeepMindの統合によって誕生した、基礎研究から製品化までを網羅する最強のAI研究集団。",
        "website": "https://deepmind.google/",
        "image": "https://images.unsplash.com/photo-1573164713988-8665fc963095?q=80&w=800&auto=format&fit=crop",
        "body": "かつてAI研究の二大巨頭であった「Google Brain」と「DeepMind」が統合されて数年。デミス・ハサビス率いるこの巨大組織は、理論研究の深さと、Googleの強大な計算資源という両輪を手に入れた。\n\nAlphaGoでの衝撃から始まり、AlphaFoldによるタンパク質構造解析の革命など、彼らの強みは「科学的発見を加速するAI」にある。現在はGeminiシリーズを通じて汎用LLM市場でも反転攻勢を強めており、量子コンピューティングとの融合など、10年後を見据えた壮大な研究開発が進められている。"
    },
    {
        "id": "meta-fair",
        "name": "Meta FAIR",
        "location": "Menlo Park, CA, USA / Paris, France",
        "description": "AIの民主化を掲げ、オープンソースコミュニティに最高峰のモデル「Llama」を無償提供し続けるヤン・ルカン率いる研究部門。",
        "website": "https://ai.meta.com/",
        "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=800&auto=format&fit=crop",
        "body": "MetaのチーフAIサイエンティストであるヤン・ルカンの信念のもと、FAIR（Fundamental AI Research）はクローズド化が進むAI業界にあって、異端かつ極めて重要なオープンソースの守護者となっている。\n\n彼らが開発したLlamaシリーズは、オープンソースAIのエコシステムを根底から支えており、世界中の開発者がこれをベースに独自のAIを構築している。マーク・ザッカーバーグの強力な支援のもと、数十万個の最新GPUを調達し、商業的利益よりも「プラットフォームの覇権」を握るための壮大な戦略を展開している。"
    },
    {
        "id": "xai",
        "name": "xAI",
        "location": "Austin, TX, USA",
        "description": "イーロン・マスクが設立した、「宇宙の真の姿を理解する」ことを目的とする独立系AIスタートアップ。",
        "website": "https://x.ai/",
        "image": "https://images.unsplash.com/photo-1620825937374-87fc7d620980?q=80&w=800&auto=format&fit=crop",
        "body": "「既存のAIはあまりにポリコレ（政治的妥当性）に縛られすぎている」。そう警鐘を鳴らしたイーロン・マスクが、OpenAIやGoogleへの対抗馬として立ち上げたのがxAIだ。\n\nテスラやスペースX、そしてX（旧Twitter）という、彼が持つ巨大なエコシステムと密接に連携しているのが最大の特徴だ。特にXから得られるリアルタイムの人間の思考データと、テスラが持つ現実世界の物理（動画）データを組み合わせることで、テキストにとどまらない真の汎用人工知能の開発を猛スピードで進めている。"
    }
]

RESEARCHERS = [
    {
        "id": "sam-altman",
        "name": "Sam Altman",
        "lab": "OpenAI",
        "role": "CEO",
        "famousFor": "OpenAIのCEOとして、ChatGPTの世界的ブームを巻き起こし、AI時代の幕を開けた立役者。",
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=800&auto=format&fit=crop",
        "links": {"x": "https://x.com/sama"},
        "body": "シリコンバレーの若き帝王とも呼ばれるサム・アルトマン。Y Combinatorのトップとしての経験を活かし、非営利の研究所だったOpenAIを、世界で最も価値のあるハイテク企業へと変貌させた。\n\n彼の凄みは、技術的な先見性以上に、その圧倒的な資金調達能力と政治的交渉力にある。数兆円規模の半導体ネットワーク構築計画や、各国の首脳とのAI規制に関する議論の主導など、彼の一挙手一投足がテクノロジー業界のみならず、世界の地政学にまで影響を与えていると言っても過言ではない。"
    },
    {
        "id": "ilya-sutskever",
        "name": "Ilya Sutskever",
        "lab": "SSI (Safe Superintelligence)",
        "role": "Founder / Chief Scientist",
        "famousFor": "ディープラーニングのブレイクスルーであるAlexNetの共同開発者。AIの安全性への懸念からOpenAIを去り、SSIを設立。",
        "image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=800&auto=format&fit=crop",
        "links": {"x": "https://x.com/ilyasut"},
        "body": "AI業界において、最も深くAIの未来を恐れ、かつその可能性を信じている男、それがイリヤ・サツケヴァーだ。OpenAIのチーフサイエンティストとしてGPT-4開発の陣頭指揮を執った彼は、「Feel the AGI（AGIを感じろ）」という有名な言葉を残している。\n\n2023年のOpenAI社内クーデター騒動の中心人物となり、その後同社を退社。「安全な超知能（Safe Superintelligence）」の開発のみを目的とする新会社SSIを立ち上げた。商業的なプロダクトリリースに追われることなく、純粋な安全性の研究に没頭する彼の哲学は、加速主義に傾くシリコンバレーにおいて重要なカウンターウェイトとなっている。"
    },
    {
        "id": "demis-hassabis",
        "name": "Demis Hassabis",
        "lab": "Google DeepMind",
        "role": "CEO",
        "famousFor": "天才チェスプレイヤーであり、DeepMindの創設者。AlphaGoやAlphaFoldでノーベル賞を受賞。",
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=800&auto=format&fit=crop",
        "links": {"x": "https://x.com/demishassabis"},
        "body": "チェスの神童、ゲーム開発者、認知神経科学者——多彩な顔を持つデミス・ハサビスの目標はただ一つ、「知能を解明し、それを使って他のすべての問題を解決する」ことだ。\n\n彼の率いるDeepMindは、囲碁の世界チャンピオンを打ち破ったAlphaGoで世界を驚愕させ、続いてタンパク質の立体構造を予測するAlphaFoldで生物学に革命を起こした。2024年のノーベル化学賞受賞は、彼が単なるソフトウェアエンジニアではなく、AIを用いて人類の科学を前に進める稀代の科学者であることを証明した。"
    },
    {
        "id": "yann-lecun",
        "name": "Yann LeCun",
        "lab": "Meta FAIR",
        "role": "VP & Chief AI Scientist",
        "famousFor": "畳み込みニューラルネットワーク（CNN）の父。チューリング賞受賞者であり、オープンソースAIの強力な擁護者。",
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=800&auto=format&fit=crop",
        "links": {"x": "https://x.com/ylecun", "scholar": "https://scholar.google.com/citations?user=WLN3QrAAAAAJ"},
        "body": "ジェフリー・ヒントン、ヨシュア・ベンジオと並び「AIのゴッドファーザー」と称されるヤン・ルカン。画像認識の基礎となるCNNを発明した彼の業績は計り知れない。\n\nSNS上では非常に率直かつ攻撃的な論客としても知られ、「AIによる人類滅亡論は馬鹿げている」「自己回帰型のLLM（GPTなど）はすぐに限界を迎える」と公言してはばからない。JEPA（Joint Embedding Predictive Architecture）という独自の自己教師あり学習のビジョンを掲げ、言語モデルの次に来る「世界モデル」の構築に向けて、MetaのAI研究を力強く牽引している。"
    },
    {
        "id": "dario-amodei",
        "name": "Dario Amodei",
        "lab": "Anthropic",
        "role": "CEO",
        "famousFor": "AIの安全なスケーリング則に関する研究の第一人者。Anthropicの創業者。",
        "image": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?q=80&w=800&auto=format&fit=crop",
        "links": {"scholar": "https://scholar.google.com/citations?user=dario-amodei-placeholder"},
        "body": "OpenAIで研究担当VPを務めていたダリオ・アモデイは、AIの能力がパラメータ数と計算量に応じて予測可能に向上するという「スケーリング則（Scaling Laws）」の論文を発表したことで知られる。\n\n彼はこの法則がもたらす未来のAIの驚異的な能力を誰よりも早く予測し、同時にその危険性に戦慄した。OpenAIの商業化路線に異を唱えて独立し、妹のダニエラらと共にAnthropicを設立。派手なプレゼンテーションを好まず、学術的で地道な研究を重んじる彼の姿勢は、熱狂するAI業界において独特の冷静な存在感を放っている。"
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
    save_data("labs", LABS)
    save_data("researchers", RESEARCHERS)

if __name__ == "__main__":
    main()
