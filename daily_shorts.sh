#!/usr/bin/env bash
# Craft&Code Daily Shorts Automation Script
# Runs the daily YouTube Shorts generator and copies output to dist
cd "$(dirname "$0")"
echo "🎬 Running Craft&Code Daily YouTube Shorts Generator..."
python3 shorts_generator.py --latest
python3 build.py
echo "✅ Daily Shorts generated and site updated!"
