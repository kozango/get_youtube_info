# 経営中毒 YouTube コンシェルジュ（ミニマム版）

YouTubeチャンネル/再生リストから字幕付き動画のメタ情報＋字幕を取得し、CSV/.txt形式で出力するツールです。

## 特徴
- 字幕付き動画のみ抽出（日本語・英語対応）
- メタ情報＋字幕をCSV/.txtで保存
- Custom GPT Knowledgeタブ用データ生成
- Dockerコンテナ一発実行
- APIキー等の機密情報は**絶対に公開しないこと**

## セットアップ
1. このリポジトリをクローン
2. `.env.example` をコピーし `.env` を作成、APIキー等を記入
3. Dockerイメージをビルド

```bash
docker build -t keiei_youtube_info .
```

4. 実行例
```bash
docker run --rm --env-file .env -v $(pwd)/output:/app/output keiei_youtube_info --help
```

## セキュリティ
- `.env` やAPIキーは**絶対にGitHub等に公開しないでください**
- `.env.example`のみ公開し、実際の値は各自で管理

## ライセンス
MIT
