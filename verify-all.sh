#!/bin/bash
# ============================================
# Final verification of notes repo
# ============================================

cd "$(dirname "$0")"

echo "=== Notes Repository Final Verification ==="
echo ""

for note in note-A note-B note-C; do
    echo "--- $note ---"
    cd "$note"
    
    # Count files
    TOTAL=$(find . -type f | wc -l)
    
    # Check gitignore
    HAS_ASSETS_RULE=$(grep -c "src/cases/case\*/assets/" .gitignore 2>/dev/null || echo "0")
    
    # Check title consistency
    TITLE=$(grep "^# " README.md | head -1)
    DESC=$(grep "^description" pyproject.toml | cut -d'"' -f2)
    
    echo "  Files: $TOTAL"
    echo "  Title: $TITLE"
    echo "  Description: $DESC"
    echo "  .gitignore assets rule: $(if [ $HAS_ASSETS_RULE -gt 0 ]; then echo '✅'; else echo '❌ MISSING'; fi)"
    
    # Check for __pycache__ in git
    PCACHE=$(find . -type d -name '__pycache__' 2>/dev/null | wc -l)
    echo "  __pycache__ dirs: $(if [ $PCACHE -gt 0 ]; then echo "❌ $PCACHE"; else echo '✅ 0'; fi)"
    
    # Check for assets in src/cases
    SRC_ASSETS=$(find ./src/cases -type d -name 'assets' 2>/dev/null | wc -l)
    echo "  src/cases/*/assets: $(if [ $SRC_ASSETS -gt 0 ]; then echo "❌ $SRC_ASSETS"; else echo '✅ 0'; fi)"
    
    echo ""
    cd ..
done

echo "=== Top-level files ==="
ls -la *.md *.toml *.sh 2>/dev/null | awk '{print "  " $NF " (" $5 " bytes)"}'

echo ""
echo "=== Git Push Scripts ==="
ls -la push-note-*.sh | awk '{print "  " $NF " ($4 bytes)"}'
