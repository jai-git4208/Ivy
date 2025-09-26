const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
    const win = new BrowserWindow({
        width: 400,
        height: 400,
        transparent: true,   // Makes the window background transparent
        frame: false,        // Removes the title bar and borders
        alwaysOnTop: true,   // Window stays on top of others
        resizable: false,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    win.loadFile('index.html');

    // Enable moving the window by dragging the orb
    // We'll use CSS -webkit-app-region: drag on the draggable element
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});
