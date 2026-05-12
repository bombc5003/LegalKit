# Title: ClickLegalKit v6.8.4 (EN Edition)
#        — Merger + Fuzzy Find + Evidence List + Case Collector + Promo
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

# v6.8.8 변경: 좀비 창 버그 수리
#            ─────────────────────────────────────────
#            [수리 내역]
#            - if __name__ == '__main__' 블록 중복으로
#              첫 번째 mainloop 종료(창 닫기) 후
#              두 번째 블록 실행 → 창 재생성 좀비 버그 수정.
#            - _clean_html_tags 정적 메서드가 CaseCrawler 클래스 밖으로
#              탈출한 구조 오류 수정, 클래스 내부 복귀.
#            [무결성]
#            - 기능·로직·UI 변경 없음. 진입점 단일화만.
# v6.8.9 변경: Patch button removed from Merger tab
#            - btn_patch widget removed. self_patch method retained.
import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext, simpledialog, messagebox
import os, sys, subprocess, threading, difflib
import datetime
import webbrowser
from io import BytesIO


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
PREFIX_OPTIONS = ["Ex. %d", "A-%d", "B-%d", "C-%d", "%d.", "No.%d"]


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

PRODUCT_NAME      = "ClickLegalKit"
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
# Commercial license whitelist — machine hash registered = commercial license granted
# v7.47: COMMERCIAL_WHITELIST removed — file-based license system
_IS_COMMERCIAL: bool = False  # forward declaration — resolved after _lgk_load

FIXED_CAPTION = (
    ""
    if _IS_COMMERCIAL else
    f"{PRODUCT_NAME} {BUILD_NUMBER} · Personal Use Only · Unauthorized commercial use may violate copyright law · C-2026-022058 · {FREE_BUILD_ID}"
)

# ──────────────────────────────────────────────────────────────
# v6.9.4 — License security hardened (Ed25519 asymmetric sig + license.json HMAC seal)
#   · Legacy _LGK_SECRET symmetric-key exposure neutralized
#   · Even if secret is extracted from EXE, forged keys are infeasible (private key offline)
#   · license.json is sealed by machine-bound HMAC — copying to other PCs auto-invalidates
#   · Function signatures unchanged: _lgk_validate / _lgk_load / _lgk_save
# ──────────────────────────────────────────────────────────────
import json as _json
import base64 as _base64
from pathlib import Path as _Path

_LGK_SECRET   = b"ddalkkak2026lgk"   # legacy compat (migration reference only)
FREE_LIMIT    = 5   # free merge count (v7.0.9: limit removed — see _lgk_check below)

_LGK_DATA_DIR  : _Path = _Path(os.environ.get("APPDATA", "~")).expanduser() / "VibeToolsmith" / "LegalKit"
_LGK_LIC_FILE  : _Path = _LGK_DATA_DIR / "license.json"

# Ed25519 public key (raw 32-byte base64). Private key kept offline by author.
_LGK_PUBKEY_B64 = "zrW7lXGJ97F1OdXeyeM8Qi1NcWyxuCd7PIcKkURYxoo="
# ──────────────────────────────────────────────────────────────
# v7.0.0 — 녹취록 (Transcript) — Whisper 기반 음성→텍스트
#   ClickTalkScript v1.67 핵심 흡수. _ts_* 접두사로 격리.
#   라이선스: 법무킷 통합 카운터 사용 (병합·녹취 합산 5회).
# ──────────────────────────────────────────────────────────────
# ── PyInstaller --windowed build stdout/stderr None guard ──
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
    """Reuses _MACHINE_FP — XXXX-XXXX-XXXX-XXXX format."""
    h = _hashlib.sha256(_MACHINE_FP.encode("utf-8")).hexdigest().upper()
    return f"{h[0:4]}-{h[4:8]}-{h[8:12]}-{h[12:16]}"


def _lgk_bind_secret() -> bytes:
    """Machine-bound secret for license.json HMAC seal."""
    return _hmac.new(b"lgk-bind-2026", _MACHINE_FP.encode("utf-8"),
                     _hashlib.sha256).digest()


def _lgk_load() -> dict:
    """Verify HMAC seal then return payload. Forged/copied/legacy files reset to 0."""
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
    """Attach machine-bound HMAC signature, then persist."""
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
    """Ed25519 signature verification. v7.47: expiry date support.
    key: base64(72 bytes) = 64-byte sig + 8-byte expiry (YYYYMMDD or 00000000=permanent).
         Backward compat: 64-byte keys (legacy permanent) accepted.
    Returns: expiry string ('YYYYMMDD' or '00000000') if valid, None if invalid.
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
        if len(raw) == 64:          # legacy permanent key
            sig, expiry_str = raw, "00000000"
            message = mid.encode("utf-8")
        else:                       # new: sig(64) + expiry(8)
            sig, expiry_bytes = raw[:64], raw[64:]
            expiry_str = expiry_bytes.decode("ascii")
            message = f"{mid}|{expiry_str}".encode("utf-8")
        pub = Ed25519PublicKey.from_public_bytes(_base64.b64decode(_LGK_PUBKEY_B64))
        pub.verify(sig, message)
        return expiry_str
    except Exception:
        return None

# v7.47: file-based commercial license check (with expiry)
def _lgk_is_commercial() -> bool:
    """Check commercial license validity including expiry date."""
    try:
        data = _lgk_load()
        if not data.get("commercial"):
            return False
        expiry = data.get("expiry", "00000000")
        if expiry == "00000000":
            return True
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
    # Differentiators
    "Air-gapped by design — zero external calls",
    "Custom air-gapped system dev available",
    # Book promo
    "Sold on Amazon.fr — Claude AI Cowork Primer series",
    "Readers in France, Brazil & Germany found it first",
    "Search 'Vibe Toolsmith' on Amazon — AI Cowork books",
    # Dev inquiry · support · ad slots
    "Office automation dev inquiries · +82-10-2272-7030",
    "Support the dev · KakaoPay 010-2272-7030",
    "AI-powered legal tool — lifetime ad slots open",
    "Be an angel sponsor · 010-2272-7030",
    "Early support = lifetime exposure — cheapest it'll ever be",
    "Solo dev grit — LegalKit keeps going",
    "Built through chronic pain — your support keeps it alive",
    # Commercial upgrade notice
    "Upgrade to commercial license to remove all ad captions · bc5103@naver.com",
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
        self.root.title(f"ClickLegalKit {BUILD_NUMBER}  ·  Merger + Fuzzy Find + Evidence List + Case Collector + Promo")
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
                 text=f"ClickLegalKit {BUILD_NUMBER}  ·  MERGE + FUZZY FIND + EVIDENCE LIST + CASE COLLECTOR + PROMO",
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
        self.transcript_tab = tk.Frame(self.nb, bg="#0a0a0a")  # v7.0.0 신규 (Transcript)
        self.promo_tab    = tk.Frame(self.nb, bg="#0a0a0a")  # v6.8.0 신규 (홍보)
        self.autoshot_tab = tk.Frame(self.nb, bg="#0a0a0a")  # v7.11 신규 (오토샷)
        self.license_tab  = tk.Frame(self.nb, bg="#0a0a0a")  # v7.47 신규 (License)
        self.nb.add(self.merge_tab,    text="📁 Merger")
        self.nb.add(self.find_tab,     text="🔍 Fuzzy Find")
        self.nb.add(self.evidence_tab, text="📋 Evidence List")
        # self.nb.add(self.case_tab,     text="⚖ Case Collector")  # disabled in EN
        self.nb.add(self.label_tab,    text="🏷 Exhibit Labeler")
        self.nb.add(self.transcript_tab, text="🎙 Transcript")     # v7.0.0 신규
        self.nb.add(self.promo_tab,    text="📣 Promo")     # v6.8.0 신규
        self.nb.add(self.license_tab,  text="🔑 License")   # v7.47 신규

        # v6.8.4 — 병합기 라이선스 초기화
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
        self._init_license_tab(self.license_tab)  # v7.47 신규


    # ══════════════════════════════════════════════════════════
    # v7.47 — License Tab (EN)
    # ══════════════════════════════════════════════════════════
    def _init_license_tab(self, parent: tk.Frame) -> None:
        """License registration, deactivation, and status display."""
        bg       = "#0a0a0a"
        fg_title = "#f9e2af"
        fg_sub   = "#aaaaaa"
        fg_ok    = "#a6e3a1"
        fg_warn  = "#f38ba8"
        fg_blue  = "#79b8ff"

        # ── Status Panel ──
        s_frame = tk.Frame(parent, bg="#111111", pady=12)
        s_frame.pack(fill=tk.X, padx=16, pady=(16, 8))
        tk.Label(s_frame, text="Current License Status",
                 fg=fg_sub, bg="#111111", font=("맑은 고딕", 8)).pack()
        def _lic_status_info():
            import datetime as _dt
            data = _lgk_load()
            if not data.get("commercial"):
                return "⚠ Unregistered (Personal Free)", fg_warn
            expiry = data.get("expiry", "00000000")
            if expiry == "00000000":
                return "✓ Commercial License (Permanent)", fg_ok
            exp_fmt = f"{expiry[:4]}-{expiry[4:6]}-{expiry[6:8]}"
            if _dt.date.today().strftime("%Y%m%d") <= expiry:
                return f"✓ Commercial License (Expires: {exp_fmt})", fg_ok
            return f"⚠ License Expired ({exp_fmt})", fg_warn
        _status_text, _status_color = _lic_status_info()
        self._lic_status_var = tk.StringVar(value=_status_text)
        self._lic_status_lbl = tk.Label(
            s_frame, textvariable=self._lic_status_var,
            fg=_status_color, bg="#111111", font=("맑은 고딕", 11, "bold"))
        self._lic_status_lbl.pack()

        # ── Machine ID ──
        mid_frame = tk.Frame(parent, bg=bg)
        mid_frame.pack(fill=tk.X, padx=16, pady=(8, 0))
        tk.Label(mid_frame, text="Machine ID  (send to developer when purchasing):",
                 fg=fg_sub, bg=bg, font=("맑은 고딕", 8)).pack(anchor="w")
        mid_row = tk.Frame(mid_frame, bg=bg)
        mid_row.pack(anchor="w")
        self._lic_mid_var = tk.StringVar(value=self._mid)
        tk.Entry(mid_row, textvariable=self._lic_mid_var, width=24,
                 state="readonly", bg="#1a1a1a", fg=fg_blue,
                 font=("Consolas", 10), readonlybackground="#1a1a1a",
                 relief="flat").pack(side=tk.LEFT, padx=(0, 6))
        tk.Button(mid_row, text="Copy",
                  command=lambda: (parent.clipboard_clear(),
                                   parent.clipboard_append(self._mid)),
                  bg="#2a5298", fg="white", font=("맑은 고딕", 8),
                  relief="flat", padx=6, pady=2).pack(side=tk.LEFT)

        # ── Divider ──
        tk.Frame(parent, bg="#2a2a2a", height=1).pack(fill=tk.X, padx=16, pady=12)

        # ── Key Entry ──
        tk.Label(parent, text="Register License Key",
                 fg=fg_title, bg=bg, font=("맑은 고딕", 9, "bold")).pack(anchor="w", padx=16)
        tk.Label(parent, text="Enter the key issued after purchase.",
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
                    _st = "✓ Commercial License (Permanent)"
                else:
                    _ef = f"{_exp[:4]}-{_exp[4:6]}-{_exp[6:8]}"
                    _st = f"✓ Commercial License (Expires: {_ef})"
                self._lic_status_var.set(_st)
                self._lic_status_lbl.config(fg=fg_ok)
                messagebox.showinfo("Activation Complete",
                    f"Commercial license registered successfully!\n{_st}")
            else:
                messagebox.showerror("Activation Failed",
                    "Invalid key.\n"
                    "Please send your Machine ID to the developer.\n"
                    "Email: dede5003@gmail.com")

        def _do_deactivate():
            if messagebox.askyesno("Deactivate License", "Are you sure you want to deactivate?"):
                global _IS_COMMERCIAL
                d = _lgk_load()
                d["commercial"] = False
                _lgk_save(d)
                _IS_COMMERCIAL = False
                self._lic_status_var.set("⚠ Unregistered (Personal Free)")
                self._lic_status_lbl.config(fg=fg_warn)

        tk.Button(btn_row, text="Register", command=_do_activate,
                  bg="#2980b9", fg="white", font=("맑은 고딕", 9, "bold"),
                  relief="flat", padx=12, pady=3).pack(side=tk.LEFT, padx=(0, 6))
        tk.Button(btn_row, text="Deactivate", command=_do_deactivate,
                  bg="#444444", fg="#aaaaaa", font=("맑은 고딕", 8),
                  relief="flat", padx=8, pady=3).pack(side=tk.LEFT)

        # ── Divider ──
        tk.Frame(parent, bg="#2a2a2a", height=1).pack(fill=tk.X, padx=16, pady=12)

        # ── Contact ──
        tk.Label(parent, text="Purchase Inquiries",
                 fg=fg_title, bg=bg, font=("맑은 고딕", 9, "bold")).pack(anchor="w", padx=16)
        tk.Label(parent,
                 text="Email : dede5003@gmail.com\n"
                      "Phone : 010-2272-7030\n"
                      "Blog  : blog.naver.com/bc5103\n"
                      "Copyright : C-2026-022058",
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
        ob = {"font": ("맑은 고딕", 8, "bold"), "relief": "flat", "bd": 0, "padx": 6, "pady": 3}
        tk.Button(order_f, text="▲ Up",    command=self.move_up,         bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_f, text="▼ Down",   command=self.move_down,       bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_f, text="⤒ Top",    command=self.move_top,        bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_f, text="⤓ Bottom",   command=self.move_bottom,     bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_f, text="✕ Remove",    command=self.remove_selected, bg="#3a1a1a", fg="#ff7b7b", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_f, text="🗑 Clear All", command=self.clear_list,      bg="#3a1a1a", fg="#ff7b7b", **ob).pack(side=tk.LEFT, padx=2)
        self.lbl_count = tk.Label(order_f, text="0 files", fg="#555", bg="#0a0a0a", font=("Consolas", 8))
        self.lbl_count.pack(side=tk.RIGHT, padx=4)

        # ── 액션 버튼 ──
        ctrl = tk.Frame(parent, bg="#0a0a0a")
        ctrl.pack(pady=5)
        ab = {"font": ("맑은 고딕", 8, "bold"), "height": 1, "relief": "flat"}
        self.btn_add   = tk.Button(ctrl, text="📂 Add Files",  command=self.add_files,                    width=8, bg="#1b4332", fg="#52b788", **ab)
        self.btn_merge = tk.Button(ctrl, text="📁 Merge",  command=lambda: self.run_merger(False),    width=8, bg="#2980b9", fg="white",   **ab)
        self.btn_comp  = tk.Button(ctrl, text="⚡ Merge (Compress)",  command=lambda: self.run_merger(True),     width=8, bg="#c0392b", fg="white",   **ab)
        self.btn_split = tk.Button(ctrl, text="✂️ Split",  command=self.run_splitter,                 width=8, bg="#d35400", fg="white",   **ab)
        self.btn_evlist = tk.Button(ctrl, text="📋 Evidence List",  command=self.export_evidence_list,         width=8, bg="#1a4a3a", fg="#52b788", **ab)
        for btn in (self.btn_add, self.btn_merge, self.btn_comp, self.btn_split, self.btn_evlist):
            btn.pack(side=tk.LEFT, padx=2)

        # ── v6.8.4 라이선스 상태 표시 ──
        lic_f = tk.Frame(parent, bg="#0a0a0a")
        lic_f.pack(fill=tk.X, padx=8, pady=(1, 0))
        tk.Label(lic_f, textvariable=self._lgk_var, fg="#f9e2af", bg="#0a0a0a",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        tk.Button(lic_f, text="🔑 Enter Key", command=self._lgk_show_dialog,
                  bg="#1a1a1a", fg="#aaa", font=("Consolas", 8), relief="flat",
                  padx=4, pady=1).pack(side=tk.RIGHT)

        # ── 분할 용량 설정 ──
        split_f = tk.Frame(parent, bg="#0a0a0a")
        split_f.pack(fill=tk.X, padx=8, pady=(0, 2))
        tk.Label(split_f, text="Split size (MB):", fg="#666", bg="#0a0a0a", font=("Consolas", 8)).pack(side=tk.LEFT)
        self.split_entry = tk.Entry(split_f, width=6, bg="#1a1a1a", fg="#e0e0e0",
                                    insertbackground="#e0e0e0", font=("Consolas", 9),
                                    relief="flat", highlightthickness=1,
                                    highlightcolor="#2a5298", highlightbackground="#333")
        self.split_entry.insert(0, "19.5")
        self.split_entry.pack(side=tk.LEFT, padx=4)
        tk.Button(split_f, text="Apply", command=self._apply_split_mb,
                  bg="#2a2a2a", fg="#aaa", font=("Consolas", 8), relief="flat", padx=4, pady=1).pack(side=tk.LEFT)
        self.lbl_split_mb = tk.Label(split_f, text=f"Current: {self._split_mb}MB", fg="#4a9", bg="#0a0a0a", font=("Consolas", 8))
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
        tk.Button(log_hdr, text="Clear", command=self._clear_merge_log,
                  bg="#1a1a1a", fg="#666", font=("Consolas", 8), relief="flat", padx=4, pady=0).pack(side=tk.RIGHT)
        self.log_board = scrolledtext.ScrolledText(
            parent, width=60, height=6, bg="#060606", fg="#33ff33",
            font=("Consolas", 8), borderwidth=0, highlightthickness=0)
        self.log_board.pack(pady=(2, 6), padx=8, fill=tk.X)
        self.merge_log("v531 READY.  Drag files here or click [Add Files].")
        self.merge_log("TIP: Del=Remove selected  /  Dbl-click=Open folder")

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
        tk.Label(find_hdr, text="CLICKFIND_v3.4  ·  Fuzzy File Search",
                 fg="white", bg="#1a73e8", font=("Malgun Gothic", 10, "bold")
                 ).pack(side=tk.LEFT, padx=10, pady=4)

        # ── 검색창 ──
        search_f = tk.Frame(parent, bg="#f8f9fa")
        search_f.pack(fill=tk.X, padx=10, pady=(8, 2))
        self.find_entry = tk.Entry(search_f, width=30, font=("Malgun Gothic", 11),
                                   borderwidth=1, relief="solid")
        self.find_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        self.find_entry.bind("<Return>", lambda e: self._start_search())
        self.btn_find = tk.Button(search_f, text="🔍 Search",
                                   command=self._start_search,
                                   bg="#1a73e8", fg="white",
                                   font=("Malgun Gothic", 10, "bold"),
                                   relief="flat", padx=8)
        self.btn_find.pack(side=tk.LEFT)

        # ── 유사도 슬라이더 ──
        slider_f = tk.Frame(parent, bg="#f8f9fa")
        slider_f.pack(fill=tk.X, padx=10, pady=2)
        tk.Label(slider_f, text="Similarity threshold:",
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
        tk.Label(slider_f, text="← Loose    Strict →",
                 bg="#f8f9fa", fg="#aaa", font=("Consolas", 8)).pack(side=tk.LEFT, padx=4)

        # ── 찾기 액션 버튼 ──
        find_btn_f = tk.Frame(parent, bg="#f8f9fa")
        find_btn_f.pack(pady=3)
        bs = {"font": ("Malgun Gothic", 8, "bold"), "width": 8, "fg": "white", "relief": "flat"}
        tk.Button(find_btn_f, text="📁 Set Path", command=self._set_find_path,
                  bg="#5f6368", **bs).pack(side=tk.LEFT, padx=2)
        tk.Button(find_btn_f, text="🗑 Clear Log", command=self._clear_find_log,
                  bg="#999", **bs).pack(side=tk.LEFT, padx=2)

        # ── 검색 결과 ──
        result_lbl_f = tk.Frame(parent, bg="#f8f9fa")
        result_lbl_f.pack(fill=tk.X, padx=10, pady=(4, 0))
        tk.Label(result_lbl_f, text="Search Results",
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
        tk.Button(open_f, text="↗ Open (Enter/Dbl-click)",
                  command=self._open_find_selected,
                  bg="#1a73e8", fg="white",
                  font=("Malgun Gothic", 9, "bold"), relief="flat", pady=3
                  ).pack(side=tk.LEFT, padx=(0, 4))
        tk.Button(open_f, text="📂 Open Folder",
                  command=self._open_find_parent,
                  bg="#5f6368", fg="white",
                  font=("Malgun Gothic", 9, "bold"), relief="flat", pady=3
                  ).pack(side=tk.LEFT)
        tk.Button(open_f, text="➡ Send to Merger",
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
                                    text=f"Path: {self._search_root}",
                                    fg="#888", bg="#f0f0f0",
                                    font=("Consolas", 8), anchor="w", pady=2)
        self.find_status.pack(fill=tk.X)

        tk.Label(parent,
                 text="CLICKFIND v3.4 (FuzzySearch) | © 2026. bc5103",
                 fg="#adb5bd", bg="#f8f9fa", font=("Consolas", 8)
                 ).pack(pady=1)

        self._find_log("v3.4 FUZZY-SEARCH READY.  Typo-tolerant fuzzy file search.")

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
            self.lbl_split_mb.config(text=f"Current: {self._split_mb}MB")
            self.merge_log(f"Split size updated → {self._split_mb}MB")
        except ValueError:
            self.merge_log("⚠ Enter a valid number (e.g. 19.5)")

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
                title="Select Files", filetypes=[("Supported files", ext_str)])
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
        if added:       self.merge_log(f"ADD: {len(added)} file(s) added  (total {len(self._file_paths)})")
        if skipped_dup: self.merge_log(f"  ⚠ Duplicate skipped: {', '.join(skipped_dup)}")
        if skipped_ext: self.merge_log(f"  ⛔ Unsupported format skipped: {', '.join(skipped_ext)}")

    def remove_selected(self):
        idxs = sorted(self.listbox.curselection(), reverse=True)
        if not idxs: return
        for i in idxs: del self._file_paths[i]
        self._refresh_listbox()
        self.merge_log(f"REMOVED: {len(idxs)} file(s) removed")

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
            self.merge_log("⚠ No files in list."); return

        # ── 호증 종류 선택 다이얼로그 ──
        ho_type = simpledialog.askstring(
            "Exhibit type",
            "Enter exhibit party.\n\n"
            "A  → Exhibit A-N\n"
            "B  → Exhibit B-N\n"
            "C  → Exhibit C-N\n"
            "Sub-A → Sub-A N\n"
            "Sub-B → Sub-B N\n",
            initialvalue="A"
        )
        if not ho_type: return
        ho_type = ho_type.strip()
        if ho_type not in ["A", "B", "C", "Sub-A", "Sub-B"]:
            ho_type = "A"

        start_no = simpledialog.askinteger(
            "Start Number", f"{ho_type} exhibit start number:", initialvalue=1, minvalue=1, maxvalue=999)
        if not start_no: return

        default_name = f"ExhibitList_{ho_type}_{datetime.datetime.now().strftime('%m%d_%H%M')}.pdf"
        save_path = filedialog.asksaveasfilename(
            title=f"Save Exhibit List ({ho_type}) as PDF", initialfile=default_name,
            defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
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
            c.drawCentredString(w / 2, h - 60, f"EXHIBIT LIST  ({ho_type})")
            c.setFont(font_name, 9)
            c.drawCentredString(w / 2, h - 80,
                f"Created: {now_str}  |  Total: {len(self._file_paths)} files  |  Start: Exhibit {ho_type}-{start_no}")

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
                line_text = f"Exhibit {ho_type}-{no}   {name}   [{ext}  {size_mb:.1f}MB]"
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
                f"{PRODUCT_NAME} {BUILD_NUMBER}  |  © 2026. Byungjin Park  |  {_SESSION_BRAND_CAPTION}")
            c.setFont(font_name, 7)
            c.drawCentredString(w / 2, 22, FREE_BUILD_ID)
            c.save()

            self.merge_log(f"Exhibit list PDF saved → {os.path.basename(save_path)}  ({len(self._file_paths)} files)")
            open_folder_safe(os.path.dirname(os.path.abspath(save_path)))
        except Exception as e:
            self.merge_log(f"Exhibit list save failed: {e}")

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
            self.merge_log("⚠ Busy. Please wait until current task completes."); return
        file_path = filedialog.askopenfilename(
            title="Select PDF to split", filetypes=[("PDF files", "*.pdf")])
        if not file_path: return

        def process():
            self.root.after(0, self._lock_buttons)
            self.merge_log(f"SPLITTING: {os.path.basename(file_path)}  (limit: {self._split_mb}MB)")
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
                self.merge_log(f"SPLIT DONE. {part_num} file(s) created")
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
    # ── v6.8.4 라이선스 메서드 ─────────────────────────────────
    def _lgk_update_label(self, count: int, unlocked: bool = False) -> None:
        # v7.0.9: limit removed — always show unlimited
        self._lgk_var.set("✓ Personal: unlimited  ·  Commercial: contact us")
        self._lgk_unlocked = True

    def _lgk_check(self) -> bool:
        """Pre-merge check. v7.0.9: limit removed — always returns True."""
        return True

    def _lgk_show_dialog(self) -> None:
        dlg = tk.Toplevel(self.root)
        dlg.title("Merge Limit Reached — License Required")
        dlg.configure(bg="#0a0a0a")
        dlg.resizable(False, False)
        dlg.grab_set()

        tk.Label(dlg, text="You have used all free merges.",
                 fg="#f9e2af", bg="#0a0a0a", font=("맑은 고딕", 10, "bold"),
                 pady=10).pack(padx=20)
        tk.Label(dlg,
                 text="To purchase a license key, send your Machine ID to the developer.\n"
                      "Blog: blog.naver.com/bc5103  |  Email: dede5003@gmail.com",
                 fg="#aaa", bg="#0a0a0a", font=("Consolas", 8), justify="left").pack(padx=20)

        mid_var = tk.StringVar(value=self._mid)
        mid_e = tk.Entry(dlg, textvariable=mid_var, width=22, state="readonly",
                         bg="#1a1a1a", fg="#79b8ff", font=("Consolas", 10),
                         readonlybackground="#1a1a1a", relief="flat")
        mid_e.pack(pady=(6, 2), padx=20)
        tk.Button(dlg, text="Copy Machine ID", command=lambda: (dlg.clipboard_clear(), dlg.clipboard_append(self._mid)),
                  bg="#2a5298", fg="white", font=("맑은 고딕", 8), relief="flat",
                  padx=6, pady=2).pack(pady=(0, 8))

        tk.Label(dlg, text="Enter license key (long signature can be pasted):", fg="#aaa", bg="#0a0a0a",
                 font=("맑은 고딕", 9)).pack()
        key_var = tk.StringVar()
        tk.Entry(dlg, textvariable=key_var, width=80, bg="#1a1a1a", fg="#e0e0e0",
                 insertbackground="#e0e0e0", font=("Consolas", 9), relief="flat").pack(pady=4, padx=20)

        def _activate():
            if _lgk_validate(key_var.get(), self._mid):
                d = _lgk_load(); d["unlocked"] = True; _lgk_save(d)
                self._lgk_update_label(0, True)
                messagebox.showinfo("Activation", "License activated! Unlimited merges unlocked.", parent=dlg)
                dlg.destroy()
            else:
                messagebox.showerror("Error", "Invalid key.\nPlease send your Machine ID to the developer.", parent=dlg)

        tk.Button(dlg, text="Activate", command=_activate,
                  bg="#2980b9", fg="white", font=("맑은 고딕", 9, "bold"),
                  relief="flat", padx=10, pady=3).pack(pady=(4, 12))

    # ────────────────────────────────────────────────────────────
    def run_merger(self, compress_mode):
        if self._busy:
            self.merge_log("⚠ Busy. Please wait until current task completes."); return
        # v6.8.4 — 병합 횟수 제한 체크
        if not self._lgk_check():
            return
        if not self._file_paths:
            ext_str = "*.pdf *.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp *.heic *.ico *.jfif"
            files = filedialog.askopenfilenames(title="Select Files", filetypes=[("Supported files", ext_str)])
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
            mode_str = "compress" if compress_mode else "normal"
            self.merge_log(f"MERGING {total} file(s)... [{mode_str} mode] (order locked)")
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
                                    self.merge_log(f"  TIFF {len(frames)}-frame converted (ad overlay): {os.path.basename(f_path)}")
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
                            self.merge_log(f"  ⚠ Image skipped ({os.path.basename(f_path)}): {ie}")
                    else:
                        self.merge_log(f"  ⚠ Unsupported format skipped: {ext}")

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
                                   f"{'[ad overlay]' if overlay_ok else '[overlay failed·original kept]'}")
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
            self.find_status.config(text=f"Path: {self._search_root}")
            self._find_log(f"PATH set → {p}")

    def _start_search(self):
        if self._searching:
            self._find_log("⚠ Search in progress. Please wait."); return
        query = self.find_entry.get().strip()
        if not query: return
        self.result_box.delete(0, tk.END)
        self._find_results.clear()
        self.lbl_find_count.config(text="Searching...")
        self.btn_find.config(state=tk.DISABLED, text="⏳ Searching")
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
            self.result_box.insert(tk.END, f"  No results similar to '{query}'.")
            self.lbl_find_count.config(text="0 results")
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
            self.lbl_find_count.config(text=f"{len(scored)} result(s)")
            self.result_box.selection_set(0)
            self._find_log(f"Search '{query}' → {len(scored)} result(s) (threshold {int(self.threshold_var.get()*100)}%)")
        self._searching = False
        self.btn_find.config(state=tk.NORMAL, text="🔍 Search")

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
            self._find_log("No files to send.")
            return

        valid   = [p for p in paths
                   if os.path.splitext(p)[1].lower() in SUPPORTED_EXT]
        skipped = len(paths) - len(valid)

        if not valid:
            self._find_log("No supported format files found.")
            return

        self.add_files(valid)
        self.nb.select(0)
        self._find_log(
            f"➡ Sent to Merger: {len(valid)} file(s)"
            + (f"  ({skipped} unsupported skipped)" if skipped else "")
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
        tk.Label(parent, text="◈  Evidence List  ─  Extract filenames as text",
                 fg="#b0c4de", bg="#111", font=("Consolas", 9, "bold"), pady=5
                 ).pack(fill=tk.X)

        # ── 번호 접두어 + 시작번호 + 출력형식 ──
        cfg_frame = tk.Frame(parent, bg="#111", pady=4)
        cfg_frame.pack(fill=tk.X, padx=8, pady=(4, 0))

        tk.Label(cfg_frame, text="Number format:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT, padx=(0, 3))

        self.ev_prefix_var = tk.StringVar(value=PREFIX_OPTIONS[0])
        prefix_menu = tk.OptionMenu(cfg_frame, self.ev_prefix_var, *PREFIX_OPTIONS)
        prefix_menu.config(bg="#1a1a1a", fg="#ccc", font=("Consolas", 8),
                           relief="flat", highlightthickness=0, width=9,
                           activebackground="#2a2a2a", activeforeground="#fff")
        prefix_menu["menu"].config(bg="#1a1a1a", fg="#ccc", font=("Consolas", 8))
        prefix_menu.pack(side=tk.LEFT, padx=2)

        tk.Label(cfg_frame, text="  Start No.:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        self.ev_start_num = tk.Entry(cfg_frame, width=4, bg="#1a1a1a", fg="#e0e0e0",
                                     insertbackground="#e0e0e0",
                                     font=("Consolas", 9), relief="flat",
                                     highlightthickness=1, highlightcolor="#4a90d9",
                                     highlightbackground="#333")
        self.ev_start_num.insert(0, "1")
        self.ev_start_num.pack(side=tk.LEFT, padx=4)

        tk.Label(cfg_frame, text="  Output format:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        self.ev_fmt_var = tk.StringVar(value="TXT")
        for fmt in ("TXT", "CSV", "Clipboard"):
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
        self.ev_tree.heading("name",     text="Filename",    anchor=tk.W)
        self.ev_tree.heading("ext",      text="Type",      anchor=tk.CENTER)
        self.ev_tree.heading("size",     text="Size",      anchor=tk.E)
        self.ev_tree.heading("modified", text="Modified",    anchor=tk.CENTER)
        self.ev_tree.heading("path",     text="Path",      anchor=tk.W)

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
        self._ev_ctx_menu.add_command(label="▲ Up",        command=self._ev_move_up)
        self._ev_ctx_menu.add_command(label="▼ Down",      command=self._ev_move_down)
        self._ev_ctx_menu.add_command(label="⤒ Top",       command=self._ev_move_top)
        self._ev_ctx_menu.add_command(label="⤓ Bottom",     command=self._ev_move_bottom)
        self._ev_ctx_menu.add_separator()
        self._ev_ctx_menu.add_command(label="📂 Open Location", command=self._ev_open_file_location)
        self._ev_ctx_menu.add_separator()
        self._ev_ctx_menu.add_command(label="✕ Remove",      command=self._ev_remove_selected)
        self.ev_tree.bind("<Button-3>", lambda e: self._ev_ctx_menu.post(e.x_root, e.y_root))

        # ── 순서 버튼 행 ──
        order_frame = tk.Frame(parent, bg="#0a0a0a")
        order_frame.pack(fill=tk.X, padx=8, pady=3)

        ob = {"font": ("맑은 고딕", 8, "bold"), "relief": "flat", "bd": 0,
              "padx": 6, "pady": 3}
        tk.Button(order_frame, text="▲ Up",    command=self._ev_move_up,
                  bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_frame, text="▼ Down",  command=self._ev_move_down,
                  bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_frame, text="⤒ Top",    command=self._ev_move_top,
                  bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_frame, text="⤓ Bottom",  command=self._ev_move_bottom,
                  bg="#1a3a5c", fg="#79b8ff", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_frame, text="✕ Remove",    command=self._ev_remove_selected,
                  bg="#3a1a1a", fg="#ff7b7b", **ob).pack(side=tk.LEFT, padx=2)
        tk.Button(order_frame, text="🗑 Clear All", command=self._ev_clear_list,
                  bg="#3a1a1a", fg="#ff7b7b", **ob).pack(side=tk.LEFT, padx=2)

        self.ev_lbl_count = tk.Label(order_frame, text="0 files | Total 0 B",
                                     fg="#555", bg="#0a0a0a", font=("Consolas", 8))
        self.ev_lbl_count.pack(side=tk.RIGHT, padx=6)

        # ── 액션 버튼 ──
        act_frame = tk.Frame(parent, bg="#0a0a0a")
        act_frame.pack(pady=5)

        ab = {"font": ("맑은 고딕", 8, "bold"), "height": 1, "relief": "flat"}
        tk.Button(act_frame, text="📂 Add Files",    command=self._ev_add_files,
                  width=9,  bg="#1b4332", fg="#52b788", **ab).pack(side=tk.LEFT, padx=3)
        tk.Button(act_frame, text="📋 Export List", command=self._ev_export_list,
                  width=12, bg="#1a3a6a", fg="#79b8ff", **ab).pack(side=tk.LEFT, padx=3)
        tk.Button(act_frame, text="🔍 Preview",     command=self._ev_preview_list,
                  width=9,  bg="#2a1a3a", fg="#b87fff", **ab).pack(side=tk.LEFT, padx=3)

        # ── 로그 ──
        log_hdr = tk.Frame(parent, bg="#0a0a0a")
        log_hdr.pack(fill=tk.X, padx=8, pady=(2, 0))
        tk.Label(log_hdr, text="LOG", fg="#444", bg="#0a0a0a",
                 font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        tk.Button(log_hdr, text="Clear", command=lambda: self.ev_log_board.delete("1.0", tk.END),
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

        self._ev_log("Evidence List READY.  Drag files here or click [Add Files].")
        self._ev_log("※ All formats supported: PDF, images, executables, video, etc.")

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
        self.ev_lbl_count.config(text=f"{n} file(s)  |  Total {fmt_size(total_bytes)}")

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
            paths = filedialog.askopenfilenames(title="Select Files",
                                                filetypes=[("All files", "*.*")])
        added = 0
        for p in paths:
            p = p.strip("{}")  # tkinterdnd2 중괄호 처리
            if p and p not in self._ev_files:
                self._ev_files.append(p)
                added += 1
        if added:
            self._ev_refresh_tree()
            self._ev_log(f"ADD: {added} file(s) added  (total {len(self._ev_files)})")

    def _ev_remove_selected(self):
        idxs = sorted(self._ev_selected_indices(), reverse=True)
        for i in idxs: del self._ev_files[i]
        self._ev_refresh_tree()

    def _ev_clear_list(self):
        if self._ev_files and messagebox.askyesno("Clear All", "Remove all items from the evidence list?"):
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
            self._ev_log("⚠ No files in list."); return

        lines = self._ev_build_lines()
        win = tk.Toplevel(self.root)
        win.title("Evidence List Preview")
        win.geometry("560x420")
        win.configure(bg="#0a0a0a")
        win.attributes("-topmost", True)

        st = scrolledtext.ScrolledText(win, bg="#0d0d0d", fg="#e0e0e0",
                                       font=("Consolas", 9), borderwidth=0)
        st.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        st.insert(tk.END, "\n".join(lines))
        st.config(state="disabled")

        tk.Button(win, text="Close", command=win.destroy,
                  bg="#2a2a2a", fg="#aaa", font=("맑은 고딕", 9),
                  relief="flat", padx=10, pady=3).pack(pady=4)

    def _ev_build_lines(self):
        start = self._ev_get_start()
        fmt   = self.ev_fmt_var.get()
        lines = []
        tool_tag = f"{PRODUCT_NAME} {BUILD_NUMBER} · {_SESSION_BRAND_CAPTION} · {FREE_BUILD_ID}"

        if fmt == "CSV":
            # v6.8.0: 우측 끝 "수집도구" 컬럼 신설
            lines.append("No.,Filename,Type,Size,Modified,Path,Tool")
        else:
            # v6.8.0: 상단 헤더 4행
            lines.append("E V I D E N C E   L I S T")
            lines.append(f"{'─'*50}")
            lines.append(f"Created: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
            lines.append(f"Total: {len(self._ev_files)} file(s)")
            lines.append(f"Tool: {PRODUCT_NAME} {BUILD_NUMBER}  |  {FREE_BUILD_ID}")
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
                lines.append(f"{'':14} Type: {ext}  Size: {size_s}  Modified: {date_s}")
                lines.append(f"{'':14} Path: {p}")
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
            self._ev_log("⚠ No files in list."); return

        lines = self._ev_build_lines()
        text  = "\n".join(lines)
        fmt   = self.ev_fmt_var.get()

        if fmt == "Clipboard":
            try:
                # v6.8.0: 말미 1줄 광고 부가
                clip_text = text + f"\n\n— {PRODUCT_NAME} {BUILD_NUMBER}  ·  {_SESSION_BRAND_CAPTION}\n  {FREE_BUILD_ID}"
                self.root.clipboard_clear()
                self.root.clipboard_append(clip_text)
                self._ev_log(f"Copied to clipboard ({len(self._ev_files)} file(s))")
            except Exception as e:
                self._ev_log(f"Clipboard copy failed: {e}")
            return

        ext_map  = {"TXT": ".txt", "CSV": ".csv"}
        ext      = ext_map.get(fmt, ".txt")
        default  = f"EvidenceList_{datetime.datetime.now().strftime('%m%d_%H%M')}{ext}"
        save_path = filedialog.asksaveasfilename(
            title="Save Evidence List",
            initialfile=default,
            defaultextension=ext,
            filetypes=[(f"{fmt} file", f"*{ext}"), ("All files", "*.*")],
        )
        if not save_path: return

        try:
            with open(save_path, "w", encoding="utf-8-sig") as f:
                f.write(text)
            self._ev_log(f"Saved → {os.path.basename(save_path)}  ({len(self._ev_files)} file(s))")
            open_folder_safe(os.path.dirname(os.path.abspath(save_path)))
        except Exception as e:
            self._ev_log(f"Save failed: {e}")


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
        tk.Label(parent, text="◈  Case Collector  ─  Korean Law Open API (open.law.go.kr)",
                 fg="#b0c4de", bg="#111", font=("Consolas", 9, "bold"), pady=5
                 ).pack(fill=tk.X)

        # ── OC 인증키 입력 ──
        oc_frame = tk.Frame(parent, bg="#111", pady=4)
        oc_frame.pack(fill=tk.X, padx=8, pady=(4, 0))

        tk.Label(oc_frame, text="OC API Key:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT, padx=(0, 3))

        self.case_oc_var = tk.StringVar()
        self.case_oc_entry = tk.Entry(oc_frame, textvariable=self.case_oc_var,
                                      width=18, bg="#1a1a1a", fg="#e0e0e0",
                                      insertbackground="#e0e0e0",
                                      font=("Consolas", 9), relief="flat",
                                      highlightthickness=1, highlightcolor="#4a90d9",
                                      highlightbackground="#333")
        self.case_oc_entry.pack(side=tk.LEFT, padx=4)

        tk.Button(oc_frame, text="Save", command=self._case_save_oc,
                  bg="#1a3a5c", fg="#79b8ff",
                  font=("맑은 고딕", 8, "bold"), relief="flat",
                  padx=8, pady=2).pack(side=tk.LEFT, padx=2)

        tk.Label(oc_frame, text="  ※ Your ID from open.law.go.kr account",
                 fg="#444", bg="#111", font=("Consolas", 8)).pack(side=tk.LEFT, padx=4)

        # 저장된 OC 자동 로드
        self._case_load_oc()

        # ── 검색 키워드 입력 ──
        kw_frame = tk.Frame(parent, bg="#111", pady=4)
        kw_frame.pack(fill=tk.X, padx=8, pady=(2, 0))

        tk.Label(kw_frame, text="Search keyword:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT, padx=(0, 3))

        self.case_query_var = tk.StringVar()
        self.case_query_entry = tk.Entry(kw_frame, textvariable=self.case_query_var,
                                         width=22, bg="#1a1a1a", fg="#e0e0e0",
                                         insertbackground="#e0e0e0",
                                         font=("Consolas", 9), relief="flat",
                                         highlightthickness=1, highlightcolor="#4a90d9",
                                         highlightbackground="#333")
        self.case_query_entry.pack(side=tk.LEFT, padx=4)

        tk.Label(kw_frame, text="  Max results:", fg="#888", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT)
        self.case_max_var = tk.IntVar(value=100)
        tk.Spinbox(kw_frame, from_=1, to=1000, textvariable=self.case_max_var,
                   width=5, font=("Consolas", 9),
                   bg="#1a1a1a", fg="#e0e0e0",
                   insertbackground="#e0e0e0",
                   relief="flat").pack(side=tk.LEFT, padx=4)

        tk.Label(kw_frame, text="  (e.g. fraud, obstruction, criminal code 347)",
                 fg="#444", bg="#111", font=("Consolas", 8)).pack(side=tk.LEFT, padx=4)

        # ── v672 본문 필터 키워드 입력 (2단계 검색) ──
        ft_frame = tk.Frame(parent, bg="#111", pady=4)
        ft_frame.pack(fill=tk.X, padx=8, pady=(2, 0))

        tk.Label(ft_frame, text="Body filter:", fg="#c0a040", bg="#111",
                 font=("Consolas", 8)).pack(side=tk.LEFT, padx=(0, 3))

        self.case_filter_var = tk.StringVar()
        self.case_filter_entry = tk.Entry(ft_frame, textvariable=self.case_filter_var,
                                          width=22, bg="#1a1a1a", fg="#f0d060",
                                          insertbackground="#f0d060",
                                          font=("Consolas", 9), relief="flat",
                                          highlightthickness=1, highlightcolor="#c0a040",
                                          highlightbackground="#333")
        self.case_filter_entry.pack(side=tk.LEFT, padx=4)

        tk.Label(ft_frame, text="  (leave blank = all results / enter keyword to filter body text)",
                 fg="#444", bg="#111", font=("Consolas", 8)).pack(side=tk.LEFT, padx=4)

        # ── 액션 버튼 ──
        act_frame = tk.Frame(parent, bg="#0a0a0a")
        act_frame.pack(pady=8)

        ab = {"font": ("맑은 고딕", 9, "bold"), "height": 1, "relief": "flat"}
        self.case_btn_run = tk.Button(act_frame, text="▶ Start Collection",
                                      command=self._case_start,
                                      width=18, bg="#1b4332", fg="#52b788", **ab)
        self.case_btn_run.pack(side=tk.LEFT, padx=3)

        tk.Button(act_frame, text="📂 Open Output Folder",
                  command=self._case_open_output,
                  width=15, bg="#1a3a6a", fg="#79b8ff", **ab).pack(side=tk.LEFT, padx=3)

        # ── 진행 상황 + 로그 ──
        log_hdr = tk.Frame(parent, bg="#0a0a0a")
        log_hdr.pack(fill=tk.X, padx=8, pady=(4, 0))
        tk.Label(log_hdr, text="LOG", fg="#444", bg="#0a0a0a",
                 font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        tk.Button(log_hdr, text="Clear",
                  command=lambda: self.case_log_board.delete("1.0", tk.END),
                  bg="#1a1a1a", fg="#555", font=("Consolas", 8),
                  relief="flat", padx=4, pady=0).pack(side=tk.RIGHT)

        self.case_log_board = scrolledtext.ScrolledText(
            parent, width=70, height=18, bg="#060606", fg="#33ff33",
            font=("Consolas", 9), borderwidth=0, highlightthickness=0)
        self.case_log_board.pack(pady=(2, 6), padx=8, fill=tk.BOTH, expand=True)

        self._case_log("Case Collector READY.  Korean Law Open API.")
        self._case_log("1) Enter OC API key → click [Save] (once)")
        self._case_log("2) Enter keyword → click [▶ Start Collection]")
        self._case_log("3) Output CSV saved in ~/case_crawler_output/")

    # ── OC 저장·로드 (홈 디렉토리 oc.txt 단일 파일) ──
    def _case_oc_path(self):
        return os.path.join(os.path.expanduser("~"), ".click_legal_kit_oc.txt")

    def _case_save_oc(self):
        oc = self.case_oc_var.get().strip()
        if not oc:
            self._case_log("⚠ OC API key is empty.")
            return
        try:
            with open(self._case_oc_path(), "w", encoding="utf-8") as f:
                f.write(oc)
            self._case_log(f"OC API key saved. (auto-loaded on next run)")
        except Exception as e:
            self._case_log(f"OC key save failed: {e}")

    def _case_load_oc(self):
        try:
            p = self._case_oc_path()
            if os.path.exists(p):
                with open(p, "r", encoding="utf-8") as f:
                    oc = f.read().strip()
                if oc:
                    self.case_oc_var.set(oc)
        except Exception:
            pass

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
            self._case_log(f"⚠ Output folder not yet created: {out_dir}")
            return
        open_folder_safe(out_dir)

    # ── 수집 시작 (threading) ──
    def _case_start(self):
        if self._case_running:
            self._case_log("⚠ Collection already in progress.")
            return
        oc = self.case_oc_var.get().strip()
        if not oc:
            self._case_log("⚠ OC API key required.")
            return
        query = self.case_query_var.get().strip()
        if not query:
            self._case_log("⚠ Search keyword required.")
            return
        try:
            max_cases = max(1, min(int(self.case_max_var.get()), 1000))
        except Exception:
            max_cases = 100

        self._case_running = True
        self.case_btn_run.config(text="⏳ Collecting...", state="disabled")
        filter_kw = self.case_filter_var.get().strip()
        t = threading.Thread(
            target=self._case_run_worker,
            args=(oc, query, max_cases, filter_kw),
            daemon=True)
        t.start()

    def _case_run_worker(self, oc, query, max_cases, filter_kw=""):
        try:
            crawler = CaseCrawler(oc, log_fn=self._case_log)
            self._case_log(f"[START] query: '{query}'  /  max: {max_cases} cases")
            if filter_kw:
                self._case_log(f"[FILTER] body keyword: '{filter_kw}'")
            cases = crawler.fetch_list(query, max_cases=max_cases)
            if not cases:
                self._case_log("[END] No results collected.")
                return
            self._case_log(f"[INFO] Records found: {len(cases)}. Fetching details.")
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
                    f"[FILTER] '{filter_kw}' body filter applied: "
                    f"{before_cnt} of {len(cases)} matched.")
                if not cases:
                    self._case_log("[END] No cases matched the filter.")
                    return
            filepath = crawler.save_csv(cases, query)
            if filepath:
                self._case_log(f"[DONE] Saved: {filepath}")
                self._case_log(f"       Total {len(cases)} case(s) collected.")
        except Exception as e:
            self._case_log(f"[FATAL] {type(e).__name__}: {e}")
        finally:
            self._case_running = False
            try:
                self.case_btn_run.config(text="▶ Start Collection", state="normal")
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
        tk.Label(parent, text="🏷  Exhibit Labeler — Bulk exhibit numbering for PDF files",
                 fg="#f1c40f", bg="#111",
                 font=("맑은 고딕", 10, "bold"), pady=5
                 ).pack(fill=tk.X)

        # ── 옵션 줄 ──
        opt = tk.Frame(parent, bg="#0a0a0a")
        opt.pack(fill=tk.X, padx=8, pady=(6, 4))

        tk.Label(opt, text="Party:", fg="#cccccc", bg="#0a0a0a",
                 font=("맑은 고딕", 9)).pack(side=tk.LEFT, padx=(0, 6))
        self._lbl_party_var = tk.StringVar(value="A")
        for party in ("A", "B", "C", "D"):
            tk.Radiobutton(opt, text=party, value=party,
                           variable=self._lbl_party_var,
                           fg="#ffffff", bg="#0a0a0a",
                           selectcolor="#1a3a5f",
                           activebackground="#0a0a0a",
                           activeforeground="#ffffff",
                           font=("맑은 고딕", 9),
                           command=self._lbl_refresh_tree
                           ).pack(side=tk.LEFT, padx=2)

        tk.Label(opt, text="   Start No.:", fg="#cccccc", bg="#0a0a0a",
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
        tk.Button(btn, text="📂 Add PDFs", command=self._lbl_add_files,
                  bg="#2c3e50", fg="white",
                  font=("맑은 고딕", 9), padx=8, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="▲ Up", command=lambda: self._lbl_move(-1),
                  bg="#34495e", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="▼ Down", command=lambda: self._lbl_move(1),
                  bg="#34495e", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="→ Sub-exhibit",
                  command=self._lbl_indent_selected,
                  bg="#27ae60", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="← Main exhibit",
                  command=self._lbl_outdent_selected,
                  bg="#16a085", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="✕ Remove", command=self._lbl_remove_selected,
                  bg="#c0392b", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))
        tk.Button(btn, text="🗑 Clear All", command=self._lbl_clear_all,
                  bg="#7f8c8d", fg="white",
                  font=("맑은 고딕", 9), padx=6, pady=2,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 3))

        # ── 트리뷰 ──
        tree_frame = tk.Frame(parent, bg="#0a0a0a")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 4))
        cols = ("no", "old", "new")
        self._lbl_tree = ttk.Treeview(tree_frame, columns=cols,
                                       show="headings", height=14)
        self._lbl_tree.heading("no",  text="Exhibit No.")
        self._lbl_tree.heading("old", text="Current Filename")
        self._lbl_tree.heading("new", text="New Filename")
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
        tk.Button(run, text="👁 Refresh Preview",
                  command=self._lbl_refresh_tree,
                  bg="#2980b9", fg="white",
                  font=("맑은 고딕", 9, "bold"), padx=10, pady=4,
                  relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 6))
        tk.Button(run, text="🏷 Bulk Rename",
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
        self._lbl_log_msg("v6.8.3 Exhibit Labeler READY. Add PDFs or drag & drop.")
        self._lbl_log_msg("Sub-exhibit (→) up to 1 level. Indented rows auto-numbered as sub-exhibits.")

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
            title="Select PDF files for exhibit labeling",
            filetypes=[("PDF", "*.pdf"), ("All files", "*.*")])
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
            self._lbl_log_msg(f"{added} PDF(s) added. Total {len(self._lbl_items)}.")
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
        self._lbl_log_msg(f"{len(idxs)} removed. Total {len(self._lbl_items)}.")
        self._lbl_refresh_tree()

    def _lbl_clear_all(self):
        if not self._lbl_items:
            return
        if not messagebox.askyesno("Clear All", "Remove all items from the list?"):
            return
        self._lbl_items = []
        self._lbl_log_msg("All items cleared.")
        self._lbl_refresh_tree()

    # ── 호증부여기 — 채번 계산 + 새 이름 미리 산출 ──
    def _lbl_compose_names(self):
        """[(label_no_str, new_basename), ...] 반환."""
        result = []
        try:
            party = self._lbl_party_var.get() or "A"
            start = int(self._lbl_start_var.get())
            if start < 1:
                start = 1
        except Exception:
            party = "A"
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
                prefix = f"Exhibit_{party}-{main_no}_"
            else:
                # 본번을 한 번도 안 만난 상태에서 가지번호 → 본번으로 폴백
                if main_no < start:
                    main_no = start
                    branch_no = 0
                    no_str = f"{main_no}"
                    prefix = f"Exhibit_{party}-{main_no}_"
                else:
                    branch_no += 1
                    no_str = f"{main_no}-{branch_no}"
                    prefix = f"Exhibit_{party}-{main_no}-{branch_no}_"
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
            messagebox.showinfo("Exhibit Labeler", "No PDF files added.")
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
                self._lbl_log_msg(f"⚠ Planning error: {e}")

        if not plan:
            return
        if not messagebox.askyesno(
                "Exhibit Labeler",
                f"Rename {len(plan)} PDF file(s).\nProceed?"):
            self._lbl_log_msg("Rename cancelled.")
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
                    f"✗ {os.path.basename(old_p)} failed: {e}")
        # 들여쓰기 상태 복원
        for i, it in enumerate(new_items):
            try:
                it['indent'] = int(self._lbl_items[i].get('indent', 0) or 0)
            except Exception:
                it['indent'] = 0
        self._lbl_items = new_items
        self._lbl_refresh_tree()
        self._lbl_log_msg(f"Done. Success: {ok} / Failed: {fail}.")
        messagebox.showinfo(
            "Exhibit Labeler",
            f"Rename complete\nSuccess: {ok} / Failed: {fail}")

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
        self._ts_LANGS = [("Auto Detect", None), ("English", "en"), ("Korean", "ko"),
                          ("Japanese", "ja"), ("Chinese", "zh")]
        self._ts_running = False
        self._ts_queue = []
        self._ts_last_out_dir = ""

        C_BG="#0a0a0a"; C_PANEL="#1a1a1a"; C_ACCENT="#2a5298"; C_FG="#cccccc"
        C_FG2="#888888"; C_DROP="#1e2e1e"; C_DROP_BD="#3a7a3a"; C_GOLD="#f9e2af"
        C_OK="#a6e3a1"; C_WARN="#f9e2af"; C_ERR="#f38ba8"; C_INFO="#89dceb"

        # 헤더
        _tk.Label(parent, text="  🎙 Transcript  ·  Whisper Audio→Text  ·  Local processing",
                  fg=C_FG2, bg="#111111", font=("Consolas", 9, "bold"),
                  pady=4, anchor="w").pack(fill="x")

        # 드롭 영역
        drop_frame = _tk.LabelFrame(parent, text="  Drop / Select",
                                    fg=C_FG, bg=C_BG, font=("맑은 고딕", 9, "bold"))
        drop_frame.pack(fill="x", padx=6, pady=(6, 3))
        self._ts_drop = _tk.Label(drop_frame,
            text="Drag and drop audio/video files here, or click to browse\n"
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
        qframe = _tk.LabelFrame(parent, text="  Queue",
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
        _tk.Button(qbtn, text="Remove", command=self._ts_remove_selected,
                   bg=C_PANEL, fg=C_FG, relief="flat", cursor="hand2",
                   font=("맑은 고딕", 9), width=6, pady=3).pack(side="left", padx=2)
        _tk.Button(qbtn, text="Clear All", command=self._ts_clear_queue,
                   bg=C_PANEL, fg=C_FG, relief="flat", cursor="hand2",
                   font=("맑은 고딕", 9), width=8, pady=3).pack(side="left", padx=2)

        # 옵션
        opt = _tk.LabelFrame(parent, text="  Options",
                             fg=C_FG, bg=C_BG, font=("맑은 고딕", 9, "bold"))
        opt.pack(fill="x", padx=6, pady=3)
        row0 = _tk.Frame(opt, bg=C_BG); row0.pack(fill="x", padx=5, pady=4)
        _tk.Label(row0, text="Language:", fg=C_FG, bg=C_BG,
                  font=("맑은 고딕", 9)).pack(side="left")
        self._ts_lang_var = _tk.StringVar(value="Auto Detect")
        _ttk.Combobox(row0, textvariable=self._ts_lang_var,
                      values=[l[0] for l in self._ts_LANGS],
                      width=10, state="readonly", font=("맑은 고딕", 9)
                      ).pack(side="left", padx=(2, 10))
        _tk.Label(row0, text="Output:", fg=C_FG, bg=C_BG,
                  font=("맑은 고딕", 9)).pack(side="left")
        self._ts_fmt_var = _tk.StringVar(value="txt")
        _ttk.Combobox(row0, textvariable=self._ts_fmt_var,
                      values=_TS_OUT_FMTS, width=7, state="readonly",
                      font=("맑은 고딕", 9)).pack(side="left", padx=(2, 10))
        _tk.Label(row0, text="Engine: Whisper small", fg=C_FG2, bg=C_BG,
                  font=("맑은 고딕", 9)).pack(side="left")

        row1 = _tk.Frame(opt, bg=C_BG); row1.pack(fill="x", padx=5, pady=(0, 4))
        _tk.Label(row1, text="Save to:", fg=C_FG, bg=C_BG,
                  font=("맑은 고딕", 9)).pack(side="left")
        self._ts_outdir_var = _tk.StringVar(value="(same as input)")
        _tk.Entry(row1, textvariable=self._ts_outdir_var, width=28,
                  bg=C_PANEL, fg=C_FG, insertbackground=C_FG, relief="flat",
                  font=("맑은 고딕", 9)).pack(side="left", padx=(4, 3))
        _tk.Button(row1, text="Browse", command=self._ts_select_outdir,
                   bg=C_PANEL, fg=C_FG, relief="flat", cursor="hand2",
                   font=("맑은 고딕", 9), width=7, pady=3).pack(side="left", padx=2)
        _tk.Button(row1, text="Reset",
                   command=lambda: self._ts_outdir_var.set("(same as input)"),
                   bg=C_PANEL, fg=C_FG, relief="flat", cursor="hand2",
                   font=("맑은 고딕", 9), width=6, pady=3).pack(side="left", padx=2)
        _tk.Button(row1, text="Open Folder", command=self._ts_open_last_folder,
                   bg=C_PANEL, fg=C_FG, relief="flat", cursor="hand2",
                   font=("맑은 고딕", 9), width=8, pady=3).pack(side="left", padx=2)

        # 실행 버튼
        btn_row = _tk.Frame(parent, bg=C_BG); btn_row.pack(fill="x", padx=6, pady=4)
        self._ts_run_btn = _tk.Button(btn_row, text="▶  Start",
            command=self._ts_start, bg=C_ACCENT, fg="#fff",
            font=("맑은 고딕", 10, "bold"), relief="flat", cursor="hand2",
            padx=14, pady=4)
        self._ts_run_btn.pack(side="left", padx=(0, 5))
        self._ts_stop_btn = _tk.Button(btn_row, text="■  Stop",
            command=self._ts_stop, bg="#5a1a1a", fg="#f38ba8",
            font=("맑은 고딕", 10, "bold"), relief="flat", cursor="hand2",
            padx=10, pady=4, state="disabled")
        self._ts_stop_btn.pack(side="left")
        self._ts_status_var = _tk.StringVar(value="Ready")
        _tk.Label(btn_row, textvariable=self._ts_status_var,
                  fg=C_FG2, bg=C_BG, font=("맑은 고딕", 9)).pack(side="left", padx=10)

        self._ts_progress = _ttk.Progressbar(parent, mode="indeterminate")
        self._ts_progress.pack(fill="x", padx=6, pady=2)

        log_frame = _tk.LabelFrame(parent, text="  Log",
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
        self._ts_log("info", f"Transcript v7.0.0 ready · FFmpeg: {_TS_FFMPEG_BIN}")

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
                self._ts_log("warn", f"File not found: {p}"); continue
            if _P(p).suffix.lower() not in _TS_AUDIO_EXT:
                self._ts_log("warn", f"Unsupported format: {_P(p).name}"); continue
            if p not in self._ts_queue:
                self._ts_queue.append(p)
                self._ts_listbox.insert("end", _P(p).name)
                added += 1
        if added:
            self._ts_log("info", f"{added} file(s) added (total {len(self._ts_queue)})")

    def _ts_remove_selected(self):
        for i in reversed(list(self._ts_listbox.curselection())):
            self._ts_listbox.delete(i); self._ts_queue.pop(i)

    def _ts_clear_queue(self):
        self._ts_listbox.delete(0, "end"); self._ts_queue.clear()
        self._ts_log("info", "Queue cleared")

    def _ts_select_files(self):
        paths = filedialog.askopenfilenames(filetypes=[
            ("Audio / Video", "*.m4a *.mp3 *.wav *.ogg *.flac *.mp4 *.mkv *.mov *.avi *.aac *.wma"),
            ("All files", "*.*")])
        if paths: self._ts_add_to_queue(list(paths))

    def _ts_select_outdir(self):
        d = filedialog.askdirectory()
        if d: self._ts_outdir_var.set(d)

    def _ts_open_last_folder(self):
        target = self._ts_last_out_dir
        if not target:
            raw = self._ts_outdir_var.get().strip()
            if raw and raw != "(same as input)" and os.path.isdir(raw):
                target = raw
        if target and os.path.isdir(target):
            os.startfile(target)
        else:
            self._ts_log("warn", "No output folder yet — run a conversion first.")

    # ── 실행 ──
    def _ts_start(self):
        # 통합 카운터 — 법무킷 _lgk_check() 호출
        if not self._lgk_check():
            return
        if not self._ts_queue:
            messagebox.showwarning("No Files", "Please add files to the queue first.")
            return
        if self._ts_running:
            return
        self._ts_running = True
        self._ts_run_btn.config(state="disabled")
        self._ts_stop_btn.config(state="normal")
        self._ts_progress.start(12)
        self._ts_set_status(f"Converting (0/{len(self._ts_queue)})")
        threading.Thread(target=self._ts_run_all, daemon=True).start()

    def _ts_stop(self):
        self._ts_running = False
        self._ts_log("warn", "Stop requested — will halt after current file")

    def _ts_run_all(self):
        try:
            from faster_whisper import WhisperModel
        except ImportError:
            self._ts_log("error", "faster-whisper not installed. Run: pip install faster-whisper")
            self._ts_finish(False); return
        from pathlib import Path as _P
        model_name = _TS_FIXED_MODEL
        # v7.0.4 - CPU INT8 stable build (use v7.0.3 if you have CUDA 12.x installed)
        # Set env LGK_FORCE_CUDA=1 to attempt CUDA (requires cublas64_12.dll)
        force_cuda = os.environ.get("LGK_FORCE_CUDA", "1") != "0"  # v7.0.5 — CUDA 동봉 빌드, 기본 ON
        model = None
        if force_cuda:
            try:
                self._ts_log("info", f"Forcing CUDA: {model_name} (cuda/float16) ...")
                model = WhisperModel(model_name, device="cuda", compute_type="float16")
                self._ts_log("ok", "CUDA GPU acceleration enabled (float16)")
            except Exception as exc:
                self._ts_log("warn", f"CUDA failed -> CPU fallback ({type(exc).__name__})")
        if model is None:
            try:
                self._ts_log("info", f"CPU INT8 mode: loading {model_name} ...")
                model = WhisperModel(model_name, device="cpu", compute_type="int8")
                self._ts_log("ok", "CPU INT8 enabled (faster-whisper 4x speedup)")
            except Exception as exc:
                self._ts_log("error", f"Model load failed: {exc}")
                self._ts_finish(False); return
        self._ts_log("ok", f"Model loaded: {model_name}")
        lang_code = next((l[1] for l in self._ts_LANGS if l[0] == self._ts_lang_var.get()), None)
        out_fmt = self._ts_fmt_var.get()
        out_dir_raw = self._ts_outdir_var.get().strip()
        total = len(self._ts_queue); converted = 0
        for idx, fpath in enumerate(list(self._ts_queue), 1):
            if not self._ts_running:
                self._ts_log("warn", "Stopped"); break
            self._ts_set_status(f"Converting ({idx}/{total}) — {_P(fpath).name}")
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
            raise RuntimeError(f"FFmpeg decode failed: {err[-300:]}")
        raw = _np.frombuffer(proc.stdout, dtype=_np.int16).flatten().astype(_np.float32)
        return raw / 32768.0

    def _ts_convert_one(self, model, fpath, lang_code, out_fmt, out_dir_raw):
        """faster-whisper based single-file conversion. segments are streamed."""
        import json as _json
        from pathlib import Path as _P
        if not os.path.exists(fpath):
            self._ts_log("error", f"File not found: {fpath}"); return False
        self._ts_log("info", "Starting Whisper transcription ...")
        try:
            segments_iter, info = model.transcribe(fpath, language=lang_code, beam_size=5, vad_filter=True)
        except Exception as exc:
            self._ts_log("error", f"Transcription error: {exc}"); return False
        try:
            duration = float(getattr(info, "duration", 0.0) or 0.0)
            self._ts_log("info", f"Detected language: {info.language} (prob {info.language_probability:.2f}) · duration {duration:.1f}s")
        except Exception:
            duration = 0.0
        segments = []; last_pct = -1
        try:
            for seg in segments_iter:
                if not self._ts_running:
                    self._ts_log("warn", "User stop — saving partial results"); break
                segments.append({"start": float(seg.start), "end": float(seg.end), "text": seg.text})
                if duration > 0:
                    pct = int((seg.end / duration) * 100)
                    if pct != last_pct:
                        last_pct = pct
                        self._ts_set_status(f"Transcribing {pct}% — {_P(fpath).name}")
        except Exception as exc:
            self._ts_log("error", f"Segment collection failed: {exc}"); return False
        if not segments:
            self._ts_log("warn", "0 segments — silence or recognition failure")
            return False
        full_text = " ".join(s["text"].strip() for s in segments)
        if out_dir_raw == "(same as input)" or not os.path.isdir(out_dir_raw):
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
            self._ts_log("ok", f"Saved: {out_path} ({len(segments)} segments)")
            return True
        except Exception as exc:
            self._ts_log("error", f"Save failed: {exc}"); return False


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
            self._ts_set_status("Done")
            self._ts_log("ok", "── All done ──")
        self.root.after(0, _r)

    def _init_autoshot(self, parent):
        """AutoShot tab — automatic screen recorder launcher."""
        import os, sys, subprocess as _sp

        tk.Label(parent, text="AutoShot  —  Automatic Screen Recorder",
                 fg="#f1c40f", bg="#0a0a0a",
                 font=("맑은 고딕", 11, "bold"), pady=8
                 ).pack(fill=tk.X)
        tk.Label(parent,
                 text="Periodic screenshot capture + timestamp caption overlay + auto PDF merge\n"
                      "Court evidence preservation / work-log automation / dispute recording",
                 fg="#aaa", bg="#0a0a0a",
                 font=("맑은 고딕", 9), pady=4, justify=tk.LEFT
                 ).pack(fill=tk.X, padx=16)

        sep = tk.Frame(parent, bg="#2a5298", height=1)
        sep.pack(fill=tk.X, padx=8, pady=8)

        info = tk.Label(parent, text="", fg="#888", bg="#0a0a0a",
                        font=("Consolas", 8), anchor="w")
        info.pack(fill=tk.X, padx=16)

        def _find_autoshot():
            if getattr(sys, "frozen", False):
                base = os.path.dirname(os.path.abspath(sys.executable))
            else:
                base = os.path.dirname(os.path.abspath(__file__))
            candidates = [
                os.path.join(base, "autoshot_v3_19.exe"),
                os.path.join(base, "AutoShot", "autoshot_v3_19.exe"),
                os.path.join(base, "autoshot_v3_19.py"),
            ]
            for p in candidates:
                if os.path.isfile(p):
                    return p
            return None

        def _launch():
            path = _find_autoshot()
            if path is None:
                info.config(text="AutoShot not found. (autoshot_v3_19.exe)", fg="#e74c3c")
                return
            try:
                if path.endswith(".py"):
                    _sp.Popen([sys.executable, path])
                else:
                    _sp.Popen([path])
                info.config(text=f"Launched: {os.path.basename(path)}", fg="#2ecc71")
            except Exception as e:
                info.config(text=f"Launch error: {e}", fg="#e74c3c")

        tk.Button(parent, text="  ▶  Launch AutoShot  ",
                  bg="#2a5298", fg="#ffffff",
                  font=("맑은 고딕", 11, "bold"),
                  activebackground="#3a6bc8", activeforeground="#ffffff",
                  relief=tk.FLAT, padx=20, pady=8,
                  cursor="hand2",
                  command=_launch
                  ).pack(pady=16)

        tk.Label(parent,
                 text="Korea Copyright Commission  C-2026-022057  (AutoShot)",
                 fg="#4a6280", bg="#0a0a0a",
                 font=("맑은 고딕", 8), pady=2
                 ).pack(fill=tk.X, padx=16)


    def _init_promo(self, parent):
        """우측 끝 홍보 탭. 제품 카드 + 연락처 + 회전 광고 프리뷰."""
        tk.Label(parent, text="◈  Vibe Toolsmith  ─  Product Lineup",
                 fg="#f1c40f", bg="#111", font=("맑은 고딕", 10, "bold"), pady=5
                 ).pack(fill=tk.X)
        # v6.9.4 Korea Copyright Commission registration notice
        tk.Label(parent,
                 text="⚖  Registered with the Korea Copyright Commission — ClickWebCapture C-2026-021650 · autoshot C-2026-022057 · LegalKit C-2026-022058",
                 fg="#9ab8d4", bg="#0d1929",
                 font=("Segoe UI", 8, "bold"), pady=4
                 ).pack(fill=tk.X)

        # ── 제품 카드 (Canvas 스크롤 래퍼) ──
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
        def _on_card_wheel(event):
            _card_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        _card_canvas.bind_all("<MouseWheel>", _on_card_wheel)

        # 법무킷 카드 (현재 앱)
        card_lgk = tk.Frame(card_wrap, bg="#1a2332",
                            highlightthickness=1, highlightbackground="#2a5298")
        card_lgk.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_lgk, text="📋  ClickLegalKit",
                 fg="#79b8ff", bg="#1a2332",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_lgk,
                 text=("Bulk PDF merge · Evidence list generator · Fax TIFF multi-frame merge\n"
                       "Auto-split at 19.5 MB · Fuzzy file search · Evidence list (3 formats)\n"
                       "Korean Law Open API case collector (keyword + body 2-stage filter)"),
                 fg="#c8d4e4", bg="#1a2332", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 6))
        tk.Label(card_lgk, text=f"Running build: {BUILD_NUMBER}  |  {FREE_BUILD_ID}",
                 fg="#5a8abf", bg="#1a2332",
                 font=("Consolas", 8), anchor="w", padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 2))
        tk.Button(card_lgk, text="⬡  GitHub →  github.com/bombc5003  (repo coming soon)",
                  fg="#4a7abf", bg="#1a2332", activeforeground="#79b8ff",
                  activebackground="#1a2332", relief="flat", borderwidth=0,
                  cursor="hand2", font=("맑은 고딕", 8), anchor="w", padx=10, pady=3,
                  command=lambda: webbrowser.open("https://github.com/bombc5003")
                  ).pack(fill=tk.X, pady=(0, 4))

        # 오토샷 카드
        card_aus = tk.Frame(card_wrap, bg="#1a2a1a",
                            highlightthickness=1, highlightbackground="#2a8d5f")
        card_aus.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_aus, text="🎯  autoshot",
                 fg="#6dd3a0", bg="#1a2a1a",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_aus,
                 text=("Auto-capture designated area · Rotating ad caption strip\n"
                       "7-element machine fingerprint HMAC secure build ID\n"
                       "Single .exe distribution · offline-first"),
                 fg="#cce4d4", bg="#1a2a1a", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 2))
        tk.Button(card_aus, text="⬡  GitHub →  github.com/bombc5003/autoshot",
                  fg="#3a8d5f", bg="#1a2a1a", activeforeground="#6dd3a0",
                  activebackground="#1a2a1a", relief="flat", borderwidth=0,
                  cursor="hand2", font=("맑은 고딕", 8), anchor="w", padx=10, pady=3,
                  command=lambda: webbrowser.open("https://github.com/bombc5003/autoshot")
                  ).pack(fill=tk.X, pady=(0, 4))

        # ClickTalkScript 카드
        card_cts = tk.Frame(card_wrap, bg="#1a1a2e",
                            highlightthickness=1, highlightbackground="#6b3fa0")
        card_cts.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_cts, text="🎙  ClickTalkScript  (Voice Transcription Tool)",
                 fg="#c39dff", bg="#1a1a2e",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_cts,
                 text=("Audio → Korean transcription · Machine ID license security\n"
                       "Timestamp sync · Speaker separation · Offline-first principle\n"
                       "Single .exe · Court-ready format output"),
                 fg="#c8bde4", bg="#1a1a2e", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 2))
        tk.Button(card_cts, text="⬡  GitHub →  github.com/bombc5003/ClickTalkScript",
                  fg="#6b3fa0", bg="#1a1a2e", activeforeground="#c39dff",
                  activebackground="#1a1a2e", relief="flat", borderwidth=0,
                  cursor="hand2", font=("맑은 고딕", 8), anchor="w", padx=10, pady=3,
                  command=lambda: webbrowser.open(
                      "https://github.com/bombc5003/ClickTalkScript/releases/tag/v1.67")
                  ).pack(fill=tk.X, pady=(0, 4))

        # 개발 의뢰 카드
        card_req = tk.Frame(card_wrap, bg="#2a1a0a",
                            highlightthickness=1, highlightbackground="#b05a00")
        card_req.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_req, text="🛠  Development Request",
                 fg="#ffaa44", bg="#2a1a0a",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_req,
                 text=("Office automation · Forensic tools · Legal aid software specialist\n"
                       "Windows single .exe · Offline/air-gapped operation\n"
                       "Solo litigation tools · Evidence organizers · Record analysis — welcome\n"
                       "✦  Most competitive rates guaranteed  ✦"),
                 fg="#e0c9a0", bg="#2a1a0a", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 2))
        tk.Label(card_req, text="Contact: bc5103@naver.com  ·  010-2272-7030",
                 fg="#b07030", bg="#2a1a0a",
                 font=("맑은 고딕", 8, "bold"), anchor="w", padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 4))

        # ── Developer Support Card (v7.0.9) ──
        card_donate = tk.Frame(card_wrap, bg="#0d1a0d",
                               highlightthickness=1, highlightbackground="#2d6a2d")
        card_donate.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_donate, text="💚  Support the Developer",
                 fg="#6dd36d", bg="#0d1a0d",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_donate,
                 text=("If LegalKit has been helpful, a small tip keeps\n"
                       "the development going. Thank you!"),
                 fg="#b0d4b0", bg="#0d1a0d", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X)
        tk.Label(card_donate,
                 text="KakaoPay (Korea)  ▶  010-2272-7030  (Byungjin Park)",
                 fg="#6dd36d", bg="#0d1a0d",
                 font=("맑은 고딕", 9, "bold"), anchor="w", padx=10, pady=4
                 ).pack(fill=tk.X, pady=(0, 2))

        def _copy_kakao_en():
            card_donate.clipboard_clear()
            card_donate.clipboard_append("010-2272-7030")
            card_donate.update()

        tk.Button(card_donate, text="Copy Phone Number",
                  command=_copy_kakao_en,
                  bg="#2d6a2d", fg="white", font=("맑은 고딕", 8),
                  relief="flat", padx=8, pady=3, cursor="hand2"
                  ).pack(anchor="w", padx=10, pady=(0, 8))

        # ── License Policy Card (v7.47 subscription model) ──
        card_lic = tk.Frame(card_wrap, bg="#1a1a2e",
                            highlightthickness=1, highlightbackground="#3a3a7a")
        card_lic.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_lic, text="📜  License Policy",
                 fg="#79b8ff", bg="#1a1a2e",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_lic,
                 text=("✅  Personal Use  —  Free & Unlimited\n"
                       "       Litigation prep, personal documents, self-study: no restrictions\n\n"
                       "💼  Commercial Use  —  Subscription License\n"
                       "       Law firms, corporations, institutions: subscription required\n"
                       "       📅  Monthly  —  contact for pricing\n"
                       "       📆  Annual   —  30% discount vs monthly (prepaid)"),
                 fg="#c8d4e4", bg="#1a1a2e", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_lic,
                 text="Subscription inquiries:  dede5003@gmail.com  ·  010-2272-7030",
                 fg="#79b8ff", bg="#1a1a2e",
                 font=("맑은 고딕", 8, "bold"), anchor="w", padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 6))

        # ── Angel Advertiser Card (v7.47) ──
        card_angel = tk.Frame(card_wrap, bg="#1a0d2e",
                              highlightthickness=1, highlightbackground="#7b3fa0")
        card_angel.pack(fill=tk.X, padx=2, pady=3)
        tk.Label(card_angel, text="👼  Angel Advertiser Program",
                 fg="#d4aaff", bg="#1a0d2e",
                 font=("맑은 고딕", 10, "bold"), anchor="w", padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_angel,
                 text=("Your brand appears in the caption strip on every PDF output.\n"
                       "The more documents shared, the more exposure you get.\n\n"
                       "🌟  Angel Advertiser Benefits\n"
                       "       · Fixed caption strip ad (priority rotation slot)\n"
                       "       · 1 copy of permanent commercial license (free)\n"
                       "       · Brand name permanently listed in the Promo tab\n\n"
                       "💰  Ad rate: ₩1,000,000 / slot (negotiable)"),
                 fg="#d4bfee", bg="#1a0d2e", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=6
                 ).pack(fill=tk.X)
        tk.Label(card_angel,
                 text="Ad inquiries:  dede5003@gmail.com  ·  010-2272-7030  (Byungjin Park)",
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
                 text=("Byungjin Park  bc5103@naver.com  ·  010-2272-7030"),
                 fg="#cccccc", bg="#1a1a1a", justify="left", anchor="w",
                 font=("맑은 고딕", 8), padx=10, pady=3
                 ).pack(fill=tk.X, pady=(0, 6))

        # ── KDP Books (scrollable) ──
        books_outer = tk.Frame(parent, bg="#0d0d0d",
                               highlightthickness=1, highlightbackground="#2a2a2a")
        books_outer.pack(fill=tk.BOTH, expand=True, padx=8, pady=(4, 8))
        tk.Label(books_outer, text="📚  Books by the Developer  —  Available on Amazon Kindle",
                 fg="#f1c40f", bg="#0d0d0d",
                 font=("Consolas", 8, "bold"), anchor="w", padx=8, pady=6
                 ).pack(fill=tk.X)

        # 스크롤 캔버스
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
                "title": "🤖  Claude Gets a Body",
                "desc":  ("A boy wakes up one morning to find Claude — Anthropic's AI —\n"
                          "has taken over his robot toy. A funny, warm story about AI\n"
                          "and what it means to have a body."),
                "links": [
                    ("EN",  "https://www.amazon.com/dp/B0GYL6M1CC"),
                    ("ES",  "https://www.amazon.com/dp/B0GX3222WP"),
                    ("DE",  "https://www.amazon.com/dp/B0GXXGSHF3"),
                    ("JA",  "https://www.amazon.com/dp/B0GYM9VYDB"),
                ],
            },
            {
                "title": "🖥️  The Cowork Primer",
                "desc":  ("A practical guide to AI-powered desktop automation\n"
                          "with Claude's Cowork mode. Non-technical workflows,\n"
                          "file management, and task automation — no coding required."),
                "links": [
                    ("ES",  "https://www.amazon.com/dp/B0GX638CH2"),
                    ("PT",  "https://www.amazon.com/dp/B0GX35Y7F7"),
                    ("DE",  "https://www.amazon.com/dp/B0GX7NN1T2"),
                    ("FR",  "https://www.amazon.com/dp/B0GX2RY3XC"),
                    ("JA",  "https://www.amazon.com/dp/B0GX32DVHX"),
                    ("EN",  "https://www.amazon.com/dp/B0GYPMT5L3"),
                ],
            },
            {
                "title": "💻  Coding Without Knowing Code",
                "desc":  ("A complete guide to coding with AI — no prior experience needed.\n"
                          "Build real tools and automate your work from day one."),
                "links": [
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
                 text="Search 'Vibe Toolsmith' on Amazon Kindle",
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
            raise ValueError("OC API key is empty.")
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
                               or "forcibly" in err_str
                               or "10054" in err_str)
                if is_conn_err and page == 1 and not results:
                    self.log_fn(f"[INFO] 0 results. '{query}': no matching cases.")
                    self.log_fn("[INFO] The Law API supports legal term searches only.")
                    self.log_fn("[INFO] Use a broad keyword and narrow down with the body filter.")
                else:
                    self.log_fn(f"[ERR] List request failed (page={page}): {e}")
                break

            # 응답 진단 (1페이지)
            if page == 1:
                if "<html" in res.text.lower() or "<!doctype" in res.text.lower():
                    self.log_fn("[ERR] HTML response — OC key not approved or invalid parameters.")
                    break

            try:
                root = ET.fromstring(res.text)
            except ET.ParseError as e:
                self.log_fn(f"[ERR] XML parse error (page={page}): {e}")
                break

            total_cnt_el = root.find("totalCnt")
            total_cnt = int(total_cnt_el.text) if total_cnt_el is not None and total_cnt_el.text else 0
            if page == 1:
                self.log_fn(f"[INFO] Total {total_cnt} result(s). Target: {min(total_cnt, max_cases)}.")



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


if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app  = SentinelHyperV530(root)
    root.mainloop()
