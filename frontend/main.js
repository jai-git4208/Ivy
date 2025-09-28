const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let space = false; 
let win; // keep reference to the window

function createWindow() {
    win = new BrowserWindow({
        width: 600,
        height: 600,
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

if (!space) {
    ipcMain.on('run-python', () => {
        space = true;

        console.log('⚡ Running app.py in venv (logs shown below)...');

        const venvPython = '/home/jaimin-pansal/Ivy/venv/bin/python';
        const appPath = '/home/jaimin-pansal/Ivy/app.py';

        const pythonProcess = spawn(venvPython, ['-u', appPath], {
            cwd: path.dirname(appPath)
        });

        // Handle stdout
        pythonProcess.stdout.on('data', (data) => {
            const text = data.toString().trim();
            process.stdout.write(`🐍 stdout: ${text}\n`);

            try {
                const json = JSON.parse(text);

                if (json.output && json.output.movement && win) {
                    const { x, y } = json.output.movement;

                    // get current window bounds
                    const bounds = win.getBounds();

                    // move relative to current position
                    win.setBounds({
                        x: bounds.x + x,
                        y: bounds.y + y,
                        width: bounds.width,
                        height: bounds.height
                    });
                }
            } catch (err) {
                // not JSON, ignore
            }
        });

        pythonProcess.stderr.on('data', (data) => {
            process.stderr.write(`🐍 stderr: ${data}`);
        });

        pythonProcess.on('close', (code) => {
            console.log(`🐍 app.py exited with code ${code}`);
        });
    });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});
