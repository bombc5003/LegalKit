"""nvidia-cublas-cu12 / nvidia-cudnn-cu12 DLL을 ASCII 경로 _nv_dlls/로 복사.
cuDNN은 Whisper 추론에 필요한 핵심 DLL만 화이트리스트 동봉 (사이즈 절감).
매 실행마다 _nv_dlls 폴더 정리 후 재복사.
"""
import sys, os, shutil

DEST = os.path.abspath("_nv_dlls")

# cuDNN 9.x 화이트리스트 — Whisper 추론 핵심
# 제외: cudnn_engines_precompiled (~1GB), cudnn_engines_runtime_compiled, cudnn_adv, cudnn_heuristic
CUDNN_KEEP_PREFIX = (
    "cudnn64_",            # 메인 wrapper
    "cudnn_ops64_",        # operations
    "cudnn_cnn64_",        # CNN
    "cudnn_graph64_",      # graph API (ctranslate2 4.x)
)

def collect(pkg_attr: str, subname: str, whitelist=None) -> int:
    try:
        if pkg_attr == "cublas":
            import nvidia.cublas as _m
        elif pkg_attr == "cudnn":
            import nvidia.cudnn as _m
        else:
            return 0
        pkg_dir = list(_m.__path__)[0]
        bin_dir = os.path.join(pkg_dir, "bin")
        if not os.path.isdir(bin_dir):
            return 0
        sub = os.path.join(DEST, subname)
        # 매 실행마다 폴더 정리
        if os.path.isdir(sub):
            shutil.rmtree(sub)
        os.makedirs(sub, exist_ok=True)
        cnt = 0; skipped = 0
        for f in os.listdir(bin_dir):
            if not f.lower().endswith(".dll"):
                continue
            if whitelist is not None:
                if not any(f.startswith(p) for p in whitelist):
                    skipped += 1
                    continue
            src = os.path.join(bin_dir, f)
            dst = os.path.join(sub, f)
            shutil.copy2(src, dst)
            cnt += 1
        print(f"  {subname}: copied={cnt} skipped={skipped}")
        return cnt
    except Exception as exc:
        print(f"ERR {pkg_attr}: {exc}", file=sys.stderr)
        return 0

if __name__ == "__main__":
    n1 = collect("cublas", "cublas")
    n2 = collect("cudnn", "cudnn", whitelist=CUDNN_KEEP_PREFIX)
    print(f"COPIED cublas={n1} cudnn={n2} dest={DEST}")
