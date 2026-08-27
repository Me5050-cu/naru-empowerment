#!/bin/bash
# Watches the site files and pushes every change to GitHub.
# GitHub Pages redeploys on its own, roughly a minute after each push.
#
#   ./_dev/autopush.sh          start watching
#   Ctrl-C                      stop
#
# Changes are batched: after a save it waits QUIET seconds for you to stop
# typing, so a burst of edits becomes one commit instead of twenty.

set -uo pipefail
cd "$(dirname "$0")/.."
QUIET=${QUIET:-8}

echo "Watching $(pwd)"
echo "Pushing to $(git remote get-url origin)"
echo "Live at https://me5050-cu.github.io/naru-empowerment/"
echo "Ctrl-C to stop."
echo

sync_now() {
  git add -A
  git diff --cached --quiet && return 0        # nothing staged
  local files msg
  files=$(git diff --cached --name-only | head -3 | tr '\n' ' ')
  msg="Update ${files}$( [ "$(git diff --cached --name-only | wc -l)" -gt 3 ] && echo 'and more' )"
  git commit -qm "$msg" || return 1
  if git push -q origin main 2>/dev/null; then
    echo "$(date '+%H:%M:%S')  pushed — $msg"
  else
    echo "$(date '+%H:%M:%S')  PUSH FAILED — commit is saved locally, run 'git push' when back online"
  fi
}

last_state=""
while true; do
  # cheap portable change detection: hash of name+mtime+size for tracked paths
  state=$(find . -path ./.git -prune -o -type f \
            \( -name '*.html' -o -name '*.css' -o -name '*.js' -o -name '*.md' -o -name '*.py' \) \
            -print0 2>/dev/null | xargs -0 stat -f '%N %m %z' 2>/dev/null | sort | shasum | cut -d' ' -f1)
  if [ -n "$last_state" ] && [ "$state" != "$last_state" ]; then
    sleep "$QUIET"          # let a burst of edits settle
    sync_now
    state=$(find . -path ./.git -prune -o -type f \
              \( -name '*.html' -o -name '*.css' -o -name '*.js' -o -name '*.md' -o -name '*.py' \) \
              -print0 2>/dev/null | xargs -0 stat -f '%N %m %z' 2>/dev/null | sort | shasum | cut -d' ' -f1)
  fi
  last_state="$state"
  sleep 3
done
