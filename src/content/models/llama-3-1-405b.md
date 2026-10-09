---
id: llama-3-1-405b
title: Llama 3.1 405B
lab: Meta
releaseDate: 2024-07-23
contextWindow: 128k
license: Llama 3.1 Community License
description: オープンソースAIの頂点。クローズドな最先端モデルと同等以上の推論能力を持つ超巨大モデル。
modalities:
- Text
image: https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=800&auto=format&fit=crop
sourceUrl: https://ai.meta.com/blog/meta-llama-3-1/
sourceTitle: Llama 3.1 405Bのリリース | Meta AI Blog
---

シリコンバレーで長らく議論されてきた「オープン vs クローズド」のAI開発競争において、Metaは決定的な一手を打った。4050億パラメータという途方もない規模を持つ『Llama 3.1 405B』のオープンソース化である。

このモデルは、1万6000個ものH100 GPUを用いて学習され、数学、プログラミング、多言語推論など、ほぼすべての主要ベンチマークにおいてGPT-4oやClaude 3.5 Sonnetといったクローズドなトップモデルと互角、あるいはそれ以上の成績を記録している。マーク・ザッカーバーグCEOは「AIの力は少数の巨大企業によって独占されるべきではない」と明言し、このモデルのウェイト（重みデータ）を世界中の開発者に向けて無償で公開した。

これにより、何が起きるのか。最も重要なのは「合成データ（Synthetic Data）」の生成と、小規模モデルへの「蒸留（Distillation）」が可能になったことだ。企業や研究機関は、高価なAPI利用料を支払い続けることなく、Llama 3.1 405Bという「教師」を用いて、自社専用の高性能かつ軽量なローカルAIモデルを構築できるようになった。これは単なる一企業のプロダクト発表ではなく、世界のソフトウェアインフラストラクチャに対する巨大なオープンソースの贈り物であり、AIエコシステム全体の進化を数年分加速させる起爆剤となるだろう。
