#!/bin/bash
set -e

# IAM Website - Deploy Script
# Run on any fresh Ubuntu/Debian VPS to get the site running
# Usage: bash deploy.sh

REPO="https://github.com/clubeedg-ship-it/iam-website.git"
APP_DIR="/var/www/iam-website"
APP_NAME="iam-website"
PORT=3007

echo ""
echo "  IAM Website — Deploy"
echo "  ─────────────────────"
echo ""

# 1. Install Node.js if missing
if ! command -v node &>/dev/null; then
    echo "[1/5] Installing Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
    sudo apt-get install -y nodejs
else
    echo "[1/5] Node.js already installed: $(node --version)"
fi

# 2. Install PM2 if missing
if ! command -v pm2 &>/dev/null; then
    echo "[2/5] Installing PM2..."
    sudo npm install -g pm2
else
    echo "[2/5] PM2 already installed: $(pm2 --version)"
fi

# 3. Clone or pull the repo
if [ -d "$APP_DIR" ]; then
    echo "[3/5] Updating existing repo..."
    cd "$APP_DIR"
    git pull origin main
else
    echo "[3/5] Cloning repo..."
    sudo mkdir -p "$APP_DIR"
    sudo chown "$(whoami)":"$(whoami)" "$APP_DIR"
    git clone "$REPO" "$APP_DIR"
    cd "$APP_DIR"
fi

# 4. Start or restart with PM2
echo "[4/5] Starting with PM2..."
pm2 describe "$APP_NAME" &>/dev/null && pm2 restart "$APP_NAME" || pm2 start server.js --name "$APP_NAME"
pm2 save

# 5. Setup PM2 to survive reboots
echo "[5/5] Enabling startup on reboot..."
pm2 startup systemd -u "$(whoami)" --hp "$HOME" 2>/dev/null | grep "sudo" | bash 2>/dev/null || true
pm2 save

echo ""
echo "  ✓ Done! Site running at http://$(hostname -I | awk '{print $1}'):${PORT}"
echo ""
echo "  Useful commands:"
echo "    pm2 status          — check if running"
echo "    pm2 logs $APP_NAME  — view logs"
echo "    pm2 restart $APP_NAME — restart after changes"
echo ""
echo "  To update later:"
echo "    cd $APP_DIR && git pull && pm2 restart $APP_NAME"
echo ""
