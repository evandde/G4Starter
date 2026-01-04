#!/bin/bash
set -e

# G4Starter installation script for macOS/Linux
# Usage: curl -fsSL https://raw.githubusercontent.com/evandde/G4Starter/main/install.sh | bash

REPO="evandde/G4Starter"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/bin}"
BINARY_NAME="g4starter"

# Detect OS
OS="$(uname -s)"
case "$OS" in
    Linux*)     ASSET_NAME="G4Starter_linux";;
    Darwin*)    ASSET_NAME="G4Starter_mac";;
    *)          echo "Error: Unsupported operating system: $OS"; exit 1;;
esac

echo "🚀 Installing G4Starter..."
echo "   OS: $OS"
echo "   Install directory: $INSTALL_DIR"

# Create install directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Download latest release
echo "📦 Downloading latest release..."
DOWNLOAD_URL="https://github.com/$REPO/releases/latest/download/$ASSET_NAME"

if command -v curl &> /dev/null; then
    curl -fsSL -o "$INSTALL_DIR/$BINARY_NAME" "$DOWNLOAD_URL"
elif command -v wget &> /dev/null; then
    wget -q -O "$INSTALL_DIR/$BINARY_NAME" "$DOWNLOAD_URL"
else
    echo "Error: curl or wget is required"
    exit 1
fi

# Make executable
chmod +x "$INSTALL_DIR/$BINARY_NAME"

echo "✅ G4Starter installed successfully!"
echo ""
echo "To use G4Starter, make sure $INSTALL_DIR is in your PATH."
echo ""

# Check if directory is in PATH
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo "⚠️  $INSTALL_DIR is not in your PATH"
    echo ""
    echo "Add this to your ~/.bashrc or ~/.zshrc:"
    echo "   export PATH=\"$INSTALL_DIR:\$PATH\""
    echo ""
    echo "Then run: source ~/.bashrc (or ~/.zshrc)"
else
    echo "Run 'g4starter' to get started!"
fi
