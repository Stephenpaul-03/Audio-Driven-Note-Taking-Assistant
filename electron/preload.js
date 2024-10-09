// electron-app/preload.js
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    transcribe: () => ipcRenderer.invoke('transcribe'),
    summarize: () => ipcRenderer.invoke('summarize'),
    identifySpeaker: () => ipcRenderer.invoke('identify-speaker'),
});
