const { remote } = require('electron');
const { dialog } = remote;

const recordButton = document.querySelector('.record');
const stopButton = document.querySelector('.stop');
const transcriptButton = document.querySelector('.transcript');
const summarizeButton = document.querySelector('.summarize');
const inputPopup = document.querySelector('.Input_popup');

// Function to show the input popup for recording
function showInputPopup() {
    inputPopup.style.display = 'block';

    const input = document.createElement('input');
    input.type = 'text';
    input.placeholder = 'Enter file name';
    input.id = 'fileNameInput';

    const submitButton = document.createElement('button');
    submitButton.innerText = 'Submit';
    submitButton.onclick = function () {
        const fileName = document.getElementById('fileNameInput').value;
        console.log('Recording:', fileName);
        inputPopup.style.display = 'none';
        recordButton.style.display = 'none';
        stopButton.style.display = 'inline-block';
    };

    inputPopup.innerHTML = ''; // Clear previous content
    inputPopup.appendChild(input);
    inputPopup.appendChild(submitButton);
}

// Function to open the file selector for transcribing
function openTranscriptionSelector() {
    dialog.showOpenDialog({
        title: 'Select a Recording for Transcription',
        defaultPath: 'C:\\user\\username\\music\\hermes recording',
        properties: ['openFile'],
        filters: [{ name: 'Audio Files', extensions: ['mp3', 'wav', 'm4a'] }] // Filter for audio files
    }).then(result => {
        if (!result.canceled) {
            console.log('Transcribing file:', result.filePaths[0]);
        }
    }).catch(err => {
        console.error(err);
    });
}

// Function to open the file selector for summarization
function openSummarizationSelector() {
    dialog.showOpenDialog({
        title: 'Select a Transcript for Summarization',
        defaultPath: 'C:\\user\\username\\documents\\hermes transcripts',
        properties: ['openFile'],
        filters: [{ name: 'Text Files', extensions: ['txt', 'pdf', 'docx'] }] // Filter for text files
    }).then(result => {
        if (!result.canceled) {
            console.log('Summarizing file:', result.filePaths[0]);
        }
    }).catch(err => {
        console.error(err);
    });
}

// Event listeners for buttons
recordButton.addEventListener('click', showInputPopup);
transcriptButton.addEventListener('click', openTranscriptionSelector);
summarizeButton.addEventListener('click', openSummarizationSelector);
