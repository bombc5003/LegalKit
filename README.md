# LegalKit · 법무킷

**PDF merger + Evidence organizer + Case collector + Voice transcriber for Korean legal self-representation**

한국 나홀로소송 전용 통합 도구 — PDF 병합기 · 증거목록 · 판례수집 · 호증부여기 · 녹취록

---

## Download · 다운로드

| Track | Version | File | Size | GPU |
| --- | --- | --- | --- | --- |
| 🇰🇷 Lite KR | v7.47 | `LegalKit_Lite_KR_v7.47_setup.exe` | 140 MB | 불요 |
| 🌐 Lite EN | v7.47 | `LegalKit_Lite_EN_v7.47_setup.exe` | 140 MB | not required |
| 🇰🇷 Pro KR | v7.47 | `LegalKit_Pro_KR_v7.47_setup.exe` | 642 MB | NVIDIA RTX 권장 |
| 🌐 Pro EN | v7.47 | `LegalKit_Pro_EN_v7.47_setup.exe` | 641 MB | NVIDIA RTX recommended |

> 인스톨러 더블클릭 → Program Files 정식 설치 · 시작메뉴·바탕화면 바로가기 자동 등록 · 제어판 정식 언인스톨
> Double-click installer → installs to Program Files · auto Start Menu / Desktop shortcuts · uninstalls cleanly via Control Panel

📥 [Latest release · 최신 릴리스](https://github.com/bombc5003/LegalKit/releases/latest)

---

## Track Comparison · 트랙 비교

| | Lite (v7.47) | Pro (v7.47) |
|---|---|---|
| Engine · 엔진 | faster-whisper CPU INT8 | faster-whisper GPU float16 |
| 30-min audio · 30분 음성 | 약 8분 (~3.7×) | 약 1~2분 (~20×) |
| GPU | 불요 / not required | NVIDIA RTX 4070급 권장 |
| CUDA Toolkit | 불요 | 불요 (cuBLAS·cuDNN 자체 동봉) |
| Installer Size | 140 MB | 641 MB |
| 월정액 · Monthly | ₩10,000 | ₩20,000 |

---

## Features · 기능 (9탭 통합 구조)

| 탭 · Tab | 기능 · Function |
| --- | --- |
| 📎 병합기 · Merger | PDF + 이미지(JPG/PNG/TIFF) 일괄 병합 · 전자소송 19.5 MB 자동 분할 |
| 🔍 퍼지찾기 · Fuzzy Find | 오타 허용 파일명 퍼지 검색 |
| 📋 증거목록 · Evidence List | 호증 목록 자동 생성 (TXT · CSV · 클립보드) |
| ⚖️ 판례수집 · Case Collector | 법제처 Open API 키워드 + 본문 2단계 수집 |
| 🏷️ 호증부여기 · Label Maker | 갑·을·병·정 파일명 자동 부여 및 리네임 |
| 🎙 녹취록 · Transcriber | 음성/영상 → 텍스트 자동 변환 (입력 11종 / 출력 5종 / 5개 언어) |
| 📣 홍보 · Promo | 개발자 출판 도서 · 개발 의뢰 안내 |
| 📷 오토샷 · AutoShot | 화면 자동 캡처 · 연속 스크롤 캡처 |
| 🔑 라이선스 · License | 머신 ID 확인 · 라이선스 키 등록 |

### 녹취록 입출력

- **입력 11종** — m4a · mp3 · wav · ogg · flac · mp4 · mkv · mov · avi · aac · wma
- **출력 5종** — txt · srt · vtt · tsv · json
- **언어** — 자동 감지 / 한국어 / 영어 / 일본어 / 중국어

---

## Security · 보안

- **Ed25519 비대칭 서명** — 시크릿 노출에도 위조 키 발급 불가
- **license.json HMAC 봉인** — 다른 PC 복사 시 자동 무효
- **stdout/stderr None 가드** — PyInstaller windowed 빌드 호환

---

## License · 라이선스

개인 비상업적 사용은 무료입니다.
상업적 사용은 월정액 라이선스가 필요합니다.

- **Lite** — ₩10,000 / 월
- **Pro** — ₩20,000 / 월

머신 ID와 함께 아래로 연락 주세요.
For commercial use, contact us with your machine ID.

📧 bc5103@naver.com

---

## Korean Copyright Registration · 한국저작권위원회 등록

| 등록번호 · Reg. No. | 한국어 제호 | English Title | 등록일 · Date |
| --- | --- | --- | --- |
| C-2026-022057 | 오토샷 | AutoShot | 2026-05-07 |
| **C-2026-022058** | **법무킷** | **LegalKit** | **2026-05-07** ← 본 프로그램 |
| C-2026-022279 | 녹취록생성기 | TranscriptMaker | — |

전건 컴퓨터프로그램저작물 > 응용프로그램 > 사무관리 분류로 정식 등록.
저작권법 제53조에 따라 저작자·창작연월일이 법적으로 추정됩니다.

> 무단 복제·재배포·소스 변형 후 재배포는 저작권법에 따라 제한됩니다.
> Unauthorized redistribution or modification prohibited under Korean Copyright Act.

---

## NVIDIA Redistributable Notice

The Pro installer includes NVIDIA cuBLAS and cuDNN libraries, redistributed under the **NVIDIA CUDA Toolkit EULA Section 2.6**.

---

## Books · 출판 도서

| 도서 · Book | 언어 · Languages | 링크 · Link |
| --- | --- | --- |
| 코드를 모르는 사람의 코딩 | EN ES DE FR PT IT NL AR JA | [Amazon Kindle](https://www.amazon.com/dp/B0GXL8WPTT) |
| 클로드AI 코웍모드 입문서 | EN ES PT DE FR JA | [Amazon Kindle](https://www.amazon.com/dp/B0GYPMT5L3) |
| 클로드, 몸을 얻다 | EN ES DE JA | [Amazon Kindle](https://www.amazon.com/dp/B0GYL6M1CC) |
| 코드를 모르는 사람의 코딩 (한국어) | KR | [부크크](https://www.bookk.co.kr/book/view/482300) · [YES24](https://www.yes24.com/product/goods/188657828) |
| 클로드AI 코웍모드 입문서 (한국어) | KR | [부크크](https://www.bookk.co.kr/book/view/483796) |

Search **"Vibe Toolsmith"** on Amazon Kindle.

---

## Contact · 연락처

**박병진 · Byungjin Park**
📧 bc5103@naver.com
📱 010-2272-7030
🔗 [github.com/bombc5003](https://github.com/bombc5003)

개발 의뢰 환영 — 사무 자동화 · 포렌식 계열 · 법무 보조 도구 전문
Development requests welcome — office automation · forensic tools · legal aid software

---

© 2026 박병진 · Byungjin Park
All rights reserved. Unauthorized redistribution prohibited.
