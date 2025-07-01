# 🟢 ETH Income Bot (10 Address Monitor)

บอทตรวจสอบรายการธุรกรรมเข้า (Deposit) ของ Ethereum (ETH) แบบเรียลไทม์ สำหรับ 10 บัญชี ETH Address โดยแจ้งเตือนผ่าน Telegram โดยอัตโนมัติ

---

## ✨ คุณสมบัติ

- ตรวจจับเฉพาะธุรกรรม "เข้า" (ขาเข้า) ของ ETH
- รองรับสูงสุด 10 ETH Address
- แจ้งเตือนผ่าน Telegram ทุก 10 วินาที
- แสดงจำนวน ETH และมูลค่าประมาณเป็น USDT (อ้างอิง Binance)
- ออกแบบให้ทำงานบน Railway หรือ VPS ที่รองรับ Python

---

## 🧾 การแจ้งเตือนที่แสดง

ตัวอย่างการแจ้งเตือนใน Telegram:

🟢 ETH 入金
👤 จาก: 0x1234...
👥 ถึง: 0xYourWalletAddress
💰 0.728000 ETH ≈ $2,523.98


---

## 📦 การติดตั้งบน Railway

### 1. โคลนหรืออัปโหลดโค้ดไปยัง GitHub

หากคุณได้แก้ไขโค้ดแล้ว ให้อัปโหลดไปยัง GitHub repository ของคุณ เช่น `myuser/eth-income-bot`

### 2. เชื่อมต่อ Railway กับ GitHub Repo ของคุณ

จากหน้า Railway Project:
- เลือก New Project > Deploy from GitHub Repo
- เลือก Repository ที่มีโค้ดของบอท

### 3. เพิ่ม Environment Variables

เพิ่มตัวแปรใน Settings > Variables:

| ชื่อ                | ค่าที่ต้องกรอก                         |
|---------------------|----------------------------------------|
| `BOT_TOKEN`         | Token ของ Telegram Bot ของคุณ         |
| `CHAT_ID`           | chat_id ของกลุ่มที่คุณจะให้บอทส่งแจ้งเตือน |
| `ETHERSCAN_API_KEY` | API Key จาก https://etherscan.io      |
| `address_1` ถึง `address_10` | ETH Address ที่ต้องการตรวจสอบ (สูงสุด 10 บัญชี) |

> 🛑 คุณสามารถเว้นว่าง `address_x` ใด ๆ ได้ หากไม่ได้ใช้ครบ 10 address

### 4. เพิ่ม `start command` ให้ Railway

ไปที่ Settings → Start Command:

```bash
python bot.py
