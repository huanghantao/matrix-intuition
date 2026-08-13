"""课程完整性验收脚本。

检查项目是否达到交付标准：
  1. SUMMARY.md 里链接的每个章节文件都存在且内容足够长（不是占位符）；
  2. 章节里引用的每张图片都真实存在；
  3. figures/out/ 里每张图都至少被引用一次；
  4. 参考答案测试全绿（IMPL=reference）；
  5. mdBook 构建成功。

用法：python scripts/verify_course.py
"""

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MIN_CHAPTER_LINES = 60     # 正文章节最少行数（占位符只有 1 行）
MIN_README_LINES = 20      # 每周 README 最少行数


def parse_summary() -> list:
    """从 SUMMARY.md 提取所有 markdown 链接（相对路径）。"""
    summary = ROOT / "SUMMARY.md"
    links = re.findall(r"\]\(([^)]+\.md)\)", summary.read_text(encoding="utf-8"))
    return [l for l in links if not l.startswith("http")]


def check_chapters(links) -> list:
    problems = []
    for link in links:
        path = ROOT / link
        if not path.exists():
            problems.append(f"[缺文件] {link} 不存在")
            continue
        n = len(path.read_text(encoding="utf-8").splitlines())
        min_lines = MIN_README_LINES if path.name == "README.md" else MIN_CHAPTER_LINES
        if n < min_lines:
            problems.append(f"[疑似占位] {link} 只有 {n} 行（要求 ≥ {min_lines}）")
    return problems


def check_image_refs(links) -> list:
    problems = []
    used = set()
    for link in links:
        path = ROOT / link
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for m in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            if m.startswith("http"):
                continue
            img = (path.parent / m).resolve()
            if not img.exists():
                problems.append(f"[缺图] {link} 引用了不存在的图片 {m}")
            else:
                used.add(img.name)
    out_dir = ROOT / "figures" / "out"
    for png in sorted(out_dir.glob("*.png")):
        if png.name not in used:
            problems.append(f"[图未被引用] figures/out/{png.name}")
    return problems


def run(cmd: list, cwd: ROOT, extra_env: dict = None) -> int:
    import os
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=env)
    print(f"  $ {' '.join(cmd)}  → exit {r.returncode}")
    if r.returncode != 0:
        print("   " + (r.stderr or r.stdout).strip().splitlines()[-1])
    return r.returncode


def main():
    print("== 1. 章节文件 ==")
    links = parse_summary()
    problems = check_chapters(links)
    print(f"   SUMMARY 链接 {len(links)} 个")
    for p in problems:
        print("   ✗", p)
    print(f"   章节检查：{'全过' if not problems else f'{len(problems)} 个问题'}")

    print("== 2. 图片引用 ==")
    img_problems = check_image_refs(links)
    for p in img_problems:
        print("   ✗", p)
    print(f"   图片检查：{'全过' if not img_problems else f'{len(img_problems)} 个问题'}")

    print("== 3. 参考答案测试 ==")
    rc_tests = run(["pytest", "tests", "-q"], ROOT, extra_env={"IMPL": "reference"})

    print("== 4. mdBook 构建 ==")
    rc_book = run(["mdbook", "build"], ROOT)

    total = len(problems) + len(img_problems) + (rc_tests != 0) + (rc_book != 0)
    print()
    if total == 0:
        print("✅ 全部通过，课程达到交付标准。")
        return 0
    print(f"❌ 共 {total} 个问题（占位/缺图/测试/构建）。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
