#!/usr/bin/env bash
# Install the strategic partnerships skills for Claude Code.
#
#   ./install.sh                     all skills, user level (~/.claude/skills)
#   ./install.sh --project           all skills, this project (.claude/skills)
#   ./install.sh deal-structure-designer negotiation-prep
#                                    only the named skills
set -euo pipefail

src="$(cd "$(dirname "$0")" && pwd)/skills"
dest="$HOME/.claude/skills"
names=()

for arg in "$@"; do
  case "$arg" in
    --project) dest="$PWD/.claude/skills" ;;
    -h|--help) sed -n '2,7p' "$0"; exit 0 ;;
    *) names+=("$arg") ;;
  esac
done

if [ ${#names[@]} -eq 0 ]; then
  for dir in "$src"/*/; do names+=("$(basename "$dir")"); done
fi

mkdir -p "$dest"
for name in "${names[@]}"; do
  if [ ! -f "$src/$name/SKILL.md" ]; then
    echo "Unknown skill: $name" >&2
    exit 1
  fi
  rm -rf "${dest:?}/$name"
  cp -r "$src/$name" "$dest/$name"
  echo "Installed $name"
done
echo "Done: ${#names[@]} skill(s) in $dest"
