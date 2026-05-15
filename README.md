# LegalKit v7.50 · 법무킷

> **Multilingual legal productivity toolkit — Pro & Lite**
> >
> >> 한국 나홀로소송 전용 통합 도구 — 9개 언어 Pro·Lite 무료 배포
> >>
> >> [![Version](https://img.shields.io/badge/version-7.50-blue)](https://github.com/bombc5003/LegalKit/releases/tag/v7.50)
> >> [![License](https://img.shields.io/badge/license-Free%20%2F%20Freeware-brightgreen)](https://github.com/bombc5003/LegalKit/releases)
> >> [![Python](https://img.shields.io/badge/python-3.11%2B-yellow)](https://www.python.org/)
> >>
> >> ---
> >>
> >> ## Download · 다운로드
> >>
> >> | Track | File | Size | GPU |
> >> |-------|------|------|-----|
> >> | 🌐 **Lite** (9 langs) | `LegalKit_v750_Lite_setup.exe` | ~140 MB | 불요 / not required |
> >> | 🌐 **Pro** (9 langs) | `LegalKit_v750_Pro_setup.exe` | ~640 MB | NVIDIA RTX 권장 |
> >>
> >> 👉 **[📥 Latest release · 최신 릴리스](https://github.com/bombc5003/LegalKit/releases/latest)**
> >>
> >> 인스톨러 더블클릭 → Program Files 정식 설치 · 시작메뉴·바탕화면 바로가기 자동 등록 · 제어판 정식 언인스톨
> >> Double-click installer → installs to Program Files · auto Start Menu / Desktop shortcuts · uninstalls cleanly via Control Panel
> >>
> >> ---
> >>
> >> ## Edition Comparison · 트랙 비교
> >>
> >> | | Lite | Pro |
> >> |-|------|-----|
> >> | STT Engine · 엔진 | 미포함 / not included | faster-whisper CUDA float16 |
> >> | 30-min audio | — | 약 1~2분 (~20×) |
> >> | GPU | 불요 / not required | NVIDIA RTX 권장 |
> >> | CUDA Toolkit | 불요 | 불요 (cuBLAS·cuDNN 자체 동봉) |
> >> | Installer Size | ~140 MB | ~640 MB |
> >>
> >> ---
> >>
> >> ## Supported Languages · 지원 언어 (9개 언어 통합 EXE)
> >>
> >> 🇰🇷 Korean · 🇺🇸 English · 🇫🇷 French · 🇩🇪 German · 🇪🇸 Spanish
> >> 🇵🇹 Portuguese · 🇮🇹 Italian · 🇯🇵 Japanese · 🇳🇱 Dutch
> >>
> >> ---
> >>
> >> ## Features · 기능 (9탭 통합 구조)
> >>
> >> | 탭 · Tab | 기능 · Function |
> >> |----------|----------------|
> >> | 📎 병합기 · Merger | PDF + 이미지(JPG/PNG/TIFF) 일괄 병합 · 전자소송 19.5 MB 자동 분할 |
> >> | 🔍 퍼지찾기 · Fuzzy Find | 오타 허용 파일명 퍼지 검색 |
> >> | 📋 증거목록 · Evidence List | 호증 목록 자동 생성 (TXT · CSV · 클립보드) |
> >> | ⚖️ 판례수집 · Case Collector | 법제처 Open API 키워드 + 본문 수집 (**한국어판 전용**) |
> >> | 🏷️ 호증부여기 · Label Maker | 갑·을·병·정 파일명 자동 부여 및 리네임 |
> >> | 🎙 녹취록 · Transcriber | 음성/영상 → 텍스트 · 발화자 구분 · 5개 언어 (**Pro 전용**) |
> >>
> >> > **Case Collector** — Korean courts only (법제처 Open API). International editions display a localized notice.
> >> > > **STT Transcriber** — Pro edition only. NVIDIA CUDA GPU required.
> >> > >
> >> > > ---
> >> > >
> >> > > ## What's New · 변경사항
> >> > >
> >> > > ### v7.50 (2026-05)
> >> > > - 🌐 **9-language bundle** — KR/EN/FR/DE/ES/PT/IT/JA/NL 통합 단일 EXE
> >> > > - - ⚡ **CUDA GPU acceleration** — float16 확정. CPU INT8 fallback 제거 (Pro 완전 GPU 전용)
> >> > >   - - 🔧 **NVIDIA DLL bundling** — nvidia-cublas-cu12 / nvidia-cudnn-cu12 자체 동봉
> >> > >     - - ⚖️ **Case Collector** — 국제판 전체 한국어판 전용 안내 화면으로 교체
> >> > >       - - 🏷️ **VibeTech** 브랜드 적용 (국제판)
> >> > >         - - 🐛 `_on_mousewheel` 바인딩 버그 수정 (14개 국제판)
> >> > >          
> >> > >           - ### v7.48 (2026-05)
> >> > >           - - 🎤 발화자 구분 — 순수 numpy FFT K-means. 추가 패키지 0. 발화자1/2 자동 분리
> >> > >             - - ⚠️ STT 경고 라벨 — 녹취록 탭 상단 오인식 주의문구
> >> > >               - - 🔒 폐쇄환경 특화 — 외부 API 미사용 · 인터넷 차단 환경 완전 지원
> >> > >                
> >> > >                 - ### v7.47
> >> > >                 - - EN 트랙 신설 · 판례수집 법제처 API 통합 · 호증부여기 갑·을·병·정 · Ed25519 라이선스
> >> > >                  
> >> > >                   - ---
> >> > >
> >> > > ## Offline / Air-gapped · 폐쇄환경 특화
> >> > >
> >> > > LegalKit은 외부 서버 통신이 전혀 없습니다.
> >> > >
> >> > > - 녹취록 변환 · 발화자 구분 모두 로컬 처리
> >> > > - - 설치 후 네트워크 완전 차단 환경에서도 모든 기능 정상 동작
> >> > >   - - 수사기관·법원 제출용 녹취 자료를 외부 클라우드 미사용으로 처리
> >> > >     - - 폐쇄망 시스템 개발 의뢰: 010-2272-7030
> >> > >      
> >> > >       - ---
> >> > >
> >> > > ## License · 라이선스
> >> > >
> >> > > **개인 사용 무료** · Free for personal use
> >> > >
> >> > > 상업적 이용은 저작권법상 허가가 필요합니다. 무단 재판매 및 소스코드 역공학 금지.
> >> > > Commercial use requires permission under copyright law. Resale and reverse engineering prohibited.
> >> > >
> >> > > © 2026 VibeTech · Korean edition © 2026 박병진
