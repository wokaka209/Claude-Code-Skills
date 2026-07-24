#!/usr/bin/env bash
set -euo pipefail

shopt -s nullglob

DRAWIO_BIN="${DRAWIO_BIN:-}"
DRAWIO_PLATFORM="${DRAWIO_PLATFORM:-}"
DRAWIO_EXPORT_SCALE="${DRAWIO_EXPORT_SCALE:-3}"
DRAWIO_EXPORT_BORDER="${DRAWIO_EXPORT_BORDER:-20}"
DRAWIO_EXPORT_SLEEP_SECONDS="${DRAWIO_EXPORT_SLEEP_SECONDS:-6}"

detect_platform() {
  local uname_s
  uname_s="$(uname -s 2>/dev/null || echo unknown)"
  case "$uname_s" in
    Darwin)
      echo "macos"
      ;;
    Linux)
      echo "linux"
      ;;
    MINGW*|MSYS*|CYGWIN*)
      echo "windows"
      ;;
    *)
      echo "unknown"
      ;;
  esac
}

resolve_command_path() {
  local candidate="$1"
  if [ -z "$candidate" ]; then
    return 1
  fi
  if [ -x "$candidate" ]; then
    printf '%s\n' "$candidate"
    return 0
  fi
  if command -v "$candidate" >/dev/null 2>&1; then
    command -v "$candidate"
    return 0
  fi
  return 1
}

resolve_drawio_bin() {
  local platform="$1"
  local username_lower
  username_lower="${USERNAME:-${USER:-}}"

  if [ -n "$DRAWIO_BIN" ]; then
    resolve_command_path "$DRAWIO_BIN" && return 0
  fi

  case "$platform" in
    macos)
      for candidate in \
        "/Applications/draw.io.app/Contents/MacOS/draw.io" \
        "/Applications/diagrams.net.app/Contents/MacOS/draw.io"
      do
        resolve_command_path "$candidate" && return 0
      done
      ;;
    linux)
      for candidate in \
        "/usr/bin/drawio" \
        "/usr/local/bin/drawio" \
        "/snap/bin/drawio" \
        "/opt/drawio/drawio" \
        "${HOME}/.local/bin/drawio"
      do
        resolve_command_path "$candidate" && return 0
      done
      ;;
    windows)
      for candidate in \
        "/c/Program Files/draw.io/draw.io.exe" \
        "/c/Program Files/diagrams.net/draw.io.exe" \
        "/c/Users/${username_lower}/AppData/Local/Programs/draw.io/draw.io.exe" \
        "/c/Users/${username_lower}/AppData/Local/Programs/diagrams.net/draw.io.exe"
      do
        resolve_command_path "$candidate" && return 0
      done
      ;;
  esac

  if command -v drawio >/dev/null 2>&1; then
    command -v drawio
    return 0
  fi

  return 1
}

if [ -z "$DRAWIO_PLATFORM" ]; then
  DRAWIO_PLATFORM="$(detect_platform)"
fi

if ! DRAWIO_BIN="$(resolve_drawio_bin "$DRAWIO_PLATFORM")"; then
  echo "draw.io binary not found for platform: $DRAWIO_PLATFORM" >&2
  echo "Set DRAWIO_BIN manually if draw.io is installed in a non-standard location." >&2
  exit 1
fi

inputs=()
if [ "$#" -gt 0 ]; then
  for input in "$@"; do
    inputs+=("$input")
  done
else
  for input in *.drawio; do
    [ -f "$input" ] || continue
    inputs+=("$input")
  done
fi

if [ "${#inputs[@]}" -eq 0 ]; then
  echo "当前目录下没有 .drawio 文件。"
  exit 0
fi

echo "Detected platform: $DRAWIO_PLATFORM"
echo "Using draw.io binary: $DRAWIO_BIN"
echo "High-res scale: $DRAWIO_EXPORT_SCALE"
echo "Border: $DRAWIO_EXPORT_BORDER"

generated_files=()
failed_files=()

for drawio_file in "${inputs[@]}"; do
  if [ ! -f "$drawio_file" ]; then
    echo "Skipping missing file: $drawio_file" >&2
    failed_files+=("$drawio_file")
    continue
  fi

  case "$drawio_file" in
    *.drawio) ;;
    *)
      echo "Skipping non-.drawio file: $drawio_file" >&2
      continue
      ;;
  esac

  png_file="${drawio_file}.png"
  echo "========================================"
  echo "处理文件: $drawio_file -> $png_file"
  echo "  尝试高分辨率导出 --scale $DRAWIO_EXPORT_SCALE ..."

  if "$DRAWIO_BIN" \
    -x -f png --scale "$DRAWIO_EXPORT_SCALE" --border "$DRAWIO_EXPORT_BORDER" \
    -o "$png_file" "$drawio_file" > /dev/null 2>&1; then
    echo "  成功！(scale=$DRAWIO_EXPORT_SCALE)"
    generated_files+=("$png_file")
  else
    echo "  scale=$DRAWIO_EXPORT_SCALE 失败 -> 切换到默认比例"
    rm -f "$png_file"

    if "$DRAWIO_BIN" \
      -x -f png --border "$DRAWIO_EXPORT_BORDER" \
      -o "$png_file" "$drawio_file" > /dev/null 2>&1; then
      echo "  成功！(无 scale，默认比例)"
      generated_files+=("$png_file")
    else
      rm -f "$png_file"
      echo "  连默认也失败: $drawio_file"
      failed_files+=("$drawio_file")
    fi
  fi

  sleep "$DRAWIO_EXPORT_SLEEP_SECONDS"
done

echo "========================================"
if [ "${#generated_files[@]}" -gt 0 ]; then
  echo "成功生成 ${#generated_files[@]} 个 PNG 文件。"
else
  echo "没有成功生成任何 PNG 文件。" >&2
fi

if [ "${#failed_files[@]}" -gt 0 ]; then
  echo "失败文件数: ${#failed_files[@]}" >&2
fi