#!/bin/bash
set -e

# IAM Website - Deploy Script
# Usage: OPENROUTER_API_KEY=sk-or-... bash deploy.sh
# Or without chatbot: bash deploy.sh

REPO="https://github.com/clubeedg-ship-it/iam-website.git"
APP_DIR="/var/www/iam-website"
APP_NAME="iam-website"
CHAT_NAME="iam-chat-proxy"
PORT=3007
CHAT_PORT=3860

echo ""
echo "  IAM Website — Deploy"
echo "  ─────────────────────"
echo ""

# 1. Install Node.js if missing
if ! command -v node &>/dev/null; then
    echo "[1/6] Installing Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
    sudo apt-get install -y nodejs
else
    echo "[1/6] Node.js already installed: $(node --version)"
fi

# 2. Install PM2 if missing
if ! command -v pm2 &>/dev/null; then
    echo "[2/6] Installing PM2..."
    sudo npm install -g pm2
else
    echo "[2/6] PM2 already installed: $(pm2 --version)"
fi

# 3. Clone or pull the repo
if [ -d "$APP_DIR" ]; then
    echo "[3/6] Updating existing repo..."
    cd "$APP_DIR"
    git pull origin main
else
    echo "[3/6] Cloning repo..."
    sudo mkdir -p "$APP_DIR"
    sudo chown "$(whoami)":"$(whoami)" "$APP_DIR"
    git clone "$REPO" "$APP_DIR"
    cd "$APP_DIR"
fi

# 4. Install chat proxy dependencies
echo "[4/6] Installing chat proxy dependencies..."
cd "$APP_DIR/api" && npm install --production 2>/dev/null && cd "$APP_DIR"

# 5. Start or restart services with PM2
echo "[5/6] Starting services with PM2..."
pm2 describe "$APP_NAME" &>/dev/null && pm2 restart "$APP_NAME" || pm2 start server.js --name "$APP_NAME"

if [ -n "$OPENROUTER_API_KEY" ]; then
    echo "       Starting chat proxy (API key provided)..."
    pm2 describe "$CHAT_NAME" &>/dev/null && pm2 restart "$CHAT_NAME" --update-env || \
        pm2 start api/chat-proxy.js --name "$CHAT_NAME" \
            --env "OPENROUTER_API_KEY=$OPENROUTER_API_KEY" \
            --env "CHAT_PORT=$CHAT_PORT"
else
    echo "       Skipping chat proxy (no OPENROUTER_API_KEY set)"
    echo "       To enable: OPENROUTER_API_KEY=sk-or-... bash deploy.sh"
fi

pm2 save

# 6. Setup PM2 to survive reboots
echo "[6/6] Enabling startup on reboot..."
pm2 startup systemd -u "$(whoami)" --hp "$HOME" 2>/dev/null | grep "sudo" | bash 2>/dev/null || true
pm2 save

echo ""
echo "  Done! Site running at http://$(hostname -I | awk '{print $1}'):${PORT}"
echo ""
echo "  Services:"
echo "    pm2 status              — check all services"
echo "    pm2 logs $APP_NAME      — website logs"
echo "    pm2 logs $CHAT_NAME     — chatbot logs"
echo ""
echo "  To update later:"
echo "    cd $APP_DIR && git pull && pm2 restart all"
echo ""
