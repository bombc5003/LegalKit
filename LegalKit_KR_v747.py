# Title: 법무킷 v6.8.5 (ClickLegalKit v6.8.5)
#        — 병합기 + 퍼지검색 + 증거목록 + 판례수집 + 홍보 통합
# Copyright: 2026. 박병진(bc5103@naver.com). All rights reserved.
# v533 변경: 멀티미디어 갑호증 부여 탭 추가 (※ v600에서 제거)
# v534 변경: 팩스 TIFF 다중 프레임(multi-frame) 전 페이지 병합 복원
# v600 변경: 증거목록 탭 통합 (구 증거목록기 v1.0 흡수, 4탭 구조)
# v610 변경: 갑호증 부여 탭 제거 (꼬임 인지) + 명칭 변경 (합체 → 법무킷)
# v670 변경: 판례수집 탭 신규 통합 (구 case_crawler v0.1.3 흡수)
#            현 4탭 구조: 병합기 + 퍼지검색 + 증거목록 + 판례수집
#            ─────────────────────────────────────────
#            [v670 사양]
#            - 명칭 확정: 법무킷 (ClickLegalKit)
#            - 증거목록 탭 (구 증거목록기 v1.0 흡수)
#              · 파일명 그대로 텍스트 추출
#              · TXT/CSV/클립보드 3종 출력
#            - 판례수집 탭 (구 case_crawler v0.1.3 흡수)
#              · 법제처 Open API 기반 (open.law.go.kr)
#              · 사용자 OC 인증키 입력 + 저장 (~/.click_legal_kit_oc.txt)
#              · 키워드 입력 → 판례 일괄 수집 → CSV 저장
#              · 후보 태그 다중 시도 (판시사항·판결요지·판례내용)
#              · threading 처리 (GUI 멈춤 방지)
#            - 드래그앤드롭은 evidence_tab 위젯에 별도 등록 (root drop과 격리)
#            - 골격 무결성 유지: SentinelHyperV530 클래스 시그니처·기존 메서드 무변경
#            - 신규 클래스 CaseCrawler 흡수 (case_crawler.py 코드 통합)
#            - 신규 메서드는 _ev_·_case_ 접두사로 흡수 (충돌 방지)
# v671 변경: 버그 픽스 2건
#            - pyperclip 미사용 import 제거 (미설치 환경 기동 크래시 원인)
#            - export_evidence_list 내 reportlab 자동설치 순서 정정
#              (서브모듈 import 전에 존재 확인 + pip install 선행)
# v672 변경: 판례수집기 개선 2건
#            - 0건 검색 시 ConnectionResetError 대신 정상 메시지 표시
#              (연결 끊김 예외를 0건 판정으로 흡수)
#            - 2단계 검색 신설: 본문 필터 키워드 입력란 추가
#              (1단계: 광범위 키워드로 API 검색,
#               2단계: 수집된 판례 본문에서 세부 키워드 2차 필터링)
#            - 골격 무결성 유지: 기존 메서드 시그니처 무변경
# v673 변경: 전체 UI 폰트 크기 상향 (가독성 개선)
#            - 전 탭 공통: 기존 폰트 크기 +1pt 일괄 적용
#            - 7pt→8pt, 8pt→9pt, 9pt→10pt (10pt 이상 기존 유지)
#            - 골격 무결성 유지: UI 속성만 변경, 로직 무변경
# v6.8.0 변경: 브랜드 아이덴티티 신설 + 광고 매립 + 홍보 탭 + 보안 식별자
#            ─────────────────────────────────────────
#            [공식 명칭 승격]
#            - 명칭 고정: 법무킷 (ClickLegalKit). 영문 식별자 LGK 도입.
#            - 브랜드 표기: Vibe Toolsmith.
#            [보안·포렌식 식별자]
#            - _FREE_BUILD_SEED HMAC-SHA256 8자 빌드 식별자 도입
#                seed: legalkit-FREE-v6.8-20260422
#            - 머신 핑거프린트 5요소 결합 HMAC-SHA256 8자 머신 해시 도입
#                MachineGuid + MAC + COMPUTERNAME + USERNAME + CPU ProcessorId
#                (wmic 호출 제거 — GUI 블로킹·콘솔 깜빡임 원천 차단)
#            - FREE_BUILD_ID = LGK-FREE-v6.8-{BUILD_HASH}-{MACHINE_HASH}
#            [광고 매립 — 병합기 출력]
#            - 이미지(JPG/PNG/BMP/WebP/ICO/JFIF) → PDF 변환 전
#                상단 28px 띠(시각·일련·도구) + 하단 24px 띠(고정·회전 광고) 합성
#            - TIFF 다중 프레임 각 프레임 동일 띠 합성
#            - 병합 직후 최종 PDF 전 페이지 하단 24px 푸터 워터마크 오버레이
#                기존 PDF 페이지도 모두 부착 (사용자 결정 C안)
#            - 갑호증 목록 PDF: 페이지마다 하단 푸터 1줄 추가
#            [광고 매립 — 텍스트 산출물]
#            - 판례수집 CSV: 우측 끝 "수집도구" 컬럼 신설.
#                값 형식: "법무킷 v6.8.0 · {BRAND_CAPTION} · {FIXED_CAPTION}"
#            - 증거목록 TXT: 상단 헤더 4행 + 하단 푸터 2행
#            - 증거목록 CSV: 우측 끝 "수집도구" 컬럼 신설 (판례수집 동일)
#            - 증거목록 클립보드: 말미 1줄 광고 부가
#            [홍보 탭 신설]
#            - 우측 끝 신규 탭 "📣 홍보" 추가
#            - 제품 카드(오토샷·법무킷) + 연락처 블록 + 회전 광고 프리뷰
#            - 외부 통신 없음 (정적 표시 전용, 폐쇄망 원칙 무훼손)
#            [BRAND_CAPTIONS 20슬롯 — 법무킷 전용 재편]
#            - 호증 병합 8 + 갑호증 목록 3 + 판례수집 3 +
#              증거목록 2 + 퍼지검색 2 + 안내·차별화 2
#            [무결성]
#            - SentinelHyperV530 클래스 시그니처·기존 메서드 시그니처 무변경
#            - 신규 메서드는 _ad_·_promo_ 접두사로 흡수 (충돌 방지)
#            - 기존 핵심 로직(PdfMerger 흐름, 판례 API 호출, 증거목록
#              라인 빌더, 퍼지검색 fuzzy_score) 무변경
# v6.8.1 변경: 기동 강종 수리 (핑거프린트 수집 블로킹 제거)
#            ─────────────────────────────────────────
#            [수리 내역]
#            - wmic 동기 호출 2건(csproduct·diskdrive) 제거
#              (Windows 11 24H2 wmic deprecated·타임아웃 응답·
#               --noconsole 빌드에서 wmic 콘솔 충돌로 인한 기동 직전 강종)
#            - 머신 핑거프린트 7요소 → 5요소 축소
#              (MachineGuid + MAC + COMPUTERNAME + USERNAME + CPU)
#            - winreg KEY_WOW64_64KEY 플래그 실패 시 플래그 없이 재시도 폴백
#            - 모든 수집 단계·HMAC 계산에 BaseException 가드 중첩
#              (폴백 문자열로 흡수해 기동 보장)
#            [식별력 영향]
#            - 메인보드 UUID·디스크 S/N 제외.
#              실제 충돌 가능성: 동일 Windows 설치·동일 NIC·동일 사용자 조합 시.
#            [무결성]
#            - 기능 변경 없음. 핑거프린트 수집 루틴만 축소.
#            - 광고 매립·홍보 탭·산출물 출력 로직 v6.8.0 그대로.
# v6.8.2 변경: 기동 강종 2차 수리 (Tk Label pady 튜플 비수용)
#            ─────────────────────────────────────────
#            [원인]
#            - _init_promo() 내 tk.Label(..., pady=(0, 6)) 5건.
#              Tkinter Label 위젯 옵션 pady는 단일 정수만 수용.
#              튜플은 .pack(pady=(a,b))에만 허용.
#              → _tkinter.TclError: bad screen distance "0 6"
#                기동 직전 SentinelHyperV530.__init__ → _init_promo
#                예외 미가드로 GUI 메인루프 진입 실패 강종.
#            [수리 내역]
#            - 5건 모두 위젯 pady는 단일 int로 축소,
#              상하 여백 의도는 .pack(pady=(a,b))로 이전.
#              (라인 2010, 2014, 2030, 2039, 2045)
#            [무결성]
#            - 시각적 여백 동일. 기능·로직 변경 없음.
#            - 핑거프린트·광고·산출물 로직 v6.8.1 그대로.
# v6.8.7 변경: 홍보 탭 개발 의뢰 접수 카드 신설
#            ─────────────────────────────────────────
#            [추가 기능]
#            - 제품 카드 스크롤 영역 하단에 개발 의뢰 카드 추가
#              사무 자동화·포렌식·법무 보조 도구 전문 의뢰 안내
#              주황 계열(bg="#2a1a0a", border="#b05a00") 카드 디자인
#            [무결성]
#            - 기존 카드·GitHub 버튼·연락처·광고 로직 무변경.
# v6.8.6 변경: 홍보 탭 제품 카드 GitHub 링크 버튼 추가
#            ─────────────────────────────────────────
#            [추가 기능]
#            - 법무킷·오토샷·녹취록 생성기 카드 하단 GitHub 버튼 신설
#              webbrowser.open() 방식. 외부 통신 없음 (클릭 시에만 브라우저 호출)
#            [무결성]
#            - 기존 카드 텍스트·색상·스크롤 로직 무변경.
#            - 연락처·회전 광고·푸터 로직 무변경.
# v6.8.5 변경: 홍보 탭 제품 카드 스크롤 + ClickTalkScript 카드 추가
#            ─────────────────────────────────────────
#            [추가 기능]
#            - _init_promo() 내 제품 카드 영역을 Canvas + Scrollbar 스크롤 래퍼로 교체
#              (카드 수 증가에 따른 세로 공간 부족 해소, expand=False 고정 높이 유지)
#            - ClickTalkScript(녹취록 생성기) 제품 카드 신설
#              오토샷 카드 아래 위치. 보라색 계열 카드 배경.
#            [무결성]
#            - 기존 법무킷·오토샷 카드 텍스트·색상 무변경.
#            - 연락처·회전 광고 프리뷰·푸터 로직 무변경.
#            - 신규 UI 위젯 _init_promo() 내 스코프 한정, 외부 메서드 시그니처 무변경.
# v6.8.3 변경: 호증부여기 탭 신설 (PDF 파일명 앞부분 일괄 리네임)
#            ─────────────────────────────────────────
#            [추가 기능]
#            - 신규 탭 "🏷 호증부여기" 병합기·퍼지검색·증거목록·판례수집
#              다음·홍보 앞 위치에 삽입. _init_evid_label() 메서드.
#            - 드래그드롭 리스트 + 선택행 들여쓰기(그룹 묶기)로
#              본번·가지번호 자동 부여. indent=0 본번 증가,
#              indent=1 직전 본번 아래 가지번호 1·2·3… 자동.
#            - 당사자 라디오(갑·을·병·정), 시작번호 Spinbox,
#              미리보기, 실제 리네임 실행 버튼.
#            - 파일명 규칙: {당사자}제{N}호증_{원제목}.pdf,
#              가지번호 있으면: {당사자}제{N}호증의{M}_{원제목}.pdf.
#            - 충돌 시 _dup2·_dup3 자동 접미로 덮어쓰기 방지.
#            [무결성]
#            - 기존 병합기·퍼지검색·증거목록·판례수집·홍보 탭
#              로직·UI·시그니처 무변경.
#            - 신규 메서드 _evid_·_label_ 접두로 네임스페이스 격리.

# v6.8.8 변경: 좀비 창 버그 수리 + fetch_list 말미 절단 복원
#            ─────────────────────────────────────────
#            [수리 내역]
#            - 한글판 v686 파일 말미 절단 복원
#              (fetch_list XML 진단 블록 + _clean_html_tags 누락 복구)
#            - _clean_html_tags 정적 메서드 CaseCrawler 클래스 내 정상 배치.
#            - if __name__ == '__main__' 단일 진입점 신설.
#            [무결성]
#            - 기능·로직·UI 변경 없음. 구조 복원만.
# v6.8.9 변경: 홍보탭 — 회전광고 프리뷰 제거 + KDP 출판 도서 섹션 신설
#            ─────────────────────────────────────────
#            [변경 내역]
#            - 회전 광고 20슬롯 프리뷰 위젯 제거.
#            - 연락처 블록 아래에 KDP 출판 도서 스크롤 섹션 신설.
#              (소년클로드·코웍입문서·코알못 3종, 언어별 링크 버튼)
#            [무결성]
#            - BRAND_CAPTIONS·_SESSION_BRAND_CAPTION 상수·PDF 워터마크 무변경.
#            - 기능·로직 변경 없음. UI 홍보탭만.
# v6.9.0 변경: 홍보탭 — 국내 유통 링크 추가 (부크크·YES24)
#            ─────────────────────────────────────────
#            [변경 내역]
#            - 코알못: 부크크(482300)·YES24(188657828) 버튼 추가.
#            - 코웍입문서: 부크크(483796) 버튼 추가.
#            - 동화(소년클로드): 심사 통과 후 추가 예정.
#            [무결성]
#            - 기능·로직·기존 링크 변경 없음. 버튼 2종 추가.
# v6.9.1 변경: 홍보탭 연락처 — 주소 제거
#            - Contact 블록 자택 주소 라인 삭제. 이메일·전화 유지.
# v6.9.3 변경: OC 인증키 파일 저장·자동 로드 비활성화
# v6.9.3 변경: OC 인증키 파일 저장·자동 로드 비활성화
# v7.25 변경: 용량분할 버튼 이모지(✂️) 제거 — 정렬 깨짐 수정
#   변경 항목:
#     - btn_split text "✂️ 용량분할" → "용량분할"
#   유지 항목:
#     - 나머지 버튼 이모지 무변경
# v7.24 변경: 액션 버튼(ab) anchor/justify center 적용 — 용량분할 등 정렬
#   변경 항목:
#     - ab 딕셔너리에 anchor/justify center 추가 (파일추가·일반병합·압축병합·용량분할·증거목록)
#   유지 항목:
#     - ob 딕셔너리 무변경
# v7.23 변경: 홍보탭 코웍 입문서 2권 부크크 한국어 링크 추가
#   변경 항목:
#     - 2권 카드 links에 부크크 KR (490829) 추가
#   유지 항목:
#     - 카드 순서·구조 무변경
# v7.22 변경: 홍보탭 코웍 입문서 2권 카드 추가
#   변경 항목:
#     - _books 리스트에 코웍 입문서 2권 카드 삽입 (EN/ES/DE/FR/PT)
#     - 1권 desc "※ 2 — 한국어판 출간 준비중" 문구 제거
#   유지 항목:
#     - 카드 순서: 입문서1 → 입문서2 → 코딩 → 동화
# v7.21 변경: 오토샷 소스 직접 통합 + 병합기 버튼 정렬 + 홍보탭 카드 순서
#   변경 항목:
#     - AutoShotPanel 클래스 LegalKit 소스 직접 임베드 (외부 EXE 런처 방식 폐기)
#     - _init_autoshot(): AutoShotPanel(parent) 직접 인스턴스화
#     - 병합기 버튼(ob) anchor/justify center 적용 — 글씨 가운데 정렬
#     - 홍보탭 _books 카드 순서: 입문서1 → 코딩 → 동화 (동화 맨 아래)
#     - _AS_ 접두어 네임스페이스 분리, AS.TNotebook 스타일 격리
#   유지 항목:
#     - 기존 8탭 구조 무변경
#     - COMMERCIAL_WHITELIST·라이선스 키 체계 무변경
# v7.11 변경: BRAND_CAPTIONS 광고 슬롯 재편 — 책·개발의뢰·후원·폐쇄망 슬롯 추가
#   변경 항목:
#     - "오프라인 단일 .exe 배포" 슬롯 삭제
#     - "부크크 '박병진' — AI협업 코딩 입문서·코웍입문서" 슬롯 추가
#     - "사무 자동화 개발의뢰 · 010-2272-7030" 슬롯 추가
#     - "개발 후원 · 카카오페이 010-2272-7030" 슬롯 추가
#     - "요청시 폐쇄망 시스템 개발 가능" 슬롯 추가
#     - 총 슬롯 20 → 23으로 확장
#   유지 항목:
#     - 기존 기능 소개 슬롯 전량 무변경
#     - 병합기·퍼지검색·증거목록·판례수집·홍보 탭 구조 무변경
# v7.0.9 변경: 병합 건수 제한 완전 해제 + 홍보탭 유료 문구 제거·개발 후원 카드 신설
#   변경 항목:
#     - FREE_LIMIT 상수 주석 처리, _lgk_check() 항상 True 반환 (건수 제한 완전 해제)
#     - _lgk_update_label() 항상 "✓ 개인 무제한 · 상업용 문의" 표시 (unlocked 고정)
#     - 홍보탭 라이선스 정책 카드 신설 (개인 무제한 허용 / 상업용 별도 문의)
#     - 홍보탭 도서 섹션 "라이센스 특전" 문구 제거
#     - 홍보탭 개발 후원 카드 신설 (카카오페이 010-2272-7030)
#   유지 항목:
#     - 병합기·퍼지검색·증거목록·판례수집·녹취록·홍보 탭 구조 무변경
#     - 라이선스 검증 코드 골격 유지 (향후 재활성화 가능)
# v6.9.2 변경: 병합기 패치 버튼 제거
#            - btn_patch 위젯 및 pack 목록에서 삭제. self_patch 메서드 잔류(내부 호출 보존).
import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext, simpledialog, messagebox
import os, sys, subprocess, threading, difflib
import datetime
import webbrowser
from io import BytesIO
import time as _time
import re as _re_mod
try:
    import winsound as _winsound
except ImportError:
    _winsound = None
try:
    import pyautogui as _pyautogui
    _AS_PYAUTOGUI_OK = True
except ImportError:
    _pyautogui = None
    _AS_PYAUTOGUI_OK = False
try:
    from PIL import ImageDraw, ImageFont
    _AS_PIL_DRAW_OK = True
except ImportError:
    _AS_PIL_DRAW_OK = False


# ──────────────────────────────────────────────────────────────
# 외부 라이브러리 자동 설치
# ──────────────────────────────────────────────────────────────
def check_engine():
    for pkg, imp in [('PyPDF2', 'PyPDF2'), ('Pillow', 'PIL'), ('tkinterdnd2', 'tkinterdnd2')]:
        try:
            __import__(imp)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

check_engine()

from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PIL import Image, ImageOps
from tkinterdnd2 import DND_FILES, TkinterDnD


# ──────────────────────────────────────────────────────────────
# 공통 유틸
# ──────────────────────────────────────────────────────────────
SUPPORTED_EXT = ['.pdf', '.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.webp', '.ico', '.jfif']
IMG_EXT       = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.webp', '.ico', '.jfif']


def beep_safe():
    try:
        import winsound; winsound.Beep(1000, 200)
    except Exception:
        pass


def open_folder_safe(path):
    try:
        if sys.platform == "win32":    os.startfile(path)
        elif sys.platform == "darwin": subprocess.Popen(["open", path])
        else:                          subprocess.Popen(["xdg-open", path])
    except Exception:
        pass


# ──────────────────────────────────────────────────────────────
# v600 증거목록 탭 전용 유틸 (구 증거목록기 v1.0 흡수)
# ──────────────────────────────────────────────────────────────
PREFIX_OPTIONS = ["증 제%d호", "갑 제%d호", "을 제%d호", "병 제%d호", "제%d호", "%d."]


def fmt_size(b):
    if b < 1024:            return f"{b} B"
    elif b < 1024**2:       return f"{b/1024:.1f} KB"
    elif b < 1024**3:       return f"{b/1024**2:.1f} MB"
    else:                   return f"{b/1024**3:.2f} GB"


def fmt_date(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")


# ──────────────────────────────────────────────────────────────
# 퍼지(오타 허용) 유사도 계산 — difflib 내장, 외부 라이브러리 불필요
# ──────────────────────────────────────────────────────────────
def fuzzy_score(query: str, target: str) -> float:
    """
    0.0 ~ 1.0 유사도 반환.
    ① 완전 포함이면 1.0
    ② 단어 단위 부분 포함이면 0.95
    ③ SequenceMatcher 비율
    ④ 짧은 쿼리는 부분 슬라이딩 비교로 보정
    """
    q, t = query.lower(), target.lower()
    if q in t:
        return 1.0
    words = t.replace("_", " ").replace("-", " ").split()
    for w in words:
        if q in w:
            return 0.95
    ratio = difflib.SequenceMatcher(None, q, t).ratio()
    if len(q) <= 4 and len(t) > len(q):
        best_sub = max(
            difflib.SequenceMatcher(None, q, t[i:i + len(q) + 2]).ratio()
            for i in range(max(1, len(t) - len(q) - 2))
        )
        ratio = max(ratio, best_sub)
    return ratio


# ──────────────────────────────────────────────────────────────
# v6.8.0 — 브랜드·광고·머신 핑거프린트 상수
# ──────────────────────────────────────────────────────────────
import hmac as _hmac
import hashlib as _hashlib
import random as _random
import platform as _platform
import socket as _socket
import uuid as _uuid

PRODUCT_NAME      = "법무킷"
PRODUCT_NAME_EN   = "ClickLegalKit"
PRODUCT_CODE      = "LGK"
BUILD_NUMBER      = "v7.47"
BUILD_DATE        = "20260422"

_HMAC_SECRET      = b"legalkit-FREE-v6.8-20260422"
_FREE_BUILD_SEED  = "legalkit-FREE-v6.8-20260422"


def _collect_machine_fp() -> str:
    """머신 핑거프린트 — 경량 5요소 (wmic 제외, GUI 블로킹 원천 차단).
    winreg MachineGuid + MAC + COMPUTERNAME + USERNAME + CPU ProcessorId.
    모든 단계 BaseException 가드. 총 수집 시간 < 50ms 목표.
    """
    parts = []
    # 1) MachineGuid (Windows) / hostid (POSIX)
    try:
        if sys.platform == "win32":
            try:
                import winreg
                try:
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                        r"SOFTWARE\Microsoft\Cryptography",
                                        0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as k:
                        parts.append(str(winreg.QueryValueEx(k, "MachineGuid")[0]))
                except BaseException:
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                        r"SOFTWARE\Microsoft\Cryptography") as k:
                        parts.append(str(winreg.QueryValueEx(k, "MachineGuid")[0]))
            except BaseException:
                parts.append("nm")
        else:
            parts.append(str(_uuid.getnode()))
    except BaseException:
        parts.append("nm")
    # 2) MAC
    try:
        parts.append(f"{_uuid.getnode():012x}")
    except BaseException:
        parts.append("nm")
    # 3) COMPUTERNAME
    try:
        parts.append(os.environ.get("COMPUTERNAME") or _socket.gethostname() or "nm")
    except BaseException:
        parts.append("nm")
    # 4) USERNAME
    try:
        parts.append(os.environ.get("USERNAME") or os.environ.get("USER") or "nm")
    except BaseException:
        parts.append("nm")
    # 5) CPU ProcessorId
    try:
        parts.append(_platform.processor() or "nm")
    except BaseException:
        parts.append("nm")
    return "|".join(parts)


# v6.8.0: 모듈 임포트 시점 동기 계산 — 5요소로 축소해 블로킹 제거.
# 외부 BaseException 가드로 어떤 예외가 발생해도 앱 기동은 보장.
try:
    _MACHINE_FP = _collect_machine_fp()
except BaseException:
    _MACHINE_FP = "fallback"

try:
    _MACHINE_HASH = _hmac.new(_HMAC_SECRET, _MACHINE_FP.encode("utf-8"),
                              _hashlib.sha256).hexdigest()[:8].upper()
except BaseException:
    _MACHINE_HASH = "00000000"

try:
    _BUILD_HASH = _hmac.new(_HMAC_SECRET, _FREE_BUILD_SEED.encode("utf-8"),
                            _hashlib.sha256).hexdigest()[:8].upper()
except BaseException:
    _BUILD_HASH = "00000000"

FREE_BUILD_ID = f"{PRODUCT_CODE}-FREE-v6.8-{_BUILD_HASH}-{_MACHINE_HASH}"
# 상업용 라이선스 화이트리스트 — 머신해시 등록 시 상업용 라이선스 자동 인정
# 등록 형식: "XXXXXXXX",  # 업체명 · 등록일
# v7.36: COMMERCIAL_WHITELIST 폐기 — 라이선스 파일 기반으로 전환
# 실제 값은 _lgk_load() 정의 이후 재설정됨
_IS_COMMERCIAL: bool = False  # 전방 선언 — 하단 라이선스 로드 후 결정

FIXED_CAPTION = (
    ""
    if _IS_COMMERCIAL else
    f"{PRODUCT_NAME} {BUILD_NUMBER} · 개인용 무료 · 상업적 이용 시 저작권법에 의해 처벌받을 수 있습니다 · C-2026-022058 · {FREE_BUILD_ID}"
)


# ════════════════════════════════════════════════════════════════════════
# 오토샷 통합 — 전용 상수 (_AS_ 접두, v7.11 직접 통합)
# autoshot_v3_19.py 소스 기반. LGK 네임스페이스와 격리.
# ════════════════════════════════════════════════════════════════════════
def _as_get_documents_dir():
    try:
        import winreg as _wr
        k = _wr.OpenKey(_wr.HKEY_CURRENT_USER,
                        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
        val, _ = _wr.QueryValueEx(k, "Personal")
        _wr.CloseKey(k)
        return val
    except Exception:
        return os.path.join(os.path.expanduser("~"), "Documents")

def _as_resolve_save_root():
    candidates = (r"D:\30_자동기록_스샷", r"C:\30_자동기록_스샷")
    for cand in candidates:
        try:
            if os.path.isdir(cand):
                return os.path.join(cand, "자동기록함")
        except Exception:
            continue
    return os.path.join(_as_get_documents_dir(), "자동기록함")

_AS_SAVE_ROOT         = _as_resolve_save_root()
_AS_DEFAULT_SAVE_DIR  = _AS_SAVE_ROOT
_AS_DEFAULT_PDF_DIR   = os.path.join(_AS_SAVE_ROOT, "PDF")
_AS_LOCK_TIMEOUT      = 5
_AS_LOG_MAX_LINES     = 300
_AS_DEFAULT_INTERVAL  = 30
_AS_BUILD_NUMBER      = "v3.19.0"
_AS_INSTANCE_NAME     = "AUTOSHOT"
_AS_CREATE_NO_WINDOW  = 0x08000000 if os.name == "nt" else 0
try:
    _AS_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "오토샷_config.json")
except Exception:
    _AS_CONFIG_PATH = "오토샷_config.json"
_AS_CAPTURE_INTERVAL_MIN  = 3
_AS_CAPTURE_INTERVAL_MAX  = 600
_AS_PDF_CYCLE_MIN         = 1
_AS_PDF_CYCLE_MAX         = 1440
_AS_PDF_CYCLE_DEFAULT     = 30
_AS_PDF_RESOLUTION        = 150.0
_AS_PDF_QUALITY           = 85
_AS_PDF_TARGET_SIZE       = (1920, 1920)
_AS_GIF_TARGET_SIZE       = (1280, 720)
_AS_GIF_DURATION_MS       = 500
_AS_GIF_LOOP              = 0
_AS_APNG_TARGET_SIZE      = (1920, 1920)
_AS_APNG_DURATION_MS      = 500
_AS_WEBP_TARGET_SIZE      = (1920, 1920)
_AS_WEBP_DURATION_MS      = 500
_AS_WEBP_QUALITY          = 85
_AS_MERGE_FORMATS         = ["pdf", "gif", "apng", "webp"]
_AS_MERGE_FORMAT_DEFAULT  = "pdf"
_AS_FLOAT_WIN_WIDTH       = 260
_AS_FLOAT_WIN_HEIGHT      = 310
_AS_FLOAT_WIN_OFFSET      = (50, 50)
_AS_FLOAT_WIN_TITLE_HEIGHT = 32
_AS_TESS_PATH             = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
_AS_CAPTION_TOP_HEIGHT    = 28
_AS_CAPTION_BOTTOM_HEIGHT = 28
_AS_CAPTION_BG_COLOR      = (0, 0, 0, 200)
_AS_CAPTION_FG_COLOR      = (255, 255, 255)
_AS_CAPTION_FONT_SIZE     = 18
_AS_CAPTION_FONT_PATHS    = [
    r"C:\Windows\Fonts\malgun.ttf",
    r"C:\Windows\Fonts\malgunbd.ttf",
    r"C:\Windows\Fonts\gulim.ttc",
    r"C:\Windows\Fonts\batang.ttc",
    r"C:\Windows\Fonts\NanumGothic.ttf",
]
# 오토샷 전용 머신 핑거프린트 (법무킷 _MACHINE_HASH 와 별개)
_AS_HMAC_SECRET = b"autoshot-free-forensic-2026"
_AS_FREE_BUILD_SEED = "autoshot-FREE-v3.15-20260422"
try:
    import hmac as _as_hmac, hashlib as _as_hl, uuid as _as_uuid
    _AS_FREE_BUILD_HASH = _as_hl.sha256(_AS_FREE_BUILD_SEED.encode()).hexdigest()[:4].upper()
    _as_parts = []
    try:
        import winreg as _as_wr2
        with _as_wr2.OpenKey(_as_wr2.HKEY_LOCAL_MACHINE,
                             r"SOFTWARE\Microsoft\Cryptography",
                             0, _as_wr2.KEY_READ | _as_wr2.KEY_WOW64_64KEY) as _k:
            _as_parts.append(str(_as_wr2.QueryValueEx(_k, "MachineGuid")[0]))
    except Exception:
        pass
    _as_parts.extend([str(_as_uuid.getnode()),
                      os.environ.get("COMPUTERNAME", ""),
                      os.environ.get("USERNAME", "")])
    _AS_MACHINE_FP_STR = "|".join(_as_parts) or "NO_FP"
    _AS_MACHINE_HASH_AS = _as_hmac.new(_AS_HMAC_SECRET,
                                        _AS_MACHINE_FP_STR.encode(),
                                        _as_hl.sha256).hexdigest()[:8].upper()
    _AS_FREE_BUILD_ID  = f"AUS-FREE-v3.19-{_AS_FREE_BUILD_HASH}-{_AS_MACHINE_HASH_AS}"
except Exception:
    _AS_FREE_BUILD_ID  = "AUS-FREE-v3.19-????-????????"
_AS_FIXED_CAPTION = f"AutoShot (autoshot) · {_AS_FREE_BUILD_ID}"
_AS_DEFAULT_CONFIG = {
    "save_dir":           _AS_DEFAULT_SAVE_DIR,
    "pdf_dir":            _AS_DEFAULT_PDF_DIR,
    "capture_interval":   _AS_DEFAULT_INTERVAL,
    "pdf_cycle_min":      _AS_PDF_CYCLE_DEFAULT,
    "beep_enabled":       True,
    "auto_delete_merged": False,
    "float_win_x":        50,
    "float_win_y":        50,
    "merge_format":       _AS_MERGE_FORMAT_DEFAULT,
    "gif_duration_ms":    _AS_GIF_DURATION_MS,
    "apng_duration_ms":   _AS_APNG_DURATION_MS,
    "webp_duration_ms":   _AS_WEBP_DURATION_MS,
}
try:
    from PyPDF2 import PdfMerger as _AS_PdfMerger
    _AS_PDF_AVAILABLE = True
except ImportError:
    _AS_PdfMerger = None
    _AS_PDF_AVAILABLE = False

# ──────────────────────────────────────────────────────────────
# v6.9.4 — 라이선스 보안 강화 (Ed25519 비대칭 서명 + license.json HMAC 봉인)
#   · 구버전 _LGK_SECRET 대칭키 노출 위협 무력화
#   · 시크릿이 EXE에서 추출되어도 위조 키 발급 불가 (개인키 본인 PC 단독 보유)
#   · license.json은 머신 종속 HMAC 봉인 — 다른 PC 복사 시 자동 무효
#   · 기존 함수 시그니처 무변경: _lgk_validate / _lgk_load / _lgk_save 동일 인터페이스
# ──────────────────────────────────────────────────────────────
import json as _json
import base64 as _base64
from pathlib import Path as _Path

_LGK_SECRET   = b"ddalkkak2026lgk"   # 구버전 호환용 (이관 시점만 참조)
FREE_LIMIT    = 5   # 병합 무료 횟수 (v7.0.9: 제한 해제 — 하단 _lgk_check 참조)

_LGK_DATA_DIR  : _Path = _Path(os.environ.get("APPDATA", "~")).expanduser() / "VibeToolsmith" / "LegalKit"
_LGK_LIC_FILE  : _Path = _LGK_DATA_DIR / "license.json"

# Ed25519 공개키 (raw 32바이트 base64). 개인키는 본인 PC 단독 보유.
_LGK_PUBKEY_B64 = "zrW7lXGJ97F1OdXeyeM8Qi1NcWyxuCd7PIcKkURYxoo="
# ──────────────────────────────────────────────────────────────
# v7.0.0 — 녹취록 (Transcript) — Whisper 기반 음성→텍스트
#   ClickTalkScript v1.67 핵심 흡수. _ts_* 접두사로 격리.
#   라이선스: 법무킷 통합 카운터 사용 (병합·녹취 합산 5회).
# ──────────────────────────────────────────────────────────────
# ── PyInstaller --windowed 빌드 stdout/stderr None 가드 ──
if sys.stdout is None:
    import io as _io
    sys.stdout = _io.StringIO()
if sys.stderr is None:
    import io as _io
    sys.stderr = _io.StringIO()


_TS_AUDIO_EXT = {".m4a",".mp3",".wav",".ogg",".flac",".mp4",".mkv",".mov",".avi",".aac",".wma"}
_TS_FIXED_MODEL = "small"
_TS_OUT_FMTS = ["txt","srt","vtt","tsv","json"]
_TS_NO_WIN = 0x08000000 if sys.platform == "win32" else 0


def _ts_get_ffmpeg() -> str:
    try:
        import imageio_ffmpeg as _iio
        return _iio.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"


def _ts_register_cuda_path() -> str:
    """CUDA Toolkit bin 폴더를 PATH에 자동 등록. cublas/cudnn DLL 로드 보장.
    NVIDIA GPU Computing Toolkit\\CUDA\\v* 디렉토리를 자동 탐색.
    """
    import glob as _glob
    if sys.platform != "win32":
        return ""
    candidates = []
    # 표준 설치 경로
    for base in (r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA",
                 r"C:\Program Files (x86)\NVIDIA GPU Computing Toolkit\CUDA"):
        candidates.extend(_glob.glob(os.path.join(base, "v*", "bin")))
    # ctranslate2 패키지 자체 동봉 .dll 폴더
    try:
        import ctranslate2 as _ct2
        ct2_dir = os.path.dirname(_ct2.__file__)
        candidates.append(ct2_dir)
    except Exception:
        pass
    # v7.0.6 — PyTorch wheel 동봉 cuBLAS/cuDNN DLL 폴더
    try:
        import torch as _torch
        torch_lib = os.path.join(os.path.dirname(_torch.__file__), "lib")
        if os.path.isdir(torch_lib):
            candidates.append(torch_lib)
    except Exception:
        pass
    # PyInstaller _MEI 임시 폴더 안의 torch/lib (frozen 빌드)
    if hasattr(sys, "_MEIPASS"):
        meipass_torch_lib = os.path.join(sys._MEIPASS, "torch", "lib")
        if os.path.isdir(meipass_torch_lib):
            candidates.append(meipass_torch_lib)
        # v7.0.7 — _MEIPASS 루트 (NVIDIA cuBLAS/cuDNN DLL이 --add-binary로 직접 동봉됨)
        candidates.append(sys._MEIPASS)
    # 등록
    added = []
    for p in candidates:
        if os.path.isdir(p):
            try:
                os.add_dll_directory(p)
                added.append(p)
            except Exception:
                pass
            os.environ["PATH"] = p + os.pathsep + os.environ.get("PATH", "")
    return ";".join(added) if added else ""


_TS_CUDA_PATHS = _ts_register_cuda_path()


_TS_FFMPEG_BIN = _ts_get_ffmpeg()




def _lgk_machine_id() -> str:
    """기존 _MACHINE_FP 재사용 — XXXX-XXXX-XXXX-XXXX 형식."""
    h = _hashlib.sha256(_MACHINE_FP.encode("utf-8")).hexdigest().upper()
    return f"{h[0:4]}-{h[4:8]}-{h[8:12]}-{h[12:16]}"


def _lgk_bind_secret() -> bytes:
    """license.json 봉인용 머신 종속 비밀 — 타 PC 복사 시 검증 실패 유도."""
    return _hmac.new(b"lgk-bind-2026", _MACHINE_FP.encode("utf-8"),
                     _hashlib.sha256).digest()


def _lgk_load() -> dict:
    """HMAC 봉인 검증 후 페이로드 반환. 위조·복사·구포맷 모두 0회 리셋."""
    try:
        _LGK_DATA_DIR.mkdir(parents=True, exist_ok=True)
        if _LGK_LIC_FILE.exists():
            raw = _json.loads(_LGK_LIC_FILE.read_text(encoding="utf-8"))
            payload = {"count": int(raw.get("count", 0)),
                       "unlocked": bool(raw.get("unlocked", False)),
                       "commercial": bool(raw.get("commercial", False)),
                       "expiry": str(raw.get("expiry", "00000000"))}
            sig_b64 = raw.get("sig", "")
            if not sig_b64:
                return {"count": 0, "unlocked": False, "commercial": False, "expiry": "00000000"}
            sig = _base64.b64decode(sig_b64.encode("ascii"))
            msg = _json.dumps(payload, sort_keys=True).encode("utf-8")
            expect = _hmac.new(_lgk_bind_secret(), msg, _hashlib.sha256).digest()
            if _hmac.compare_digest(sig, expect):
                return payload
    except Exception:
        pass
    return {"count": 0, "unlocked": False, "commercial": False, "expiry": "00000000"}


def _lgk_save(data: dict) -> None:
    """페이로드에 머신 종속 HMAC 서명 첨부 후 저장."""
    try:
        _LGK_DATA_DIR.mkdir(parents=True, exist_ok=True)
        payload = {"count": int(data.get("count", 0)),
                   "unlocked": bool(data.get("unlocked", False)),
                   "commercial": bool(data.get("commercial", False)),
                   "expiry": str(data.get("expiry", "00000000"))}
        msg = _json.dumps(payload, sort_keys=True).encode("utf-8")
        sig = _hmac.new(_lgk_bind_secret(), msg, _hashlib.sha256).digest()
        out = dict(payload)
        out["sig"] = _base64.b64encode(sig).decode("ascii")
        _LGK_LIC_FILE.write_text(_json.dumps(out), encoding="utf-8")
    except Exception:
        pass


def _lgk_validate(key: str, mid: str):
    """Ed25519 서명 검증. v7.46: 만료일 지원.
    key: base64(72바이트) = 64바이트 서명 + 8바이트 만료일(YYYYMMDD 또는 00000000=영구).
         하위호환: 64바이트 키(구버전 영구 라이선스)도 허용.
    반환: 만료일 문자열('YYYYMMDD' 또는 '00000000') — 유효. None — 유효하지 않음.
    """
    try:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    except Exception:
        return None
    try:
        clean = "".join(ch for ch in key.strip() if not ch.isspace() and ch != "-")
        raw = None
        for dec in (_base64.urlsafe_b64decode, _base64.b64decode):
            try:
                pad = "=" * (-len(clean) % 4)
                cand = dec(clean + pad)
                if len(cand) in (64, 72):
                    raw = cand; break
            except Exception:
                continue
        if raw is None:
            return None
        if len(raw) == 64:          # 구버전 영구 키 (하위호환)
            sig, expiry_str = raw, "00000000"
            message = mid.encode("utf-8")
        else:                       # 신버전: sig(64) + expiry(8)
            sig, expiry_bytes = raw[:64], raw[64:]
            expiry_str = expiry_bytes.decode("ascii")
            message = f"{mid}|{expiry_str}".encode("utf-8")
        pub = Ed25519PublicKey.from_public_bytes(_base64.b64decode(_LGK_PUBKEY_B64))
        pub.verify(sig, message)
        return expiry_str
    except Exception:
        return None

# v7.46: 라이선스 파일 기반 상업용 여부 확정 (만료일 체크 포함)
def _lgk_is_commercial() -> bool:
    """상업용 라이선스 유효 여부 — commercial 플래그 + 만료일 동시 체크."""
    try:
        data = _lgk_load()
        if not data.get("commercial"):
            return False
        expiry = data.get("expiry", "00000000")
        if expiry == "00000000":
            return True  # 영구 라이선스
        import datetime as _dt
        return _dt.date.today().strftime("%Y%m%d") <= expiry
    except Exception:
        return False

_IS_COMMERCIAL = _lgk_is_commercial()

# 캡션 띠 사양
CAPTION_TOP_H    = 28   # 상단 띠 높이(px)
CAPTION_BOT_H    = 24   # 하단 띠 높이(px)
CAPTION_TOP_BG   = (245, 245, 240)
CAPTION_BOT_BG   = (250, 250, 245)
CAPTION_TEXT_FG  = (60, 60, 60)
CAPTION_FOOTER_FG = (95, 95, 95)

_CAPTION_FONT_PATHS = [
    "C:/Windows/Fonts/malgun.ttf",
    "C:/Windows/Fonts/gulim.ttc",
    "C:/Windows/Fonts/batang.ttc",
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

# 법무킷 전용 20슬롯 회전 광고 (호증병합 8 + 갑호증목록 3 + 판례수집 3 + 증거목록 2 + 퍼지검색 2 + 안내 2)
BRAND_CAPTIONS = [
    # 차별화
    "폐쇄망 원칙 — 외부 통신 없음",
    "요청시 폐쇄망 시스템 개발 가능",
    # 책 광고
    "Amazon.fr 프랑스에서 팔린 AI 협업 도서 — 코웍입문서",
    "프랑스·브라질·독일 독자가 먼저 알아본 책",
    "부크크 '클로드AI 코웍모드 입문서' — 박병진",
    "부크크 '코드를 모르는 사람의 코딩' — 박병진",
    # 개발의뢰·후원·광고주
    "사무 자동화 개발의뢰 · 010-2272-7030",
    "개발 후원 · 카카오페이 010-2272-7030",
    "AI협업 특화 법무 도구 — 법무킷 평생 광고주 모집 중",
    "엔젤 광고주로 이름 남기세요 · 010-2272-7030",
    "초창기 후원 = 평생 노출 — 지금이 가장 쌉니다",
    "1인 개발자의 뚝심 — 법무킷은 계속됩니다",
    "척추 붙잡고 만든 프로그램 — 후원이 힘이 됩니다",
    # 상업용 전환 안내
    "상업용 라이선스 전환 시 모든 광고 구문이 제거됩니다 · 010-2272-7030",
]


def _pick_brand_caption() -> str:
    return _random.choice(BRAND_CAPTIONS)


# 세션 회전 광고 (실행 1회 결정 — 단일 PDF 출력 일관성)
_SESSION_BRAND_CAPTION = "" if _IS_COMMERCIAL else _pick_brand_caption()


# ──────────────────────────────────────────────────────────────
# 메인 앱 — ttk.Notebook 5탭 구조 (병합기 + 퍼지검색 + 증거목록 + 판례수집 + 홍보)
# ──────────────────────────────────────────────────────────────
class SentinelHyperV530:
    def __init__(self, root):
        self.root = root
        self.root.title(f"법무킷 {BUILD_NUMBER}  ·  병합기 + 퍼지검색 + 증거목록 + 판례수집 + 홍보 + 라이선스")
        self.root.geometry("540x680")
        self.root.minsize(460, 560)
        self.root.resizable(True, True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#0a0a0a")

        # DnD 등록
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self._handle_drop)

        # ── 공통 헤더 ──
        tk.Label(self.root,
                 text=f"ClickLegalKit {BUILD_NUMBER}  ·  MERGE + FUZZY SEARCH + EVIDENCE LIST + CASE COLLECTOR + PROMO",
                 fg="#aaaaaa", bg="#111",
                 font=("Consolas", 8, "bold"), pady=4
                 ).pack(fill=tk.X)

        # ── Notebook ──
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook",        background="#0a0a0a", borderwidth=0)
        style.configure("TNotebook.Tab",    background="#1a1a1a", foreground="#888",
                                            font=("맑은 고딕", 8, "bold"), padding=[6, 4])
        style.map("TNotebook.Tab",
                  background=[("selected", "#2a5298")],
                  foreground=[("selected", "#ffffff")])

        self.nb = ttk.Notebook(self.root)
        self.nb.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

        # 탭 프레임
        self.merge_tab    = tk.Frame(self.nb, bg="#0a0a0a")
        self.find_tab     = tk.Frame(self.nb, bg="#f8f9fa")
        self.evidence_tab = tk.Frame(self.nb, bg="#0a0a0a")  # v600 신규
        self.case_tab     = tk.Frame(self.nb, bg="#0a0a0a")  # v600 신규 (판례수집)
        self.label_tab    = tk.Frame(self.nb, bg="#0a0a0a")  # v6.8.3 신규 (호증부여기)
        self.transcript_tab = tk.Frame(self.nb, bg="#0a0a0a")  # v7.0.0 신규 (녹취록)
        self.promo_tab    = tk.Frame(self.nb, bg="#0a0a0a")  # v6.8.0 신규 (홍보)
        self.autoshot_tab = tk.Frame(self.nb, bg="#0a0a0a")  # v7.11 신규 (오토샷)
        self.license_tab  = tk.Frame(self.nb, bg="#0a0a0a")  # v7.36 신규 (라이선스)
        self.nb.add(self.merge_tab,    text="병합기")
        self.nb.add(self.find_tab,     text="퍼지검색")
        self.nb.add(self.evidence_tab, text="증거목록")
        self.nb.add(self.case_tab,     text="판례수집")  # v600 신규
        self.nb.add(self.label_tab,    text="호증부여기")  # v6.8.3 신규
        self.nb.add(self.transcript_tab, text="녹취록")     # v7.0.0 신규
        self.nb.add(self.promo_tab,    text="홍보")     # v6.8.0 신규
        self.nb.add(self.autoshot_tab, text="오토샷")   # v7.11 신규
        self.nb.add(self.license_tab,  text="라이선스")  # v7.36 신규

        # v6.8.5 — 병합기 라이선스 초기화
        self._mid = _lgk_machine_id()
        _d = _lgk_load()
        self._lgk_unlocked = _d.get("unlocked", False)
        self._lgk_var = tk.StringVar()
        self._lgk_update_label(_d.get("count", 0), self._lgk_unlocked)

        # 각 탭 초기화
        self._init_merger(self.merge_tab)
        self._init_finder(self.find_tab)
        self._init_evidence(self.evidence_tab)
        self._init_case(self.case_tab)    # v600 신규
        self._init_evid_label(self.label_tab)  # v6.8.3 신규
        self._init_transcript(self.transcript_tab)  # v7.0.0 신규
        self._init_promo(self.promo_tab)  # v6.8.0 신규
        self._init_autoshot(self.autoshot_tab)  # v7.11 신규
        self._init_license_tab(self.license_tab)   # v7.36 신규


    # ══════════════════════════════════════════════════════════
    # v7.36 — 라이선스 탭
    # ══════════════════════════════════════════════════════════
    def _init_license_tab(self, parent: tk.Frame) -> None:
        """라이선스 등록·해제·상태 표시 탭."""
        bg       = "#0a0a0a"
        fg_title = "#f9e2af"
        fg_sub   = "#aaaaaa"
        fg_ok    = "#a6e3a1"
        fg_warn  = "#f38ba8"
        fg_blue  = "#79b8ff"

        # ── 상태 패널 ──
        s_frame = tk.Frame(parent, bg="#111111", pady=12)
        s_frame.pack(fill=tk.X, padx=16, pady=(16, 8))
        tk.Label(s_frame, text="현재 라이선스 상태",
                 fg=fg_sub, bg="#111111", font=("맑은 고딕", 8)).pack()
        def _lic_status_info():
            import datetime as _dt
            data = _lgk_load()
            if not data.get("commercial"):
                return "⚠ 미등록 (개인용 무료)", fg_warn
            expiry = data.get("expiry", "00000000")
            if expiry == "00000000":
                return "✓ 상업용 등록됨 (영구)", fg_ok
            exp_fmt = f"{expiry[:4]}-{expiry[4:6]}-{expiry[6:8]}"
            if _dt.date.today().strftime("%Y%m%d") <= expiry:
                return f"✓ 상업용 등록됨 (만료: {exp_fmt})", fg_ok
            return f"⚠ 라이선스 만료됨 ({exp_fmt})", fg_warn
        _status_text, _status_color = _lic_status_info()
        self._lic_status_var = tk.StringVar(value=_status_text)
        self._lic_status_lbl = tk.Label(
            s_frame, textvariable=self._lic_status_var,
            fg=_status_color, bg="#111111", font=("맑은 고딕", 11, "bold"))
        self._lic_status_lbl.pack()

        # ── 머신 ID ──
        mid_frame = tk.Frame(parent, bg=bg)
        mid_frame.pack(fill=tk.X, padx=16, pady=(8, 0))
        tk.Label(mid_frame, text="머신 ID  (구매 시 개발자에게 전달):",
                 fg=fg_sub, bg=bg, font=("맑은 고딕", 8)).pack(anchor="w")
        mid_row = tk.Frame(mid_frame, bg=bg)
        mid_row.pack(anchor="w")
        self._lic_mid_var = tk.StringVar(value=self._mid)
        tk.Entry(mid_row, textvariable=self._lic_mid_var, width=24,
                 state="readonly", bg="#1a1a1a", fg=fg_blue,
                 font=("Consolas", 10), readonlybackground="#1a1a1a",
                 relief="flat").pack(side=tk.LEFT, padx=(0, 6))
        tk.Button(mid_row, text="복사",
                  command=lambda: (parent.clipboard_clear(),
                                   parent.clipboard_append(self._mid)),
                  bg="#2a5298", fg="white", font=("맑은 고딕", 8),
                  relief="flat", padx=6, pady=2).pack(side=tk.LEFT)

        # ── 구분선 ──
        tk.Frame(parent, bg="#2a2a2a", height=1).pack(fill=tk.X, padx=16, pady=12)

        # ── 키 입력 ──
        tk.Label(parent, text="라이선스 키 등록",
                 fg=fg_title, bg=bg, font=("맑은 고딕", 9, "bold")).pack(anchor="w", padx=16)
        tk.Label(parent, text="구매 후 발급받은 키를 입력하세요.",
                 fg=fg_sub, bg=bg, font=("맑은 고딕", 8)).pack(anchor="w", padx=16, pady=(2, 4))

        self._lic_key_var = tk.StringVar()
        tk.Entry(parent, textvariable=self._lic_key_var, width=52,
                 bg="#1a1a1a", fg="#e0e0e0", insertbackground="#e0e0e0",
                 font=("Consolas", 9), relief="flat").pack(padx=16, fill=tk.X, pady=(0, 6))

        btn_row = tk.Frame(parent, bg=bg)
        btn_row.pack(anchor="w", padx=16)

        def _do_activate():
            import datetime as _dt
            key = self._lic_key_var.get().strip()
            _exp = _lgk_validate(key, self._mid)
            if _exp is not None:
                global _IS_COMMERCIAL
                d = _lgk_load()
                d["unlocked"]   = True
                d["commercial"] = True
                d["expiry"]     = _exp
                _lgk_save(d)
                _IS_COMMERCIAL = True
                if _exp == "00000000":
                    _st = "✓ 상업용 등록됨 (영구)"
                else:
                    _ef = f"{_exp[:4]}-{_exp[4:6]}-{_exp[6:8]}"
                    _st = f"✓ 상업용 등록됨 (만료: {_ef})"
                self._lic_status_var.set(_st)
                self._lic_status_lbl.config(fg=fg_ok)
                messagebox.showinfo("인증 완료",
                    f"상업용 라이선스 등록 완료!\n{_st}")
            else:
                messagebox.showerror("인증 실패",
                    "키가 올바르지 않습니다.\n"
                    "머신 ID를 개발자에게 전달하세요.\n"
                    "이메일: dede5003@gmail.com")

        def _do_deactivate():
            if messagebox.askyesno("라이선스 해제", "정말 라이선스를 해제하시겠습니까?"):
                global _IS_COMMERCIAL
                d = _lgk_load()
                d["commercial"] = False
                _lgk_save(d)
                _IS_COMMERCIAL = False
                self._lic_status_var.set("⚠ 미등록 (개인용 무료)")
                self._lic_status_lbl.config(fg=fg_warn)

        tk.Button(btn_row, text="등록", command=_do_activate,
                  bg="#2980b9", fg="white", font=("맑은 고딕", 9, "bold"),
                  relief="flat", padx=12, pady=3).pack(side=tk.LEFT, padx=(0, 6))
        tk.Button(btn_row, text="해제", command=_do_deactivate,
                  bg="#444444", fg="#aaaaaa", font=("맑은 고딕", 8),
                  relief="flat", padx=8, pady=3).pack(side=tk.LEFT)

        # ── 구분선 ──
        tk.Frame(parent, bg="#2a2a2a", height=1).pack(fill=tk.X, padx=16, pady=12)

        # ── 문의 ──
        tk.Label(parent, text="구매 문의",
                 fg=fg_title, bg=bg, font=("맑은 고딕", 9, "bold")).pack(anchor="w", padx=16)
        tk.Label(parent,
                 text="이메일 : dede5003@gmail.com\n"
                      "전화 : 010-2272-7030\n"
                      "블로그 : blog.naver.com/bc5103\n"
                      "저작권 : C-2026-022058",
                 fg=fg_sub, bg=bg, font=("맑은 고딕", 8), justify="left"
                 ).pack(anchor="w", padx=16, pady=(4, 0))

    # ══════════════════════════════════════════════════════════
    # v6.8.0 — 광고 매립 헬퍼 (이미지 캡션 띠 + PDF 푸터 워터마크)
    # ══════════════════════════════════════════════════════════
    def _ad_get_font(self, size: int = 12):
        """캡션용 폰트 핸들 — Pillow ImageFont. 폴백 default."""
        try:
            from PIL import ImageFont
            for fp in _CAPTION_FONT_PATHS:
                if os.path.exists(fp):
                    try:
                        return ImageFont.truetype(fp, size)
                    except Exception:
                        continue
            return ImageFont.load_default()
        except Exception:
            return None

    def _ad_overlay_image(self, pil_img):
        """이미지 PIL 객체에 상단(시각·일련·도구) + 하단(고정·회전 광고) 띠 합성.
        반환: 새 PIL.Image (RGB). 원본 변형 없음.
        """
        try:
            from PIL import Image as _PI, ImageDraw
            base = pil_img.convert("RGB")
            w, h = base.size
            new_h = h + CAPTION_TOP_H + CAPTION_BOT_H
            canvas_img = _PI.new("RGB", (w, new_h), (255, 255, 255))
            # 상단 띠
            top = _PI.new("RGB", (w, CAPTION_TOP_H), CAPTION_TOP_BG)
            # 하단 띠
            bot = _PI.new("RGB", (w, CAPTION_BOT_H), CAPTION_BOT_BG)
            canvas_img.paste(top, (0, 0))
            canvas_img.paste(base, (0, CAPTION_TOP_H))
            canvas_img.paste(bot, (0, CAPTION_TOP_H + h))

            draw = ImageDraw.Draw(canvas_img)
            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            top_text = f"{ts}  ·  {PRODUCT_NAME} {BUILD_NUMBER}  ·  {FREE_BUILD_ID}"
            bot_text = f"{FIXED_CAPTION}  —  {_SESSION_BRAND_CAPTION}"
            font_top = self._ad_get_font(size=max(10, CAPTION_TOP_H - 14))
            font_bot = self._ad_get_font(size=max(10, CAPTION_BOT_H - 12))
            try:
                draw.text((10, 6), top_text, fill=CAPTION_TEXT_FG, font=font_top)
                draw.text((10, CAPTION_TOP_H + h + 4), bot_text,
                          fill=CAPTION_FOOTER_FG, font=font_bot)
            except Exception:
                draw.text((10, 6), top_text, fill=CAPTION_TEXT_FG)
                draw.text((10, CAPTION_TOP_H + h + 4), bot_text, fill=CAPTION_FOOTER_FG)
            return canvas_img
        except Exception:
            # 합성 실패 시 원본 그대로 반환 (병합 흐름 보호)
            return pil_img

    def _ad_overlay_pdf_footer(self, src_pdf_path: str, dst_pdf_path: str):
        """병합 직후 PDF 전 페이지 하단 푸터 1줄 워터마크 오버레이.
        실패 시 원본을 그대로 dst에 복사.
        """
        try:
            try:
                import reportlab
            except ImportError:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
            from reportlab.pdfgen import canvas as _rcanvas
            from reportlab.pdfbase import pdfmetrics as _pmet
            from reportlab.pdfbase.ttfonts import TTFont as _TTF

            font_name = "Helvetica"
            for fp in _CAPTION_FONT_PATHS:
                if os.path.exists(fp):
                    try:
                        _pmet.registerFont(_TTF("KorFootFont", fp))
                        font_name = "KorFootFont"
                        break
                    except Exception:
                        continue

            reader = PdfReader(src_pdf_path)
            writer = PdfWriter()
            footer_text = f"{FIXED_CAPTION}  —  {_SESSION_BRAND_CAPTION}"

            for page in reader.pages:
                try:
                    pw = float(page.mediabox.width)
                    ph = float(page.mediabox.height)
                except Exception:
                    pw, ph = 595.0, 842.0  # A4 fallback (pt)
                buf = BytesIO()
                c = _rcanvas.Canvas(buf, pagesize=(pw, ph))
                c.setFillColorRGB(0.37, 0.37, 0.37)
                c.setFont(font_name, 7.5)
                # 하단 좌측에서 시작
                c.drawString(20, 12, footer_text)
                c.save()
                buf.seek(0)
                overlay = PdfReader(buf).pages[0]
                try:
                    page.merge_page(overlay)
                except Exception:
                    pass
                writer.add_page(page)

            with open(dst_pdf_path, "wb") as f:
                writer.write(f)
            return True
        except Exception:
            # 실패 시 src→dst 복사로 안전 폴백
            try:
                if src_pdf_path != dst_pdf_path:
                    import shutil as _shutil
                    _shutil.copyfile(src_pdf_path, dst_pdf_path)
            except Exception:
                pass
            return False

    # ══════════════════════════════════════════════════════════
    # ① 병합기 탭
    # ══════════════════════════════════════════════════════════
    def _init_merger(self, parent):
        self._busy       = False
        self._split_mb   = 19.5
        self._file_paths = []

        # ── 파일 리스트 영역 ──
        list_frame = tk.Frame(parent, bg="#0a0a0a")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=(6, 0))

        scrollbar = tk.Scrollbar(list_frame, bg="#222", troughcolor="#111",
                                 activebackground="#444", relief="flat", width=10)
        self.listbox = tk.Listbox(
            list_frame,
            bg="#0d0d0d", fg="#e0e0e0",
            selectbackground="#2a5298", selectforeground="#ffffff",
            font=("Consolas", 9),
            borderwidth=0, highlightthickness=1, highlightcolor="#2a5298",
            activestyle="none",
            yscrollcommand=scrollbar.set,
            selectmode=tk.EXTENDED,
        )
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.listbox.bind("<Delete>",          lambda e: self.remove_selected())
        self.listbox.bind("<Double-Button-1>", self._open_selected_folder)
        self.listbox.bind("<ButtonPress-1>",   self._drag_start)
        self.listbox.bind("<B1-Motion>",       self._drag_motion)
        self.listbox.bind("<ButtonRelease-1>", self._drag_release)
        self._drag_src = None

        # ── 순서 조정 버튼 ──
        order_f = tk.Frame(parent, bg="#0a0a0a")
        order_f.pack(fill=tk.X, padx=8, pady=3)
        ob = {"font": ("맑은 고딕", 8, "bold"), "relief": "flat", "bd": 0, "padx": 6, "pady": 3, "anchor": "center", "justify": "center"}
        tk.Button(order_f, text="▲ 위로",    command=self.move_up,         bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_f, text="▼ 아래로",   command=self.move_down,       bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_f, text="⤒ 맨위",    command=self.move_top,        bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_f, text="⤓ 맨아래",   command=self.move_bottom,     bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_f, text="✕ 제거",    command=self.remove_selected, bg="#3a1a1a", fg="#ff7b7b", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_f, text="🗑 전체삭제", command=self.clear_list,      bg="#3a1a1a", fg="#ff7b7b", **ob).pack(side=tk.LEFT, padx=2)
        self.lbl_count = tk.Label(order_f, text="0 files", fg="#555", bg="#0a0a0a", font=("Consolas", 8))
        self.lbl_count.pack(side=tk.RIGHT, padx=4)

        # ── 액션 버튼 ──
        ctrl = tk.Frame(parent, bg="#0a0a0a")
        ctrl.pack(pady=5)
        ab = {"font": ("맑은 고딕", 8, "bold"), "height": 1, "relief": "flat", "anchor": "center", "justify": "center"}
        self.btn_add   = tk.Button(ctrl, text="📂 파일추가",  command=self.add_files,                    width=8, bg="#1b4332", fg="#52b788", **ab)
        self.btn_merge = tk.Button(ctrl, text="📁 일반병합",  command=lambda: self.run_merger(False),    width=8, bg="#2980b9", fg="white",   **ab)
        self.btn_comp  = tk.Button(ctrl, text="⚡ 압축병합",  command=lambda: self.run_merger(True),     width=8, bg="#c0392b", fg="white",   **ab)
        self.btn_split = tk.Button(ctrl, text="용량분할",  command=self.run_splitter,                 width=8, bg="#d35400", fg="white",   **ab)
        self.btn_evlist = tk.Button(ctrl, text="증거목록",  command=self.export_evidence_list,         width=8, bg="#1a4a3a", fg="#52b788", **ab)
        for btn in (self.btn_add, self.btn_merge, self.btn_comp, self.btn_split, self.btn_evlist):
            btn.pack(side=tk.LEFT, padx=2)

        # ── v6.8.5 라이선스 상태 표시 ──
        lic_f = tk.Frame(parent, bg="#0a0a0a")
        lic_f.pack(fill=tk.X, padx=8, pady=(1, 0))
        tk.Label(lic_f, textvariable=self._lgk_var, fg="#f9e2af", bg="#0a0a0a",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        tk.Button(lic_f, text="🔑 키 입력", command=self._lgk_show_dialog,
                  bg="#1a1a1a", fg="#aaa", font=("Consolas", 8), relief="flat",
                  padx=4, pady=1).pack(side=tk.RIGHT)

        # ── 분할 용량 설정 ──
        split_f = tk.Frame(parent, bg="#0a0a0a")
        split_f.pack(fill=tk.X, padx=8, pady=(0, 2))
        tk.Label(split_f, text="분할 기준 용량 (MB):", fg="#666", bg="#0a0a0a", font=("Consolas", 8)).pack(side=tk.LEFT)
        self.split_entry = tk.Entry(split_f, width=6, bg="#1a1a1a", fg="#e0e0e0",
                                    insertbackground="#e0e0e0", font=("Consolas", 9),
                                    relief="flat", highlightthickness=1,
                                    highlightcolor="#2a5298", highlightbackground="#333")
        self.split_entry.insert(0, "19.5")
        self.split_entry.pack(side=tk.LEFT, padx=4)
        tk.Button(split_f, text="적용", command=self._apply_split_mb,
                  bg="#2a2a2a", fg="#aaa", font=("Consolas", 8), relief="flat", padx=4, pady=1).pack(side=tk.LEFT)
        self.lbl_split_mb = tk.Label(split_f, text=f"현재: {self._split_mb}MB", fg="#4a9", bg="#0a0a0a", font=("Consolas", 8))
        self.lbl_split_mb.pack(side=tk.LEFT, padx=6)

        # ── 진행률 바 ──
        prog_f = tk.Frame(parent, bg="#0a0a0a")
        prog_f.pack(fill=tk.X, padx=8)
        self.canvas_bar = tk.Canvas(prog_f, height=4, bg="#111", highlightthickness=0)
        self.canvas_bar.pack(fill=tk.X)
        self._bar_rect = None

        # ── 병합기 로그 ──
        log_hdr = tk.Frame(parent, bg="#0a0a0a")
        log_hdr.pack(fill=tk.X, padx=8, pady=(4, 0))
        tk.Label(log_hdr, text="LOG", fg="#444", bg="#0a0a0a", font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        tk.Button(log_hdr, text="지우기", command=self._clear_merge_log,
                  bg="#1a1a1a", fg="#666", font=("Consolas", 8), relief="flat", padx=4, pady=0).pack(side=tk.RIGHT)
        self.log_board = scrolledtext.ScrolledText(
            parent, width=60, height=6, bg="#060606", fg="#33ff33",
            font=("Consolas", 8), borderwidth=0, highlightthickness=0)
        self.log_board.pack(pady=(2, 6), padx=8, fill=tk.X)
        self.merge_log("v531 READY.  드래그하거나 [파일추가]로 파일을 올려주세요.")
        self.merge_log("TIP: Del=선택삭제  /  더블클릭=해당 폴더 열기")

    # ══════════════════════════════════════════════════════════
    # ② 퍼지검색 탭
    # ══════════════════════════════════════════════════════════
    def _init_finder(self, parent):
        self._search_root = os.path.join(os.path.expanduser("~"), "Documents")
        self._find_results  = []
        self._searching     = False

        # ── 찾기 헤더 ──
        find_hdr = tk.Frame(parent, bg="#1a73e8", height=32)
        find_hdr.pack(fill=tk.X)
        tk.Label(find_hdr, text="FUZZY_v3.4  ·  퍼지검색  (오타 허용 검색)",
                 fg="white", bg="#1a73e8", font=("Malgun Gothic", 10, "bold")
                 ).pack(side=tk.LEFT, padx=10, pady=4)

        # ── 검색창 ──
        search_f = tk.Frame(parent, bg="#f8f9fa")
        search_f.pack(fill=tk.X, padx=10, pady=(8, 2))
        self.find_entry = tk.Entry(search_f, width=30, font=("Malgun Gothic", 11),
                                   borderwidth=1, relief="solid")
        self.find_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        self.find_entry.bind("<Return>", lambda e: self._start_search())
        self.btn_find = tk.Button(search_f, text="🔍 찾기",
                                   command=self._start_search,
                                   bg="#1a73e8", fg="white",
                                   font=("Malgun Gothic", 10, "bold"),
                                   relief="flat", padx=8)
        self.btn_find.pack(side=tk.LEFT)

        # ── 유사도 슬라이더 ──
        slider_f = tk.Frame(parent, bg="#f8f9fa")
        slider_f.pack(fill=tk.X, padx=10, pady=2)
        tk.Label(slider_f, text="유사도 허용 임계값:",
                 bg="#f8f9fa", font=("Malgun Gothic", 9), fg="#555").pack(side=tk.LEFT)
        self.threshold_var = tk.DoubleVar(value=0.55)
        self.find_slider = ttk.Scale(slider_f, from_=0.3, to=1.0,
                                     variable=self.threshold_var,
                                     orient=tk.HORIZONTAL, length=160,
                                     command=self._update_threshold_label)
        self.find_slider.pack(side=tk.LEFT, padx=6)
        self.lbl_thresh = tk.Label(slider_f, text="55%", width=4,
                                   bg="#f8f9fa", fg="#1a73e8", font=("Consolas", 9, "bold"))
        self.lbl_thresh.pack(side=tk.LEFT)
        tk.Label(slider_f, text="← 관대    엄격 →",
                 bg="#f8f9fa", fg="#aaa", font=("Consolas", 8)).pack(side=tk.LEFT, padx=4)

        # ── 찾기 액션 버튼 ──
        find_btn_f = tk.Frame(parent, bg="#f8f9fa")
        find_btn_f.pack(pady=3)
        bs = {"font": ("Malgun Gothic", 8, "bold"), "width": 8, "fg": "white", "relief": "flat"}
        tk.Button(find_btn_f, text="📁 경로설정", command=self._set_find_path,
                  bg="#5f6368", **bs).pack(side=tk.LEFT, padx=2)
        tk.Button(find_btn_f, text="🗑 로그삭제", command=self._clear_find_log,
                  bg="#999", **bs).pack(side=tk.LEFT, padx=2)

        # ── 검색 결과 ──
        result_lbl_f = tk.Frame(parent, bg="#f8f9fa")
        result_lbl_f.pack(fill=tk.X, padx=10, pady=(4, 0))
        tk.Label(result_lbl_f, text="검색 결과",
                 bg="#f8f9fa", font=("Malgun Gothic", 9, "bold"), fg="#333").pack(side=tk.LEFT)
        self.lbl_find_count = tk.Label(result_lbl_f, text="",
                                       bg="#f8f9fa", font=("Consolas", 8), fg="#888")
        self.lbl_find_count.pack(side=tk.LEFT, padx=6)

        res_f = tk.Frame(parent, bg="#f8f9fa")
        res_f.pack(fill=tk.BOTH, expand=True, padx=10, pady=(2, 0))
        res_sb = tk.Scrollbar(res_f)
        res_sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_box = tk.Listbox(res_f, font=("Consolas", 9),
                                     bg="#ffffff", fg="#222",
                                     selectbackground="#1a73e8",
                                     selectforeground="white",
                                     borderwidth=1, relief="solid",
                                     activestyle="none",
                                     yscrollcommand=res_sb.set)
        self.result_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        res_sb.config(command=self.result_box.yview)
        self.result_box.bind("<Double-Button-1>", self._open_find_selected)
        self.result_box.bind("<<ListboxSelect>>",  self._preview_find_path)
        self.result_box.bind("<Return>",           self._open_find_selected)

        # ── 열기 버튼 ──
        open_f = tk.Frame(parent, bg="#f8f9fa")
        open_f.pack(fill=tk.X, padx=10, pady=3)
        tk.Button(open_f, text="↗ 열기 (Enter/더블클릭)",
                  command=self._open_find_selected,
                  bg="#1a73e8", fg="white",
                  font=("Malgun Gothic", 9, "bold"), relief="flat", pady=3
                  ).pack(side=tk.LEFT, padx=(0, 4))
        tk.Button(open_f, text="📂 폴더만 열기",
                  command=self._open_find_parent,
                  bg="#5f6368", fg="white",
                  font=("Malgun Gothic", 9, "bold"), relief="flat", pady=3
                  ).pack(side=tk.LEFT)
        tk.Button(open_f, text="➡ 병합기로 전송",
                  command=self._send_to_merger,
                  bg="#1b4332", fg="#52b788",
                  font=("Malgun Gothic", 9, "bold"), relief="flat", pady=3
                  ).pack(side=tk.LEFT, padx=(4, 0))

        # ── 찾기 로그 ──
        self.find_log_text = tk.Text(parent, height=4, bg="white",
                                     font=("Consolas", 8), padx=5, pady=3,
                                     state=tk.DISABLED)
        self.find_log_text.pack(pady=(2, 0), padx=10, fill=tk.X)

        # ── 찾기 상태바 ──
        self.find_status = tk.Label(parent,
                                    text=f"경로: {self._search_root}",
                                    fg="#888", bg="#f0f0f0",
                                    font=("Consolas", 8), anchor="w", pady=2)
        self.find_status.pack(fill=tk.X)

        tk.Label(parent,
                 text="FUZZY v3.4 (FuzzySearch) | © 2026. bc5103",
                 fg="#adb5bd", bg="#f8f9fa", font=("Consolas", 8)
                 ).pack(pady=1)

        self._find_log("v3.4 FUZZY-SEARCH READY.  오타가 있어도 비슷한 이름을 찾아드립니다.")

    # ══════════════════════════════════════════════════════════
    # DnD
    # ══════════════════════════════════════════════════════════
    def _handle_drop(self, event):
        files = self.root.tk.splitlist(event.data)
        if files:
            self.add_files(files)
            self.nb.select(0)   # 드롭 시 병합기 탭으로 포커스

    # ══════════════════════════════════════════════════════════
    # 병합기 — 로그
    # ══════════════════════════════════════════════════════════
    def merge_log(self, msg):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.log_board.insert(tk.END, f"> [{now}] {msg}\n")
        self.log_board.see(tk.END)

    def _clear_merge_log(self):
        self.log_board.delete("1.0", tk.END)

    # ══════════════════════════════════════════════════════════
    # 병합기 — 분할 용량
    # ══════════════════════════════════════════════════════════
    def _apply_split_mb(self):
        try:
            val = float(self.split_entry.get())
            if val <= 0: raise ValueError
            self._split_mb = val
            self.lbl_split_mb.config(text=f"현재: {self._split_mb}MB")
            self.merge_log(f"분할 기준 용량 변경 → {self._split_mb}MB")
        except ValueError:
            self.merge_log("⚠ 올바른 숫자를 입력하세요 (예: 19.5)")

    # ══════════════════════════════════════════════════════════
    # 병합기 — 버튼 잠금
    # ══════════════════════════════════════════════════════════
    def _lock_buttons(self):
        self._busy = True
        for btn in (self.btn_merge, self.btn_comp, self.btn_split):
            btn.config(state=tk.DISABLED)

    def _unlock_buttons(self):
        self._busy = False
        for btn in (self.btn_merge, self.btn_comp, self.btn_split):
            btn.config(state=tk.NORMAL)

    # ══════════════════════════════════════════════════════════
    # 병합기 — 파일 리스트
    # ══════════════════════════════════════════════════════════
    def _get_file_info(self, path):
        ext = os.path.splitext(path)[1].lower()
        size_mb = os.path.getsize(path) / 1024 / 1024
        try:
            if ext == '.pdf':
                r = PdfReader(path)
                return f"[{size_mb:.1f}MB · {len(r.pages)}p]"
            elif ext in IMG_EXT:
                with Image.open(path) as im:
                    w, h = im.size
                return f"[{size_mb:.1f}MB · {w}×{h}]"
        except Exception:
            pass
        return f"[{size_mb:.1f}MB]"

    def _refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for i, p in enumerate(self._file_paths):
            info = self._get_file_info(p)
            name = os.path.basename(p)
            self.listbox.insert(tk.END, f" {i+1:02d}  {name}  {info}")
        self.lbl_count.config(text=f"{len(self._file_paths)} files")

    def add_files(self, paths=None):
        if paths is None:
            ext_str = "*.pdf *.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp *.heic *.ico *.jfif"
            paths = filedialog.askopenfilenames(
                title="파일 선택", filetypes=[("지원 파일", ext_str)])
        added, skipped_dup, skipped_ext = [], [], []
        for p in paths:
            ext = os.path.splitext(p)[1].lower()
            if ext not in SUPPORTED_EXT:
                skipped_ext.append(os.path.basename(p))
            elif p in self._file_paths:
                skipped_dup.append(os.path.basename(p))
            else:
                self._file_paths.append(p)
                added.append(p)
        self._refresh_listbox()
        if added:       self.merge_log(f"ADD: {len(added)}개 추가됨  (총 {len(self._file_paths)}개)")
        if skipped_dup: self.merge_log(f"  ⚠ 중복 스킵: {', '.join(skipped_dup)}")
        if skipped_ext: self.merge_log(f"  ⛔ 비지원 형식 스킵: {', '.join(skipped_ext)}")

    def remove_selected(self):
        idxs = sorted(self.listbox.curselection(), reverse=True)
        if not idxs: return
        for i in idxs: del self._file_paths[i]
        self._refresh_listbox()
        self.merge_log(f"REMOVED: {len(idxs)}개 제거됨")

    def clear_list(self):
        self._file_paths.clear()
        self._refresh_listbox()
        self.merge_log("LIST CLEARED.")

    def _open_selected_folder(self, event=None):
        idxs = self.listbox.curselection()
        if not idxs: return
        path = self._file_paths[idxs[0]]
        open_folder_safe(os.path.dirname(os.path.abspath(path)))
        self.merge_log(f"OPEN FOLDER: {os.path.dirname(path)}")

    # ── 순서 이동 ──
    def _move(self, delta):
        idxs = list(self.listbox.curselection())
        if not idxs: return
        if delta < 0 and idxs[0] == 0: return
        if delta > 0 and idxs[-1] == len(self._file_paths) - 1: return
        for i in (idxs if delta > 0 else reversed(idxs)):
            j = i + delta
            self._file_paths[i], self._file_paths[j] = self._file_paths[j], self._file_paths[i]
        self._refresh_listbox()
        new_idxs = [i + delta for i in idxs]
        for i in new_idxs: self.listbox.selection_set(i)

    def move_up(self):    self._move(-1)
    def move_down(self):  self._move(+1)

    def move_top(self):
        idxs = list(self.listbox.curselection())
        if not idxs: return
        items = [self._file_paths[i] for i in idxs]
        for i in sorted(idxs, reverse=True): del self._file_paths[i]
        self._file_paths = items + self._file_paths
        self._refresh_listbox()
        for i in range(len(items)): self.listbox.selection_set(i)

    def move_bottom(self):
        idxs = list(self.listbox.curselection())
        if not idxs: return
        items = [self._file_paths[i] for i in idxs]
        for i in sorted(idxs, reverse=True): del self._file_paths[i]
        self._file_paths = self._file_paths + items
        self._refresh_listbox()
        n = len(self._file_paths)
        for i in range(n - len(items), n): self.listbox.selection_set(i)

    # ── 마우스 드래그 ──
    def _drag_start(self, event):   self._drag_src = self.listbox.nearest(event.y)
    def _drag_release(self, event): self._drag_src = None

    def _drag_motion(self, event):
        dst = self.listbox.nearest(event.y)
        if dst != self._drag_src and 0 <= dst < len(self._file_paths):
            self._file_paths[self._drag_src], self._file_paths[dst] = \
                self._file_paths[dst], self._file_paths[self._drag_src]
            self._refresh_listbox()
            self.listbox.selection_set(dst)
            self._drag_src = dst

    # ── 진행률 바 ──
    def _set_progress(self, ratio):
        self.canvas_bar.update_idletasks()
        w = self.canvas_bar.winfo_width()
        if self._bar_rect: self.canvas_bar.delete(self._bar_rect)
        color = "#2a9d8f" if ratio < 1.0 else "#52b788"
        self._bar_rect = self.canvas_bar.create_rectangle(
            0, 0, int(w * ratio), 4, fill=color, outline="")

    # ══════════════════════════════════════════════════════════
    # 병합기 — 증거목록 (PDF 출력 / 전자소송 호환)
    # ══════════════════════════════════════════════════════════
    def export_evidence_list(self):
        if not self._file_paths:
            self.merge_log("⚠ 목록이 비어 있습니다."); return

        # ── 호증 종류 선택 다이얼로그 ──
        ho_type = simpledialog.askstring(
            "호증 종류 선택",
            "호증 종류를 입력하십시오.\n\n"
            "갑  → 갑 제N호증\n"
            "을  → 을 제N호증\n"
            "병  → 병 제N호증\n"
            "소갑 → 소갑 제N호증\n"
            "소을 → 소을 제N호증\n",
            initialvalue="갑"
        )
        if not ho_type: return
        ho_type = ho_type.strip()
        if ho_type not in ["갑", "을", "병", "소갑", "소을"]:
            ho_type = "갑"

        start_no = simpledialog.askinteger(
            "시작 번호", f"{ho_type}호증 시작 번호:", initialvalue=1, minvalue=1, maxvalue=999)
        if not start_no: return

        default_name = f"{ho_type}호증목록_{datetime.datetime.now().strftime('%m%d_%H%M')}.pdf"
        save_path = filedialog.asksaveasfilename(
            title=f"{ho_type}호증 목록 저장 (PDF)", initialfile=default_name,
            defaultextension=".pdf", filetypes=[("PDF 파일", "*.pdf")])
        if not save_path: return
        try:
            try:
                import reportlab
            except ImportError:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
            from reportlab.pdfgen import canvas
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.ttfonts import TTFont
            from reportlab.lib.pagesizes import A4

            # 한글 폰트 탐색
            font_candidates = [
                "C:/Windows/Fonts/malgun.ttf",
                "C:/Windows/Fonts/gulim.ttc",
                "C:/Windows/Fonts/batang.ttc",
                "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
            ]
            font_path = next((f for f in font_candidates if os.path.exists(f)), None)
            if font_path:
                pdfmetrics.registerFont(TTFont("KorFont", font_path))
                font_name = "KorFont"
            else:
                font_name = "Helvetica"

            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            w, h = A4
            c = canvas.Canvas(save_path, pagesize=A4)

            # 제목
            c.setFont(font_name, 16)
            c.drawCentredString(w / 2, h - 60, f"증 거 목 록  ({ho_type}호증)")
            c.setFont(font_name, 9)
            c.drawCentredString(w / 2, h - 80,
                f"작성일시: {now_str}  |  총 {len(self._file_paths)}건  |  시작번호: {ho_type} 제{start_no}호증")

            # 구분선
            c.setLineWidth(0.8)
            c.line(50, h - 90, w - 50, h - 90)

            # 목록
            c.setFont(font_name, 11)
            y = h - 120
            for i, p in enumerate(self._file_paths, start=0):
                no   = start_no + i
                name = os.path.basename(p)
                ext  = os.path.splitext(name)[1].upper().lstrip(".")
                size_mb = os.path.getsize(p) / 1024 / 1024 if os.path.exists(p) else 0
                line_text = f"{ho_type} 제{no}호증   {name}   [{ext}  {size_mb:.1f}MB]"
                c.drawString(55, y, line_text)
                y -= 22
                if y < 80:
                    c.showPage()
                    c.setFont(font_name, 11)
                    y = h - 60

            # 하단 (v6.8.0: 광고 문구 매립)
            c.setFont(font_name, 8)
            c.setLineWidth(0.5)
            c.line(50, 50, w - 50, 50)
            c.drawCentredString(w / 2, 35,
                f"{PRODUCT_NAME} {BUILD_NUMBER}  |  © 2026. 박병진  |  {_SESSION_BRAND_CAPTION}")
            c.setFont(font_name, 7)
            c.drawCentredString(w / 2, 22, FREE_BUILD_ID)
            c.save()

            self.merge_log(f"갑호증 목록 PDF 생성 완료 → {os.path.basename(save_path)}  ({len(self._file_paths)}건)")
            open_folder_safe(os.path.dirname(os.path.abspath(save_path)))
        except Exception as e:
            self.merge_log(f"갑호증 목록 저장 실패: {e}")

    # ══════════════════════════════════════════════════════════
    # 병합기 — 패치
    # ══════════════════════════════════════════════════════════
    def self_patch(self):
        try:
            new_code = self.root.clipboard_get()
            if "import" in new_code:
                script_path = os.path.abspath(sys.argv[0])
                with open(script_path, "w", encoding="utf-8") as f:
                    f.write(new_code)
                subprocess.Popen([sys.executable, script_path])
                self.root.destroy(); os._exit(0)
        except Exception as e:
            self.merge_log(f"PATCH FAIL: {e}")

    # ══════════════════════════════════════════════════════════
    # 병합기 — 분할
    # ══════════════════════════════════════════════════════════
    def run_splitter(self):
        if self._busy:
            self.merge_log("⚠ 처리 중입니다. 완료 후 다시 시도하세요."); return
        file_path = filedialog.askopenfilename(
            title="분할할 PDF 선택", filetypes=[("PDF 파일", "*.pdf")])
        if not file_path: return

        def process():
            self.root.after(0, self._lock_buttons)
            self.merge_log(f"SPLITTING: {os.path.basename(file_path)}  (기준: {self._split_mb}MB)")
            reader = PdfReader(file_path)
            total  = len(reader.pages)
            base   = os.path.splitext(file_path)[0]
            part_num, writer = 1, PdfWriter()
            try:
                for idx, page in enumerate(reader.pages):
                    writer.add_page(page)
                    tmp = BytesIO(); writer.write(tmp)
                    size_mb = tmp.tell() / 1024 / 1024
                    self.root.after(0, self._set_progress, (idx + 1) / total)
                    if size_mb > self._split_mb:
                        out = f"{base}_PART_{part_num}.pdf"
                        with open(out, "wb") as f: writer.write(f)
                        self.merge_log(f"SAVED: PART {part_num} ({size_mb:.1f}MB)")
                        writer, part_num = PdfWriter(), part_num + 1
                if len(writer.pages) > 0:
                    out = f"{base}_PART_{part_num}.pdf"
                    with open(out, "wb") as f: writer.write(f)
                    self.merge_log(f"SAVED: FINAL PART {part_num}")
                self.root.after(0, self._set_progress, 1.0)
                self.merge_log(f"SPLIT DONE. 총 {part_num}개 파일 생성됨")
                beep_safe()
                open_folder_safe(os.path.dirname(file_path))
            except Exception as e:
                self.merge_log(f"SPLIT ERR: {e}")
            finally:
                self.root.after(0, self._unlock_buttons)

        threading.Thread(target=process, daemon=True).start()

    # ══════════════════════════════════════════════════════════
    # 병합기 — 병합
    # ══════════════════════════════════════════════════════════
    # ── v6.8.5 라이선스 메서드 ─────────────────────────────────
    def _lgk_update_label(self, count: int, unlocked: bool = False) -> None:
        # v7.0.9: 건수 제한 해제 — 항상 무제한 표시
        self._lgk_var.set("✓ 개인 무제한  ·  상업용 문의")
        self._lgk_unlocked = True

    def _lgk_check(self) -> bool:
        """병합 실행 전 확인. v7.0.9: 건수 제한 해제 — 항상 True 반환."""
        return True

    def _lgk_show_dialog(self) -> None:
        dlg = tk.Toplevel(self.root)
        dlg.title("병합 한도 초과 — 라이선스 필요")
        dlg.configure(bg="#0a0a0a")
        dlg.resizable(False, False)
        dlg.grab_set()

        tk.Label(dlg, text="무료 병합 횟수를 모두 사용했습니다.",
                 fg="#f9e2af", bg="#0a0a0a", font=("맑은 고딕", 10, "bold"),
                 pady=10).pack(padx=20)
        tk.Label(dlg,
                 text="라이선스 키를 구매하려면 아래 머신ID를 개발자에게 전달하세요.\n"
                      "블로그: blog.naver.com/bc5103  |  이메일: dede5003@gmail.com",
                 fg="#aaa", bg="#0a0a0a", font=("Consolas", 8), justify="left").pack(padx=20)

        mid_var = tk.StringVar(value=self._mid)
        mid_e = tk.Entry(dlg, textvariable=mid_var, width=22, state="readonly",
                         bg="#1a1a1a", fg="#79b8ff", font=("Consolas", 10),
                         readonlybackground="#1a1a1a", relief="flat")
        mid_e.pack(pady=(6, 2), padx=20)
        tk.Button(dlg, text="머신ID 복사", command=lambda: (dlg.clipboard_clear(), dlg.clipboard_append(self._mid)),
                  bg="#2a5298", fg="white", font=("맑은 고딕", 8), relief="flat",
                  padx=6, pady=2).pack(pady=(0, 8))

        tk.Label(dlg, text="라이선스 키 입력 (장문 서명 붙여넣기 가능):", fg="#aaa", bg="#0a0a0a",
                 font=("맑은 고딕", 9)).pack()
        key_var = tk.StringVar()
        tk.Entry(dlg, textvariable=key_var, width=80, bg="#1a1a1a", fg="#e0e0e0",
                 insertbackground="#e0e0e0", font=("Consolas", 9), relief="flat").pack(pady=4, padx=20)

        def _activate():
            _exp = _lgk_validate(key_var.get(), self._mid)
            if _exp is not None:
                global _IS_COMMERCIAL
                d = _lgk_load()
                d["unlocked"]   = True
                d["commercial"] = True
                d["expiry"]     = _exp
                _lgk_save(d)
                _IS_COMMERCIAL = True
                self._lgk_update_label(0, True)
                messagebox.showinfo("인증 완료", "상업용 라이선스 등록 완료!\n병합 횟수 제한이 해제됩니다.", parent=dlg)
                dlg.destroy()
            else:
                messagebox.showerror("오류", "키가 올바르지 않습니다.\n이 기기의 머신ID를 개발자에게 전달하세요.", parent=dlg)

        tk.Button(dlg, text="인증", command=_activate,
                  bg="#2980b9", fg="white", font=("맑은 고딕", 9, "bold"),
                  relief="flat", padx=10, pady=3).pack(pady=(4, 12))

    # ────────────────────────────────────────────────────────────
    def run_merger(self, compress_mode):
        if self._busy:
            self.merge_log("⚠ 처리 중입니다. 완료 후 다시 시도하세요."); return
        # v6.8.5 — 병합 횟수 제한 체크
        if not self._lgk_check():
            return
        if not self._file_paths:
            ext_str = "*.pdf *.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp *.heic *.ico *.jfif"
            files = filedialog.askopenfilenames(title="파일 선택", filetypes=[("지원 파일", ext_str)])
            if not files: return
            self.add_files(files)
        self.execute_merge(compress_mode)

    def execute_merge(self, compress_mode):
        files = list(self._file_paths)
        if not files: return
        base_dir = os.path.dirname(files[0])
        total    = len(files)

        def process():
            self.root.after(0, self._lock_buttons)
            merger   = PdfMerger()
            mode_str = "압축" if compress_mode else "일반"
            self.merge_log(f"MERGING {total}개 파일... [{mode_str}모드] (순서 고정)")
            try:
                for idx, f_path in enumerate(files):
                    ext = os.path.splitext(f_path)[1].lower()
                    self.root.after(0, self._set_progress, idx / total)
                    self.merge_log(f"  [{idx+1}/{total}] {os.path.basename(f_path)}")
                    if ext == '.pdf':
                        with open(f_path, 'rb') as f:
                            if compress_mode:
                                reader = PdfReader(f); writer = PdfWriter()
                                for page in reader.pages:
                                    page.compress_content_streams()
                                    writer.add_page(page)
                                tmp = BytesIO(); writer.write(tmp); tmp.seek(0)
                                merger.append(tmp)
                            else:
                                merger.append(f)
                    elif ext in IMG_EXT:
                        try:
                            # ── 팩스 TIFF 다중 프레임 처리 ──────────────────────
                            if ext in ('.tiff', '.tif'):
                                tiff_img = Image.open(f_path)
                                frames = []
                                try:
                                    while True:
                                        frame = tiff_img.copy().convert('RGB')
                                        frame = ImageOps.exif_transpose(frame)
                                        target_size = (1024, 1448) if compress_mode else (2480, 3508)
                                        frame.thumbnail(target_size, Image.Resampling.LANCZOS)
                                        # v6.8.0: 프레임별 캡션 띠 합성
                                        frame = self._ad_overlay_image(frame)
                                        frames.append(frame)
                                        tiff_img.seek(tiff_img.tell() + 1)
                                except EOFError:
                                    pass  # 프레임 끝 — 정상 종료
                                if frames:
                                    pdf_bytes = BytesIO()
                                    frames[0].save(
                                        pdf_bytes, format='PDF',
                                        resolution=150.0 if compress_mode else 300.0,
                                        quality=75 if compress_mode else 95,
                                        save_all=True,
                                        append_images=frames[1:]
                                    )
                                    pdf_bytes.seek(0)
                                    merger.append(pdf_bytes)
                                    self.merge_log(f"  TIFF {len(frames)}프레임 변환(광고 매립): {os.path.basename(f_path)}")
                            # ── 일반 이미지 처리 (기존 로직 유지 + v6.8.0 캡션) ──
                            else:
                                img = Image.open(f_path).convert('RGB')
                                img = ImageOps.exif_transpose(img)
                                target_size = (1024, 1448) if compress_mode else (2480, 3508)
                                img.thumbnail(target_size, Image.Resampling.LANCZOS)
                                # v6.8.0: 상·하단 캡션 띠 합성
                                img = self._ad_overlay_image(img)
                                pdf_bytes = BytesIO()
                                img.save(pdf_bytes, format='PDF',
                                         resolution=150.0 if compress_mode else 300.0,
                                         quality=75 if compress_mode else 95)
                                pdf_bytes.seek(0); merger.append(pdf_bytes)
                        except Exception as ie:
                            self.merge_log(f"  ⚠ 이미지 스킵 ({os.path.basename(f_path)}): {ie}")
                    else:
                        self.merge_log(f"  ⚠ 미지원 포맷 스킵: {ext}")

                self.root.after(0, self._set_progress, 1.0)
                output_pdf = filedialog.asksaveasfilename(
                    initialdir=base_dir, defaultextension=".pdf",
                    initialfile=f"MERGED_{datetime.datetime.now().strftime('%m%d_%H%M')}.pdf")
                if output_pdf:
                    # ── v6.8.0: 병합 결과를 임시 파일로 저장 후 전 페이지 푸터 오버레이 ──
                    tmp_out = output_pdf + ".raw.pdf"
                    with open(tmp_out, 'wb') as fout: merger.write(fout)
                    overlay_ok = self._ad_overlay_pdf_footer(tmp_out, output_pdf)
                    try:
                        if os.path.exists(tmp_out):
                            os.remove(tmp_out)
                    except Exception:
                        pass
                    size_mb = os.path.getsize(output_pdf) / 1024 / 1024
                    self.merge_log(f"DONE ✅  {os.path.basename(output_pdf)}  ({size_mb:.1f}MB)  "
                                   f"{'[광고 매립]' if overlay_ok else '[광고 매립 실패·원본 유지]'}")
                    open_folder_safe(os.path.dirname(os.path.abspath(output_pdf)))
                beep_safe()
            except Exception as e:
                self.merge_log(f"ERR: {str(e)[:80]}")
            finally:
                self.root.after(0, self._unlock_buttons)

        threading.Thread(target=process, daemon=True).start()

    # ══════════════════════════════════════════════════════════
    # 퍼지검색 — 내부 메서드
    # ══════════════════════════════════════════════════════════
    def _find_log(self, msg):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.find_log_text.config(state=tk.NORMAL)
        self.find_log_text.insert(tk.END, f"[{now}] {msg}\n")
        self.find_log_text.see(tk.END)
        self.find_log_text.config(state=tk.DISABLED)

    def _clear_find_log(self):
        self.find_log_text.config(state=tk.NORMAL)
        self.find_log_text.delete("1.0", tk.END)
        self.find_log_text.config(state=tk.DISABLED)

    def _update_threshold_label(self, val=None):
        pct = int(float(self.threshold_var.get()) * 100)
        self.lbl_thresh.config(text=f"{pct}%")

    def _set_find_path(self):
        p = filedialog.askdirectory(initialdir=self._search_root)
        if p:
            self._search_root = p
            self.find_status.config(text=f"경로: {self._search_root}")
            self._find_log(f"PATH 변경 → {p}")

    def _start_search(self):
        if self._searching:
            self._find_log("⚠ 검색 중입니다. 잠시 기다려주세요."); return
        query = self.find_entry.get().strip()
        if not query: return
        self.result_box.delete(0, tk.END)
        self._find_results.clear()
        self.lbl_find_count.config(text="검색 중...")
        self.btn_find.config(state=tk.DISABLED, text="⏳ 검색중")
        self._searching = True
        threading.Thread(target=self._do_search, args=(query,), daemon=True).start()

    def _do_search(self, query):
        threshold = self.threshold_var.get()
        scored = []
        try:
            for dirpath, dirs, files in os.walk(self._search_root):
                for d in dirs:
                    score = fuzzy_score(query, d)
                    if score >= threshold:
                        scored.append((score, os.path.join(dirpath, d), True))
                for f in files:
                    name_noext = os.path.splitext(f)[0]
                    score = max(fuzzy_score(query, f), fuzzy_score(query, name_noext))
                    if score >= threshold:
                        scored.append((score, os.path.join(dirpath, f), False))
        except Exception as e:
            self.root.after(0, self._find_log, f"ERR: {e}")

        scored.sort(key=lambda x: -x[0])
        scored = scored[:50]
        self._find_results = [(s, p) for s, p, _ in scored]
        self.root.after(0, self._show_find_results, query, scored)

    def _show_find_results(self, query, scored):
        self.result_box.delete(0, tk.END)
        if not scored:
            self.result_box.insert(tk.END, f"  '{query}'과 유사한 항목을 찾지 못했습니다.")
            self.lbl_find_count.config(text="0건")
        else:
            for score, path, is_dir in scored:
                icon = "📁" if is_dir else "📄"
                name = os.path.basename(path)
                pct  = int(score * 100)
                self.result_box.insert(tk.END, f"  {icon} [{pct:3d}%] {name}")
                idx = self.result_box.size() - 1
                if score >= 0.9:
                    self.result_box.itemconfig(idx, fg="#1a73e8")
                elif score >= 0.7:
                    self.result_box.itemconfig(idx, fg="#188038")
                else:
                    self.result_box.itemconfig(idx, fg="#888")
            self.lbl_find_count.config(text=f"{len(scored)}건")
            self.result_box.selection_set(0)
            self._find_log(f"검색 '{query}' → {len(scored)}건 (임계값 {int(self.threshold_var.get()*100)}%)")
        self._searching = False
        self.btn_find.config(state=tk.NORMAL, text="🔍 찾기")

    def _get_selected_find_path(self):
        idxs = self.result_box.curselection()
        if not idxs or idxs[0] >= len(self._find_results): return None
        return self._find_results[idxs[0]][1]

    def _preview_find_path(self, event=None):
        path = self._get_selected_find_path()
        if path: self.find_status.config(text=path)

    def _open_find_selected(self, event=None):
        path = self._get_selected_find_path()
        if not path: return
        try:
            if sys.platform == "win32":    os.startfile(path)
            elif sys.platform == "darwin": subprocess.Popen(["open", path])
            else:                          subprocess.Popen(["xdg-open", path])
            self._find_log(f"OPEN: {os.path.basename(path)}")
        except Exception as e:
            self._find_log(f"OPEN ERR: {e}")

    def _open_find_parent(self, event=None):
        path = self._get_selected_find_path()
        if not path: return
        folder = path if os.path.isdir(path) else os.path.dirname(path)
        try:
            if sys.platform == "win32":    os.startfile(folder)
            elif sys.platform == "darwin": subprocess.Popen(["open", folder])
            else:                          subprocess.Popen(["xdg-open", folder])
            self._find_log(f"FOLDER: {folder}")
        except Exception as e:
            self._find_log(f"FOLDER ERR: {e}")

    def _send_to_merger(self):
        """검색 결과 선택 항목을 병합기 탭으로 전송. 선택 없으면 전체 전송."""
        idxs = list(self.result_box.curselection())
        if idxs:
            paths = [self._find_results[i][1] for i in idxs
                     if i < len(self._find_results)]
        else:
            paths = [item[1] for item in self._find_results]

        if not paths:
            self._find_log("전송할 파일 없음.")
            return

        valid   = [p for p in paths
                   if os.path.splitext(p)[1].lower() in SUPPORTED_EXT]
        skipped = len(paths) - len(valid)

        if not valid:
            self._find_log("병합기 지원 형식 파일 없음.")
            return

        self.add_files(valid)
        self.nb.select(0)
        self._find_log(
            f"➡ 병합기 전송: {len(valid)}건"
            + (f"  (미지원 형식 {skipped}건 제외)" if skipped else "")
        )


# ──────────────────────────────────────────────────────────────
    # ══════════════════════════════════════════════════════════
    # ④ 증거목록 탭 (v600 신규 — 구 증거목록기 v1.0 흡수)
    # ══════════════════════════════════════════════════════════
    def _init_evidence(self, parent):
        """
        증거목록 탭 초기화. 파일명 그대로 텍스트 추출 전용.
        갑호증 부여(병합기 탭) 와는 별개 영역.
        """
        self._ev_files    = []
        self._ev_drag_src = None

        # ── 헤더 ──
        tk.Label(parent, text="◈  증거목록  ─  파일명 그대로 텍스트 추출",
                 fg="#b0c4de", bg="#111", font=("Consolas", 9, "bold"), pady=5
                 ).pack(fill=tk.X)

        # ── 번호 접두어 + 시작번호 + 출력형식 ──
        cfg_frame = tk.Frame(parent, bg="#111", pady=4)
        cfg_frame.pack(fill=tk.X, padx=8, pady=(4, 0))

        tk.Label(cfg_frame, text="번호형식:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT, padx=(0, 3))

        self.ev_prefix_var = tk.StringVar(value=PREFIX_OPTIONS[0])
        prefix_menu = tk.OptionMenu(cfg_frame, self.ev_prefix_var, *PREFIX_OPTIONS)
        prefix_menu.config(bg="#1a1a1a", fg="#ccc", font=("Consolas", 8),
                           relief="flat", highlightthickness=0, width=9,
                           activebackground="#2a2a2a", activeforeground="#fff")
        prefix_menu["menu"].config(bg="#1a1a1a", fg="#ccc", font=("Consolas", 8))
        prefix_menu.pack(side=tk.LEFT, padx=2)

        tk.Label(cfg_frame, text="  시작번호:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        self.ev_start_num = tk.Entry(cfg_frame, width=4, bg="#1a1a1a", fg="#e0e0e0",
                                     insertbackground="#e0e0e0",
                                     font=("Consolas", 9), relief="flat",
                                     highlightthickness=1, highlightcolor="#4a90d9",
                                     highlightbackground="#333")
        self.ev_start_num.insert(0, "1")
        self.ev_start_num.pack(side=tk.LEFT, padx=4)

        tk.Label(cfg_frame, text="  출력형식:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        self.ev_fmt_var = tk.StringVar(value="TXT")
        for fmt in ("TXT", "CSV", "클립보드"):
            tk.Radiobutton(cfg_frame, text=fmt, variable=self.ev_fmt_var, value=fmt,
                           bg="#111", fg="#aaa", selectcolor="#111",
                           activebackground="#111", activeforeground="#fff",
                           font=("Consolas", 8)).pack(side=tk.LEFT, padx=2)

        # ── 파일 리스트 (Treeview) ──
        tree_frame = tk.Frame(parent, bg="#0a0a0a")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=(6, 0))

        style = ttk.Style()
        style.configure("EV.Treeview",
                        background="#0d0d0d", foreground="#e0e0e0",
                        fieldbackground="#0d0d0d",
                        rowheight=22, font=("Consolas", 9))
        style.configure("EV.Treeview.Heading",
                        background="#1a1a1a", foreground="#79b8ff",
                        font=("Consolas", 8, "bold"), relief="flat")
        style.map("EV.Treeview",
                  background=[("selected", "#2a5298")],
                  foreground=[("selected", "#ffffff")])

        cols = ("no", "name", "ext", "size", "modified", "path")
        self.ev_tree = ttk.Treeview(tree_frame, columns=cols,
                                    show="headings", style="EV.Treeview",
                                    selectmode="extended")

        self.ev_tree.heading("no",       text="#",        anchor=tk.CENTER)
        self.ev_tree.heading("name",     text="파일명",    anchor=tk.W)
        self.ev_tree.heading("ext",      text="형식",      anchor=tk.CENTER)
        self.ev_tree.heading("size",     text="크기",      anchor=tk.E)
        self.ev_tree.heading("modified", text="수정일",    anchor=tk.CENTER)
        self.ev_tree.heading("path",     text="경로",      anchor=tk.W)

        self.ev_tree.column("no",       width=30,  stretch=False, anchor=tk.CENTER)
        self.ev_tree.column("name",     width=200, stretch=True,  anchor=tk.W)
        self.ev_tree.column("ext",      width=50,  stretch=False, anchor=tk.CENTER)
        self.ev_tree.column("size",     width=70,  stretch=False, anchor=tk.E)
        self.ev_tree.column("modified", width=120, stretch=False, anchor=tk.CENTER)
        self.ev_tree.column("path",     width=0,   stretch=False)

        vsb = ttk.Scrollbar(tree_frame, orient="vertical",   command=self.ev_tree.yview)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.ev_tree.xview)
        self.ev_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side=tk.RIGHT,  fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        self.ev_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 키 바인딩
        self.ev_tree.bind("<Delete>",          lambda e: self._ev_remove_selected())
        self.ev_tree.bind("<Double-Button-1>", self._ev_open_file_location)
        self.ev_tree.bind("<ButtonPress-1>",   self._ev_drag_start)
        self.ev_tree.bind("<B1-Motion>",       self._ev_drag_motion)
        self.ev_tree.bind("<ButtonRelease-1>", self._ev_drag_release)

        # 우클릭 메뉴
        self._ev_ctx_menu = tk.Menu(parent, tearoff=0, bg="#1a1a1a", fg="#ccc",
                                    activebackground="#2a5298", activeforeground="#fff",
                                    font=("맑은 고딕", 9))
        self._ev_ctx_menu.add_command(label="▲ 위로",       command=self._ev_move_up)
        self._ev_ctx_menu.add_command(label="▼ 아래로",      command=self._ev_move_down)
        self._ev_ctx_menu.add_command(label="⤒ 맨 위",      command=self._ev_move_top)
        self._ev_ctx_menu.add_command(label="⤓ 맨 아래",    command=self._ev_move_bottom)
        self._ev_ctx_menu.add_separator()
        self._ev_ctx_menu.add_command(label="📂 위치 열기",  command=self._ev_open_file_location)
        self._ev_ctx_menu.add_separator()
        self._ev_ctx_menu.add_command(label="✕ 제거",        command=self._ev_remove_selected)
        self.ev_tree.bind("<Button-3>", lambda e: self._ev_ctx_menu.post(e.x_root, e.y_root))

        # ── 순서 버튼 행 ──
        order_frame = tk.Frame(parent, bg="#0a0a0a")
        order_frame.pack(fill=tk.X, padx=8, pady=3)

        ob = {"font": ("맑은 고딕", 8, "bold"), "relief": "flat", "bd": 0,
              "padx": 6, "pady": 3}
        tk.Button(order_frame, text="▲ 위로",    command=self._ev_move_up,
                  bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_frame, text="▼ 아래로",  command=self._ev_move_down,
                  bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_frame, text="⤒ 맨위",    command=self._ev_move_top,
                  bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_frame, text="⤓ 맨아래",  command=self._ev_move_bottom,
                  bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_frame, text="✕ 제거",    command=self._ev_remove_selected,
                  bg="#3a1a1a", fg="#ff7b7b", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_frame, text="🗑 전체삭제", command=self._ev_clear_list,
                  bg="#3a1a1a", fg="#ff7b7b", **ob).pack(side=tk.LEFT, padx=2)

        self.ev_lbl_count = tk.Label(order_frame, text="0 개 | 합계 0 B",
                                     fg="#555", bg="#0a0a0a", font=("Consolas", 8))
        self.ev_lbl_count.pack(side=tk.RIGHT, padx=6)

        # ── 액션 버튼 ──
        act_frame = tk.Frame(parent, bg="#0a0a0a")
        act_frame.pack(pady=5)

        ab = {"font": ("맑은 고딕", 8, "bold"), "height": 1, "relief": "flat"}
        tk.Button(act_frame, text="📂 파일추가",    command=self._ev_add_files,
                  width=9,  bg="#1b4332", fg="#52b788", **ab).pack(side=tk.LEFT, padx=3)
        tk.Button(act_frame, text="📋 목록 내보내기", command=self._ev_export_list,
                  width=12, bg="#1a3a6a", fg="#79b8ff", **ab).pack(side=tk.LEFT, padx=3)
        tk.Button(act_frame, text="🔍 미리보기",     command=self._ev_preview_list,
                  width=9,  bg="#2a1a3a", fg="#b87fff", **ab).pack(side=tk.LEFT, padx=3)

        # ── 로그 ──
        log_hdr = tk.Frame(parent, bg="#0a0a0a")
        log_hdr.pack(fill=tk.X, padx=8, pady=(2, 0))
        tk.Label(log_hdr, text="LOG", fg="#444", bg="#0a0a0a",
                 font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        tk.Button(log_hdr, text="지우기", command=lambda: self.ev_log_board.delete("1.0", tk.END),
                  bg="#1a1a1a", fg="#555", font=("Consolas", 8),
                  relief="flat", padx=4, pady=0).pack(side=tk.RIGHT)

        self.ev_log_board = scrolledtext.ScrolledText(
            parent, width=70, height=5, bg="#060606", fg="#33ff33",
            font=("Consolas", 8), borderwidth=0, highlightthickness=0)
        self.ev_log_board.pack(pady=(2, 6), padx=8, fill=tk.X)

        # 드래그앤드롭 — evidence_tab 위젯에 별도 등록 (root drop과 격리)
        try:
            parent.drop_target_register(DND_FILES)
            parent.dnd_bind('<<Drop>>', self._ev_on_drop)
        except Exception:
            pass

        self._ev_log("증거목록 탭 READY.  파일을 드래그하거나 [파일추가] 버튼을 누르세요.")
        self._ev_log("※ PDF·이미지·실행파일·동영상 등 모든 형식 인식. 파일명 그대로 텍스트화.")

    # ── 증거목록 로그 ─────────────────────────────
    def _ev_log(self, msg):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.ev_log_board.insert(tk.END, f"> [{now}] {msg}\n")
        self.ev_log_board.see(tk.END)

    # ── 증거목록 트리 갱신 ─────────────────────────
    def _ev_refresh_tree(self):
        self.ev_tree.delete(*self.ev_tree.get_children())
        total_bytes = 0
        for i, p in enumerate(self._ev_files):
            try:
                stat   = os.stat(p)
                size_b = stat.st_size
                mtime  = stat.st_mtime
            except Exception:
                size_b, mtime = 0, 0
            total_bytes += size_b
            name = os.path.basename(p)
            ext  = os.path.splitext(name)[1].upper() or "-"
            self.ev_tree.insert("", tk.END, values=(
                i + 1,
                name,
                ext,
                fmt_size(size_b),
                fmt_date(mtime) if mtime else "-",
                p,
            ))
        n = len(self._ev_files)
        self.ev_lbl_count.config(text=f"{n} 개  |  합계 {fmt_size(total_bytes)}")

    def _ev_selected_indices(self):
        items     = self.ev_tree.selection()
        all_items = self.ev_tree.get_children()
        return [all_items.index(it) for it in items]

    def _ev_reselect(self, idxs):
        all_items = self.ev_tree.get_children()
        self.ev_tree.selection_set([all_items[i] for i in idxs if 0 <= i < len(all_items)])

    # ── 파일 추가/제거/정렬 ───────────────────────
    def _ev_add_files(self, paths=None):
        if paths is None:
            paths = filedialog.askopenfilenames(title="파일 선택 (모든 형식 가능)",
                                                filetypes=[("모든 파일", "*.*")])
        added = 0
        for p in paths:
            p = p.strip("{}")  # tkinterdnd2 중괄호 처리
            if p and p not in self._ev_files:
                self._ev_files.append(p)
                added += 1
        if added:
            self._ev_refresh_tree()
            self._ev_log(f"ADD: {added}개 추가  (총 {len(self._ev_files)}개)")

    def _ev_remove_selected(self):
        idxs = sorted(self._ev_selected_indices(), reverse=True)
        for i in idxs: del self._ev_files[i]
        self._ev_refresh_tree()

    def _ev_clear_list(self):
        if self._ev_files and messagebox.askyesno("전체 삭제", "증거목록을 모두 지우시겠습니까?"):
            self._ev_files.clear()
            self._ev_refresh_tree()
            self._ev_log("LIST CLEARED.")

    def _ev_move(self, delta):
        idxs = self._ev_selected_indices()
        if not idxs: return
        if delta < 0 and idxs[0] == 0: return
        if delta > 0 and idxs[-1] == len(self._ev_files) - 1: return
        for i in (idxs if delta > 0 else reversed(idxs)):
            j = i + delta
            self._ev_files[i], self._ev_files[j] = self._ev_files[j], self._ev_files[i]
        self._ev_refresh_tree()
        self._ev_reselect([i + delta for i in idxs])

    def _ev_move_up(self):   self._ev_move(-1)
    def _ev_move_down(self): self._ev_move(+1)

    def _ev_move_top(self):
        idxs = self._ev_selected_indices()
        if not idxs: return
        items = [self._ev_files[i] for i in idxs]
        for i in sorted(idxs, reverse=True): del self._ev_files[i]
        self._ev_files = items + self._ev_files
        self._ev_refresh_tree()
        self._ev_reselect(list(range(len(items))))

    def _ev_move_bottom(self):
        idxs = self._ev_selected_indices()
        if not idxs: return
        items = [self._ev_files[i] for i in idxs]
        for i in sorted(idxs, reverse=True): del self._ev_files[i]
        self._ev_files += items
        self._ev_refresh_tree()
        n = len(self._ev_files)
        self._ev_reselect(list(range(n - len(items), n)))

    # ── 드래그 순서 변경 ──────────────────────────
    def _ev_drag_start(self, event):
        row = self.ev_tree.identify_row(event.y)
        if row:
            all_items = self.ev_tree.get_children()
            self._ev_drag_src = all_items.index(row)

    def _ev_drag_motion(self, event):
        if self._ev_drag_src is None: return
        row = self.ev_tree.identify_row(event.y)
        if not row: return
        all_items = self.ev_tree.get_children()
        dst = all_items.index(row)
        if dst != self._ev_drag_src and 0 <= dst < len(self._ev_files):
            self._ev_files[self._ev_drag_src], self._ev_files[dst] = \
                self._ev_files[dst], self._ev_files[self._ev_drag_src]
            self._ev_refresh_tree()
            self._ev_reselect([dst])
            self._ev_drag_src = dst

    def _ev_drag_release(self, event):
        self._ev_drag_src = None

    # ── 파일 위치 열기 ───────────────────────────
    def _ev_open_file_location(self, event=None):
        idxs = self._ev_selected_indices()
        if idxs:
            open_folder_safe(os.path.dirname(self._ev_files[idxs[0]]))

    # ── 드롭 처리 (evidence_tab 전용) ─────────────
    def _ev_on_drop(self, event):
        paths    = self.root.tk.splitlist(event.data)
        expanded = []
        for p in paths:
            if os.path.isdir(p):
                for root_d, _, fnames in os.walk(p):
                    for fn in fnames:
                        expanded.append(os.path.join(root_d, fn))
            else:
                expanded.append(p)
        self._ev_add_files(expanded)

    # ── 번호 포맷 ────────────────────────────────
    def _ev_make_number(self, i):
        fmt = self.ev_prefix_var.get()
        return fmt % i

    def _ev_get_start(self):
        try:    return max(1, int(self.ev_start_num.get()))
        except: return 1

    # ── 미리보기 ──────────────────────────────────
    def _ev_preview_list(self):
        if not self._ev_files:
            self._ev_log("⚠ 목록이 비어있습니다."); return

        lines = self._ev_build_lines()
        win = tk.Toplevel(self.root)
        win.title("증거목록 미리보기")
        win.geometry("560x420")
        win.configure(bg="#0a0a0a")
        win.attributes("-topmost", True)

        st = scrolledtext.ScrolledText(win, bg="#0d0d0d", fg="#e0e0e0",
                                       font=("Consolas", 9), borderwidth=0)
        st.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        st.insert(tk.END, "\n".join(lines))
        st.config(state="disabled")

        tk.Button(win, text="닫기", command=win.destroy,
                  bg="#2a2a2a", fg="#aaa", font=("맑은 고딕", 9),
                  relief="flat", padx=10, pady=3).pack(pady=4)

    def _ev_build_lines(self):
        start = self._ev_get_start()
        fmt   = self.ev_fmt_var.get()
        lines = []
        tool_tag = f"{PRODUCT_NAME} {BUILD_NUMBER} · {_SESSION_BRAND_CAPTION} · {FREE_BUILD_ID}"

        if fmt == "CSV":
            # v6.8.0: 우측 끝 "수집도구" 컬럼 신설
            lines.append("번호,파일명,형식,크기,수정일,경로,수집도구")
        else:
            # v6.8.0: 상단 헤더 4행
            lines.append("증  거  목  록")
            lines.append(f"{'─'*50}")
            lines.append(f"생성일시: {datetime.datetime.now().strftime('%Y년 %m월 %d일 %H:%M')}")
            lines.append(f"총 {len(self._ev_files)}건")
            lines.append(f"수집도구: {PRODUCT_NAME} {BUILD_NUMBER}  |  {FREE_BUILD_ID}")
            lines.append(f"{'─'*50}")

        for i, p in enumerate(self._ev_files):
            num  = self._ev_make_number(start + i)
            name = os.path.basename(p)
            ext  = os.path.splitext(name)[1].upper() or "-"
            try:
                stat   = os.stat(p)
                size_s = fmt_size(stat.st_size)
                date_s = fmt_date(stat.st_mtime)
            except Exception:
                size_s, date_s = "-", "-"

            if fmt == "CSV":
                lines.append(f'"{num}","{name}","{ext}","{size_s}","{date_s}","{p}","{tool_tag}"')
            else:
                lines.append(f"{num:<14} {name}")
                lines.append(f"{'':14} 형식: {ext}  크기: {size_s}  수정: {date_s}")
                lines.append(f"{'':14} 경로: {p}")
                lines.append("")

        # v6.8.0: 하단 푸터 2행 (TXT 전용)
        if fmt != "CSV":
            lines.append(f"{'─'*50}")
            lines.append(f"※ {FIXED_CAPTION}")
            lines.append(f"※ {_SESSION_BRAND_CAPTION}")
        return lines

    # ── 내보내기 ──────────────────────────────────
    def _ev_export_list(self):
        if not self._ev_files:
            self._ev_log("⚠ 목록이 비어있습니다."); return

        lines = self._ev_build_lines()
        text  = "\n".join(lines)
        fmt   = self.ev_fmt_var.get()

        if fmt == "클립보드":
            try:
                # v6.8.0: 말미 1줄 광고 부가
                clip_text = text + f"\n\n— {PRODUCT_NAME} {BUILD_NUMBER}  ·  {_SESSION_BRAND_CAPTION}\n  {FREE_BUILD_ID}"
                self.root.clipboard_clear()
                self.root.clipboard_append(clip_text)
                self._ev_log(f"클립보드 복사 완료 ({len(self._ev_files)}건)")
            except Exception as e:
                self._ev_log(f"클립보드 복사 실패: {e}")
            return

        ext_map  = {"TXT": ".txt", "CSV": ".csv"}
        ext      = ext_map.get(fmt, ".txt")
        default  = f"증거목록_{datetime.datetime.now().strftime('%m%d_%H%M')}{ext}"
        save_path = filedialog.asksaveasfilename(
            title="증거목록 저장",
            initialfile=default,
            defaultextension=ext,
            filetypes=[(f"{fmt} 파일", f"*{ext}"), ("모든 파일", "*.*")],
        )
        if not save_path: return

        try:
            with open(save_path, "w", encoding="utf-8-sig") as f:
                f.write(text)
            self._ev_log(f"저장 완료 → {os.path.basename(save_path)}  ({len(self._ev_files)}건)")
            open_folder_safe(os.path.dirname(os.path.abspath(save_path)))
        except Exception as e:
            self._ev_log(f"저장 실패: {e}")


    # ══════════════════════════════════════════════════════════
    # ⑤ 판례수집 탭 (v600 신규 — 구 case_crawler v0.1.3 흡수)
    # ══════════════════════════════════════════════════════════
    def _init_case(self, parent):
        """
        판례수집 탭 초기화. 법제처 Open API 기반.
        OC 인증키 입력 → 키워드 입력 → 판례 일괄 수집 → CSV 저장.
        """
        self._case_running = False  # 중복 실행 방지

        # ── 헤더 ──
        tk.Label(parent, text="◈  판례수집  ─  법제처 Open API (open.law.go.kr)",
                 fg="#b0c4de", bg="#111", font=("Consolas", 9, "bold"), pady=5
                 ).pack(fill=tk.X)

        # ── OC 인증키 입력 ──
        oc_frame = tk.Frame(parent, bg="#111", pady=4)
        oc_frame.pack(fill=tk.X, padx=8, pady=(4, 0))

        tk.Label(oc_frame, text="OC 인증키:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT, padx=(0, 3))

        self.case_oc_var = tk.StringVar()
        self.case_oc_entry = tk.Entry(oc_frame, textvariable=self.case_oc_var,
                                      width=18, bg="#1a1a1a", fg="#e0e0e0",
                                      insertbackground="#e0e0e0",
                                      font=("Consolas", 9), relief="flat",
                                      highlightthickness=1, highlightcolor="#4a90d9",
                                      highlightbackground="#333")
        self.case_oc_entry.pack(side=tk.LEFT, padx=4)


        tk.Label(oc_frame, text="  ※ open.law.go.kr 회원가입 후 발급받은 아이디",
                 fg="#444", bg="#111", font=("Consolas", 8)).pack(side=tk.LEFT, padx=4)

        # 저장된 OC 자동 로드
        # OC 자동 로드 비활성화 (v6.9.3)

        # ── 검색 키워드 입력 ──
        kw_frame = tk.Frame(parent, bg="#111", pady=4)
        kw_frame.pack(fill=tk.X, padx=8, pady=(2, 0))

        tk.Label(kw_frame, text="검색 키워드:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT, padx=(0, 3))

        self.case_query_var = tk.StringVar()
        self.case_query_entry = tk.Entry(kw_frame, textvariable=self.case_query_var,
                                         width=22, bg="#1a1a1a", fg="#e0e0e0",
                                         insertbackground="#e0e0e0",
                                         font=("Consolas", 9), relief="flat",
                                         highlightthickness=1, highlightcolor="#4a90d9",
                                         highlightbackground="#333")
        self.case_query_entry.pack(side=tk.LEFT, padx=4)

        tk.Label(kw_frame, text="  최대 건수:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        self.case_max_var = tk.IntVar(value=100)
        tk.Spinbox(kw_frame, from_=1, to=1000, textvariable=self.case_max_var,
                   width=5, font=("Consolas", 9),
                   bg="#1a1a1a", fg="#e0e0e0",
                   insertbackground="#e0e0e0",
                   relief="flat").pack(side=tk.LEFT, padx=4)

        tk.Label(kw_frame, text="  (예: 형법 347조, 사기, 업무방해)",
                 fg="#444", bg="#111", font=("Consolas", 8)).pack(side=tk.LEFT, padx=4)

        # ── v672 본문 필터 키워드 입력 (2단계 검색) ──
        ft_frame = tk.Frame(parent, bg="#111", pady=4)
        ft_frame.pack(fill=tk.X, padx=8, pady=(2, 0))

        tk.Label(ft_frame, text="본문 필터:", fg="#c0a040", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT, padx=(0, 3))

        self.case_filter_var = tk.StringVar()
        self.case_filter_entry = tk.Entry(ft_frame, textvariable=self.case_filter_var,
                                          width=22, bg="#1a1a1a", fg="#f0d060",
                                          insertbackground="#f0d060",
                                          font=("Consolas", 9), relief="flat",
                                          highlightthickness=1, highlightcolor="#c0a040",
                                          highlightbackground="#333")
        self.case_filter_entry.pack(side=tk.LEFT, padx=4)

        tk.Label(ft_frame, text="  (비워두면 전건 수집 / 입력 시 본문 내 해당 키워드 포함건만 추출)",
                 fg="#444", bg="#111", font=("Consolas", 8)).pack(side=tk.LEFT, padx=4)

        # ── 액션 버튼 ──
        act_frame = tk.Frame(parent, bg="#0a0a0a")
        act_frame.pack(pady=8)

        ab = {"font": ("맑은 고딕", 9, "bold"), "height": 1, "relief": "flat"}
        self.case_btn_run = tk.Button(act_frame, text="▶ 판례 수집 시작",
                                      command=self._case_start,
                                      width=18, bg="#1b4332", fg="#52b788", **ab)
        self.case_btn_run.pack(side=tk.LEFT, padx=3)

        tk.Button(act_frame, text="📂 출력 폴더 열기",
                  command=self._case_open_output,
                  width=15, bg="#1a3a6a", fg="#79b8ff", **ab).pack(side=tk.LEFT, padx=3)

        # ── 진행 상황 + 로그 ──
        log_hdr = tk.Frame(parent, bg="#0a0a0a")
        log_hdr.pack(fill=tk.X, padx=8, pady=(4, 0))
        tk.Label(log_hdr, text="LOG", fg="#444", bg="#0a0a0a",
                 font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        tk.Button(log_hdr, text="지우기",
                  command=lambda: self.case_log_board.delete("1.0", tk.END),
                  bg="#1a1a1a", fg="#555", font=("Consolas", 8),
                  relief="flat", padx=4, pady=0).pack(side=tk.RIGHT)

        self.case_log_board = scrolledtext.ScrolledText(
            parent, width=70, height=18, bg="#060606", fg="#33ff33",
            font=("Consolas", 9), borderwidth=0, highlightthickness=0)
        self.case_log_board.pack(pady=(2, 6), padx=8, fill=tk.BOTH, expand=True)

        self._case_log("판례수집 READY.  법제처 Open API 기반.")
        self._case_log("1) OC 인증키 입력 → [저장] 클릭 (1회)")
        self._case_log("2) 검색 키워드 입력 → [▶ 판례 수집 시작] 클릭")
        self._case_log("3) 결과 CSV는 사용자 홈 폴더의 case_crawler_output/ 에 저장됩니다.")

    # ── OC 저장·로드 (홈 디렉토리 oc.txt 단일 파일) ──
    def _case_oc_path(self):
        return os.path.join(os.path.expanduser("~"), ".click_legal_kit_oc.txt")

    def _case_save_oc(self):
        pass  # v6.9.3 — OC 키 파일 저장 비활성화

    def _case_load_oc(self):
        pass  # v6.9.3 비활성화

    # ── 로그 ──
    def _case_log(self, msg):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        try:
            self.case_log_board.insert(tk.END, f"> [{now}] {msg}\n")
            self.case_log_board.see(tk.END)
        except Exception:
            pass

    # ── 출력 폴더 열기 ──
    def _case_open_output(self):
        out_dir = os.path.join(os.path.expanduser("~"), "case_crawler_output")
        if not os.path.exists(out_dir):
            self._case_log(f"⚠ 출력 폴더 없음 (수집 후 생성): {out_dir}")
            return
        open_folder_safe(out_dir)

    # ── 수집 시작 (threading) ──
    def _case_start(self):
        if self._case_running:
            self._case_log("⚠ 이미 수집 진행 중.")
            return
        oc = self.case_oc_var.get().strip()
        if not oc:
            self._case_log("⚠ OC 인증키 입력 필요.")
            return
        query = self.case_query_var.get().strip()
        if not query:
            self._case_log("⚠ 검색 키워드 입력 필요.")
            return
        try:
            max_cases = max(1, min(int(self.case_max_var.get()), 1000))
        except Exception:
            max_cases = 100

        self._case_running = True
        self.case_btn_run.config(text="⏳ 수집 중...", state="disabled")
        filter_kw = self.case_filter_var.get().strip()
        t = threading.Thread(
            target=self._case_run_worker,
            args=(oc, query, max_cases, filter_kw),
            daemon=True)
        t.start()

    def _case_run_worker(self, oc, query, max_cases, filter_kw=""):
        try:
            crawler = CaseCrawler(oc, log_fn=self._case_log)
            self._case_log(f"[START] 검색: '{query}'  /  최대: {max_cases}건")
            if filter_kw:
                self._case_log(f"[FILTER] 본문 필터 키워드: '{filter_kw}'")
            cases = crawler.fetch_list(query, max_cases=max_cases)
            if not cases:
                self._case_log("[END] 수집 결과 없음.")
                return
            self._case_log(f"[INFO] 목록 확보: {len(cases)}건. 본문 조회 시작.")
            for i, case in enumerate(cases, start=1):
                detail = crawler.fetch_detail(case.get("판례일련번호", ""))
                case.update(detail)
                if i % 10 == 0 or i == len(cases):
                    self._case_log(
                        f"  [{i}/{len(cases)}] {case.get('법원명','')} "
                        f"{case.get('사건번호','')} {case.get('선고일자','')}")
            # v672: 본문 필터 키워드 2차 필터링
            if filter_kw:
                filter_lower = filter_kw.lower()
                before_cnt = len(cases)
                filtered = []
                for case in cases:
                    combined = " ".join([
                        case.get("판시사항", ""),
                        case.get("판결요지", ""),
                        case.get("판례내용", ""),
                        case.get("사건명", ""),
                        case.get("참조조문", ""),
                    ]).lower()
                    if filter_lower in combined:
                        filtered.append(case)
                cases = filtered
                self._case_log(
                    f"[FILTER] '{filter_kw}' 본문 필터 적용: "
                    f"{before_cnt}건 중 {len(cases)}건 일치.")
                if not cases:
                    self._case_log("[END] 필터 조건에 일치하는 판례 없음.")
                    return
            filepath = crawler.save_csv(cases, query)
            if filepath:
                self._case_log(f"[DONE] 저장 완료: {filepath}")
                self._case_log(f"       총 {len(cases)}건 수집.")
        except Exception as e:
            self._case_log(f"[FATAL] {type(e).__name__}: {e}")
        finally:
            self._case_running = False
            try:
                self.case_btn_run.config(text="▶ 판례 수집 시작", state="normal")
            except Exception:
                pass

    # ══════════════════════════════════════════════════════════
    # ⑥ 호증부여기 탭 (v6.8.3 신규 — PDF 파일명 일괄 호증 채번)
    # ══════════════════════════════════════════════════════════
    def _init_evid_label(self, parent):
        """호증부여기 탭. 그룹 드래그(들여쓰기) 방식 가지번호 전자동.
        당사자 라디오·시작번호·미리보기·일괄 리네임."""
        # 상태
        self._lbl_items = []  # [{'path': str, 'indent': 0|1}, ...]

        # 헤더
        tk.Label(parent, text="🏷  호증부여기 — PDF 파일명 일괄 호증 채번",
                 fg="#f1c40f", bg="#111",
                 font=("맑은 고딕", 10, "bold"), pady=5
                 ).pack(fill=tk.X)

        # ── 옵션 줄 ──
        opt = tk.Frame(parent, bg="#0a0a0a")
        opt.pack(fill=tk.X, padx=8, pady=(6, 4))

        tk.Label(opt, text="당사자:", fg="#cccccc", bg="#0a0a0a",
                 font=("맑은 고딕", 9)).pack(side=tk.LEFT, padx=(0, 6))
        self._lbl_party_var = tk.StringVar(value="갑")
        for party in ("갑", "을", "병", "정"):
            tk.Radiobutton(opt, text=party, value=party,
                           variable=self._lbl_party_var,
                           fg="#ffffff", bg="#0a0a0a",
                           selectcolor="#1a3a5f",
                           activebackground="#0a0a0a",
                           activeforeground="#ffffff",
                           font=("맑은 고딕", 9),
                           command=self._lbl_refresh_tree
                           ).pack(side=tk.LEFT, padx=2)

        tk.Label(opt, text="   시작번호:", fg="#cccccc", bg="#0a0a0a",
                 font=("맑은 고딕", 9)).pack(side=tk.LEFT, padx=(12, 4))
        self._lbl_start_var = tk.IntVar(value=1)
        sp = tk.Spinbox(opt, from_=1, to=999, width=5,
                        textvariable=self._lbl_start_var,
                        font=("Consolas", 9),
                        command=self._lbl_refresh_tree)
        sp.pack(side=tk.LEFT)
        try:
            sp.bind("<KeyRelease>", lambda e: self._lbl_refresh_tree())
        except Exception:
            pass

        # ── 버튼 줄 ──
        btn = tk.Frame(parent, bg="#0a0a0a")
        btn.pack(fill=tk.X, padx=8, pady=(0, 4))
        tk.Button(btn, text="📂 PDF 추가", command=self._lbl_add_files,
                  bg="#2c3e50", fg="white",
                  font=("맑은 고딕", 9), padx=8, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="▲ 위", command=lambda: self._lbl_move(-1),
                  bg="#34495e", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="▼ 아래", command=lambda: self._lbl_move(1),
                  bg="#34495e", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="→ 들여쓰기 (가지번호)",
                  command=self._lbl_indent_selected,
                  bg="#27ae60", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="← 내어쓰기 (본번)",
                  command=self._lbl_outdent_selected,
                  bg="#16a085", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="✕ 제거", command=self._lbl_remove_selected,
                  bg="#c0392b", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="🗑 전체삭제", command=self._lbl_clear_all,
                  bg="#7f8c8d", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))

        # ── 트리뷰 ──
        tree_frame = tk.Frame(parent, bg="#0a0a0a")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 4))
        cols = ("no", "old", "new")
        self._lbl_tree = ttk.Treeview(tree_frame, columns=cols,
                                       show="headings", height=14)
        self._lbl_tree.heading("no",  text="호증번호")
        self._lbl_tree.heading("old", text="현재 파일명")
        self._lbl_tree.heading("new", text="변경 후 파일명")
        self._lbl_tree.column("no",  width=110, anchor="center", stretch=False)
        self._lbl_tree.column("old", width=320, anchor="w")
        self._lbl_tree.column("new", width=420, anchor="w")
        ysb = ttk.Scrollbar(tree_frame, orient="vertical",
                            command=self._lbl_tree.yview)
        self._lbl_tree.configure(yscrollcommand=ysb.set)
        self._lbl_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        ysb.pack(side=tk.RIGHT, fill=tk.Y)

        # 트리뷰 DnD — PDF 파일 직접 드롭 허용
        try:
            self._lbl_tree.drop_target_register(DND_FILES)
            self._lbl_tree.dnd_bind('<<Drop>>', self._lbl_on_drop)
        except Exception:
            pass

        # ── 실행 줄 ──
        run = tk.Frame(parent, bg="#0a0a0a")
        run.pack(fill=tk.X, padx=8, pady=(0, 4))
        tk.Button(run, text="👁 미리보기 갱신",
                  command=self._lbl_refresh_tree,
                  bg="#2980b9", fg="white",
                  font=("맑은 고딕", 9, "bold"), padx=10, pady=4,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 6))
        tk.Button(run, text="🏷 일괄 리네임 실행",
                  command=self._lbl_run_rename,
                  bg="#e67e22", fg="white",
                  font=("맑은 고딕", 9, "bold"), padx=10, pady=4,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 6))

        # ── LOG ──
        log_wrap = tk.Frame(parent, bg="#0a0a0a")
        log_wrap.pack(fill=tk.X, padx=8, pady=(0, 8))
        tk.Label(log_wrap, text="LOG", fg="#888", bg="#0a0a0a",
                 font=("Consolas", 8), anchor="w").pack(fill=tk.X)
        self._lbl_log = scrolledtext.ScrolledText(
            log_wrap, height=5, bg="#0d1b1f", fg="#7fffd4",
            font=("Consolas", 9), insertbackground="#7fffd4",
            relief=tk.FLAT, borderwidth=0
        )
        self._lbl_log.pack(fill=tk.X)
        self._lbl_log_msg("v6.8.3 호증부여기 READY. PDF를 추가하거나 드래그드롭하세요.")
        self._lbl_log_msg("들여쓰기(→) 1단계까지 지원. 들여쓴 행은 직전 본번의 가지번호로 자동 부여.")

    # ── 호증부여기 — 로깅 ──
    def _lbl_log_msg(self, msg):
        try:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            self._lbl_log.insert(tk.END, f"> [{now}] {msg}\n")
            self._lbl_log.see(tk.END)
        except Exception:
            pass

    # ── 호증부여기 — 파일 추가 ──
    def _lbl_add_files(self):
        paths = filedialog.askopenfilenames(
            title="호증으로 부여할 PDF 선택",
            filetypes=[("PDF", "*.pdf"), ("모든 파일", "*.*")])
        self._lbl_append_paths(paths)

    def _lbl_on_drop(self, event):
        try:
            files = self.root.tk.splitlist(event.data)
        except Exception:
            files = []
        self._lbl_append_paths(files)

    def _lbl_append_paths(self, paths):
        added = 0
        for p in paths or []:
            try:
                p = str(p).strip().strip('{}').strip('"')
                if not p:
                    continue
                if not os.path.isfile(p):
                    continue
                self._lbl_items.append({'path': p, 'indent': 0})
                added += 1
            except Exception:
                continue
        if added:
            self._lbl_log_msg(f"PDF {added}건 추가. 총 {len(self._lbl_items)}건.")
        self._lbl_refresh_tree()

    # ── 호증부여기 — 선택 인덱스 ──
    def _lbl_selected_indices(self):
        sel = self._lbl_tree.selection()
        idx = []
        for s in sel:
            try:
                idx.append(int(s))
            except Exception:
                continue
        return sorted(idx)

    # ── 호증부여기 — 이동 ──
    def _lbl_move(self, delta: int):
        idxs = self._lbl_selected_indices()
        if not idxs:
            return
        n = len(self._lbl_items)
        if delta < 0:
            for i in idxs:
                if i + delta >= 0:
                    self._lbl_items[i + delta], self._lbl_items[i] = \
                        self._lbl_items[i], self._lbl_items[i + delta]
        else:
            for i in reversed(idxs):
                if i + delta < n:
                    self._lbl_items[i + delta], self._lbl_items[i] = \
                        self._lbl_items[i], self._lbl_items[i + delta]
        self._lbl_refresh_tree()
        try:
            new_sel = [str(i + delta) for i in idxs
                       if 0 <= i + delta < n]
            self._lbl_tree.selection_set(new_sel)
        except Exception:
            pass

    # ── 호증부여기 — 들여쓰기/내어쓰기 ──
    def _lbl_indent_selected(self):
        idxs = self._lbl_selected_indices()
        if not idxs:
            return
        for i in idxs:
            if i == 0:
                continue   # 첫 행은 항상 본번
            self._lbl_items[i]['indent'] = 1
        self._lbl_refresh_tree()
        try:
            self._lbl_tree.selection_set([str(i) for i in idxs])
        except Exception:
            pass

    def _lbl_outdent_selected(self):
        idxs = self._lbl_selected_indices()
        if not idxs:
            return
        for i in idxs:
            self._lbl_items[i]['indent'] = 0
        self._lbl_refresh_tree()
        try:
            self._lbl_tree.selection_set([str(i) for i in idxs])
        except Exception:
            pass

    # ── 호증부여기 — 제거/전체삭제 ──
    def _lbl_remove_selected(self):
        idxs = self._lbl_selected_indices()
        if not idxs:
            return
        for i in reversed(idxs):
            try:
                del self._lbl_items[i]
            except Exception:
                pass
        self._lbl_log_msg(f"{len(idxs)}건 제거. 총 {len(self._lbl_items)}건.")
        self._lbl_refresh_tree()

    def _lbl_clear_all(self):
        if not self._lbl_items:
            return
        if not messagebox.askyesno("전체 삭제", "리스트 전체를 삭제할까요?"):
            return
        self._lbl_items = []
        self._lbl_log_msg("전체 삭제 완료.")
        self._lbl_refresh_tree()

    # ── 호증부여기 — 채번 계산 + 새 이름 미리 산출 ──
    def _lbl_compose_names(self):
        """[(label_no_str, new_basename), ...] 반환."""
        result = []
        try:
            party = self._lbl_party_var.get() or "갑"
            start = int(self._lbl_start_var.get())
            if start < 1:
                start = 1
        except Exception:
            party = "갑"
            start = 1

        main_no   = start - 1   # 첫 본번 만나면 +1
        branch_no = 0

        for i, item in enumerate(self._lbl_items):
            indent = int(item.get('indent', 0) or 0)
            # 첫 행은 무조건 본번 취급
            if i == 0:
                indent = 0
            if indent == 0:
                main_no += 1
                branch_no = 0
                no_str = f"{main_no}"
                prefix = f"{party}제{main_no}호증_"
            else:
                # 본번을 한 번도 안 만난 상태에서 가지번호 → 본번으로 폴백
                if main_no < start:
                    main_no = start
                    branch_no = 0
                    no_str = f"{main_no}"
                    prefix = f"{party}제{main_no}호증_"
                else:
                    branch_no += 1
                    no_str = f"{main_no}의{branch_no}"
                    prefix = f"{party}제{main_no}호증의{branch_no}_"
            try:
                base = os.path.basename(item['path'])
            except Exception:
                base = "(unknown).pdf"
            new_name = prefix + base
            result.append((no_str, new_name))
        return result

    # ── 호증부여기 — 트리뷰 갱신 ──
    def _lbl_refresh_tree(self):
        try:
            for iid in self._lbl_tree.get_children(""):
                self._lbl_tree.delete(iid)
        except Exception:
            pass
        names = self._lbl_compose_names()
        for i, item in enumerate(self._lbl_items):
            try:
                old = os.path.basename(item['path'])
            except Exception:
                old = "(unknown)"
            no_str, new_name = names[i]
            indent = int(item.get('indent', 0) or 0)
            display_old = ("    └ " + old) if indent == 1 else old
            try:
                self._lbl_tree.insert("", tk.END, iid=str(i),
                                      values=(no_str, display_old, new_name))
            except Exception:
                pass

    # ── 호증부여기 — 일괄 리네임 실행 ──
    def _lbl_run_rename(self):
        if not self._lbl_items:
            messagebox.showinfo("호증부여기", "PDF가 추가되지 않았습니다.")
            return
        names = self._lbl_compose_names()
        # 미리 충돌 정리 (동일 폴더 내 새 이름 중복 회피)
        plan = []   # [(old_path, new_path)]
        used_names = {}   # 폴더별 set
        for i, item in enumerate(self._lbl_items):
            try:
                old_path = item['path']
                folder   = os.path.dirname(old_path)
                _, new_name = names[i]
                # 충돌 회피 — _dup2·_dup3 …
                cand = new_name
                seen = used_names.setdefault(folder, set())
                base, ext = os.path.splitext(cand)
                n = 2
                while (cand in seen) or (
                    os.path.exists(os.path.join(folder, cand))
                    and os.path.abspath(os.path.join(folder, cand)) !=
                        os.path.abspath(old_path)
                ):
                    cand = f"{base}_dup{n}{ext}"
                    n += 1
                seen.add(cand)
                plan.append((old_path, os.path.join(folder, cand)))
            except Exception as e:
                self._lbl_log_msg(f"⚠ 계획 단계 오류: {e}")

        if not plan:
            return
        if not messagebox.askyesno(
                "호증부여기",
                f"총 {len(plan)}건의 PDF 파일명을 변경합니다.\n진행할까요?"):
            self._lbl_log_msg("리네임 취소.")
            return

        ok, fail = 0, 0
        new_items = []
        for old_p, new_p in plan:
            try:
                if old_p == new_p:
                    new_items.append({'path': new_p, 'indent': 0})
                    ok += 1
                    continue
                os.rename(old_p, new_p)
                new_items.append({'path': new_p, 'indent': 0})
                ok += 1
                self._lbl_log_msg(
                    f"✓ {os.path.basename(old_p)} → {os.path.basename(new_p)}")
            except Exception as e:
                fail += 1
                new_items.append({'path': old_p, 'indent': 0})
                self._lbl_log_msg(
                    f"✗ {os.path.basename(old_p)} 실패: {e}")
        # 들여쓰기 상태 복원
        for i, it in enumerate(new_items):
            try:
                it['indent'] = int(self._lbl_items[i].get('indent', 0) or 0)
            except Exception:
                it['indent'] = 0
        self._lbl_items = new_items
        self._lbl_refresh_tree()
        self._lbl_log_msg(f"완료. 성공 {ok}건 / 실패 {fail}건.")
        messagebox.showinfo(
            "호증부여기",
            f"리네임 완료\n성공 {ok}건 / 실패 {fail}건")

    # ══════════════════════════════════════════════════════════
    # ⑦ 홍보 탭 (v6.8.0 신규 — 외부 통신 없음, 정적 표시 전용)
    # ══════════════════════════════════════════════════════════

    # ══════════════════════════════════════════════════════════
    # v7.0.0 — 녹취록 탭 (음성 → 텍스트, Whisper)
    # ══════════════════════════════════════════════════════════
    def _init_transcript(self, parent):
        """녹취록 탭 — Whisper 기반 음성/영상 파일 → 텍스트 변환."""
        import tkinter as _tk
        from tkinter import scrolledtext as _stext, ttk as _ttk
        # 한글 언어 표기
        self._ts_LANGS = [("자동 감지", None), ("한국어", "ko"), ("영어", "en"),
                          ("일본어", "ja"), ("중국어", "zh")]
        self._ts_running = False
        self._ts_queue = []
        self._ts_last_out_dir = ""

        C_BG="#0a0a0a"; C_PANEL="#1a1a1a"; C_ACCENT="#2a5298"; C_FG="#cccccc"
        C_FG2="#888888"; C_DROP="#1e2e1e"; C_DROP_BD="#3a7a3a"; C_GOLD="#f9e2af"
        C_OK="#a6e3a1"; C_WARN="#f9e2af"; C_ERR="#f38ba8"; C_INFO="#89dceb"

        # 헤더
        _tk.Label(parent, text="  🎙 녹취록 변환  ·  Whisper Audio→Text  ·  로컬 처리",
                  fg=C_FG2, bg="#111111", font=("Consolas", 9, "bold"),
                  pady=4, anchor="w").pack(fill="x")

        # 드롭 영역
        drop_frame = _tk.LabelFrame(parent, text="  파일 드롭 / 선택",
                                    fg=C_FG, bg=C_BG, font=("맑은 고딕", 9, "bold"))
        drop_frame.pack(fill="x", padx=6, pady=(6, 3))
        self._ts_drop = _tk.Label(drop_frame,
            text="음성/영상 파일을 여기로 끌어다 놓거나 클릭하여 선택\n"
                 "( .m4a  .mp3  .wav  .ogg  .flac  .mp4  .mkv  .mov ... )",
            fg=C_DROP_BD, bg=C_DROP, font=("맑은 고딕", 9),
            relief="ridge", bd=2, cursor="hand2", pady=12)
        self._ts_drop.pack(fill="x", padx=6, pady=6, ipady=2)
        try:
            self._ts_drop.drop_target_register(DND_FILES)
            self._ts_drop.dnd_bind("<<Drop>>", self._ts_on_drop)
        except Exception:
            pass
        self._ts_drop.bind("<Button-1>", lambda _: self._ts_select_files())

        # 큐
        qframe = _tk.LabelFrame(parent, text="  대기열",
                                fg=C_FG, bg=C_BG, font=("맑은 고딕", 9, "bold"))
        qframe.pack(fill="x", padx=6, pady=3)
        qrow = _tk.Frame(qframe, bg=C_BG); qrow.pack(fill="x", padx=5, pady=3)
        self._ts_listbox = _tk.Listbox(qrow, height=3, bg=C_PANEL, fg=C_FG,
            selectbackground=C_ACCENT, selectforeground="#fff",
            font=("Consolas", 9), relief="flat", bd=0)
        qsb = _tk.Scrollbar(qrow, orient="vertical", command=self._ts_listbox.yview)
        self._ts_listbox.config(yscrollcommand=qsb.set)
        self._ts_listbox.pack(side="left", fill="x", expand=True)
        qsb.pack(side="right", fill="y")
        qbtn = _tk.Frame(qframe, bg=C_BG); qbtn.pack(fill="x", padx=5, pady=(0, 3))
        _tk.Button(qbtn, text="제거", command=self._ts_remove_selected,
                   bg=C_PANEL, fg=C_FG, relief="flat", cursor="hand2",
                   font=("맑은 고딕", 9), width=6, pady=3).pack(side="left", padx=2)
        _tk.Button(qbtn, text="전체삭제", command=self._ts_clear_queue,
                   bg=C_PANEL, fg=C_FG, relief="flat", cursor="hand2",
                   font=("맑은 고딕", 9), width=8, pady=3).pack(side="left", padx=2)

        # 옵션
        opt = _tk.LabelFrame(parent, text="  옵션",
                             fg=C_FG, bg=C_BG, font=("맑은 고딕", 9, "bold"))
        opt.pack(fill="x", padx=6, pady=3)
        row0 = _tk.Frame(opt, bg=C_BG); row0.pack(fill="x", padx=5, pady=4)
        _tk.Label(row0, text="언어:", fg=C_FG, bg=C_BG,
                  font=("맑은 고딕", 9)).pack(side="left")
        self._ts_lang_var = _tk.StringVar(value="자동 감지")
        _ttk.Combobox(row0, textvariable=self._ts_lang_var,
                      values=[l[0] for l in self._ts_LANGS],
                      width=10, state="readonly", font=("맑은 고딕", 9)
                      ).pack(side="left", padx=(2, 10))
        _tk.Label(row0, text="출력:", fg=C_FG, bg=C_BG,
                  font=("맑은 고딕", 9)).pack(side="left")
        self._ts_fmt_var = _tk.StringVar(value="txt")
        _ttk.Combobox(row0, textvariable=self._ts_fmt_var,
                      values=_TS_OUT_FMTS, width=7, state="readonly",
                      font=("맑은 고딕", 9)).pack(side="left", padx=(2, 10))
        _tk.Label(row0, text="엔진: Whisper small", fg=C_FG2, bg=C_BG,
                  font=("맑은 고딕", 9)).pack(side="left")

        row1 = _tk.Frame(opt, bg=C_BG); row1.pack(fill="x", padx=5, pady=(0, 4))
        _tk.Label(row1, text="저장 위치:", fg=C_FG, bg=C_BG,
                  font=("맑은 고딕", 9)).pack(side="left")
        self._ts_outdir_var = _tk.StringVar(value="(입력 파일과 동일)")
        _tk.Entry(row1, textvariable=self._ts_outdir_var, width=28,
                  bg=C_PANEL, fg=C_FG, insertbackground=C_FG, relief="flat",
                  font=("맑은 고딕", 9)).pack(side="left", padx=(4, 3))
        _tk.Button(row1, text="찾아보기", command=self._ts_select_outdir,
                   bg=C_PANEL, fg=C_FG, relief="flat", cursor="hand2",
                   font=("맑은 고딕", 9), width=7, pady=3).pack(side="left", padx=2)
        _tk.Button(row1, text="초기화",
                   command=lambda: self._ts_outdir_var.set("(입력 파일과 동일)"),
                   bg=C_PANEL, fg=C_FG, relief="flat", cursor="hand2",
                   font=("맑은 고딕", 9), width=6, pady=3).pack(side="left", padx=2)
        _tk.Button(row1, text="폴더 열기", command=self._ts_open_last_folder,
                   bg=C_PANEL, fg=C_FG, relief="flat", cursor="hand2",
                   font=("맑은 고딕", 9), width=8, pady=3).pack(side="left", padx=2)

        # 실행 버튼
        btn_row = _tk.Frame(parent, bg=C_BG); btn_row.pack(fill="x", padx=6, pady=4)
        self._ts_run_btn = _tk.Button(btn_row, text="▶  변환 시작",
            command=self._ts_start, bg=C_ACCENT, fg="#fff",
            font=("맑은 고딕", 10, "bold"), relief="flat", cursor="hand2",
            padx=14, pady=4)
        self._ts_run_btn.pack(side="left", padx=(0, 5))
        self._ts_stop_btn = _tk.Button(btn_row, text="■  중지",
            command=self._ts_stop, bg="#5a1a1a", fg="#f38ba8",
            font=("맑은 고딕", 10, "bold"), relief="flat", cursor="hand2",
            padx=10, pady=4, state="disabled")
        self._ts_stop_btn.pack(side="left")
        self._ts_status_var = _tk.StringVar(value="대기 중")
        _tk.Label(btn_row, textvariable=self._ts_status_var,
                  fg=C_FG2, bg=C_BG, font=("맑은 고딕", 9)).pack(side="left", padx=10)

        self._ts_progress = _ttk.Progressbar(parent, mode="indeterminate")
        self._ts_progress.pack(fill="x", padx=6, pady=2)

        log_frame = _tk.LabelFrame(parent, text="  로그",
                                   fg=C_FG, bg=C_BG, font=("맑은 고딕", 9, "bold"))
        log_frame.pack(fill="both", expand=True, padx=6, pady=(3, 6))
        self._ts_log_box = _stext.ScrolledText(log_frame, height=7,
            font=("Consolas", 9), bg="#0d0d0d", fg=C_FG,
            insertbackground=C_FG, state="disabled", relief="flat")
        self._ts_log_box.pack(fill="both", expand=True, padx=3, pady=3)
        self._ts_log_box.tag_config("info",  foreground=C_INFO)
        self._ts_log_box.tag_config("ok",    foreground=C_OK)
        self._ts_log_box.tag_config("warn",  foreground=C_WARN)
        self._ts_log_box.tag_config("error", foreground=C_ERR)
        self._ts_log("info", f"녹취록 v7.0.0 준비 · FFmpeg: {_TS_FFMPEG_BIN}")

    # ── 큐 관리 ──
    def _ts_on_drop(self, event):
        import re as _re, os as _os
        raw = event.data
        paths = _re.findall(r"\{([^}]+)\}", raw) or raw.split()
        self._ts_add_to_queue([_os.path.normpath(p.strip()) for p in paths if p.strip()])

    def _ts_add_to_queue(self, paths):
        from pathlib import Path as _P
        added = 0
        for p in paths:
            if not os.path.isfile(p):
                self._ts_log("warn", f"파일 없음: {p}"); continue
            if _P(p).suffix.lower() not in _TS_AUDIO_EXT:
                self._ts_log("warn", f"미지원 형식: {_P(p).name}"); continue
            if p not in self._ts_queue:
                self._ts_queue.append(p)
                self._ts_listbox.insert("end", _P(p).name)
                added += 1
        if added:
            self._ts_log("info", f"{added}건 추가 (총 {len(self._ts_queue)}건)")

    def _ts_remove_selected(self):
        for i in reversed(list(self._ts_listbox.curselection())):
            self._ts_listbox.delete(i); self._ts_queue.pop(i)

    def _ts_clear_queue(self):
        self._ts_listbox.delete(0, "end"); self._ts_queue.clear()
        self._ts_log("info", "대기열 비움")

    def _ts_select_files(self):
        paths = filedialog.askopenfilenames(filetypes=[
            ("음성/영상", "*.m4a *.mp3 *.wav *.ogg *.flac *.mp4 *.mkv *.mov *.avi *.aac *.wma"),
            ("전체", "*.*")])
        if paths: self._ts_add_to_queue(list(paths))

    def _ts_select_outdir(self):
        d = filedialog.askdirectory()
        if d: self._ts_outdir_var.set(d)

    def _ts_open_last_folder(self):
        target = self._ts_last_out_dir
        if not target:
            raw = self._ts_outdir_var.get().strip()
            if raw and raw != "(입력 파일과 동일)" and os.path.isdir(raw):
                target = raw
        if target and os.path.isdir(target):
            os.startfile(target)
        else:
            self._ts_log("warn", "출력 폴더 없음 — 변환을 먼저 실행하세요.")

    # ── 실행 ──
    def _ts_start(self):
        # 통합 카운터 — 법무킷 _lgk_check() 호출
        if not self._lgk_check():
            return
        if not self._ts_queue:
            messagebox.showwarning("파일 없음", "대기열에 파일을 추가하세요.")
            return
        if self._ts_running:
            return
        self._ts_running = True
        self._ts_run_btn.config(state="disabled")
        self._ts_stop_btn.config(state="normal")
        self._ts_progress.start(12)
        self._ts_set_status(f"변환 중 (0/{len(self._ts_queue)})")
        threading.Thread(target=self._ts_run_all, daemon=True).start()

    def _ts_stop(self):
        self._ts_running = False
        self._ts_log("warn", "중지 요청 — 현재 파일 완료 후 정지")

    def _ts_run_all(self):
        try:
            from faster_whisper import WhisperModel
        except ImportError:
            self._ts_log("error", "faster-whisper 미설치. pip install faster-whisper")
            self._ts_finish(False); return
        from pathlib import Path as _P
        model_name = _TS_FIXED_MODEL
        # v7.0.4 — CPU INT8 안정 빌드 (CUDA 12.x 설치 환경에서는 v7.0.3 사용 권장)
        # 환경변수 LGK_FORCE_CUDA=1 설정 시 CUDA 시도 (cublas64_12.dll 필요)
        force_cuda = os.environ.get("LGK_FORCE_CUDA", "1") != "0"  # v7.0.5 — CUDA 동봉 빌드, 기본 ON
        model = None
        if force_cuda:
            try:
                self._ts_log("info", f"CUDA 강제 시도: {model_name} (cuda/float16) ...")
                model = WhisperModel(model_name, device="cuda", compute_type="float16")
                self._ts_log("ok", "CUDA GPU 가속 활성화 (float16)")
            except Exception as exc:
                self._ts_log("warn", f"CUDA 실패 → CPU fallback ({type(exc).__name__})")
        if model is None:
            try:
                self._ts_log("info", f"CPU INT8 모드: {model_name} 로드 중 ...")
                model = WhisperModel(model_name, device="cpu", compute_type="int8")
                self._ts_log("ok", "CPU INT8 활성화 (faster-whisper 4배 가속)")
            except Exception as exc:
                self._ts_log("error", f"모델 로드 실패: {exc}")
                self._ts_finish(False); return
        self._ts_log("ok", f"모델 로드 완료: {model_name}")
        lang_code = next((l[1] for l in self._ts_LANGS if l[0] == self._ts_lang_var.get()), None)
        out_fmt = self._ts_fmt_var.get()
        out_dir_raw = self._ts_outdir_var.get().strip()
        total = len(self._ts_queue); converted = 0
        for idx, fpath in enumerate(list(self._ts_queue), 1):
            if not self._ts_running:
                self._ts_log("warn", "중지됨"); break
            self._ts_set_status(f"변환 중 ({idx}/{total}) — {_P(fpath).name}")
            self._ts_log("info", f"[{idx}/{total}] {_P(fpath).name}")
            if self._ts_convert_one(model, fpath, lang_code, out_fmt, out_dir_raw):
                converted += 1
        self._ts_finish(converted > 0)

    @staticmethod
    def _ts_load_audio(fpath, sr=16000):
        import numpy as _np, subprocess as _sp
        proc = _sp.run(
            [_TS_FFMPEG_BIN, "-nostdin", "-threads", "0",
             "-i", fpath, "-f", "s16le", "-ac", "1",
             "-acodec", "pcm_s16le", "-ar", str(sr), "pipe:1"],
            stdout=_sp.PIPE, stderr=_sp.PIPE, creationflags=_TS_NO_WIN)
        if proc.returncode != 0:
            err = proc.stderr.decode(errors="ignore")
            raise RuntimeError(f"FFmpeg 디코딩 실패: {err[-300:]}")
        raw = _np.frombuffer(proc.stdout, dtype=_np.int16).flatten().astype(_np.float32)
        return raw / 32768.0

    def _ts_convert_one(self, model, fpath, lang_code, out_fmt, out_dir_raw):
        """faster-whisper 기반 단일 파일 변환. segments는 generator — 즉시 소비하며 진행률 갱신."""
        import json as _json
        from pathlib import Path as _P
        if not os.path.exists(fpath):
            self._ts_log("error", f"파일 없음: {fpath}"); return False
        self._ts_log("info", "Whisper 추론 시작 ...")
        try:
            segments_iter, info = model.transcribe(fpath, language=lang_code, beam_size=5, vad_filter=True)
        except Exception as exc:
            self._ts_log("error", f"추론 실패: {exc}"); return False
        try:
            duration = float(getattr(info, "duration", 0.0) or 0.0)
            self._ts_log("info", f"감지 언어: {info.language} (확률 {info.language_probability:.2f}) · 길이 {duration:.1f}초")
        except Exception:
            duration = 0.0
        # 진행률 측정 — segment.end / duration
        segments = []
        last_pct = -1
        try:
            for seg in segments_iter:
                if not self._ts_running:
                    self._ts_log("warn", "사용자 중지 — 부분 결과 저장"); break
                segments.append({"start": float(seg.start), "end": float(seg.end), "text": seg.text})
                if duration > 0:
                    pct = int((seg.end / duration) * 100)
                    if pct != last_pct:
                        last_pct = pct
                        self._ts_set_status(f"추론 중 {pct}% — {_P(fpath).name}")
        except Exception as exc:
            self._ts_log("error", f"세그먼트 수집 실패: {exc}"); return False
        if not segments:
            self._ts_log("warn", "세그먼트 0건 — 무음 또는 인식 실패")
            return False
        full_text = " ".join(s["text"].strip() for s in segments)
        if out_dir_raw == "(입력 파일과 동일)" or not os.path.isdir(out_dir_raw):
            out_dir = str(_P(fpath).parent)
        else:
            out_dir = out_dir_raw
        stem = _P(fpath).stem
        out_path = os.path.join(out_dir, f"{stem}.{out_fmt}")
        try:
            if out_fmt == "txt":
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(full_text.strip())
            elif out_fmt == "srt":
                with open(out_path, "w", encoding="utf-8") as f:
                    for i, seg in enumerate(segments, 1):
                        f.write(f"{i}\n{self._ts_tc(seg['start'])} --> {self._ts_tc(seg['end'])}\n{seg['text'].strip()}\n\n")
            elif out_fmt == "vtt":
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write("WEBVTT\n\n")
                    for seg in segments:
                        f.write(f"{self._ts_tc(seg['start'],vtt=True)} --> {self._ts_tc(seg['end'],vtt=True)}\n{seg['text'].strip()}\n\n")
            elif out_fmt == "tsv":
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write("start\tend\ttext\n")
                    for seg in segments:
                        f.write(f"{seg['start']:.3f}\t{seg['end']:.3f}\t{seg['text'].strip()}\n")
            elif out_fmt == "json":
                with open(out_path, "w", encoding="utf-8") as f:
                    _json.dump({"text": full_text, "segments": segments,
                                "language": getattr(info, "language", None),
                                "duration": duration}, f, ensure_ascii=False, indent=2)
            self._ts_last_out_dir = out_dir
            self._ts_log("ok", f"저장: {out_path} ({len(segments)} segments)")
            return True
        except Exception as exc:
            self._ts_log("error", f"저장 실패: {exc}"); return False

    @staticmethod
    def _ts_tc(s: float, vtt: bool = False) -> str:
        h, r = divmod(int(s), 3600); m, sec = divmod(r, 60)
        ms = int((s - int(s)) * 1000)
        return f"{h:02d}:{m:02d}:{sec:02d}{'.' if vtt else ','}{ms:03d}"

    def _ts_log(self, level, msg):
        from datetime import datetime as _dt
        def _ins():
            line = f"[{_dt.now().strftime('%H:%M:%S')}][{level.upper()}] {msg}\n"
            self._ts_log_box.config(state="normal")
            self._ts_log_box.insert("end", line, level)
            self._ts_log_box.see("end")
            self._ts_log_box.config(state="disabled")
        self.root.after(0, _ins)

    def _ts_set_status(self, msg):
        self.root.after(0, lambda: self._ts_status_var.set(msg))

    def _ts_finish(self, success=True):
        def _r():
            self._ts_running = False
            self._ts_progress.stop()
            self._ts_run_btn.config(state="normal")
            self._ts_stop_btn.config(state="disabled")
            self._ts_set_status("완료")
            self._ts_log("ok", "── 모두 완료 ──")
        self.root.after(0, _r)

    def _init_autoshot(self, parent):
        """오토샷 탭 — AutoShotPanel 직접 통합 (v7.11)."""
        self._as_panel = AutoShotPanel(parent)


    def _init_promo(self, parent):
        """우측 끝 홍보 탭. 제품 카드 + 연락처 + 회전 광고 프리뷰."""
        tk.Label(parent, text="◈  Vibe Toolsmith  ─  Product Lineup",
                 fg="#f1c40f", bg="#111", font=("맑은 고딕", 10, "bold"), pady=5
                 ).pack(fill=tk.X)
        # v6.9.4 저작권 등록 명기 띠
        tk.Label(parent,
                 text="⚖  한국저작권위원회 등록완료 — 웹캡처 C-2026-021650 · 오토샷 C-2026-022057 · 법무킷 C-2026-022058",
                 fg="#9ab8d4", bg="#0d1929",
                 font=("맑은 고딕", 8, "bold"), pady=4
                 ).pack(fill=tk.X)

        # ── 제품 카드 (스크롤 래퍼) ──
        _scroll_outer = tk.Frame(parent, bg="#0a0a0a")
        _scroll_outer.pack(fill=tk.BOTH, expand=False, padx=8, pady=(6, 4))
        _card_canvas = tk.Canvas(_scroll_outer, bg="#0a0a0a",
                                 highlightthickness=0, height=230)
        _card_vbar   = tk.Scrollbar(_scroll_outer, orient="vertical",
                                    command=_card_canvas.yview)
        _card_vbar.pack(side=tk.RIGHT, fill=tk.Y)
        _card_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        _card_canvas.configure(yscrollcommand=_card_vbar.set)
        card_wrap = tk.Frame(_card_canvas, bg="#0a0a0a")
        _card_win = _card_canvas.create_window((0, 0), window=card_wrap, anchor="nw")
        card_wrap.bind("<Configure>",
                       lambda e: _card_canvas.configure(
                           scrollregion=_card_canvas.bbox("all")))
        _card_canvas.bind("<Configure>",
                          lambda e: _card_canvas.itemconfig(_card_win, width=e.width))
        # 마우스 휠 스크롤 바인딩
        def _on_mousewheel(event):
            _card_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        _card_canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # 법무킷 카드 (현재 앱)
        card_lgk = tk.Frame(card_wrap, bg="#1a2332",
                            highlightthickness=1, highlightbackground="#2a5298")
        card_lgk.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_lgk, text="📋  법무킷 (ClickLegalKit)",
                 fg="#79b8ff", bg="#1a2332",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_lgk,
                 text=("호증 PDF 일괄 병합 · 갑호증 목록 자동 생성 · 팩스 TIFF 다중 프레임 병합\n"
                       "전자소송 19.5MB 자동 분할 · 오타 허용 퍼지 검색 · 증거목록 3종 출력\n"
                       "법제처 Open API 판례 일괄 수집 (키워드·본문 2단계 필터)"),
                 fg="#c8d4e4", bg="#1a2332", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 6))
        tk.Label(card_lgk, text=f"현재 실행 빌드: {BUILD_NUMBER}  |  {FREE_BUILD_ID}",
                 fg="#5a8abf", bg="#1a2332",
                 font=("Consolas", 8), anchor="w", padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 2))
        tk.Button(card_lgk, text="⬡  GitHub →  github.com/bombc5003  (저장소 준비중)",
                  fg="#4a7abf", bg="#1a2332", activeforeground="#79b8ff",
                  activebackground="#1a2332", relief="flat", borderwidth=0,
                  cursor="hand2", font=("맑은 고딕", 8), anchor="w", padx=10, pady=3,
                  command=lambda: webbrowser.open(
                      "https://github.com/bombc5003")
                  ).pack(fill=tk.X, pady=(0, 4))

        # 오토샷 카드
        card_aus = tk.Frame(card_wrap, bg="#1a2a1a",
                            highlightthickness=1, highlightbackground="#2a8d5f")
        card_aus.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_aus, text="🎯  오토샷 (autoshot)",
                 fg="#6dd3a0", bg="#1a2a1a",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_aus,
                 text=("지정 영역 자동 캡처 · 회전 광고 상·하단 캡션 띠\n"
                       "머신 핑거프린트 7요소 HMAC 보안 빌드 ID\n"
                       "단일 .exe 배포 · 폐쇄망 오프라인 원칙"),
                 fg="#cce4d4", bg="#1a2a1a", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 2))
        tk.Button(card_aus, text="⬡  GitHub →  github.com/bombc5003/autoshot",
                  fg="#3a8d5f", bg="#1a2a1a", activeforeground="#6dd3a0",
                  activebackground="#1a2a1a", relief="flat", borderwidth=0,
                  cursor="hand2", font=("맑은 고딕", 8), anchor="w", padx=10, pady=3,
                  command=lambda: webbrowser.open(
                      "https://github.com/bombc5003/autoshot")
                  ).pack(fill=tk.X, pady=(0, 4))

        # ClickTalkScript 카드 (v6.8.5 신설)
        card_cts = tk.Frame(card_wrap, bg="#1a1a2e",
                            highlightthickness=1, highlightbackground="#6b3fa0")
        card_cts.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_cts, text="🎙  녹취록 생성기 (ClickTalkScript)",
                 fg="#c39dff", bg="#1a1a2e",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_cts,
                 text=("음성 파일 → 한국어 녹취록 자동 변환 · 머신ID 라이선스 보안\n"
                       "타임스탬프 싱크 · 화자 구분 지원 · 오프라인 변환 원칙\n"
                       "단일 .exe 배포 · 법정 제출용 포맷 출력"),
                 fg="#c8bde4", bg="#1a1a2e", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 2))
        tk.Button(card_cts,
                  text="⬡  GitHub →  github.com/bombc5003/ClickTalkScript",
                  fg="#6b3fa0", bg="#1a1a2e", activeforeground="#c39dff",
                  activebackground="#1a1a2e", relief="flat", borderwidth=0,
                  cursor="hand2", font=("맑은 고딕", 8), anchor="w", padx=10, pady=3,
                  command=lambda: webbrowser.open(
                      "https://github.com/bombc5003/ClickTalkScript/releases/tag/v1.67")
                  ).pack(fill=tk.X, pady=(0, 4))

        # 개발 의뢰 카드 (v6.8.7 신설)
        card_req = tk.Frame(card_wrap, bg="#2a1a0a",
                            highlightthickness=1, highlightbackground="#b05a00")
        card_req.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_req, text="🛠  개발 의뢰 접수",
                 fg="#ffaa44", bg="#2a1a0a",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_req,
                 text=("사무 자동화 · 포렌식 계열 · 법무 보조 도구 전문\n"
                       "Windows 단일 실행본(.exe) · 폐쇄망·오프라인 동작 원칙\n"
                       "나홀로소송 보조 도구 · 증거 정리 자동화 · 기록 분석 도구 등 환영\n"
                       "✦  업계 최저가 보장  ✦"),
                 fg="#e0c9a0", bg="#2a1a0a", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 2))
        tk.Label(card_req, text="문의: bc5103@naver.com  ·  010-2272-7030",
                 fg="#b07030", bg="#2a1a0a",
                 font=("맑은 고딕", 8, "bold"), anchor="w", padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 4))

        # ── 개발 후원 카드 (v7.0.9 신설) ──
        card_donate = tk.Frame(card_wrap, bg="#0d1a0d",
                               highlightthickness=1, highlightbackground="#2d6a2d")
        card_donate.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_donate, text="💚  개발 후원",
                 fg="#6dd36d", bg="#0d1a0d",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_donate,
                 text=("법무킷이 도움이 되셨다면 커피 한 잔 값의 후원으로\n"
                       "지속적인 개발을 응원해 주세요!"),
                 fg="#b0d4b0", bg="#0d1a0d", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X)
        tk.Label(card_donate,
                 text="카카오페이 송금  ▶  010-2272-7030  (박병진)",
                 fg="#6dd36d", bg="#0d1a0d",
                 font=("맑은 고딕", 9, "bold"), anchor="w", padx=10, pady=4
                 ).pack(fill=tk.X, pady=(0, 2))

        def _copy_kakao():
            card_donate.clipboard_clear()
            card_donate.clipboard_append("010-2272-7030")
            card_donate.update()

        tk.Button(card_donate, text="전화번호 복사",
                  command=_copy_kakao,
                  bg="#2d6a2d", fg="white", font=("맑은 고딕", 8),
                  relief="flat", padx=8, pady=3, cursor="hand2"
                  ).pack(anchor="w", padx=10, pady=(0, 8))

        # ── 라이선스 정책 카드 (v7.47 구독 모델 반영) ──
        card_lic = tk.Frame(card_wrap, bg="#1a1a2e",
                            highlightthickness=1, highlightbackground="#3a3a7a")
        card_lic.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_lic, text="📜  라이선스 정책",
                 fg="#79b8ff", bg="#1a1a2e",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_lic,
                 text=("✅  개인 사용  —  무제한 무료\n"
                       "       소송 준비·개인 문서 정리·학습 목적 등 개인 용도는 제한 없이 사용 가능\n\n"
                       "💼  상업적 사용  —  구독 라이선스\n"
                       "       사무소·법인·기관 등 영리 목적 사용 시 구독 후 이용\n"
                       "       📅  월정액  —  문의 요망\n"
                       "       📆  연간    —  월정액 대비 30% 할인 (선결제)"),
                 fg="#c8d4e4", bg="#1a1a2e", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_lic,
                 text="구독 문의:  dede5003@gmail.com  ·  010-2272-7030",
                 fg="#79b8ff", bg="#1a1a2e",
                 font=("맑은 고딕", 8, "bold"), anchor="w", padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 6))

        # ── 엔젤 광고주 카드 (v7.47 신설) ──
        card_angel = tk.Frame(card_wrap, bg="#1a0d2e",
                              highlightthickness=1, highlightbackground="#7b3fa0")
        card_angel.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_angel, text="👼  엔젤 광고주 모집",
                 fg="#d4aaff", bg="#1a0d2e",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_angel,
                 text=("법무킷 하단 캡션 띠에 귀사·브랜드 광고를 게재합니다.\n"
                       "PDF 출력물마다 노출 — 문서가 공유될수록 더 많이 보입니다.\n\n"
                       "🌟  엔젤 광고주 혜택\n"
                       "       ∙ 캡션 띠 고정 광고 (로테이션 우선 노출)\n"
                       "       ∙ 영구 상업용 라이선스 1카피 무상 제공\n"
                       "       ∙ 이름·브랜드 홍보탭 영구 등재\n\n"
                       "💰  광고 단가: 100만원 / 1슬롯 (협의 가능)"),
                 fg="#d4bfee", bg="#1a0d2e", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_angel,
                 text="광고 문의:  dede5003@gmail.com  ·  010-2272-7030  (박병진)",
                 fg="#d4aaff", bg="#1a0d2e",
                 font=("맑은 고딕", 8, "bold"), anchor="w", padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 6))

        # ── 연락처 블록 ──
        contact = tk.Frame(parent, bg="#1a1a1a",
                           highlightthickness=1, highlightbackground="#333")
        contact.pack(fill=tk.X, padx=8, pady=(4, 4))
        tk.Label(contact, text="✉  Contact",
                 fg="#ffc857", bg="#1a1a1a",
                 font=("맑은 고딕", 9, "bold"), anchor="w", padx=10, pady=2
                 ).pack(fill=tk.X, pady=(6, 2))
        tk.Label(contact,
                 text="박병진  bc5103@naver.com  ·  010-2272-7030",
                 fg="#cccccc", bg="#1a1a1a", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 6))

        # ── KDP 출판 도서 (스크롤) ──
        books_outer = tk.Frame(parent, bg="#0d0d0d",
                               highlightthickness=1, highlightbackground="#2a2a2a")
        books_outer.pack(fill=tk.BOTH, expand=True, padx=8, pady=(4, 8))
        tk.Label(books_outer, text="📚  개발자 출판 도서  —  Amazon Kindle",
                 fg="#f1c40f", bg="#0d0d0d",
                 font=("Consolas", 8, "bold"), anchor="w", padx=8, pady=6
                 ).pack(fill=tk.X)
        tk.Label(books_outer,
                 text="  도움이 되셨다면 책 한 권 사주세요~  ☕  개발 후원도 환영합니다!",
                 fg="#888855", bg="#0d0d0d",
                 font=("맑은 고딕", 7), anchor="w", padx=8, pady=2
                 ).pack(fill=tk.X)

        _bcanvas = tk.Canvas(books_outer, bg="#0d0d0d", highlightthickness=0)
        _bsb     = ttk.Scrollbar(books_outer, orient="vertical", command=_bcanvas.yview)
        _bcanvas.configure(yscrollcommand=_bsb.set)
        _bsb.pack(side=tk.RIGHT, fill=tk.Y)
        _bcanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        _binner = tk.Frame(_bcanvas, bg="#0d0d0d")
        _bwin   = _bcanvas.create_window((0, 0), window=_binner, anchor="nw")

        def _books_resize(e):
            _bcanvas.itemconfig(_bwin, width=e.width)
        _bcanvas.bind("<Configure>", _books_resize)
        def _books_scroll(e):
            _bcanvas.yview_scroll(int(-1*(e.delta/120)), "units")
        _bcanvas.bind_all("<MouseWheel>", _books_scroll)

        _books = [
            {
                "title": "\U0001f5a5\ufe0f  클로드AI 코웍 입문서 1",
                "desc":  ("Claude 코웍 모드로 파일 정리·업무 자동화를 비개발자도\n"
                          "바로 시작하는 실전 가이드."),
                "links": [
                    ("부크크", "https://www.bookk.co.kr/book/view/483796"),
                    ("ES",  "https://www.amazon.com/dp/B0GX638CH2"),
                    ("PT",  "https://www.amazon.com/dp/B0GX35Y7F7"),
                    ("DE",  "https://www.amazon.com/dp/B0GX7NN1T2"),
                    ("FR",  "https://www.amazon.com/dp/B0GX2RY3XC"),
                    ("JA",  "https://www.amazon.com/dp/B0GX32DVHX"),
                    ("EN",  "https://www.amazon.com/dp/B0GYPMT5L3"),
                ],
            },
            {
                "title": "\U0001f5a5\ufe0f  클로드AI 코웍 입문서 2",
                "desc":  ("에이전트 설계·MCP 연결·자동화 파이프라인 구축 실전편.\n"
                          "1권 이후 더 깊이 파고드는 고급 코웍 워크플로우 가이드.\n"
                          "※ 한국어판 출간 준비중"),
                "links": [
                    ("부크크", "https://www.bookk.co.kr/book/view/490829"),
                    ("EN",  "https://www.amazon.com/dp/B0H1832Y54"),
                    ("ES",  "https://www.amazon.com/dp/B0H185FXSX"),
                    ("DE",  "https://www.amazon.com/dp/B0H18DXTQ1"),
                    ("FR",  "https://www.amazon.com/dp/B0H18MH2X2"),
                    ("PT",  "https://www.amazon.com/dp/B0GX555JKN"),
                ],
            },
            {
                "title": "\U0001f4bb  코드를 모르는 사람의 코딩",
                "desc":  ("AI와 함께하는 코딩 완전 입문.\n"
                          "사전 지식 없이 첫날부터 실제 도구를 만들고 업무를 자동화한다."),
                "links": [
                    ("부크크", "https://www.bookk.co.kr/book/view/482300"),
                    ("YES24", "https://www.yes24.com/product/goods/188657828"),
                    ("EN",  "https://www.amazon.com/dp/B0GXL8WPTT"),
                    ("ES",  "https://www.amazon.com/dp/B0GYL323QJ"),
                    ("DE",  "https://www.amazon.com/dp/B0GX32PB4S"),
                    ("FR",  "https://www.amazon.com/dp/B0GX52PWP9"),
                    ("PT",  "https://www.amazon.com/dp/B0GYK2HH62"),
                    ("IT",  "https://www.amazon.com/dp/B0GYK2MRKG"),
                    ("NL",  "https://www.amazon.com/dp/B0GX3673WR"),
                    ("AR",  "https://www.amazon.com/dp/B0GX32KNX4"),
                    ("JA",  "https://www.amazon.com/dp/B0GYJTTLJN"),
                ],
            },
            {
                "title": "\U0001f916  클로드 몸을 얻다",
                "desc":  ("어느 날 아침, 로봇 장난감 속에 AI 클로드가 들어와 있다.\n"
                          "AI와 몸을 갖는다는 것의 의미를 따뜻하게 풀어낸 동화."),
                "links": [
                    ("EN",  "https://www.amazon.com/dp/B0GYL6M1CC"),
                    ("ES",  "https://www.amazon.com/dp/B0GX3222WP"),
                    ("DE",  "https://www.amazon.com/dp/B0GXXGSHF3"),
                    ("JA",  "https://www.amazon.com/dp/B0GYM9VYDB"),
                ],
            },
        ]

        import webbrowser as _wb
        for book in _books:
            card = tk.Frame(_binner, bg="#1a1a2e",
                            highlightthickness=1, highlightbackground="#3a3a5a")
            card.pack(fill=tk.X, padx=8, pady=4)
            tk.Label(card, text=book["title"],
                     fg="#79b8ff", bg="#1a1a2e",
                     font=("맑은 고딕", 9, "bold"), anchor="w", padx=10, pady=5
                     ).pack(fill=tk.X)
            tk.Label(card, text=book["desc"],
                     fg="#c8d4e4", bg="#1a1a2e",
                     justify="left", anchor="w",
                     font=("맑은 고딕", 8), padx=10, pady=2
                     ).pack(fill=tk.X)
            btn_row = tk.Frame(card, bg="#1a1a2e")
            btn_row.pack(fill=tk.X, padx=8, pady=(2, 6))
            for lang, url in book["links"]:
                if url.startswith("http"):
                    b = tk.Button(btn_row, text=lang,
                                  bg="#2a3a5a", fg="#79b8ff",
                                  font=("Consolas", 7, "bold"),
                                  relief=tk.FLAT, padx=6, pady=2,
                                  cursor="hand2",
                                  command=lambda u=url: _wb.open(u))
                    b.pack(side=tk.LEFT, padx=2)
                else:
                    tk.Label(btn_row, text=f"{lang}: {url}",
                             fg="#555", bg="#1a1a2e",
                             font=("Consolas", 7)).pack(side=tk.LEFT, padx=4)

        tk.Label(_binner,
                 text="Amazon Kindle에서 'Vibe Toolsmith' 검색",
                 fg="#555", bg="#0d0d0d",
                 font=("Consolas", 7), anchor="w", padx=10, pady=8
                 ).pack(fill=tk.X)

        def _update_books_scroll(e):
            _bcanvas.configure(scrollregion=_bcanvas.bbox("all"))
        _binner.bind("<Configure>", _update_books_scroll)

        # ── 하단 고정 푸터 ──
        tk.Label(parent,
                 text=f"{FIXED_CAPTION}",
                 fg="#5a5a5a", bg="#0a0a0a",
                 font=("Consolas", 7), pady=3
                 ).pack(fill=tk.X, side=tk.BOTTOM)


# ════════════════════════════════════════════════════════════════════════
# CaseCrawler — 법제처 Open API 판례 수집 엔진 (구 case_crawler v0.1.3 흡수)
# ════════════════════════════════════════════════════════════════════════
class CaseCrawler:
    """
    법제처 Open API 기반 판례 수집기.
    목록 조회 → 본문 조회 2단계 파이프라인.
    GUI 통합용으로 log_fn 콜백 지원.
    """

    BASE_LIST   = "http://www.law.go.kr/DRF/lawSearch.do"
    BASE_DETAIL = "http://www.law.go.kr/DRF/lawService.do"
    DISPLAY_PER_PAGE = 100
    REQUEST_DELAY = 0.5
    TIMEOUT = 15

    def __init__(self, oc_key, log_fn=None):
        if not oc_key:
            raise ValueError("OC 인증키가 비어있음.")
        self.oc = oc_key
        self.log_fn = log_fn or (lambda m: print(m))
        # requests 지연 import (전역 의존성 회피)
        try:
            import requests
        except ImportError:
            import subprocess as _sp, sys as _sys
            _sp.check_call([_sys.executable, "-m", "pip", "install", "requests"])
            import requests
        self._requests = requests
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "ClickLegalKit/0.67 CaseCrawler"
        })

    def fetch_list(self, query, max_cases=100):
        """판례 목록 조회. XML 응답 파싱 후 메타데이터 반환."""
        import xml.etree.ElementTree as ET
        results = []
        page = 1
        fetched = 0

        while fetched < max_cases:
            params = {
                "OC":      self.oc,
                "target":  "prec",
                "type":    "XML",
                "query":   query,
                "display": self.DISPLAY_PER_PAGE,
                "page":    page,
            }
            try:
                res = self.session.get(self.BASE_LIST, params=params, timeout=self.TIMEOUT)
                res.raise_for_status()
            except Exception as e:
                # v672: 연결 끊김 계열 에러를 0건 판정으로 흡수
                err_str = str(e).lower()
                is_conn_err = ("connectionreset" in err_str
                               or "connection aborted" in err_str
                               or "forcibly closed" in err_str
                               or "강제로 끊" in err_str
                               or "10054" in err_str)
                if is_conn_err and page == 1 and not results:
                    self.log_fn(f"[INFO] 검색 결과 총 0건. '{query}' 키워드에 해당하는 판례 없음.")
                    self.log_fn("[INFO] 법제처 API는 법률 용어 단위 검색만 지원합니다.")
                    self.log_fn("[INFO] 복합 키워드는 검색 키워드를 넓게, 본문 필터로 좁히십시오.")
                else:
                    self.log_fn(f"[ERR] 목록 요청 실패 (page={page}): {e}")
                break

            # 응답 진단 (1페이지)
            if page == 1:
                if "<html" in res.text.lower() or "<!doctype" in res.text.lower():
                    self.log_fn("[ERR] HTML 응답 — OC 키 미승인 또는 파라미터 오류.")
                    break

            try:
                root = ET.fromstring(res.text)
            except ET.ParseError as e:
                self.log_fn(f"[ERR] XML 파싱 오류 (page={page}): {e}")
                break

            total_cnt_el = root.find("totalCnt")
            total_cnt = int(total_cnt_el.text) if total_cnt_el is not None and total_cnt_el.text else 0
            if page == 1:
                self.log_fn(f"[INFO] 총 {total_cnt}건 검색됨. 수집 목표: {min(total_cnt, max_cases)}건.")


    @staticmethod
    def _clean_html_tags(text):
        if not text:
            return ""
        import re as _re
        text = _re.sub(r"<[^>]+>", " ", text)
        text = (text.replace("&lt;", "<").replace("&gt;", ">")
                    .replace("&amp;", "&").replace("&quot;", '"')
                    .replace("&nbsp;", " "))
        text = _re.sub(r"\s+", " ", text).strip()
        return text



# ════════════════════════════════════════════════════════════════════════
# AutoShotPanel — 오토샷 탭 임베드 패널 (v7.11 직접 통합)
# 원본: autoshot_v3_19.py SnapDashboard → 탭 프레임 임베드 적응
# 변경: root=Tk창→parent=Frame, 창 전용 메서드 제거, 스타일 AS.TNotebook 분리
# ════════════════════════════════════════════════════════════════════════
class AutoShotPanel:
    def __init__(self, parent):
        self.root = parent          # 법무킷 탭 프레임 (Tk 창 아님)
        self.root.configure(bg="#000")
        # 창 전용 호출 제거: title / geometry / attributes-topmost
        self.save_dir = _AS_DEFAULT_SAVE_DIR
        os.makedirs(self.save_dir, exist_ok=True)
        self.pdf_dir = _AS_DEFAULT_PDF_DIR
        os.makedirs(self.pdf_dir, exist_ok=True)
        self._pdf_busy            = False
        self._pdf_cycle_active    = False
        self._pdf_cycle_thread    = None
        self._pdf_cycle_stop_event = threading.Event()
        self._pdf_cycle_count     = 0
        self._pdf_next_at         = None
        self._session_start_at    = None
        self._last_merge_at       = None
        self._force_full_merge    = False
        self._include_manual_once = False
        self._beep_enabled        = True
        self._auto_delete_merged  = False
        self._snap_serial         = 0
        self._caption_font        = self._find_caption_font()
        self._ocr_ok              = 0
        self._ocr_fail            = 0
        self._scan_cache          = {}
        self._save_timer          = None
        self._config              = self._load_config()
        self._apply_config_pre_ui()
        self._lock      = threading.Event()
        self._lock_time = 0
        self._auto_active     = False
        self._auto_thread     = None
        self._auto_stop_event = threading.Event()
        self._auto_count      = 0
        self.float_win = None
        self._build_ui()
        self._apply_config_post_ui()
        self.setup_hotkey()
        self._build_floating_window()
        self.queue_log(f"오토샷 {_AS_BUILD_NUMBER} — 법무킷 통합 탭")
        self.queue_log(f"📂 저장 경로: {self.save_dir[-30:]}")
        self.queue_log(f"📑 출력 경로: {self.pdf_dir[-30:]}")
        if not _AS_PDF_AVAILABLE:
            self.queue_log("⚠️ PyPDF2 미설치 — PDF 병합 비활성")

    # ── UI 빌드 ──────────────────────────────────────────────────────
    def _build_ui(self):
        self.dash = tk.Frame(self.root, bg="#111", bd=1, relief=tk.RIDGE)
        self.dash.pack(fill=tk.X, padx=5, pady=5, ipady=8)
        tk.Label(self.dash, text=f"■ 오토샷 {_AS_BUILD_NUMBER} ■",
                 bg="#111", fg="#bc13fe", font=("Consolas", 10, "bold")).pack()
        self._common_line1 = tk.StringVar(value="● 시스템 가동 대기")
        self._common_line2 = tk.StringVar(value="")
        common_frame = tk.Frame(self.root, bg="#0a0a0a", bd=1, relief=tk.RIDGE)
        common_frame.pack(fill=tk.X, padx=5, pady=(0, 5), ipady=4)
        tk.Label(common_frame, textvariable=self._common_line1,
                 bg="#0a0a0a", fg="#00ff41", font=("Consolas", 8),
                 anchor='w').pack(fill=tk.X, padx=6)
        tk.Label(common_frame, textvariable=self._common_line2,
                 bg="#0a0a0a", fg="#888", font=("Consolas", 8),
                 anchor='w').pack(fill=tk.X, padx=6)
        # 스타일: AS.TNotebook (법무킷 TNotebook.Tab 와 격리)
        style = ttk.Style()
        try:
            style.configure('AS.TNotebook', background="#000", borderwidth=0)
            style.configure('AS.TNotebook.Tab', background="#222", foreground="#00ff00",
                            padding=(10, 5), font=("Consolas", 8, "bold"))
            style.map('AS.TNotebook.Tab',
                      background=[('selected', '#002200')],
                      foreground=[('selected', '#00ff41')])
        except Exception:
            pass
        self.notebook = ttk.Notebook(self.root, style='AS.TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
        self.tab_capture = tk.Frame(self.notebook, bg="#000")
        self.notebook.add(self.tab_capture, text=" 캡처 ")
        self._build_capture_tab(self.tab_capture)
        self.tab_pdf = tk.Frame(self.notebook, bg="#000")
        self.notebook.add(self.tab_pdf, text=" 병합 ")
        self._build_pdf_tab_placeholder(self.tab_pdf)
        self.tab_config = tk.Frame(self.notebook, bg="#000")
        self.notebook.add(self.tab_config, text=" 설정 ")
        self._build_config_tab_placeholder(self.tab_config)

    # ── TAB1: 캡처 ────────────────────────────────────────────────
    def _build_capture_tab(self, parent):
        self.txt = scrolledtext.ScrolledText(
            parent, bg="#000", fg="#00ff00", font=("Consolas", 9), height=4)
        self.txt.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.status_var = tk.StringVar(value="● 대기")
        tk.Label(parent, textvariable=self.status_var, bg="#000", fg="#00ff41",
                 font=("Consolas", 9)).pack()
        auto_frame = tk.Frame(parent, bg="#0a0a1a", bd=1, relief=tk.RIDGE)
        auto_frame.pack(fill=tk.X, padx=5, pady=(0, 4), ipady=8)
        tk.Label(auto_frame, text="자동 촬영", bg="#0a0a1a", fg="#bc13fe",
                 font=("Consolas", 9, "bold")).pack(side=tk.LEFT, padx=8)
        tk.Label(auto_frame, text="주기(초):", bg="#0a0a1a", fg="#888",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        self.interval_var = tk.StringVar(value=str(_AS_DEFAULT_INTERVAL))
        self.interval_entry = tk.Entry(
            auto_frame, textvariable=self.interval_var,
            bg="#111", fg="#00ff00", font=("Consolas", 9),
            width=5, insertbackground="#00ff00", justify=tk.CENTER,
            relief=tk.FLAT, bd=1)
        self.interval_entry.pack(side=tk.LEFT, padx=4)
        self.auto_count_var = tk.StringVar(value="[0]")
        tk.Label(auto_frame, textvariable=self.auto_count_var,
                 bg="#0a0a1a", fg="#555", font=("Consolas", 8)).pack(side=tk.LEFT, padx=2)
        self.auto_btn_var = tk.StringVar(value="[ 자동 : 정지 ]")
        self.auto_btn = tk.Button(
            auto_frame, textvariable=self.auto_btn_var,
            bg="#1a0a00", fg="#ff6600", font=("Consolas", 9, "bold"),
            activebackground="#002200", activeforeground="#00ff00",
            relief=tk.FLAT, bd=1, command=self.toggle_auto)
        self.auto_btn.pack(side=tk.RIGHT, padx=8)
        self.progress_var    = tk.DoubleVar(value=0.0)
        self.progress_canvas = tk.Canvas(parent, height=4, bg="#111", highlightthickness=0)
        self.progress_canvas.pack(fill=tk.X, padx=5, pady=(0, 3))
        manual_frame = tk.Frame(parent, bg="#000")
        manual_frame.pack(fill=tk.X, padx=5, pady=(2, 2))
        tk.Button(manual_frame, text="[ 수동 촬영 ]", bg="#1a001a", fg="#ff00ff",
                  font=("Consolas", 11, "bold"),
                  activebackground="#330033", activeforeground="#ff66ff",
                  relief=tk.FLAT, bd=1,
                  command=lambda: self.snap_action(snap_type='MANUAL', keyword='')
                  ).pack(fill=tk.X, ipady=6)
        ctrl_frame = tk.Frame(parent, bg="#000")
        ctrl_frame.pack(fill=tk.X, padx=5, pady=5)
        tk.Button(ctrl_frame, text="[ 경로 변경 ]", bg="#222", fg="#00ff00",
                  font=("Consolas", 9, "bold"),
                  command=self.change_dir).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        self.beep_btn_var = tk.StringVar(value="[ 알림음: 켜짐 ]")
        self.beep_btn = tk.Button(
            ctrl_frame, textvariable=self.beep_btn_var, bg="#222", fg="#00ff41",
            font=("Consolas", 9, "bold"), command=self.toggle_beep)
        self.beep_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        tk.Button(ctrl_frame, text="[ 강제 해제 ]", bg="#222", fg="#ff4444",
                  font=("Consolas", 9, "bold"),
                  command=self.force_unlock).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        float_frame = tk.Frame(parent, bg="#000")
        float_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        tk.Button(float_frame, text="[ 플로팅 표시 ]", bg="#001a1a", fg="#00ffff",
                  font=("Consolas", 9, "bold"),
                  activebackground="#003333", activeforeground="#66ffff",
                  relief=tk.FLAT, bd=1,
                  command=self._show_floating_window
                  ).pack(fill=tk.X, ipady=2)

    # ── TAB2: 병합 ────────────────────────────────────────────────
    def _build_pdf_tab_placeholder(self, parent):
        tk.Label(parent, text="[ 병합 출력 ]", bg="#000", fg="#bc13fe",
                 font=("Consolas", 12, "bold")).pack(pady=(5, 3))
        fmt_frame = tk.Frame(parent, bg="#0a0a1a", bd=1, relief=tk.RIDGE)
        fmt_frame.pack(fill=tk.X, padx=5, pady=(0, 4), ipady=5)
        tk.Label(fmt_frame, text="출력 포맷:", bg="#0a0a1a", fg="#bc13fe",
                 font=("Consolas", 9, "bold")).pack(side=tk.LEFT, padx=8)
        self.merge_format_var = tk.StringVar(value=_AS_MERGE_FORMAT_DEFAULT)
        fmt_combo = ttk.Combobox(
            fmt_frame, textvariable=self.merge_format_var,
            values=_AS_MERGE_FORMATS, state="readonly",
            font=("Consolas", 9), width=8)
        fmt_combo.pack(side=tk.LEFT, padx=4)
        fmt_combo.bind("<<ComboboxSelected>>", lambda _: self._save_config())
        tk.Label(fmt_frame, text="(pdf/gif/apng/webp)", bg="#0a0a1a", fg="#555",
                 font=("Consolas", 8)).pack(side=tk.LEFT, padx=4)
        self.pdf_txt = scrolledtext.ScrolledText(
            parent, bg="#000", fg="#00ff00", font=("Consolas", 9), height=3)
        self.pdf_txt.pack(fill=tk.BOTH, expand=False, padx=5, pady=5)
        self.pdf_status_var = tk.StringVar(value="● 대기")
        tk.Label(parent, textvariable=self.pdf_status_var, bg="#000", fg="#00ff41",
                 font=("Consolas", 9)).pack()
        info_frame = tk.Frame(parent, bg="#0a0a1a", bd=1, relief=tk.RIDGE)
        info_frame.pack(fill=tk.X, padx=5, pady=(4, 4), ipady=6)
        tk.Label(info_frame, text="출력 경로", bg="#0a0a1a", fg="#bc13fe",
                 font=("Consolas", 9, "bold")).pack(side=tk.LEFT, padx=8)
        self.pdf_dir_var = tk.StringVar(value=self.pdf_dir[-32:])
        tk.Label(info_frame, textvariable=self.pdf_dir_var, bg="#0a0a1a", fg="#888",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        merge_info_frame = tk.Frame(parent, bg="#0a0a0a")
        merge_info_frame.pack(fill=tk.X, padx=5, pady=(0, 2))
        self.pdf_mode_var = tk.StringVar(value="병합 모드: 전체 (최초)")
        tk.Label(merge_info_frame, textvariable=self.pdf_mode_var,
                 bg="#0a0a0a", fg="#888", font=("Consolas", 8), anchor='w').pack(fill=tk.X, padx=4)
        self.pdf_last_merge_var = tk.StringVar(value="마지막 병합: 미병합")
        tk.Label(merge_info_frame, textvariable=self.pdf_last_merge_var,
                 bg="#0a0a0a", fg="#888", font=("Consolas", 8), anchor='w').pack(fill=tk.X, padx=4)
        ctrl_frame = tk.Frame(parent, bg="#000")
        ctrl_frame.pack(fill=tk.X, padx=5, pady=5)
        tk.Button(ctrl_frame, text="[ 즉시 병합 ]", bg="#222", fg="#00ff41",
                  font=("Consolas", 9, "bold"),
                  command=self._on_pdf_merge_now).pack(
                  side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        tk.Button(ctrl_frame, text="[ 출력 경로 변경 ]", bg="#222", fg="#00ff00",
                  font=("Consolas", 9, "bold"),
                  command=self._on_change_pdf_dir).pack(
                  side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        full_btn_frame = tk.Frame(parent, bg="#000")
        full_btn_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        tk.Button(full_btn_frame, text="[ 전체 병합 (강제) ]",
                  bg="#1a1a00", fg="#ffaa00",
                  font=("Consolas", 9, "bold"),
                  command=self._on_pdf_merge_full).pack(fill=tk.X, padx=2)
        del_btn_frame = tk.Frame(parent, bg="#000")
        del_btn_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        self.del_btn_var = tk.StringVar(value="[ 병합 후 삭제: 꺼짐 ]")
        self.del_btn = tk.Button(
            del_btn_frame, textvariable=self.del_btn_var,
            bg="#1a0000", fg="#666", font=("Consolas", 9, "bold"),
            activebackground="#330000", activeforeground="#ff4444",
            relief=tk.FLAT, bd=1, command=self.toggle_auto_delete)
        self.del_btn.pack(fill=tk.X, padx=2)
        open_btn_frame = tk.Frame(parent, bg="#000")
        open_btn_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        tk.Button(open_btn_frame, text="[ 출력 폴더 열기 ]",
                  bg="#0a0a2a", fg="#79b8ff", font=("Consolas", 9, "bold"),
                  command=self._on_open_pdf_dir).pack(
                  side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        tk.Button(open_btn_frame, text="[ 캡처 폴더 열기 ]",
                  bg="#0a0a2a", fg="#79b8ff", font=("Consolas", 9, "bold"),
                  command=self._on_open_save_dir).pack(
                  side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        cycle_frame = tk.Frame(parent, bg="#0a0a1a", bd=1, relief=tk.RIDGE)
        cycle_frame.pack(fill=tk.X, padx=5, pady=(4, 4), ipady=8)
        tk.Label(cycle_frame, text="자동 병합", bg="#0a0a1a", fg="#bc13fe",
                 font=("Consolas", 9, "bold")).pack(side=tk.LEFT, padx=8)
        tk.Label(cycle_frame, text="주기(분):", bg="#0a0a1a", fg="#888",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        self.pdf_cycle_var = tk.StringVar(value=str(_AS_PDF_CYCLE_DEFAULT))
        self.pdf_cycle_entry = tk.Entry(
            cycle_frame, textvariable=self.pdf_cycle_var,
            bg="#111", fg="#00ff00", font=("Consolas", 9),
            width=6, insertbackground="#00ff00", justify=tk.CENTER,
            relief=tk.FLAT, bd=1)
        self.pdf_cycle_entry.pack(side=tk.LEFT, padx=4)
        self.pdf_cycle_count_var = tk.StringVar(value="[0]")
        tk.Label(cycle_frame, textvariable=self.pdf_cycle_count_var,
                 bg="#0a0a1a", fg="#555", font=("Consolas", 8)).pack(side=tk.LEFT, padx=2)
        self.pdf_cycle_btn_var = tk.StringVar(value="[ 자동 병합: 정지 ]")
        self.pdf_cycle_btn = tk.Button(
            cycle_frame, textvariable=self.pdf_cycle_btn_var,
            bg="#1a0a00", fg="#ff6600", font=("Consolas", 9, "bold"),
            activebackground="#002200", activeforeground="#00ff00",
            relief=tk.FLAT, bd=1, command=self.toggle_pdf_cycle)
        self.pdf_cycle_btn.pack(side=tk.RIGHT, padx=8)
        self.pdf_next_var = tk.StringVar(value="다음 생성: ─")
        tk.Label(parent, textvariable=self.pdf_next_var, bg="#000", fg="#888",
                 font=("Consolas", 8)).pack(pady=(2, 5))

    # ── TAB3: 설정 ────────────────────────────────────────────────
    def _build_config_tab_placeholder(self, parent):
        tk.Label(parent, text="[ 설정 ]", bg="#000", fg="#bc13fe",
                 font=("Consolas", 12, "bold")).pack(pady=(15, 5))
        info_frame = tk.Frame(parent, bg="#0a0a1a", bd=1, relief=tk.RIDGE)
        info_frame.pack(fill=tk.X, padx=5, pady=4, ipady=6)
        tk.Label(info_frame, text="빌드 정보", bg="#0a0a1a", fg="#bc13fe",
                 font=("Consolas", 9, "bold"), anchor='w').pack(fill=tk.X, padx=8, pady=(2, 4))
        tk.Label(info_frame, text=f"  제호: 오토샷(autoshot)",
                 bg="#0a0a1a", fg="#888", font=("Consolas", 8), anchor='w').pack(fill=tk.X, padx=8)
        tk.Label(info_frame, text=f"  빌드: {_AS_BUILD_NUMBER}  /  식별자: {_AS_INSTANCE_NAME}",
                 bg="#0a0a1a", fg="#888", font=("Consolas", 8), anchor='w').pack(fill=tk.X, padx=8)
        tk.Label(info_frame, text=f"  설정: {os.path.basename(_AS_CONFIG_PATH)}",
                 bg="#0a0a1a", fg="#888", font=("Consolas", 8), anchor='w').pack(fill=tk.X, padx=8)
        path_frame = tk.Frame(parent, bg="#0a0a1a", bd=1, relief=tk.RIDGE)
        path_frame.pack(fill=tk.X, padx=5, pady=4, ipady=6)
        tk.Label(path_frame, text="저장 경로", bg="#0a0a1a", fg="#bc13fe",
                 font=("Consolas", 9, "bold"), anchor='w').pack(fill=tk.X, padx=8, pady=(2, 4))
        sd_row = tk.Frame(path_frame, bg="#0a0a1a")
        sd_row.pack(fill=tk.X, padx=8, pady=2)
        tk.Label(sd_row, text="  캡처:", bg="#0a0a1a", fg="#888",
                 font=("Consolas", 8), width=8, anchor='w').pack(side=tk.LEFT)
        self.cfg_save_dir_var = tk.StringVar(value=self.save_dir)
        tk.Label(sd_row, textvariable=self.cfg_save_dir_var, bg="#0a0a1a",
                 fg="#00ff41", font=("Consolas", 8), anchor='w').pack(
                 side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(sd_row, text="변경", bg="#222", fg="#00ff00",
                  font=("Consolas", 8, "bold"), padx=6,
                  command=self._on_cfg_change_save_dir).pack(side=tk.RIGHT)
        pd_row = tk.Frame(path_frame, bg="#0a0a1a")
        pd_row.pack(fill=tk.X, padx=8, pady=2)
        tk.Label(pd_row, text="  출력:", bg="#0a0a1a", fg="#888",
                 font=("Consolas", 8), width=8, anchor='w').pack(side=tk.LEFT)
        self.cfg_pdf_dir_var = tk.StringVar(value=self.pdf_dir)
        tk.Label(pd_row, textvariable=self.cfg_pdf_dir_var, bg="#0a0a1a",
                 fg="#00ff41", font=("Consolas", 8), anchor='w').pack(
                 side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(pd_row, text="변경", bg="#222", fg="#00ff00",
                  font=("Consolas", 8, "bold"), padx=6,
                  command=self._on_cfg_change_pdf_dir).pack(side=tk.RIGHT)
        op_frame = tk.Frame(parent, bg="#0a0a1a", bd=1, relief=tk.RIDGE)
        op_frame.pack(fill=tk.X, padx=5, pady=4, ipady=6)
        tk.Label(op_frame, text="운용 설정 (현재 값)", bg="#0a0a1a", fg="#bc13fe",
                 font=("Consolas", 9, "bold"), anchor='w').pack(fill=tk.X, padx=8, pady=(2, 4))
        tk.Label(op_frame, textvariable=self._cfg_interval_view(),
                 bg="#0a0a1a", fg="#888", font=("Consolas", 8), anchor='w').pack(fill=tk.X, padx=8)
        tk.Label(op_frame, textvariable=self._cfg_pdf_cycle_view(),
                 bg="#0a0a1a", fg="#888", font=("Consolas", 8), anchor='w').pack(fill=tk.X, padx=8)
        tk.Label(op_frame, textvariable=self._cfg_beep_view(),
                 bg="#0a0a1a", fg="#888", font=("Consolas", 8), anchor='w').pack(fill=tk.X, padx=8)
        cfg_ctrl_frame = tk.Frame(parent, bg="#000")
        cfg_ctrl_frame.pack(fill=tk.X, padx=5, pady=8)
        tk.Button(cfg_ctrl_frame, text="[ 설정 다시 로드 ]", bg="#222", fg="#00ff00",
                  font=("Consolas", 9, "bold"),
                  command=self._on_reload_config).pack(
                  side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        tk.Button(cfg_ctrl_frame, text="[ 설정 폴더 열기 ]", bg="#222", fg="#00ff00",
                  font=("Consolas", 9, "bold"),
                  command=self._on_open_config_folder).pack(
                  side=tk.LEFT, expand=True, fill=tk.X, padx=2)

    # ── 자동 촬영 ────────────────────────────────────────────────
    def toggle_auto(self):
        if not self._auto_active:
            self._start_auto()
        else:
            self._stop_auto()

    def _get_interval(self):
        try:
            v = float(self.interval_var.get())
        except ValueError:
            self.interval_var.set(str(_AS_DEFAULT_INTERVAL))
            return float(_AS_DEFAULT_INTERVAL)
        if v < _AS_CAPTURE_INTERVAL_MIN:
            self.interval_var.set(str(_AS_CAPTURE_INTERVAL_MIN))
            return float(_AS_CAPTURE_INTERVAL_MIN)
        if v > _AS_CAPTURE_INTERVAL_MAX:
            self.interval_var.set(str(_AS_CAPTURE_INTERVAL_MAX))
            return float(_AS_CAPTURE_INTERVAL_MAX)
        return v

    def _start_auto(self):
        interval = self._get_interval()
        self._auto_active = True
        self._auto_stop_event.clear()
        self._auto_count = 0
        self.auto_count_var.set("[0]")
        self.interval_entry.config(state=tk.DISABLED)
        self.auto_btn_var.set("[ 자동 : 가동 ]")
        self.auto_btn.config(bg="#002200", fg="#00ff00")
        self.status_var.set(f"⏱ 자동 {interval:.0f}초")
        self._session_start_at = datetime.datetime.now()
        self._auto_thread = threading.Thread(
            target=self._auto_loop, args=(interval,), daemon=True)
        self._auto_thread.start()
        self.queue_log(f"⏱ 자동촬영 시작 — 주기: {interval:.1f}초")
        self.root.after(0, self._refresh_pdf_info_labels)
        self._save_config()

    def _stop_auto(self):
        self._auto_active = False
        self._auto_stop_event.set()
        self.auto_btn_var.set("[ 자동 : 정지 ]")
        self.auto_btn.config(bg="#1a0a00", fg="#ff6600")
        self.interval_entry.config(state=tk.NORMAL)
        self.status_var.set("● 대기")
        self._draw_progress(0.0)
        self.queue_log(f"⏹ 자동촬영 정지 — 누적: {self._auto_count}장")

    def _auto_loop(self, interval):
        elapsed = 0.0
        tick    = 0.1
        while not self._auto_stop_event.is_set():
            elapsed += tick
            progress = min(elapsed / interval, 1.0)
            self.root.after(0, lambda p=progress: self._draw_progress(p))
            if elapsed >= interval:
                elapsed = 0.0
                self._auto_count += 1
                cnt = self._auto_count
                self.root.after(0, lambda c=cnt: self.auto_count_var.set(f"[{c}]"))
                self.snap_action(snap_type='AUTO', keyword='')
            _time.sleep(tick)
        self.root.after(0, lambda: self._draw_progress(0.0))

    def _draw_progress(self, ratio):
        self.progress_canvas.delete("all")
        w = self.progress_canvas.winfo_width()
        if w < 2:
            return
        filled = int(w * ratio)
        self.progress_canvas.create_rectangle(0, 0, w, 4, fill="#1a1a1a", outline="")
        color = "#00ff41" if ratio < 0.8 else "#ff6600"
        if filled > 0:
            self.progress_canvas.create_rectangle(0, 0, filled, 4, fill=color, outline="")

    def change_dir(self):
        new_path = filedialog.askdirectory(initialdir=self.save_dir, title="저장 폴더 선택")
        if new_path:
            self.save_dir = new_path
            os.makedirs(self.save_dir, exist_ok=True)
            self.queue_log(f"📂 경로 변경: {self.save_dir[-30:]}")
            self._save_config()

    def setup_hotkey(self):
        pass  # keyboard 라이브러리 비의존 (v1.7 폐기)

    # ── 캡처 실행 ────────────────────────────────────────────────
    def snap_action(self, snap_type='MANUAL', keyword=''):
        if self._lock.is_set():
            if _time.time() - self._lock_time > _AS_LOCK_TIMEOUT:
                self._lock.clear()
        if not self._lock.is_set():
            self._lock.set()
            self._lock_time = _time.time()
            threading.Thread(target=self._execute_snap,
                             args=(snap_type, keyword), daemon=True).start()

    def _execute_snap(self, snap_type='MANUAL', keyword=''):
        import re as _re
        tmp_path = None
        now = None
        try:
            if _pyautogui is None:
                self.root.after(0, lambda: self.queue_log("❌ pyautogui 미설치 — 캡처 불가"))
                return
            now = datetime.datetime.now()
            self._beep_safe(800, 80)
            type_tag = 'AUTO' if snap_type == 'AUTO' else 'MANUAL'
            if keyword:
                safe_kw = _re.sub(r'[\\/:*?"<>|\s]', '_', keyword)[:15]
                tmp_name = f"autoshot_{type_tag}_{safe_kw}_{now.strftime('%H%M%S')}.png"
            else:
                tmp_name = f"autoshot_{type_tag}_{now.strftime('%Y%m%d_%H%M%S')}.png"
            tmp_path = os.path.join(self.save_dir, tmp_name)
            screenshot = _pyautogui.screenshot()
            self._snap_serial += 1
            img_with_caption = self._overlay_caption_mem(
                screenshot, now, type_tag, self._snap_serial)
            img_with_caption.save(tmp_path, "PNG")
            self._beep_safe(1200, 120)
            self.root.after(0, lambda f=tmp_name: self.queue_log(f"📸 저장: {f}"))
        except Exception as err:
            self.root.after(0, lambda m=str(err): self.queue_log(f"❌ 캡처 오류: {m}"))
            tmp_path = None
        finally:
            self._lock.clear()
        if tmp_path and now and os.path.exists(tmp_path):
            threading.Thread(target=self._rename_with_ocr,
                             args=(tmp_path, now, snap_type, keyword), daemon=True).start()

    def _rename_with_ocr(self, tmp_path, now, snap_type='MANUAL', trigger_kw=''):
        import re as _re
        type_tag = 'AUTO' if snap_type == 'AUTO' else 'MANUAL'
        try:
            ocr_kw = ""
            if not ocr_kw and os.path.exists(_AS_TESS_PATH):
                try:
                    result = subprocess.run(
                        [_AS_TESS_PATH, tmp_path, 'stdout', '-l', 'kor+eng'],
                        capture_output=True, text=True,
                        encoding='utf-8', errors='ignore', timeout=10,
                        creationflags=_AS_CREATE_NO_WINDOW,
                    )
                    text  = result.stdout
                    words = _re.findall(r'[가-힣A-Za-z0-9]{2,}', text)
                    ocr_kw = "_".join(words[:2]) if words else ""
                except Exception as te:
                    self.root.after(0, lambda m=str(te): self.queue_log(f"Tesseract 실패: {m}"))
                    ocr_kw = ""
            if ocr_kw:
                self._ocr_ok += 1
                import re as _re2
                new_name = _re2.sub(r'[\/:*?"<>|]', '',
                                    f"autoshot_{type_tag}_{ocr_kw}_{now.strftime('%H%M%S')}.png")
                new_path = os.path.join(self.save_dir, new_name)
                if not os.path.exists(new_path):
                    os.rename(tmp_path, new_path)
                    self.root.after(0, lambda f=new_name: self.queue_log(f"🏷️ 이름변경: {f}"))
            else:
                self._ocr_fail += 1
        except Exception as err:
            self._ocr_fail += 1
            self.root.after(0, lambda m=str(err): self.queue_log(f"⚠️ OCR 건너뜀: {m}"))

    # ── PDF 병합 ─────────────────────────────────────────────────
    def _on_pdf_merge_now(self):
        if self._pdf_busy:
            self.pdf_log("⚠️ 병합 진행 중 — 대기")
            return
        self._include_manual_once = True
        threading.Thread(target=self._dispatch_merge, daemon=True).start()

    def _on_pdf_merge_full(self):
        if self._pdf_busy:
            self.pdf_log("⚠️ 병합 진행 중 — 대기")
            return
        self._force_full_merge = True
        self._include_manual_once = True
        self.pdf_log("⚡ 강제 전체 병합 모드")
        threading.Thread(target=self._dispatch_merge, daemon=True).start()

    def _refresh_pdf_info_labels(self):
        try:
            _, mode_label = self._decide_merge_filter()
            self.pdf_mode_var.set(f"병합 모드: {mode_label}")
        except Exception:
            pass
        try:
            if self._last_merge_at:
                self.pdf_last_merge_var.set(
                    f"마지막 병합: {self._last_merge_at.strftime('%H:%M:%S')}")
            else:
                self.pdf_last_merge_var.set("마지막 병합: 미병합")
        except Exception:
            pass

    def _on_change_pdf_dir(self):
        new_path = filedialog.askdirectory(initialdir=self.pdf_dir, title="출력 폴더 선택")
        if new_path:
            self.pdf_dir = new_path
            os.makedirs(self.pdf_dir, exist_ok=True)
            self.pdf_dir_var.set(self.pdf_dir[-32:])
            self.pdf_log(f"📂 PDF 경로 변경: {self.pdf_dir[-30:]}")
            self._save_config()

    def _on_open_pdf_dir(self):
        target = self.pdf_dir
        if not os.path.isdir(target):
            os.makedirs(target, exist_ok=True)
        try:
            os.startfile(target) if sys.platform == "win32" else \
                subprocess.Popen(["open" if sys.platform == "darwin" else "xdg-open", target])
            self.pdf_log(f"📂 PDF 폴더: {target[-30:]}")
        except Exception as e:
            self.pdf_log(f"[ERR] 폴더 열기 실패: {e}")

    def _on_open_save_dir(self):
        target = self.save_dir
        if not os.path.isdir(target):
            os.makedirs(target, exist_ok=True)
        try:
            os.startfile(target) if sys.platform == "win32" else \
                subprocess.Popen(["open" if sys.platform == "darwin" else "xdg-open", target])
            self.pdf_log(f"📂 캡처 폴더: {target[-30:]}")
        except Exception as e:
            self.pdf_log(f"[ERR] 폴더 열기 실패: {e}")

    def _scan_png_files(self, after_at=None, include_manual=False):
        if not os.path.isdir(self.save_dir):
            return []
        files = []
        threshold = after_at.timestamp() if after_at else 0
        for fn in os.listdir(self.save_dir):
            if not fn.lower().endswith('.png'):
                continue
            is_auto   = fn.startswith('autoshot_AUTO_')
            is_manual = fn.startswith('autoshot_MANUAL_')
            if not (is_auto or (include_manual and is_manual)):
                continue
            full = os.path.join(self.save_dir, fn)
            if not os.path.isfile(full):
                continue
            mtime = os.path.getmtime(full)
            if mtime < threshold:
                continue
            self._scan_cache[full] = mtime
            files.append(full)
        files.sort(key=lambda p: os.path.getmtime(p))
        return files

    def _decide_merge_filter(self):
        if self._force_full_merge:
            return None, "전체 (강제)"
        if self._last_merge_at:
            return self._last_merge_at, f"마지막 병합 후 ({self._last_merge_at.strftime('%H:%M:%S')})"
        if self._session_start_at:
            return self._session_start_at, f"세션 시작 후 ({self._session_start_at.strftime('%H:%M:%S')})"
        return None, "전체 (최초)"

    def _merge_to_pdf(self):
        self._pdf_busy = True
        self.root.after(0, lambda: self.pdf_status_var.set("⏳ 생성 중..."))
        try:
            if _AS_PdfMerger is None:
                self.pdf_log("⚠️ PyPDF2 미설치")
                return
            after_at, mode_label = self._decide_merge_filter()
            include_manual = self._include_manual_once
            files = self._scan_png_files(after_at=after_at, include_manual=include_manual)
            total = len(files)
            self.pdf_log(f"📋 PDF 병합 모드: {mode_label}" +
                         (" (MANUAL 포함)" if include_manual else ""))
            if total == 0:
                self.pdf_log("⚠️ 대상 PNG 0건")
                self._force_full_merge = False
                return
            self.pdf_log(f"🔧 병합 시작 — {total}장")
            merger = _AS_PdfMerger()
            ok_cnt, err_cnt, ok_files = 0, 0, []
            for idx, f_path in enumerate(files, 1):
                try:
                    img = Image.open(f_path).convert('RGB')
                    img = ImageOps.exif_transpose(img)
                    img.thumbnail(_AS_PDF_TARGET_SIZE, Image.Resampling.LANCZOS)
                    pdf_bytes = BytesIO()
                    img.save(pdf_bytes, format='PDF',
                             resolution=_AS_PDF_RESOLUTION, quality=_AS_PDF_QUALITY)
                    pdf_bytes.seek(0)
                    merger.append(pdf_bytes)
                    ok_cnt += 1
                    ok_files.append(f_path)
                    if idx % 10 == 0 or idx == total:
                        self.pdf_log(f"  [{idx}/{total}]")
                except Exception as ie:
                    err_cnt += 1
                    self.pdf_log(f"  ⚠️ 건너뜀 ({os.path.basename(f_path)}): {ie}")
            if ok_cnt == 0:
                self.pdf_log("❌ 변환 가능 파일 0건")
                merger.close()
                self._force_full_merge = False
                return
            ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            out_name = f"AUTOSHOT_{ts}.pdf"
            out_path = os.path.join(self.pdf_dir, out_name)
            with open(out_path, 'wb') as fout:
                merger.write(fout)
            merger.close()
            size_mb = os.path.getsize(out_path) / 1024 / 1024
            self.pdf_log(f"✅ 완료: {out_name}  ({ok_cnt}장, {size_mb:.1f}MB)")
            if err_cnt:
                self.pdf_log(f"   누락: {err_cnt}장")
            if self._auto_delete_merged and ok_files:
                del_ok = del_err = 0
                for fp in ok_files:
                    try:
                        os.remove(fp)
                        del_ok += 1
                    except Exception as de:
                        del_err += 1
                        self.pdf_log(f"  ⚠️ 삭제 실패: {os.path.basename(fp)}")
                self.pdf_log(f"🗑 원본 삭제: {del_ok}건" +
                             (f"  실패: {del_err}건" if del_err else ""))
            self._last_merge_at = datetime.datetime.now()
            self.root.after(0, self._refresh_pdf_info_labels)
        except Exception as err:
            self.pdf_log(f"❌ 병합 오류: {err}")
        finally:
            self._force_full_merge = False
            self._include_manual_once = False
            self._pdf_busy = False
            self.root.after(0, lambda: self.pdf_status_var.set("● 대기"))

    def _dispatch_merge(self):
        try:
            fmt = self.merge_format_var.get()
        except Exception:
            fmt = _AS_MERGE_FORMAT_DEFAULT
        if fmt not in _AS_MERGE_FORMATS:
            fmt = _AS_MERGE_FORMAT_DEFAULT
        if fmt == "gif":
            self._merge_to_gif()
        elif fmt == "apng":
            self._merge_to_apng()
        elif fmt == "webp":
            self._merge_to_webp()
        else:
            if not _AS_PDF_AVAILABLE:
                self.pdf_log("⚠️ PyPDF2 미설치")
                return
            self._merge_to_pdf()

    def _merge_to_gif(self):
        self._pdf_busy = True
        self.root.after(0, lambda: self.pdf_status_var.set("⏳ GIF 생성 중..."))
        try:
            after_at, mode_label = self._decide_merge_filter()
            include_manual = self._include_manual_once
            files = self._scan_png_files(after_at=after_at, include_manual=include_manual)
            total = len(files)
            self.pdf_log(f"📋 GIF 병합: {mode_label}" + (" MANUAL 포함" if include_manual else ""))
            if total == 0:
                self.pdf_log("⚠️ 대상 0건")
                self._force_full_merge = False
                return
            try:
                dur = int(self._config.get("gif_duration_ms", _AS_GIF_DURATION_MS))
            except Exception:
                dur = _AS_GIF_DURATION_MS
            frames, ok_cnt, err_cnt, ok_files = [], 0, 0, []
            for idx, f_path in enumerate(files, 1):
                try:
                    img = Image.open(f_path).convert("RGB")
                    img = ImageOps.exif_transpose(img)
                    img.thumbnail(_AS_GIF_TARGET_SIZE, Image.Resampling.LANCZOS)
                    frames.append(img)
                    ok_cnt += 1
                    ok_files.append(f_path)
                    if idx % 10 == 0 or idx == total:
                        self.pdf_log(f"  [{idx}/{total}]")
                except Exception as ie:
                    err_cnt += 1
                    self.pdf_log(f"  ⚠️ 건너뜀: {os.path.basename(f_path)}")
            if ok_cnt == 0:
                self.pdf_log("❌ 변환 파일 0건")
                self._force_full_merge = False
                return
            ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            out_name = f"AUTOSHOT_{ts}.gif"
            out_path = os.path.join(self.pdf_dir, out_name)
            frames[0].save(out_path, format="GIF", save_all=True,
                           append_images=frames[1:], duration=dur,
                           loop=_AS_GIF_LOOP, optimize=True)
            size_mb = os.path.getsize(out_path) / 1024 / 1024
            self.pdf_log(f"✅ GIF: {out_name}  ({ok_cnt}장, {size_mb:.1f}MB, {dur}ms/프레임)")
            if self._auto_delete_merged and ok_files:
                del_ok = del_err = 0
                for fp in ok_files:
                    try:
                        os.remove(fp)
                        del_ok += 1
                    except Exception:
                        del_err += 1
                self.pdf_log(f"🗑 원본 삭제: {del_ok}건" + (f"  실패: {del_err}" if del_err else ""))
            self._last_merge_at = datetime.datetime.now()
            self.root.after(0, self._refresh_pdf_info_labels)
        except Exception as err:
            self.pdf_log(f"❌ GIF 오류: {err}")
        finally:
            self._force_full_merge = False
            self._include_manual_once = False
            self._pdf_busy = False
            self.root.after(0, lambda: self.pdf_status_var.set("● 대기"))

    def _merge_to_apng(self):
        self._pdf_busy = True
        self.root.after(0, lambda: self.pdf_status_var.set("⏳ APNG 생성 중..."))
        try:
            after_at, mode_label = self._decide_merge_filter()
            include_manual = self._include_manual_once
            files = self._scan_png_files(after_at=after_at, include_manual=include_manual)
            total = len(files)
            self.pdf_log(f"📋 APNG 병합: {mode_label}")
            if total == 0:
                self.pdf_log("⚠️ 대상 0건")
                self._force_full_merge = False
                return
            try:
                dur = int(self._config.get("apng_duration_ms", _AS_APNG_DURATION_MS))
            except Exception:
                dur = _AS_APNG_DURATION_MS
            frames, ok_cnt, err_cnt, ok_files = [], 0, 0, []
            for idx, f_path in enumerate(files, 1):
                try:
                    img = Image.open(f_path).convert("RGBA")
                    img = ImageOps.exif_transpose(img)
                    img.thumbnail(_AS_APNG_TARGET_SIZE, Image.Resampling.LANCZOS)
                    frames.append(img)
                    ok_cnt += 1
                    ok_files.append(f_path)
                    if idx % 10 == 0 or idx == total:
                        self.pdf_log(f"  [{idx}/{total}]")
                except Exception as ie:
                    err_cnt += 1
                    self.pdf_log(f"  ⚠️ 건너뜀: {os.path.basename(f_path)}")
            if ok_cnt == 0:
                self.pdf_log("❌ 변환 파일 0건")
                self._force_full_merge = False
                return
            ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            out_name = f"AUTOSHOT_{ts}.png"
            out_path = os.path.join(self.pdf_dir, out_name)
            frames[0].save(out_path, format="PNG", save_all=True,
                           append_images=frames[1:], duration=dur, loop=0)
            size_mb = os.path.getsize(out_path) / 1024 / 1024
            self.pdf_log(f"✅ APNG: {out_name}  ({ok_cnt}장, {size_mb:.1f}MB)")
            if self._auto_delete_merged and ok_files:
                del_ok = del_err = 0
                for fp in ok_files:
                    try:
                        os.remove(fp)
                        del_ok += 1
                    except Exception:
                        del_err += 1
                self.pdf_log(f"🗑 원본 삭제: {del_ok}건" + (f"  실패: {del_err}" if del_err else ""))
            self._last_merge_at = datetime.datetime.now()
            self.root.after(0, self._refresh_pdf_info_labels)
        except Exception as err:
            self.pdf_log(f"❌ APNG 오류: {err}")
        finally:
            self._force_full_merge = False
            self._include_manual_once = False
            self._pdf_busy = False
            self.root.after(0, lambda: self.pdf_status_var.set("● 대기"))

    def _merge_to_webp(self):
        self._pdf_busy = True
        self.root.after(0, lambda: self.pdf_status_var.set("⏳ WebP 생성 중..."))
        try:
            after_at, mode_label = self._decide_merge_filter()
            include_manual = self._include_manual_once
            files = self._scan_png_files(after_at=after_at, include_manual=include_manual)
            total = len(files)
            self.pdf_log(f"📋 WebP 병합: {mode_label}")
            if total == 0:
                self.pdf_log("⚠️ 대상 0건")
                self._force_full_merge = False
                return
            try:
                dur = int(self._config.get("webp_duration_ms", _AS_WEBP_DURATION_MS))
            except Exception:
                dur = _AS_WEBP_DURATION_MS
            frames, ok_cnt, err_cnt, ok_files = [], 0, 0, []
            for idx, f_path in enumerate(files, 1):
                try:
                    img = Image.open(f_path).convert("RGB")
                    img = ImageOps.exif_transpose(img)
                    img.thumbnail(_AS_WEBP_TARGET_SIZE, Image.Resampling.LANCZOS)
                    frames.append(img)
                    ok_cnt += 1
                    ok_files.append(f_path)
                    if idx % 10 == 0 or idx == total:
                        self.pdf_log(f"  [{idx}/{total}]")
                except Exception as ie:
                    err_cnt += 1
                    self.pdf_log(f"  ⚠️ 건너뜀: {os.path.basename(f_path)}")
            if ok_cnt == 0:
                self.pdf_log("❌ 변환 파일 0건")
                self._force_full_merge = False
                return
            ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            out_name = f"AUTOSHOT_{ts}.webp"
            out_path = os.path.join(self.pdf_dir, out_name)
            frames[0].save(out_path, format="WEBP", save_all=True,
                           append_images=frames[1:], duration=dur,
                           loop=0, quality=_AS_WEBP_QUALITY)
            size_mb = os.path.getsize(out_path) / 1024 / 1024
            self.pdf_log(f"✅ WebP: {out_name}  ({ok_cnt}장, {size_mb:.1f}MB)")
            if self._auto_delete_merged and ok_files:
                del_ok = del_err = 0
                for fp in ok_files:
                    try:
                        os.remove(fp)
                        del_ok += 1
                    except Exception:
                        del_err += 1
                self.pdf_log(f"🗑 원본 삭제: {del_ok}건" + (f"  실패: {del_err}" if del_err else ""))
            self._last_merge_at = datetime.datetime.now()
            self.root.after(0, self._refresh_pdf_info_labels)
        except Exception as err:
            self.pdf_log(f"❌ WebP 오류: {err}")
        finally:
            self._force_full_merge = False
            self._include_manual_once = False
            self._pdf_busy = False
            self.root.after(0, lambda: self.pdf_status_var.set("● 대기"))

    def pdf_log(self, msg):
        ts = datetime.datetime.now().strftime('%H:%M:%S')
        def _append():
            self.pdf_txt.insert(tk.END, f"[{ts}] {msg}\n")
            lines = int(self.pdf_txt.index('end-1c').split('.')[0])
            if lines > _AS_LOG_MAX_LINES:
                self.pdf_txt.delete('1.0', f'{lines - _AS_LOG_MAX_LINES}.0')
            self.pdf_txt.see(tk.END)
            self._push_common(f"[병합 {ts}] {msg}")
        self.root.after(0, _append)

    def _push_common(self, line):
        prev = self._common_line1.get()
        self._common_line1.set(line)
        self._common_line2.set(prev)

    # ── PDF 주기 워커 ────────────────────────────────────────────
    def _get_pdf_cycle(self):
        try:
            v = int(self.pdf_cycle_var.get())
        except ValueError:
            self.pdf_cycle_var.set(str(_AS_PDF_CYCLE_DEFAULT))
            return _AS_PDF_CYCLE_DEFAULT
        if v < _AS_PDF_CYCLE_MIN:
            self.pdf_cycle_var.set(str(_AS_PDF_CYCLE_MIN))
            return _AS_PDF_CYCLE_MIN
        if v > _AS_PDF_CYCLE_MAX:
            self.pdf_cycle_var.set(str(_AS_PDF_CYCLE_MAX))
            return _AS_PDF_CYCLE_MAX
        return v

    def toggle_auto_delete(self):
        self._auto_delete_merged = not self._auto_delete_merged
        if self._auto_delete_merged:
            self.del_btn_var.set("[ 병합 후 삭제: 켜짐 ]")
            self.del_btn.config(fg="#ff4444")
            self.pdf_log("🗑 자동 삭제: 켜짐")
        else:
            self.del_btn_var.set("[ 병합 후 삭제: 꺼짐 ]")
            self.del_btn.config(fg="#666")
            self.pdf_log("🗑 자동 삭제: 꺼짐")
        self._save_config()

    def toggle_pdf_cycle(self):
        if not self._pdf_cycle_active:
            self._start_pdf_cycle()
        else:
            self._stop_pdf_cycle()

    def _start_pdf_cycle(self):
        if not _AS_PDF_AVAILABLE:
            self.pdf_log("⚠️ PyPDF2 미설치 — 자동 병합 비활성")
            return
        cycle_min = self._get_pdf_cycle()
        self._pdf_cycle_active = True
        self._pdf_cycle_stop_event.clear()
        self._pdf_cycle_count = 0
        self.pdf_cycle_count_var.set("[0]")
        self.pdf_cycle_entry.config(state=tk.DISABLED)
        self.pdf_cycle_btn_var.set("[ 자동 병합: 가동 ]")
        self.pdf_cycle_btn.config(bg="#002200", fg="#00ff00")
        self._pdf_cycle_thread = threading.Thread(
            target=self._pdf_cycle_loop, args=(cycle_min,), daemon=True)
        self._pdf_cycle_thread.start()
        self.pdf_log(f"⏱ 자동 병합 시작 — 주기: {cycle_min}분")
        self._save_config()

    def _stop_pdf_cycle(self):
        self._pdf_cycle_active = False
        self._pdf_cycle_stop_event.set()
        self.pdf_cycle_btn_var.set("[ 자동 병합: 정지 ]")
        self.pdf_cycle_btn.config(bg="#1a0a00", fg="#ff6600")
        self.pdf_cycle_entry.config(state=tk.NORMAL)
        self.pdf_next_var.set("다음 생성: ─")
        self.pdf_log(f"⏹ 자동 병합 정지 — 누적: {self._pdf_cycle_count}건")

    def _pdf_cycle_loop(self, cycle_min):
        cycle_sec = cycle_min * 60
        while not self._pdf_cycle_stop_event.is_set():
            next_at = datetime.datetime.now() + datetime.timedelta(seconds=cycle_sec)
            self._pdf_next_at = next_at
            self.root.after(0, lambda t=next_at: self.pdf_next_var.set(
                f"다음 생성: {t.strftime('%H:%M:%S')}"))
            if self._pdf_cycle_stop_event.wait(timeout=cycle_sec):
                break
            if self._pdf_busy:
                self.pdf_log("⏭ 자동 병합 스킵 — 이전 작업 진행 중")
                continue
            self.pdf_log(f"⏱ 자동 병합 주기 도래")
            self._dispatch_merge()
            self._pdf_cycle_count += 1
            cnt = self._pdf_cycle_count
            self.root.after(0, lambda c=cnt: self.pdf_cycle_count_var.set(f"[{c}]"))

    # ── 비프음 ───────────────────────────────────────────────────
    def toggle_beep(self):
        self._beep_enabled = not self._beep_enabled
        if self._beep_enabled:
            self.beep_btn_var.set("[ 알림음: 켜짐 ]")
            self.beep_btn.config(fg="#00ff41")
            self.queue_log("🔔 알림음 켜짐")
        else:
            self.beep_btn_var.set("[ 알림음: 꺼짐 ]")
            self.beep_btn.config(fg="#666")
            self.queue_log("🔕 알림음 꺼짐")
        self._save_config()

    def _beep_safe(self, freq, dur):
        if self._beep_enabled and _winsound is not None:
            try:
                _winsound.Beep(freq, dur)
            except Exception:
                pass

    # ── config I/O ───────────────────────────────────────────────
    def _load_config(self):
        import json as _j
        if not os.path.exists(_AS_CONFIG_PATH):
            try:
                with open(_AS_CONFIG_PATH, 'w', encoding='utf-8') as f:
                    _j.dump(_AS_DEFAULT_CONFIG, f, ensure_ascii=False, indent=2)
            except Exception:
                pass
            return dict(_AS_DEFAULT_CONFIG)
        try:
            with open(_AS_CONFIG_PATH, 'r', encoding='utf-8') as f:
                cfg = _j.load(f)
            merged = dict(_AS_DEFAULT_CONFIG)
            merged.update(cfg)
            return merged
        except Exception:
            return dict(_AS_DEFAULT_CONFIG)

    def _save_config(self):
        if self._save_timer is not None:
            self._save_timer.cancel()
        self._save_timer = threading.Timer(0.5, self._save_config_exec)
        self._save_timer.daemon = True
        self._save_timer.start()

    def _save_config_exec(self):
        import json as _j
        try:
            self._config["save_dir"]           = self.save_dir
            self._config["pdf_dir"]            = self.pdf_dir
            self._config["beep_enabled"]       = self._beep_enabled
            self._config["auto_delete_merged"] = self._auto_delete_merged
            try:
                self._config["capture_interval"] = int(float(self.interval_var.get()))
            except Exception:
                pass
            try:
                self._config["pdf_cycle_min"] = int(self.pdf_cycle_var.get())
            except Exception:
                pass
            try:
                fmt = self.merge_format_var.get()
                self._config["merge_format"] = fmt if fmt in _AS_MERGE_FORMATS else _AS_MERGE_FORMAT_DEFAULT
            except Exception:
                pass
            with open(_AS_CONFIG_PATH, 'w', encoding='utf-8') as f:
                _j.dump(self._config, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def _apply_config_pre_ui(self):
        try:
            self.save_dir = self._config.get("save_dir", _AS_DEFAULT_SAVE_DIR)
            os.makedirs(self.save_dir, exist_ok=True)
        except Exception:
            self.save_dir = _AS_DEFAULT_SAVE_DIR
        try:
            self.pdf_dir = self._config.get("pdf_dir", _AS_DEFAULT_PDF_DIR)
            os.makedirs(self.pdf_dir, exist_ok=True)
        except Exception:
            self.pdf_dir = _AS_DEFAULT_PDF_DIR
        self._beep_enabled = bool(self._config.get("beep_enabled", True))
        self._auto_delete_merged = bool(self._config.get("auto_delete_merged", False))
        _fmt = self._config.get("merge_format", _AS_MERGE_FORMAT_DEFAULT)
        self._merge_format_init = _fmt if _fmt in _AS_MERGE_FORMATS else _AS_MERGE_FORMAT_DEFAULT

    def _apply_config_post_ui(self):
        try:
            interval = int(self._config.get("capture_interval", _AS_DEFAULT_INTERVAL))
            self.interval_var.set(str(interval))
        except Exception:
            pass
        try:
            cycle = int(self._config.get("pdf_cycle_min", _AS_PDF_CYCLE_DEFAULT))
            self.pdf_cycle_var.set(str(cycle))
        except Exception:
            pass
        try:
            if self._beep_enabled:
                self.beep_btn_var.set("[ 알림음: 켜짐 ]")
                self.beep_btn.config(fg="#00ff41")
            else:
                self.beep_btn_var.set("[ 알림음: 꺼짐 ]")
                self.beep_btn.config(fg="#666")
        except Exception:
            pass
        try:
            if self._auto_delete_merged:
                self.del_btn_var.set("[ 병합 후 삭제: 켜짐 ]")
                self.del_btn.config(fg="#ff4444")
            else:
                self.del_btn_var.set("[ 병합 후 삭제: 꺼짐 ]")
                self.del_btn.config(fg="#666")
        except Exception:
            pass
        try:
            self.merge_format_var.set(self._merge_format_init)
        except Exception:
            pass

    # ── 설정 탭 콜백 ─────────────────────────────────────────────
    def _cfg_interval_view(self):
        var = tk.StringVar()
        def _refresh(*_):
            try:
                var.set(f"  캡처 주기:    {self.interval_var.get()}초")
            except Exception:
                var.set("  캡처 주기:    -")
        try:
            self.interval_var.trace_add('write', _refresh)
        except Exception:
            pass
        _refresh()
        return var

    def _cfg_pdf_cycle_view(self):
        var = tk.StringVar()
        def _refresh(*_):
            try:
                var.set(f"  병합 주기:    {self.pdf_cycle_var.get()}분")
            except Exception:
                var.set("  병합 주기:    -")
        try:
            self.pdf_cycle_var.trace_add('write', _refresh)
        except Exception:
            pass
        _refresh()
        return var

    def _cfg_beep_view(self):
        var = tk.StringVar()
        def _refresh(*_):
            try:
                state = "켜짐" if self._beep_enabled else "꺼짐"
                var.set(f"  알림음:       {state}")
            except Exception:
                var.set("  알림음:       -")
        try:
            self.beep_btn_var.trace_add('write', _refresh)
        except Exception:
            pass
        _refresh()
        return var

    def _on_cfg_change_save_dir(self):
        self.change_dir()
        try:
            self.cfg_save_dir_var.set(self.save_dir)
        except Exception:
            pass

    def _on_cfg_change_pdf_dir(self):
        self._on_change_pdf_dir()
        try:
            self.cfg_pdf_dir_var.set(self.pdf_dir)
        except Exception:
            pass

    def _on_reload_config(self):
        try:
            self._config = self._load_config()
            self._apply_config_pre_ui()
            self._apply_config_post_ui()
            try:
                self.cfg_save_dir_var.set(self.save_dir)
                self.cfg_pdf_dir_var.set(self.pdf_dir)
            except Exception:
                pass
            self.queue_log("⚙️ 설정 다시 로드 완료")
        except Exception as err:
            self.queue_log(f"⚠️ 설정 로드 실패: {err}")

    def _on_open_config_folder(self):
        try:
            cfg_folder = os.path.dirname(os.path.abspath(_AS_CONFIG_PATH))
            if sys.platform == "win32":
                os.startfile(cfg_folder)
            else:
                subprocess.Popen(["open" if sys.platform == "darwin" else "xdg-open", cfg_folder])
            self.queue_log(f"📂 설정 폴더: {cfg_folder[-30:]}")
        except Exception as err:
            self.queue_log(f"⚠️ 폴더 열기 실패: {err}")

    # ── 캡션 합성 ────────────────────────────────────────────────
    def _find_caption_font(self):
        if not _AS_PIL_DRAW_OK:
            return None
        for fpath in _AS_CAPTION_FONT_PATHS:
            if os.path.exists(fpath):
                try:
                    return ImageFont.truetype(fpath, _AS_CAPTION_FONT_SIZE)
                except Exception:
                    continue
        try:
            return ImageFont.load_default()
        except Exception:
            return None

    def _overlay_caption_mem(self, img, now, snap_type, serial):
        if not _AS_PIL_DRAW_OK:
            return img.convert("RGB")
        try:
            img_rgba = img.convert("RGBA")
            w, h = img_rgba.size
            font = self._caption_font
            top_overlay = Image.new("RGBA", (w, _AS_CAPTION_TOP_HEIGHT), _AS_CAPTION_BG_COLOR)
            top_draw    = ImageDraw.Draw(top_overlay)
            time_str    = now.strftime("%Y-%m-%d %H:%M:%S")
            serial_str  = f"#{serial:04d}"
            top_text    = "  |  ".join([time_str, serial_str, snap_type])
            if font:
                try:
                    tb = top_draw.textbbox((0, 0), top_text, font=font)
                    th = tb[3] - tb[1]
                except Exception:
                    th = _AS_CAPTION_FONT_SIZE
                y_top = max(0, (_AS_CAPTION_TOP_HEIGHT - th) // 2)
                top_draw.text((8, y_top), top_text, fill=_AS_CAPTION_FG_COLOR, font=font)
            else:
                top_draw.text((8, 6), top_text, fill=_AS_CAPTION_FG_COLOR)
            bot_overlay = Image.new("RGBA", (w, _AS_CAPTION_BOTTOM_HEIGHT), _AS_CAPTION_BG_COLOR)
            bot_draw    = ImageDraw.Draw(bot_overlay)
            bot_text    = _AS_FIXED_CAPTION
            if font:
                try:
                    bb = bot_draw.textbbox((0, 0), bot_text, font=font)
                    bh = bb[3] - bb[1]
                except Exception:
                    bh = _AS_CAPTION_FONT_SIZE
                y_bot = max(0, (_AS_CAPTION_BOTTOM_HEIGHT - bh) // 2)
                bot_draw.text((8, y_bot), bot_text, fill=_AS_CAPTION_FG_COLOR, font=font)
            else:
                bot_draw.text((8, 6), bot_text, fill=_AS_CAPTION_FG_COLOR)
            total_h = h + _AS_CAPTION_TOP_HEIGHT + _AS_CAPTION_BOTTOM_HEIGHT
            result  = Image.new("RGBA", (w, total_h), (0, 0, 0, 255))
            result.paste(top_overlay, (0, 0))
            result.paste(img_rgba,    (0, _AS_CAPTION_TOP_HEIGHT))
            result.paste(bot_overlay, (0, _AS_CAPTION_TOP_HEIGHT + h))
            return result.convert("RGB")
        except Exception:
            return img.convert("RGB")

    # ── 플로팅 창 ─────────────────────────────────────────────────
    def _build_floating_window(self):
        try:
            toplevel_root = self.root.winfo_toplevel()
            self.float_win = tk.Toplevel(toplevel_root)
            self.float_win.title("수동 촬영")
            x = self._config.get("float_win_x", _AS_FLOAT_WIN_OFFSET[0])
            y = self._config.get("float_win_y", _AS_FLOAT_WIN_OFFSET[1])
            self.float_win.geometry(
                f"{_AS_FLOAT_WIN_WIDTH}x{_AS_FLOAT_WIN_HEIGHT}+{x}+{y}")
            self.float_win.minsize(_AS_FLOAT_WIN_WIDTH, _AS_FLOAT_WIN_HEIGHT)
            self.float_win.configure(bg="#000")
            self.float_win.attributes("-topmost", True)
            self.float_win.protocol("WM_DELETE_WINDOW", self._on_float_close)
            title_frame = tk.Frame(self.float_win, bg="#1a1a1a",
                                   height=_AS_FLOAT_WIN_TITLE_HEIGHT,
                                   relief=tk.RAISED, bd=1)
            title_frame.pack(side=tk.TOP, fill=tk.X, expand=False)
            title_frame.pack_propagate(False)
            title_label = tk.Label(title_frame, text="[ 수동 촬영 ] — 드래그 이동",
                                   bg="#1a1a1a", fg="#cccccc",
                                   font=("Consolas", 9), anchor=tk.W, padx=8)
            title_label.pack(fill=tk.BOTH, expand=True)
            self._float_drag_data = {"x": 0, "y": 0}
            def _on_title_press(event):
                self._float_drag_data["x"] = event.x_root - self.float_win.winfo_x()
                self._float_drag_data["y"] = event.y_root - self.float_win.winfo_y()
            def _on_title_drag(event):
                x = event.x_root - self._float_drag_data["x"]
                y = event.y_root - self._float_drag_data["y"]
                self.float_win.geometry(f"+{x}+{y}")
                self._config["float_win_x"] = x
                self._config["float_win_y"] = y
                self._save_config()
            title_frame.bind("<Button-1>", _on_title_press)
            title_frame.bind("<B1-Motion>", _on_title_drag)
            title_label.bind("<Button-1>", _on_title_press)
            title_label.bind("<B1-Motion>", _on_title_drag)
            btn_frame = tk.Frame(self.float_win, bg="#000")
            btn_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
            tk.Button(btn_frame, text="[ 수동 촬영 ]",
                      bg="#1a001a", fg="#ff00ff",
                      font=("Consolas", 11, "bold"),
                      activebackground="#330033", activeforeground="#ff66ff",
                      relief=tk.FLAT, bd=1,
                      command=lambda: self.snap_action(snap_type='MANUAL', keyword='')
                      ).pack(fill=tk.BOTH, expand=True, pady=(0, 3))
            tk.Button(btn_frame, textvariable=self.auto_btn_var,
                      bg="#001a00", fg="#00ff88",
                      font=("Consolas", 10, "bold"),
                      activebackground="#003300", activeforeground="#66ffaa",
                      relief=tk.FLAT, bd=1,
                      command=self.toggle_auto
                      ).pack(fill=tk.BOTH, expand=True, pady=(0, 3))
            tk.Button(btn_frame, text="[ 즉시 병합 ]",
                      bg="#1a1a00", fg="#ffaa00",
                      font=("Consolas", 10, "bold"),
                      activebackground="#333300", activeforeground="#ffcc00",
                      relief=tk.FLAT, bd=1,
                      command=self._on_pdf_merge_now
                      ).pack(fill=tk.BOTH, expand=True, pady=(0, 3))
            tk.Button(btn_frame, text="[ 전체 병합 ]",
                      bg="#1a0a00", fg="#ff6600",
                      font=("Consolas", 10, "bold"),
                      activebackground="#331a00", activeforeground="#ff8833",
                      relief=tk.FLAT, bd=1,
                      command=self._on_pdf_merge_full
                      ).pack(fill=tk.BOTH, expand=True, pady=(0, 3))
            tk.Button(btn_frame, text="[ 폴더 열기 ]",
                      bg="#0a0a2a", fg="#79b8ff",
                      font=("Consolas", 10, "bold"),
                      activebackground="#001133", activeforeground="#99ccff",
                      relief=tk.FLAT, bd=1,
                      command=self._on_open_pdf_dir
                      ).pack(fill=tk.BOTH, expand=True)
        except Exception as err:
            self.queue_log(f"플로팅 창 생성 실패: {err}")
            self.float_win = None

    def _on_float_close(self):
        try:
            if self.float_win is not None:
                self.float_win.withdraw()
                self.queue_log("플로팅 창 숨김")
        except Exception:
            pass

    def _show_floating_window(self):
        try:
            if self.float_win is None:
                self._build_floating_window()
                return
            self.float_win.deiconify()
            self.float_win.attributes("-topmost", True)
            self.float_win.lift()
            self.queue_log("플로팅 창 표시")
        except Exception as err:
            self.queue_log(f"플로팅 창 표시 실패: {err}")

    # ── 유틸 ─────────────────────────────────────────────────────
    def force_unlock(self):
        self._lock.clear()
        self.setup_hotkey()
        self.status_var.set("● 대기" if not self._auto_active
                            else f"⏱ 자동 {self._get_interval():.0f}초")
        self.queue_log("🔓 강제 잠금해제")

    def queue_log(self, msg):
        ts = datetime.datetime.now().strftime('%H:%M:%S')
        self.txt.insert(tk.END, f"[{ts}] {msg}\n")
        lines = int(self.txt.index('end-1c').split('.')[0])
        if lines > _AS_LOG_MAX_LINES:
            self.txt.delete('1.0', f'{lines - _AS_LOG_MAX_LINES}.0')
        self.txt.see(tk.END)
        self._push_common(f"[캡처 {ts}] {msg}")

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app  = SentinelHyperV530(root)
    root.mainloop()