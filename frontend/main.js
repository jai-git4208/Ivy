const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

function createWindow() {
    const win = new BrowserWindow({
        width: 400,
        height: 400,
        transparent: true,
        frame: false,
        alwaysOnTop: true,
        resizable: false,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    win.loadFile('index.html');
}

ipcMain.on('run-python', () => {
    console.log('⚡ Running app.py in venv (logs shown below)...');

    const venvPython = '/home/jaimin-pansal/Ivy/venv/bin/python';
    const appPath = '/home/jaimin-pansal/Ivy/app.py';

    const pythonProcess = spawn(venvPython, ['-u', appPath], {
        cwd: path.dirname(appPath)
    });

    // Print stdout in real-time
    pythonProcess.stdout.on('data', (data) => {
        process.stdout.write(`🐍 stdout: ${data}`);
    });

    // Print stderr in real-time
    pythonProcess.stderr.on('data', (data) => {
        process.stderr.write(`🐍 stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`🐍 app.py exited with code ${code}`);
    });
});

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});
