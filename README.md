# LegalKit · 법무킷

**PDF merger + Evidence organizer + Case collector + Voice transcriber for Korean legal self-representation**

한국 나홀로소송 전용 통합 도구 — PDF 병합기 · 증거목록 · 판례수집 · 호증부여기 · 녹취록


---

## Download · 다운로드

| Track | Version | File | Size | GPU |
| --- | --- | --- | --- | --- |
| 🇰🇷 Lite KR | v7.48 | `LegalKit_Lite_KR_v7.48_setup.exe` | 140 MB | 불요 |
| 🌐 Lite EN | v7.48 | `LegalKit_Lite_EN_v7.48_setup.exe` | 140 MB | not required |
| 🇰🇷 Pro KR | v7.48 | `LegalKit_Pro_KR_v7.48_setup.exe` | 642 MB | NVIDIA RTX 권장 |
| 🌐 Pro EN | v7.48 | `LegalKit_Pro_EN_v7.48_setup.exe` | 641 MB | NVIDIA RTX recommended |

> 인스톨러 더블클릭 → Program Files 정식 설치 · 시작메뉴·바탕화면 바로가기 자동 등록 · 제어판 정식 언인스톨
> Double-click installer → installs to Program Files · auto Start Menu / Desktop shortcuts · uninstalls cleanly via Control Panel

📥 [Latest release · 최신 릴리스](https://github.com/bombc5003/LegalKit/releases/latest)

---

## Track Comparison · 트랙 비교

| | Lite (v7.48) | Pro (v7.48) |
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
| 🎙 녹취록 · Transcriber | 음성/영상 → 텍스트 자동 변환 · **발화자 구분(발화자1/2)** · 입력 11종 / 출력 5종 / 5개 언어 |
| 📣 홍보 · Promo | 개발자 출판 도서 · 개발 의뢰 안내 |

---

## What's New · 변경사항

### v7.48 (2026-05-13)
- 🎤 **발화자 구분** — 순수 numpy FFT K-means 알고리즘. 추가 패키지 0. 발화자1/2 자동 분리 · 【발화자1】헤더 그룹핑 출력
- ⚠️ **STT 경고 라벨** — 녹취록 탭 상단에 오인식 주의문구 표시 ("제출 전 녹취 원본 청취·수정 필수")
- 🔒 **폐쇄환경 특화** — 외부 API 미사용 · 인터넷 차단 환경 완전 지원 · 데이터 유출 Zero
- 📣 **순환광고 슬롯** — 폐쇄망·오프라인 처리 특화 문구 6종 회전 표시

### v7.47
- EN 트랙 신설 (영문판 Pro/Lite)
- 판례수집 법제처 API 통합
- 호증부여기 갑·을·병·정 자동 리네임

---

## Offline / Air-gapped · 폐쇄환경 특화

LegalKit은 **외부 서버 통신이 전혀 없습니다.**

- 녹취록 변환 · 발화자 구분 모두 로컬 처리
- 설치 후 네트워크 완전 차단 환경에서도 모든 기능 정상 동작
- 수사기관·법원 제출용 녹취 자료를 외부 클라우드 미사용으로 처리
- 폐쇄망 시스템 개발 의뢰: 010-2272-7030

---

## License · 라이선스

Private / Commercial — redistribution prohibited · 무단 재배포 금지
