# Flask Blueprint 範例專案

這是一個使用 Flask 和 Blueprint 的範例專案，展示了如何組織一個模組化的 Flask 應用程式。

## 專案結構

```
.
├── app.py          # 主應用程式檔案
├── config.py       # 配置檔案
├── routes.py       # 路由和 Blueprint 定義
├── requirements.txt # 專案依賴
└── templates/      # HTML 模板
    └── index.html  # 主頁面模板
```

## 安裝

1. 建立虛擬環境：
```bash
python -m venv venv
```

2. 啟動虛擬環境：
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. 安裝依賴：
```bash
pip install -r requirements.txt
```

## 執行

```bash
python app.py
```

應用程式將在 http://localhost:5000 運行。

## 功能

- 使用 Blueprint 組織路由
- 分離主頁面和 API 路由
- 使用 Bootstrap 的響應式設計
- 簡單的 API 端點示範 