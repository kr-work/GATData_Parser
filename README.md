## GATデータの取得
GATの過去のデジタルカーリングの盤面データを取得できる、パーサを作成しました。

### 使用方法
envを作成し、
```bash
# pipの場合
pip install -r requirements.txt

# uvの場合
uv pip install -r requirements.txt
```

[こちらのリンク](http://minerva.cs.uec.ac.jp/cgi-bin/curling/wiki.cgi?page=%C2%E81%B2%F3UEC%C7%D5%A5%C7%A5%B8%A5%BF%A5%EB%A5%AB%A1%BC%A5%EA%A5%F3%A5%B0%C2%E7%B2%F1)から、各対戦データを取得し、展開してからDC1～DC3_GATDataに格納してください。

格納するには
```bash
cd src
python data_manager.py
```
を実行してください。

データベースはsqliteを採用しており、
- end
- shot
- my_team_stones
- opponent_team_stones
- my_team_scores
- opponent_team_scores

が格納されています。
なお、例えばmy_team_stonesには、次にショットを打つチームが設定してあります。これにより、どの盤面データもシミュレーションに使用しやすいよう設定してあります。

### データベースからの情報取得
end(0～9)とshot(0～15)を決定し、
``` python
ReadData.read_state_data(0, 0)
```
を指定すれば、エンド0番目、ショット0番目のデータを全て取得できます。
なお、他に必要な関数は随時追加する予定です。
